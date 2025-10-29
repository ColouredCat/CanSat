import analogio
import board

adc = analogio.AnalogIn(board.GP26)


def read_temperature():
    adc_raw = adc.value
    print(f"Raw ADC Value = {adc_raw}")
    adc_voltage = (adc_raw * 3.3) / 65536
    print(f"ADC voltage = {adc_voltage}")
