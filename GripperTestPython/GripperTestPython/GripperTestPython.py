import sys
import glob
import dh_modbus_gripper
import dh_socket_gripper
from time import sleep

m_gripper = dh_modbus_gripper.dh_modbus_gripper()
#m_gripper = dh_socket_gripper.dh_socket_gripper()

def modbus_gripper() :
    port='/dev/ttyUSB0'   # change port
    baudrate=115200
    initstate = 0
    g_state = 0 
    force = 100
    speed = 100

    m_gripper.open(port,baudrate)
    m_gripper.Initialization();
    print('Send grip init')

    while(initstate != 1) :
        initstate = m_gripper.GetInitState();
        sleep(0.2)
        
    m_gripper.SetTargetForce(force)
    m_gripper.SetTargetSpeed(speed)

    while True:
        g_state = 0
        m_gripper.SetTargetPosition(2)
        while(g_state == 0) :
            g_state = m_gripper.GetGripState()
            print(g_state)
            sleep(0.2)
        print("CHANGE")
        g_state = 0;
        m_gripper.SetTargetPosition(1000)
        while(g_state == 0) :
            g_state = m_gripper.GetGripState()  # 0 means moving 1 means arrive 2 means jiazhu 3 means diaoluo
            print(g_state)
            sleep(0.2)
        print("CHANGE")
        g_state = 0
        m_gripper.SetTargetPosition(500)
        while(g_state == 0) :
            g_state = m_gripper.GetGripState()
            print(g_state)
            sleep(0.2)
    m_gripper.close()

def socket_gripper() :
    ip='192.168.1.29'
    port=8888
    initstate = 0
    g_state = 0
    force = 100
    speed = 100

    m_gripper.open(ip,port)
    m_gripper.Initialization()
    print('Send grip init')

    while(initstate != 1) :
        initstate = m_gripper.GetInitState();
        sleep(0.2)
        
    m_gripper.SetTargetForce(force)
    #m_gripper.SetTargetSpeed(speed)

    while True:
        g_state = 0
        m_gripper.SetTargetPosition(0)
        while(g_state == 0) :
            g_state = m_gripper.GetGripState()
            sleep(0.2)
        
        g_state = 0;
        m_gripper.SetTargetPosition(1000)
        while(g_state == 0) :
            g_state = m_gripper.GetGripState()
            sleep(0.2)
    m_gripper.close()

if __name__ == '__main__':
    #socket_gripper()
    modbus_gripper()
            


