# 🎮 Interactive Simulation - Quick Start Guide

## 🆕 NEW: User Input Features!

You now have **interactive versions** that let you test with custom vehicle counts!

---

## 📦 Files You Have

### Basic Versions (Auto-generate counts):
1. `traffic_simulation.py` - Python simulation
2. `traffic_visualization.html` - Web visualization

### **Interactive Versions (Custom inputs):**
3. **`traffic_simulation_interactive.py`** ⭐ - Python with menus
4. **`traffic_visualization_interactive.html`** ⭐ - Web with input forms

---

## 🚀 Quick Start - Interactive Web Version (EASIEST!)

### Step 1: Open the File
Double-click **`traffic_visualization_interactive.html`**

### Step 2: Choose Your Mode

You'll see **3 options**:

#### 🎲 **Random Mode** (Quick Testing)
- Automatically generates random vehicle counts
- Good for: Quick demos, seeing variety

#### ✏️ **Custom Input** (Precise Testing)
- Enter exact vehicle counts for each lane
- Good for: Testing specific cases, debugging

#### 📋 **Test Scenarios** (Pre-defined Cases)
- Choose from 6 built-in scenarios:
  - 🌤️ **Light Traffic**: 5-15 vehicles/lane
  - 🌥️ **Moderate Traffic**: 15-30 vehicles/lane
  - ⛈️ **Heavy Traffic**: 30-50 vehicles/lane
  - ⚖️ **Unbalanced**: One busy lane
  - 🚨 **Emergency**: One critical lane (80+ vehicles)
  - 🔽 **Minimum**: All lanes minimal

### Step 3: Set Number of Cycles
- Enter how many cycles you want (1-10)
- Default is 3 cycles

### Step 4: Enter Data (if Custom mode)
- Enter vehicle counts for each lane
- Range: 0-150 vehicles
- The form shows inputs for all cycles

### Step 5: Start!
- Click **"▶ Start Simulation"**
- Watch the traffic lights in action!
- See the 10-second buffer warning appear

---

## 🐍 Interactive Python Version

### How to Run:

```bash
python traffic_simulation_interactive.py
```

### What Happens:

```
======================================================================
🚦 ADAPTIVE TRAFFIC CONTROL SYSTEM - INTERACTIVE SIMULATION
======================================================================

🎯 Choose simulation mode:
   1. Random vehicle counts (automatic)
   2. Custom vehicle counts (manual input)
   3. Test specific scenarios

Enter your choice (1/2/3): 2

How many traffic cycles to simulate? (default: 3): 5

✅ Mode: Custom vehicle counts
📝 You will enter vehicle counts for each of the 5 cycles

📊 Enter vehicle counts for Cycle 1:
   Lane 1 vehicles: 25
   Lane 2 vehicles: 30
   Lane 3 vehicles: 15
   Lane 4 vehicles: 20
   ✅ Cycle 1: [25, 30, 15, 20]

[... repeat for all 5 cycles ...]

Press ENTER to start simulation...
```

### Features:

- **Interactive menus** - Choose mode step-by-step
- **Input validation** - Won't accept invalid numbers
- **Test scenarios** - 7 pre-defined scenarios
- **Detailed logs** - See everything happening

---

## 💡 Test Cases You Can Try

### Case 1: Equal Traffic
```
All lanes: 20 vehicles each
Expected: ~30 seconds green per lane
```

### Case 2: One Busy Lane
```
Lane 1: 80 vehicles
Lane 2-4: 10 vehicles each
Expected: Lane 1 gets much more green time
```

### Case 3: Minimum Traffic
```
All lanes: 5 vehicles each
Expected: All get minimum green (15s)
Total cycle: 80s (60s green + 20s yellow)
```

### Case 4: Maximum Traffic
```
All lanes: 100 vehicles each
Expected: All get maximum green (90s)
Total cycle: 380s (360s green + 20s yellow)
```

### Case 5: Rush Hour Simulation
```
Cycle 1: [40, 35, 38, 42]  (Heavy)
Cycle 2: [25, 28, 22, 30]  (Moderate)
Cycle 3: [10, 12, 8, 15]   (Light)
Expected: See cycle time decrease as traffic reduces
```

---

## 🎯 Testing Checklist

Use this to verify your algorithm works correctly:

### ✅ Basic Algorithm Tests
- [ ] All lanes with 20 vehicles → Equal green times
- [ ] One lane with 80, others with 10 → Busy lane gets more time
- [ ] All lanes with 5 → All get minimum (15s)
- [ ] Total vehicles = 85 → Base cycle time (120s green)
- [ ] Total vehicles = 150 → Extended cycle time (150s green)

### ✅ Edge Cases
- [ ] Zero vehicles in one lane → Gets minimum time
- [ ] Very unbalanced (90:5:5:5) → Algorithm handles correctly
- [ ] All lanes at max (100 each) → Doesn't exceed 90s per lane

### ✅ Buffer Functionality
- [ ] Buffer activates at 10s remaining
- [ ] Next cycle starts immediately
- [ ] No gaps between cycles

---

## 📊 Understanding the Output

### Web Version Shows:
- **Current Cycle Number** (top left)
- **Cycle Progress** (percentage and bar)
- **Vehicle Counts** (top boxes)
- **Lane States** (Green/Yellow/Red with timers)
- **Green Times** (calculated for each lane)
- **Buffer Warning** (yellow box when active)

### Python Version Shows:
```
🚦 CYCLE 1 STARTED
Green times: [22, 32, 18, 28]
Vehicle counts: [18, 25, 12, 30]

🟢 Lane 1 - GREEN (22s)
🟡 Lane 1 - YELLOW (5s)
🔴 Lane 1 - RED (others' turn)

⏰ PRE-CALCULATION BUFFER ACTIVATED (Last 10s)
📊 Vehicle counts detected: [15, 28, 20, 22]
☁️  Cloud processing...
✅ Next cycle ready!
```

---

## 🎓 Learning Exercises

### Exercise 1: Understand Proportional Allocation
1. Set Cycle 1: [10, 20, 30, 40]
2. Run simulation
3. Notice: Green times are proportional to vehicle counts
4. Lane 4 (40 vehicles) gets most green time

### Exercise 2: Test Minimum Constraint
1. Set all lanes: [5, 3, 2, 4]
2. Run simulation
3. Notice: All lanes get minimum 15s (not proportional)

### Exercise 3: Verify Buffer Timing
1. Use Random mode with 3 cycles
2. Watch carefully when ~10s remain in cycle
3. See buffer warning appear
4. Next cycle starts immediately

### Exercise 4: Stress Test
1. Choose "Heavy Traffic" scenario
2. Run multiple cycles
3. Verify cycle times increase with vehicle count
4. Check no lane exceeds 90s maximum

---

## 🐛 Troubleshooting

### Web Version Issues

**Can't enter vehicle counts:**
- Make sure you selected "Custom Input" mode first
- Click on the input fields to activate them

**Simulation won't start:**
- Check if you selected a mode
- For scenario mode, select a scenario
- Make sure number of cycles is valid (1-10)

**Page is blank:**
- Try refreshing the page (F5)
- Try a different browser (Chrome recommended)

### Python Version Issues

**Import Error: "No module named 'traffic_calculator'":**
```bash
# Make sure both files are in same folder:
ls
# You should see:
# traffic_calculator.py
# traffic_simulation_interactive.py
```

**Input not working:**
- Make sure you're typing numbers
- Press Enter after each input
- Use integers only (no decimals)

---

## 📝 Example Session (Web)

1. **Open** `traffic_visualization_interactive.html`
2. **Click** "Custom Input" mode card
3. **Set** number of cycles to 3
4. **Enter** counts for Cycle 1: [25, 30, 20, 15]
5. **Enter** counts for Cycle 2: [15, 20, 25, 30]
6. **Enter** counts for Cycle 3: [10, 10, 10, 10]
7. **Click** "Start Simulation"
8. **Watch** the lights change
9. **Observe** green times adjust to traffic
10. **See** buffer activate in last 10 seconds

---

## 📝 Example Session (Python)

```bash
$ python traffic_simulation_interactive.py

🎯 Choose simulation mode:
   1. Random
   2. Custom
   3. Scenarios

Enter choice: 3

📋 Available test scenarios:
   1. Light traffic
   2. Moderate traffic
   3. Heavy traffic
   ...

Enter scenario: 3

✅ Mode: Test Scenario - Heavy Traffic
📊 Running 3 predefined cycles

   Cycle 1: [35, 40, 38, 42]
   Cycle 2: [40, 38, 41, 39]
   Cycle 3: [37, 42, 40, 38]

Press ENTER to start...

[Watch detailed simulation logs...]

✅ Successfully completed 3 traffic cycles
✨ Simulation finished!
```

---

## 🎯 Best Practices

### For Testing Algorithm:
1. Start with simple cases (equal traffic)
2. Test edge cases (zero vehicles, max vehicles)
3. Try unbalanced scenarios
4. Verify buffer works in all cases

### For Demonstrations:
1. Use test scenarios (pre-made, professional)
2. Web version looks better for presentations
3. Show the buffer warning feature
4. Explain how green times adapt

### For Development:
1. Use custom inputs for specific bugs
2. Python version gives detailed logs
3. Test with many cycles (5-10)
4. Verify calculations manually

---

## 🚀 Next Steps

Once comfortable with interactive simulation:

1. **Modify the algorithm** in `traffic_calculator.py`
2. **Test changes** with custom inputs
3. **Compare results** before/after changes
4. **Document edge cases** you discover
5. **Plan hardware integration** (ESP32 + Raspberry Pi)

---

## 🎉 Summary

You now have **4 ways** to run the simulation:

| File | Mode | Best For |
|------|------|----------|
| `traffic_visualization_interactive.html` | Web + Input | **Testing specific cases visually** |
| `traffic_simulation_interactive.py` | Python + Input | **Detailed testing with logs** |
| `traffic_visualization.html` | Web Auto | Quick demos |
| `traffic_simulation.py` | Python Auto | Development |

**Start with the interactive web version - it's the easiest and most fun!**

---

**Happy Testing! 🚦**
