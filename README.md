# Sea Level Rise (SLR) AR App Setup & User Manual

## 1\. System Requirements & Checklist

* **VR Headset:** Meta Quest 3 or Quest Pro headset with both handheld controllers.  
* **Laptop:** MacBook running the Python Eyedropper Server.  
* **Network:** Both the MacBook and Quest headset must be connected to the exact same Wi-Fi network or phone personal hotspot.  
* **Files:** Python server file (`pythonserver.py`).  
* **Phone:** Any smartphone with a camera to take calibration photos. (perferably Iphone to use airdrop)

---

## 2\. Setting Up the Laptop (Host Machine)

1. Open the **Terminal** app on your Mac (press `Command + Space`, type `Terminal`, and hit `Enter`).  
2. Navigate to the folder containing your server file using the `cd` command (for example: `cd Downloads` or `cd Desktop/SLR-Project`).  
3. Start the server by running:

```sh
python pythonserver.py
```

4. Verify the server is running. You will see text ending with:

```
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:8080
```

*(Note: You do not need to look up or type any IP addresses manually, the app automatically discovers your laptop over the shared network\!)*

---

## 3\. Setting Up at the Beach (Field Prep & Orientation)

Follow these quick steps before putting on the headset so the simulation matches the real beach:

1. **Take Your Calibration Photos:**  
   * Use your phone to take a clear, close up photo of the real ocean water.  
   * Take a second clear, close up photo of the sand near your feet.  
2. **Transfer to Laptop:**  
   * Send both photos to your MacBook (using AirDrop is fastest).  
   * Open both images on your laptop screen so they are clearly visible.  
3. **Physical Orientation:**  
   * Stand at your designated shoreline observation spot.  
   * **Face straight toward the real ocean.**  
   * *Why it matters —* The virtual floodwater is generated directly in front of you. Facing the ocean makes sure the digital water aligns with the real horizon.

---

## 4\. Putting on the Headset & Launching

1. Put on the Quest headset and pick up both controllers.  
2. Open your **App Library**, find the **SLR Simulation** app under **Unknown Sources**, and launch it.  
3. Allow a few seconds for the app to load and it will open directly to the **Beach Selection Menu**.

---

## 5\. How to Use the App (Step by Step)

### Step 1: Pick Your Beach

* Tilt your **Right Controller Thumbstick (Left or Right)** to cycle through the available beaches:  
  * Rocky Neck  
  * Silver Sands  
  * Sherwood Island  
  * Hammonasset  
* Press the **\[A\] Button** on the right controller to confirm your choice.

### Step 2: Calibrate the Real World Colors

* The headset will switch to passthrough mode so you can see your real surroundings and your open laptop.  
* Look at your laptop screen showing your reference photos:  
  * Look at the water photo and click down on the **Right Thumbstick (R3)** to sample water color.  
  * Look at the sand photo and click down on the **Left Thumbstick (L3)** to sample sand color.  
* *Haptic Feedback:*  
  * Controllers will **vibrate once** when a color is successfully captured.  
  * Controllers will **vibrate twice** if there is an error (see Section 6).  
* Once both are calibrated, press the **\[A\] Button** to load the first era (**2030**).

### Step 3: Explore the Timeline

* **Advance the Year:** Press the **\[A\] Button** on the right controller to move through the timeline: **2030 → 2050 → 2100**.

---

## 6\. Boundary & View Reset Reminders

* **Stay in Position:** Try not to walk too far outside your starting spot so the virtual water model stays anchored properly to the physical shore.  
* **Fix / Recenter Orientation:** If the virtual water ever looks crooked or shifted away from the real ocean, face directly forward toward the water, press and hold the **Meta / Options button** (the flat button on your right controller), or select the **Recenter** icon from the universal menu to instantly snap your view back into alignment.

---

## 7\. Troubleshooting Common Issues

1. **App skips or jumps past a scene when pressing \[A\]:** Ensure you tap the button once gently rather than double tapping. Wait roughly 1 to 2 seconds between transitions to allow the safety cooldown timer to reset.  
2. **Colors fail to update after clicking the thumbstick:** Double check that your laptop and Quest headset are on the exact same Wi-Fi network or mobile hotspot. If using university or public Wi-Fi, ensure you have logged in through their web portal, or switch both devices to a phone hotspot.  
   