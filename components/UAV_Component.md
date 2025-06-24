| Component                | Purpose              | How Controlled   | Power Use        | Data Out           | Needs           |
|:-------------------------|:---------------------|:-----------------|:-----------------|:-------------------|:----------------|
| GPS                      | Position             | UART, PX4        | 0.1W             | Lat/Lon            | Satellite lock  |
| ESC                      | Motor control        | PWM              | 10-20W per motor | RPM                | FC signal       |
| LiDAR                    | Obstacle/altitude    | I2C/USB          | 1W+              | Distance           | Software driver |
| EO/IR Camera             | Surveillance         | CSI/USB          | 2-10W            | Image/stream       | Encoding        |
| Flight Controller        | Flight management    | Various          | 1-5W             | Sensor fusion data | Firmware        |
| IMU                      | Orientation sensing  | I2C/SPI          | 0.1-0.5W         | Accel/Gyro         | Calibration     |
| Barometer                | Altitude sensing     | I2C              | 0.1W             | Pressure/Altitude  | Shielding       |
| Compass (Magnetometer)   | Heading              | I2C/SPI          | 0.05W            | Magnetic field     | Calibration     |
| Battery (LiPo)           | Power supply         | nan              | 100-1000W+       | Voltage/Current    | Charger/BMS     |
| Power Distribution Board | Power management     | Wired            | nan              | Power rails        | Correct rating  |
| Telemetry Module         | Remote data          | UART             | 0.5-1W           | Flight data        | Antenna         |
| Radio Receiver           | RC input             | PWM/SBUS         | 0.1W             | Control signals    | Binding         |
| Antenna                  | Signal transmission  | Connected        | nan              | Signal strength    | Correct tuning  |
| Wi-Fi/Bluetooth Module   | Local comm           | UART             | 0.2-1W           | Data/commands      | Pairing         |
| 4G/5G Module             | Remote comm          | USB/UART         | 2-5W             | Network data       | SIM card        |
| Gimbal                   | Camera stabilization | PWM/I2C          | 1-10W            | Angle position     | Balance setup   |
| Servos                   | Actuation            | PWM              | 1-5W             | Position           | Control setup   |
| Cooling Fan              | Heat management      | Wired            | 1-3W             | nan                | Ventilation     |
| Altimeter                | Altitude             | I2C              | 0.1W             | Height             | Calibration     |
| Ultrasonic Sensor        | Close obstacle       | I2C/Analog       | 0.1-0.5W         | Distance           | Clear field     |
| SD Card Module           | Data storage         | SPI              | 0.1W             | Logs               | Formatted card  |
| LED Indicators           | Status display       | GPIO             | 0.1-0.5W         | Blink status       | Code mapping    |
| Autopilot                | Autonomous control   | I2C/UART         | Varies           | Command outputs    | Software        |
| Temperature Sensor       | Thermal status       | I2C              | 0.05W            | Temp data          | Shielding       |
| Radar                    | Obstacle detection   | SPI/USB          | 1-5W             | Range data         | Driver          |
| Microphone               | Audio input          | I2C/Analog       | 0.05W            | Sound              | Amplifier       |
| Speakers                 | Audio output         | PWM              | 0.1-1W           | Alerts             | Amp circuit     |