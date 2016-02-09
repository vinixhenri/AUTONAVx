class UserCode:
    def __init__(self):
        # TODO: tune gains
        self.Kp = 5
        self.Kd = 5
        self.last = 0.0
            
    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to compute_control_command
        :param x_measured: measured position (scalar)
        :param x_desired: desired position (scalar)
        :return - control command u
        '''
        # TODO: implement PD controller
        u = 0.0
        
        speed = (x_measured - self.last) / dt
        
        u = self.Kp * (x_desired - x_measured) + self.Kd * (0 - speed)
        
        self.last = x_measured
        
        return u
