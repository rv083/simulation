"""
Traffic Calculator Service - Adaptive Traffic Light Timing Algorithm
SIMULATION VERSION – Backend-Matched Logic
"""

import logging
from typing import List, Tuple
from datetime import datetime


class TrafficCalculator:

    YELLOW_LIGHT_TIME = 5  # seconds per lane

    def __init__(
        self,
        min_time: int = 15,
        max_time: int = 90,
        base_cycle_time: int = 120,
    ):
        self.min_time = min_time
        self.max_time = max_time
        self.base_cycle_time = base_cycle_time
        self.logger = logging.getLogger(__name__)

    async def calculate_green_times(
        self,
        lane_counts: List[int],
        junction_id: int = None
    ) -> Tuple[List[int], int]:

        start_time = datetime.now()

        # -----------------------------
        # Validation
        # -----------------------------
        if len(lane_counts) != 4:
            raise ValueError("Exactly 4 lane counts are required")

        if any(c < 0 for c in lane_counts):
            raise ValueError("Lane counts cannot be negative")

        num_lanes = 4
        total_cars = sum(lane_counts)

        # -----------------------------
        # Step 1: Calculate green cycle time (backend logic)
        # -----------------------------
        if total_cars <= 100:
            green_cycle_time = self.base_cycle_time
        else:
            increments = (total_cars - 100) // 10
            green_cycle_time = min(
                self.base_cycle_time + increments * 10,
                180
            )

        # -----------------------------
        # Step 2: Initial allocation (backend logic)
        # -----------------------------
        remaining_time = green_cycle_time - (self.min_time * num_lanes)

        green_times_raw = []
        fixed_lanes = []
        adjustable_lanes = []

        for idx, count in enumerate(lane_counts):
            if count <= self.min_time:
                green_times_raw.append(self.min_time)
                fixed_lanes.append(idx)
            else:
                green_time = self.min_time + (
                    (count - self.min_time) / total_cars
                ) * remaining_time
                green_times_raw.append(green_time)
                adjustable_lanes.append(idx)

        # -----------------------------
        # Step 3: Normalize adjustable lanes (backend double-scaling)
        # -----------------------------
        fixed_sum = sum(green_times_raw[i] for i in fixed_lanes)
        adjustable_cycle_time = green_cycle_time - fixed_sum
        adjustable_raw_sum = sum(
            green_times_raw[i] for i in adjustable_lanes
        )

        green_times = green_times_raw.copy()

        if adjustable_raw_sum > 0:
            for i in adjustable_lanes:
                green_times[i] = (
                    green_times_raw[i] / adjustable_raw_sum
                ) * adjustable_cycle_time

        # -----------------------------
        # Step 4: Enforce maximum green time (backend logic)
        # -----------------------------
        while True:
            excess_time = 0
            under_max_lanes = []

            for i in adjustable_lanes:
                if green_times[i] > self.max_time:
                    excess_time += green_times[i] - self.max_time
                    green_times[i] = self.max_time
                else:
                    under_max_lanes.append(i)

            if excess_time > 0 and under_max_lanes:
                distribute = excess_time / len(under_max_lanes)
                for i in under_max_lanes:
                    green_times[i] += distribute
            else:
                break

        # -----------------------------
        # Step 5: Final rounding and balancing
        # -----------------------------
        green_times_rounded = [round(t) for t in green_times]
        diff = green_cycle_time - sum(green_times_rounded)

        # Distribute rounding difference evenly across adjustable lanes
        # to prevent any single lane from getting too much time
        if diff != 0 and adjustable_lanes:
            # Distribute difference incrementally (1 second at a time)
            diff_abs = abs(diff)
            diff_direction = 1 if diff > 0 else -1
            
            for _ in range(diff_abs):
                # Find the lane that needs adjustment most
                # Cycle through adjustable lanes to spread the adjustment
                lane_idx = adjustable_lanes[_ % len(adjustable_lanes)]
                green_times_rounded[lane_idx] += diff_direction

        # -----------------------------
        # Step 6: Total cycle time (green + yellow)
        # -----------------------------
        total_cycle_time = green_cycle_time + (
            num_lanes * self.YELLOW_LIGHT_TIME
        )

        exec_time = (
            datetime.now() - start_time
        ).total_seconds() * 1000

        self.logger.info(
            f"[SIMULATION] Lane counts: {lane_counts} | "
            f"Green times: {green_times_rounded} | "
            f"Green cycle: {green_cycle_time}s | "
            f"Total cycle: {total_cycle_time}s | "
            f"Exec: {exec_time:.2f}ms"
        )

        return green_times_rounded, total_cycle_time
