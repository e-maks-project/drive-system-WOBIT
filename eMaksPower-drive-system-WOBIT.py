# -*- coding: iso-8859-1 -*-
#*===========================================================================*#
#*                                                                           *#
#* File     : eMaksPower-drive-system-WOBIT                               *#
#*                                                                           *#
#* Project  : mPLC                                                           *#
#* System   : MPU2                                                           *#
#* Version  : 1.00                                                           *#
#* Company  : Ko�o Naukowe Robotyk�w                                         *#
#*                                                                           *#
#* Author   : Hubert Graczyk / Piotr Saffarini                               *#
#* Date     : 17.09.2019                                                     *#
#*===========================================================================*#

Desired_Velocity = 0    # Joy X position               
max_velocity_positive = 3000     # Max velocity positive in RPM 
max_velocity_negative = 1000     # Max velocity positive in RPM  

# Configuration Init  -----------------------------------------------------------
def InitPars():
   Sp(0x3004, 0x00, 0)                # DEV_Enable - Disable
   Sp(0x3000, 0x00, 0x1)              # DEV_Cmd - Clear error
   Sp(0x3000, 0x00, 0x82)             # DEV_Cmd - Default parameter

   Sp(0x3221, 0x00, 40000)            # CURR_LimitMaxPos
   Sp(0x3223, 0x00, 40000)            # CURR_LimitMaxNeg
   Sp(0x3224, 0x01, 40000)            # CURR_DynLimitPeak
   Sp(0x3224, 0x02, 40000)            # CURR_DynLimitCont

   Sp(0x3240, 0x00, 40000)            # CURR_Acc_dI
   Sp(0x3241, 0x00, 40000)            # CURR_Acc_dT
   Sp(0x3242, 0x00, 40000)            # CURR_Dec_dI
   Sp(0x3243, 0x00, 10)               # CURR_Dec_dT
   Sp(0x3244, 0x00, 40000)            # CURR_Dec_QuickStop_dI
   Sp(0x3245, 0x00, 2)                # CURR_Dec_QuickStop_dT

   Sp(0x324C, 0x00, 1)                # CURR_RampType

   Sp(0x3350, 0x00, 0x94A)            # VEL_Feedback

   Sp(0x3550, 0x00, 0x94A)            # SVEL_Feedback

   Sp(0x3830, 0x00, 32000)            # PWM_Frequency

   Sp(0x3900, 0x00, 1)                # MOTOR_Type
   Sp(0x3901, 0x00, 3000)             # MOTOR_Nn
   Sp(0x3902, 0x00, 48000)            # MOTOR_Un

   Sp(0x3910, 0x00, 8)                # MOTOR_PolN
   Sp(0x3911, 0x00, 2)                # MOTOR_Polarity

   Sp(0x3962, 0x00, 2000)             # MOTOR_ENC_Resolution 
   
   # Movement parameters ------------------------------------------------------                 
   Sp(0x3003, 0x00, 3)                # DEV_Mode - VEL mode
   Sp(0x3300, 0x00, 1000)             # Velocity = 1000 RPM 
   Sp(0x334C, 0x00, 0)                # Deactivate the ramp generator 
     
   '''
   Sp(0x334C, 0x00, 1)                # Activate the ramp generator
   Sp(0x3340, 0x00, 2000)             # Acceleration_dV = 2000 RPM 
   Sp(0x3341, 0x00, 100)              # Acceleration_dT = 100 s                                                          
   Sp(0x3342, 0x00, 1000)             # Deceleration_dV = 1000 RPM
   Sp(0x3343, 0x00, 200)              # Deceleration_dT = 200 s   
   '''                                                         
   Sp(0x3321, 0x00, max_velocity_positive)             # Velocity pos. limit = 3000
   Sp(0x3323, 0x00, max_velocity_negative)             # Velocity neg. limit = 1000
   
   Sp(0x3004, 0x00, 1)                # DEV_Enable - Enable
       
# Configuration of CAN frames -------------------------------------------------

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
   #0x21D
   Sp(0x1600, 0x00, 0x0)              # Disable mapping
   Sp(0x1600, 0x01, 0x33400020)       # object 0: JOY_ADC_X AXIS in % (2 bytes)
   Sp(0x1600, 0x00, 0x1)              # Enable mapping with 1 objects

   #0x22D
   Sp(0x1601, 0x00, 0x0)              # Disable mapping       
   Sp(0x1601, 0x01, 0x51010110)       # object 0: JOY_ADC_Y AXIS in % (2 bytes)
   Sp(0x1601, 0x00, 0x1)              # Enable mapping with 1 objects          

   #0x30D
   Sp(0x1603, 0x00, 0x0)              # Disable mapping
   Sp(0x1603, 0x01, 0x31580008)       # object 0: LED Enable (1 bytes)
   Sp(0x1603, 0x02, 0x31580108)       # object 1: LED State (1 bytes)
   Sp(0x1603, 0x00, 0x2)              # Enable mapping with 2 objects

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
   #0x11D
   Sp(0x1A00, 0x00, 0x0)              # Disable mapping
   Sp(0x1A00, 0x01, 0x31100020)       # object 0: Electronic Voltage [mV](4 bytes)
   Sp(0x1A00, 0x02, 0x31110020)       # object 1: Power Voltage [mV](4 bytes)
   Sp(0x1A00, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x12D
   Sp(0x1A01, 0x00, 0x0)              # Disable mapping
   Sp(0x1A01, 0x01, 0x31120020)       # object 0: Motor Voltage [mV] (4 bytes)
   Sp(0x1A01, 0x02, 0x31130020)       # object 1: Motor Current [mA] (4 bytes)
   Sp(0x1A01, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x13D
   Sp(0x1A02, 0x00, 0x0)              # Disable mapping
   Sp(0x1A02, 0x01, 0x31140010)       # object 0: Electronic Temperature (2 bytes)
   Sp(0x1A02, 0x00, 0x1)              # Enable mapping with 1 objects   
   
   #0x14D
   Sp(0x1A03, 0x00, 0x0)              # Disable mapping
   Sp(0x1A03, 0x01, 0x33620020)       # object 0: Actual Velocity (4 bytes) 
   Sp(0x1A03, 0x02, 0x37620020)       # object 1: Actual Motor Position (4 bytes)
   Sp(0x1A03, 0x00, 0x2)              # Enable mapping with 2 objects


# Main program ================================================================
InitPars()                                     
Sp(0x2040,0x02,5)                     # NMT communication Enable   
if(Desired_velocity>50):
   Sp(0x3300,0x00,(Desired_velocity-50)/50*max_velocity_positive)    # Velocity positive- desired value
else:   
   Sp(0x3300,0x00,(50-Desired_velocity)/50*max_velocity_negative)    # Velocity negative - desired value
 
# Main loop -------------------------------------------------------------------
while 1:
   pass

