# JSON (Javascript Object Notion) | Diccionario de datos
# Nota: Si una llave se repite su valor será modificado y se perderá el anterior valor

curso = {
    "nombre": "Backend",
    'dificultad': "Difícil",
    'skills': [
        {
            'nombre': 'Base de datos',
            'nivel': 'Intermedio'
        },
        {
            'nombre': 'ORM',
            'nivel': 'Avanzado'
        }
    ],
}

print(curso['dificultad'])

# quiero el nivel del skill ORM
print(curso['skills'][1]['nivel'])

personas = [
    {
        'nombre': 'Juan',
        'nacionalidad': 'Mexicana',
        'hobbies': [
            {
                'nombre': 'Leer',
                'experiencia': '2 años'
            },
            {
                'nombre': 'Programar',
                'experiencia': '1 mes'
            }
        ]
    },
    {
        'nombre': 'Juliana',
        'nacionalidad': 'Colombiana',
        'hobbies': [
            {
                'nombre': 'Montar bicicleta',
                'experiencia': '4 años'
            },
            {
                'nombre': 'Bases de datos',
                'experiencia': '18 meses'
            }
        ]
    }
]

# La nacionalidad de la primera persona
print(personas[0]['nacionalidad'])

# El nombre del primer hobby de la segunda persona
print(personas[1]['hobbies'])

# La experiencia del segundo hobby de la primera persona
print(personas[0]['hobbies'][1]['experiencia'])
