import math

# (We will measure these later)
# Lengths in cm
# We split Link 2 into two parts so we can measure them separately.
LINK_1 = 15.0        # Upper Arm (Shoulder to Elbow)

FOREARM_LENGTH = 15.0  # Elbow to Wrist
GRIPPER_LENGTH = 5.0   # Wrist to Tip of the Claw

# The math treats the Forearm and Gripper as one long arm
LINK_2 = FOREARM_LENGTH + GRIPPER_LENGTH

# Safety: Reach limit
MAX_REACH = LINK_1 + LINK_2

def solve_inverse_kinematics(x, y, z):
    """
    The Geometry Engine.
    Input: x, y, z target coordinates.
    Output: angles for base, shoulder, elbow.
    """
    print(f"Calculating path to: X={x}, Y={y}, Z={z}")

    # PART 1: THE BASE (Top-Down View)
    # atan2 handles the quadrants automatically.
    theta_base_rad = math.atan2(y, x)
    theta_base = math.degrees(theta_base_rad)

    # PART 2: THE TRIANGLE (Side View)

    # 1. Distance from Base to Target on the ground (Horizontal)
    r = math.sqrt(x**2 + y**2)

    # 2. Distance from Shoulder to Target in 3D (Hypotenuse)
    #    We use 'z' here because we are looking from the side.
    distance_to_target = math.sqrt(r**2 + z**2)

    # SAFETY CHECK (to prevent crashing in case the distance is too far)
    if distance_to_target > MAX_REACH:
        print("ERROR: Distance is too far!")
        return 0, 0, 0

    # LAW OF COSINES
    # Formula for the ELBOW angle (Theta 2)
    # cos(angle) = (a^2 + b^2 - c^2) / (2ab)
    cos_angle_elbow = (LINK_1**2 + LINK_2**2 - distance_to_target**2) / (2 * LINK_1 * LINK_2)

    # Safety: ensure value is between -1 and 1 for acos
    cos_angle_elbow = max(-1, min(1, cos_angle_elbow))

    theta_elbow_rad = math.acos(cos_angle_elbow)
    theta_elbow = math.degrees(theta_elbow_rad)

    # Formula for the SHOULDER angle (Theta 1)

    angle_to_target = math.atan2(z, r)

    cos_angle_shoulder = (LINK_1**2 + distance_to_target**2 - LINK_2**2) / (2 * LINK_1 * distance_to_target)
    cos_angle_shoulder = max(-1, min(1, cos_angle_shoulder)) # Safety clamp

    theta_shoulder_rad = angle_to_target + math.acos(cos_angle_shoulder)
    theta_shoulder = math.degrees(theta_shoulder_rad)

    return theta_base, theta_shoulder, theta_elbow

# TEST CODE: 
if __name__ == "__main__":
    # Test with a point we know works (Diagonal up)
    angles = solve_inverse_kinematics(10, 10, 10)

    print("-" * 30)
    print(f"Base Angle:     {angles[0]:.2f}°")
    print(f"Shoulder Angle: {angles[1]:.2f}°")
    print(f"Elbow Angle:    {angles[2]:.2f}°")
    print("-" * 30)
