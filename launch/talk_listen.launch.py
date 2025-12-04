import launch
import launch.actions
import launch.subtitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package = 'mypkg'
            executable = 'talker',
            )
        listener = launch_ros.actions.Node(
                package = 'mypkg'
                executable = 'listener'
                output = 'screen'
                )

        return launch.launchDescription([talker , listener])

