# -*- coding: iso-8859-1 -*-
#*===========================================================================*#
#*                                                                           *#
#* File     : eMaksPower-drive-system-WOBIT                                  *#
#*                                                                           *#
#* Project  : mPLC                                                           *#
#* System   : MPU2                                                           *#
#* Version  : 1.00                                                           *#
#* Company  : Ko�o Naukowe Robotyk�w                                         *#
#*                                                                           *#
#* Author   : Hubert Graczyk / Piotr Saffarini                               *#
#* Date     : 29.11.2019                                                     *#
#*===========================================================================*#

DefUserVar(name="x_dir", value = 1, descr ="", min_value=0x00, max_value =0xFFFF)# X DIR - 0x5101.01h
DefUserVar(name="x_axis_value", value = 0, descr ="", min_value=0x0, max_value =0xFFFF)# X Joy position - 0x5101.02h

DefUserVar(name="y_dir", value = 1, descr ="", min_value=0x00, max_value =0xFFFF)# Y DIR - 0x5102.01h
DefUserVar(name="y_axis_value", value = 0, descr ="", min_value=0x0, max_value =0xFFFF)# Y Joy position - 0x5102.02h

DefUserVar(name="x_precent_value", value = 0, descr ="", min_value=0x0, max_value =0xFF)# X Joy position in precentage scale - 0x5103.01h
DefUserVar(name="y_precent_value", value = 0, descr ="", min_value=0x0, max_value =0xFF)# Y Joy position in precentage scale - 0x5103.02h

# Configuration Init  -----------------------------------------------------------
def InitPars():
   Sp(0x3004, 0x00, 0)                # DEV_Enable - Disable
   Sp(0x3000, 0x00, 0x1)              # DEV_Cmd - Clear error
   Sp(0x3000, 0x00, 0x82)             # DEV_Cmd - Default parameter

   # Current Limits
   Sp(0x3221, 0x00, 65000)            # CURR_LimitMaxPos
   Sp(0x3223, 0x00, 65000)            # CURR_LimitMaxNeg

   # Current Ramp deactivate
   #Sp(0x324C, 0x00, 0)                # CURR_RampType deactivate

   '''
   # Current Ramp activate
   Sp(0x324C, 0x00, 1)                # CURR_RampType activate

   # Acceleration ramp = 4000[mA] / 1000[ms]
   Sp(0x3240, 0x00, 4000)             # CURR_Acc_dI
   Sp(0x3241, 0x00, 1000)             # CURR_Acc_dT

   # Deceleration ramp = 4000[mA] / 1000[ms]
   Sp(0x3242, 0x00, 4000)             # CURR_Dec_dI
   Sp(0x3243, 0x00, 1000)             # CURR_Dec_dT

   # QuickStop ramp = 20000[mA] / 100[ms]
   Sp(0x3244, 0x00, 20000)            # CURR_Dec_QuickStop_dI
   Sp(0x3245, 0x00, 100)              # CURR_Dec_QuickStop_dT
   '''

   Sp(0x3350, 0x00, 0x94A)            # VEL_Feedback
   Sp(0x3550, 0x00, 0x94A)            # SVEL_Feedback

   Sp(0x3830, 0x00, 32000)            # PWM_Frequency

   # Motor parameters ------------------------------------------------------
   Sp(0x3900, 0x00, 1)                # MOTOR_Type
   Sp(0x3901, 0x00, 3000)             # MOTOR_Nn
   Sp(0x3902, 0x00, 48000)            # MOTOR_Un
   Sp(0x3910, 0x00, 8)                # MOTOR_PolN
   Sp(0x3911, 0x00, 2)                # MOTOR_Polarity

   # Movement parameters ------------------------------------------------------
   Sp(0x3003, 0x00, 3)                # DEV_Mode - VEL mode
   Sp(0x3304, 0x00, 0x0300)           # Enable Velocity from 0x3300 register
   Sp(0x3300, 0x00, 0)                # Velocity = 0 RPM

   # Velocity Limits
   Sp(0x3321, 0x00, 100)             # VEL_LimitMaxPos - pos. limit = 1000
   Sp(0x3323, 0x00, -600)            # VEL_LimitMaxNeg - neg. limit = -1000

   # Velocity Ramp deactivate
   #Sp(0x334C, 0x00, 0)               # Deactivate the ramp generator

   # Velocity Ramp activate
   Sp(0x334C, 0x00, 1)                # Activate the ramp generator

   # Acceleration ramp = 1000[RPM] / 5000[ms]
   Sp(0x3340, 0x00, 1000)             # Acceleration_dV = 1000 RPM
   Sp(0x3341, 0x00, 5000)             # Acceleration_dT = 5000 ms

   # Deceleration ramp = 1000[RPM] / 3000[ms]
   Sp(0x3342, 0x00, 1000)             # Deceleration_dV = 1000 RPM
   Sp(0x3343, 0x00, 1000)             # Deceleration_dT = 1000 ms

   # QuickStop deceleration = 3000[RPM] / 500[ms]
   Sp(0x3344, 0x00, 3000)             # VEL_Dec_QuickStop_dV = 3000 RPM
   Sp(0x3345, 0x00, 100)              # VEL_Dec_QuickStop_dT = 500 ms


   # Velocity and Current regulators ------------------------------------------

   # PID Velocity regulator
   Sp(0x3310, 0x00, 290)             # VEL_Kp - Kp = 300
   Sp(0x3311, 0x00, 80)               # VEL_Ki - Ki = 60
   Sp(0x3312, 0x00, 100)               # VEL_Kd - Kd = 80

   # PI Current regulator
   Sp(0x3210, 0x00, 50)               # CURR_Kp - set factor Kp of the current controller
   Sp(0x3211, 0x00, 32)               # CURR_Ki - set factor Ki of the current controller

   Sp(0x3004, 0x00, 1)                # DEV_Enable - Enable

# Configuration of CAN frames -------------------------------------------------
   Sp(0x2011, 0x02, 1684107116)       # ...tion - Default parameter communication
   Sp(0x2011, 0x05, 1684107116)       # DS2000_RestoreD...000 - Default parameter

   Sp(0x2011, 0x02, 1684107116)       # ...tion - Default parameter communication
   Sp(0x2011, 0x05, 1684107116)       # DS2000_RestoreD...000 - Default parameter

# ===== RX CAN CONFIG ===== #
   Sp(0x1400, 0x01, 0xC000021D)       # COP_RxPDO1_CommunicationParameter_CobId
   Sp(0x1400, 0x01, 0x4000021D)       # COP_RxPDO1_CommunicationParameter_CobId

   Sp(0x1401, 0x01, 0xC000022D)       # COP_RxPDO2_CommunicationParameter_CobId
   Sp(0x1401, 0x01, 0x4000022D)       # COP_RxPDO2_CommunicationParameter_CobId

   Sp(0x1402, 0x01, 0xC000030D)       # COP_RxPDO3_CommunicationParameter_CobId
   Sp(0x1402, 0x01, 0x4000030D)       # COP_RxPDO3_CommunicationParameter_CobId

# ===== RX FRAME DATA ===== #
   #0x21D - AXIS X
   Sp(0x1600, 0x00, 0x0)              # Disable mapping
   Sp(0x1600, 0x01, 0x51010210)       # object 0: JOY_ADC_X AXIS Value   (2 bytes)
   Sp(0x1600, 0x02, 0x51010110)       # object 1: DIR: 1-Forward, 0-Rear (2 byte)
   Sp(0x1600, 0x00, 0x2)              # Enable mapping with 3 objects

   #0x22D - AXIS Y
   Sp(0x1601, 0x00, 0x0)              # Disable mapping
   Sp(0x1601, 0x01, 0x51020210)       # object 0: JOY_ADC_Y AXIS Value   (2 bytes)
   Sp(0x1601, 0x02, 0x51020110)       # object 1: DIR: 1-Forward, 0-Rear (2 byte)
   Sp(0x1601, 0x00, 0x2)              # Enable mapping with 3 objects

   #0x30D - LEDs State
   Sp(0x1602, 0x00, 0x0)              # Disable mapping
   Sp(0x1602, 0x01, 0x31580008)       # object 0: LED Enable (1 bytes)
   Sp(0x1602, 0x02, 0x31580108)       # object 1: LED State  (1 bytes)
   Sp(0x1602, 0x00, 0x2)              # Enable mapping with 2 objects

   # ===== TX CAN CONFIG ===== #
   Sp(0x1800, 0x01, 0xC000011D)       # COP_TxPDO1_CommunicationParameter_CobId
   Sp(0x1800, 0x01, 0x4000011D)       # COP_TxPDO1_CommunicationParameter_CobId

   Sp(0x1801, 0x01, 0xC000012D)       # COP_TxPDO2_CommunicationParameter_CobId
   Sp(0x1801, 0x01, 0x4000012D)       # COP_TxPDO2_CommunicationParameter_CobId

   Sp(0x1802, 0x01, 0xC000013D)       # COP_TxPDO3_CommunicationParameter_CobId
   Sp(0x1802, 0x01, 0x4000013D)       # COP_TxPDO3_CommunicationParameter_CobId

   Sp(0x1803, 0x01, 0xC000014D)       # COP_TxPDO4_CommunicationParameter_CobId
   Sp(0x1803, 0x01, 0x4000014D)       # COP_TxPDO4_CommunicationParameter_CobId


   # ===== TX FRAME DATA ===== #
   #0x31D
   Sp(0x1A00, 0x00, 0x0)              # Disable mapping
   Sp(0x1A00, 0x01, 0x31100020)       # object 0: Electronic Voltage [mV](4 bytes)
   Sp(0x1A00, 0x02, 0x31110020)       # object 1: Power Voltage [mV](4 bytes)
   Sp(0x1A00, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x32D
   Sp(0x1A01, 0x00, 0x0)              # Disable mapping
   Sp(0x1A01, 0x01, 0x31120020)       # object 0: Motor Voltage [mV] (4 bytes)
   Sp(0x1A01, 0x02, 0x31130020)       # object 1: Motor Current [mA] (4 bytes)
   Sp(0x1A01, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x33D
   Sp(0x1A02, 0x00, 0x0)              # Disable mapping
   Sp(0x1A02, 0x01, 0x31140010)       # object 0: Electronic Temperature (2 bytes)
   Sp(0x1A02, 0x00, 0x1)              # Enable mapping with 1 objects

   #0x34D
   Sp(0x1A03, 0x00, 0x0)              # Disable mapping
   Sp(0x1A03, 0x01, 0x33000020)       # object 0: Actual Velocity (4 bytes)
   Sp(0x1A03, 0x02, 0x37620020)       # object 1: Actual Motor Position (4 bytes)
   Sp(0x1A03, 0x00, 0x2)              # Enable mapping with 2 objects



# Main program ----------------------------------------------------------------
InitPars()
Sp(0x2040,0x02,5)                     # NMT communication Enable

# Main loop -------------------------------------------------------------------
while 1:
   x_precent_value = (x_axis_value*128)/65535  #precentage conversion

   # Drive forward
   if(x_dir == 1 and (x_precent_value > 15) and (115*x_precent_value/100 * Gp(0x3323, 0x00)/100)<Gp(0x3362, 0x00)):
     Sp(0x3004, 0x00, 1)                # DEV_Enable - Enable
     Sp(0x3300, 0x00, (115*x_precent_value/100 * Gp(0x3323, 0x00)/100))

   # Drive backwards
   elif(x_dir == 0 and (x_precent_value > 15)):
     Sp(0x3004, 0x00, 1)                # DEV_Enable - Enable
     Sp(0x3300, 0x00, (130*x_precent_value/100 * Gp(0x3321, 0x00)/100))

   # Stop
   #elif(x_precent_value < 15 and (Gp(0x3361, 0x00)<50 and Gp(0x3361, 0x00)>-50)):
   elif(x_precent_value < 15 and Gp(0x3362, 0x00)<50):
     Sp(0x3300, 0x00, 0)
     Sp(0x3004, 0x00, 0)                # DEV_Enable - Disable


   #===== TO DO =====#
   #                 #
   # QuickStop Event #
   #                 #
   #     aktywne     #
   #    hamowanie    #
   #    silnikiem    #
   #                 #
   #=================#




