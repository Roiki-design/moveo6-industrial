#include <ROBOT_hardware_interface/ROBOT_hardware_interface.h>
int main(int argc, char** argv)
{
    ros::init(argc, argv, "ROBOT_hardware_interface");
    ros::NodeHandle nh;
    ros::AsyncSpinner spinner(1);
    spinner.start();
    ROBOT_hardware_interface::ROBOTHardwareInterface ROBOT(nh);
    ros::spin();
    return 0;
}
