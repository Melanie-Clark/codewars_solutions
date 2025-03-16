def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp):
    celsius_temp = 273.15 + temp
    return (((given_mass1 / molar_mass1) + (given_mass2 / molar_mass2))* 0.082 * celsius_temp) / volume