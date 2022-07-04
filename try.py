def airResistance(T=0):
        T = T
        mod = T % 5
        if mod>=3:
            T += (5-mod)
        elif mod<3:
            T -= mod

        return T

