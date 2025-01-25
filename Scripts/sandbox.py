

def get_age_group(age): 
     """
     Devuelve el grupo de edad basado en la edad en años dentro del intervalo 0..150
     de lo contrario, devuelve 'desconocido'.
     """
 
     if 0 < age < 15:
         return 'infancia'
     elif age < 25:
         return 'adulto'
     elif age < 120:
         return 'vejez'
     else:
         return 'desconocido'
        # Completa esta función para que pase la prueba unitaria
 
def test_get_age_group():
    """prueba unitaria para get_age_group"""

    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adulto'
    assert get_age_group(64) == 'adulto'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'