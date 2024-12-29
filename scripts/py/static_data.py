
colors_lines_jerez = {
	"1":  "#FFD400",
    "2":  "#f33600",
    "3":  "#e9ac14",
    "4":  "#c5013a",
    "5":  "#991e4f",
    "6":  "#bd9600",
    "7":  "#6d9000",
    "8":  "#007e80",
    "9":  "#00609d",
    "10": "#8356c4",
    "11": "#df9fc3",
    "12": "#b15215",
    "13": "#00adb3",
    "14": "#d13866",
    "15": "#232f5c",
    "16": "#b5be03",
    "17": "#752315",
    "18": "#00e0f4",
}


final_bus_stop_code_switcher = {
    1:401, # San Telmo
    2:334, # Picadueña baja
    3:261, # Las Torres
    4:206, # Hipercor
    5:195, # Guadalcacín
    6:60, # Avda. Europa
    7:172, # "Estella"
    8:-1, # Circulares
    9:-1, # Circulares
    10:447, # Urgencias
    11:243, # La Marquesa
    12:61, # Avda. Europa
    13:41, # Asisa
    14:384, # Rotonda 6
    15:157, # El Portal
    16:313, # Ortega y Gasset
    17:301, # Montealto
    18:32, # Area Sur
}


bus_lines_descriptions = {
    "1": "Esteve - San Telmo", 
    "2": "Esteve - Picadueñas", 
    "3": "Esteve - Las Torres", 
    "4": "Esteve - San Joaquín - Hipercor", 
    "5": "Canal Sur - Guadalcacín", 
    "6": "Esteve - La Granja", 
    "7": "Angustias - Estella", 
    "8": "Circular 1 - Sentido antihorario", 
    "9": "Circular 2 - Sentido horario", 
    "10": "La Canaleja - Esteve - Hospital", 
    "11": "Esteve » La Marquesa", 
    "12": "Corredera - San José Obrero", 
    "13": "Alcázar - Puertas del Sur - Asisa", 
    "14": "Esteve - Rotonda Nº6", 
    "15": "Nueva Jarilla - Guadalcacín - Angustias - El Portal", 
    "16": "Rotonda Casino - Hipercor - Ortega y Gasset", 
    "17": "Rotonda Casino - Montealto", 
    "18": "Corredera - Luz Shopping"
}

direction_names = {
    1: [
        {
            "destination": "Vallesequillo II",
            "direction": "San Telmo"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ],
    2: [
        {
            "destination": "Picadueña Baja",
            "direction": "Picadueñas"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ] ,
    3: [
        {
            "destination": "Av. Soleá",
            "direction": "Las Torres"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ] ,
    4: [
        {
            "destination": "Guatemala II",
            "direction": "Hipercor"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ],
    5: [
        {
            "destination": "C/ Divina Pastora",
            "direction": "Guadalcacín"
        },
        {
            "destination": "Diego F. Herrera",
            "direction": "La Corredera"
        }
    ],
    6: [
        {
            "destination": "Av. de Europa",
            "direction": "La Granja"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ],
    7: [
        {
            "destination": "C/ del Pozo",
            "direction": "Estella"
        },
        {
            "destination": "C/ Cartuja",
            "direction": "Pz. Angustias-Bodega"
        }
    ],
    10: [
        {
            "destination": "Consultas Externas",
            "direction": "Hospital"
        },
        {
            "destination": "Parque Eroski",
            "direction": "La Canaleja"
        }
    ],
    11: [
        {
            "destination": "C/ Alcázar de Jerez I",
            "direction": "La Marquesa"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ],
    12: [
        {
            "destination": "Arroyo Membrillar",
            "direction": "San José Obrero"
        },
        {
            "destination": "Diego F. Herrera",
            "direction": "Corredera"
        }
    ],
    13: [
        {
            "destination": "Vallesequillo II",
            "direction": "Zona Sur"
        },
        {
            "destination": "Torresoto",
            "direction": "Alcázar-Centro"
        }
    ],
    14: [
        {
            "destination": "El Encinar",
            "direction": "Rotonda nº 6"
        },
        {
            "destination": "Pz. Angustias-Canal Sur",
            "direction": "Plaza Esteve"
        }
    ],
    15: [
        {
            "destination": "Estaciones",
            "direction": "Pz. Angustias-El Portal"
        },
        {
            "destination": "Recauchutados Córdoba",
            "direction": "El Portal"
        },
        {
            "destination": "Madre de Dios",
            "direction": "Pz. Angustias-N.Jarilla"
        },
        {
            "destination": "Nueva Jarilla II",
            "direction": "Nueva Jarilla"
        }
    ],
    16: [
        {
            "destination": "Las Flores",
            "direction": "Ortega y Gasset"
        },
        {
            "destination": "Santo Domingo",
            "direction": "Rotonda Casinos"
        }
    ],
    17: [
        {
            "destination": "C/ Doctor Arruga",
            "direction": "Montealto"
        },
        {
            "destination": "Santo Domingo",
            "direction": "Rotonda Casinos"
        }
    ],
    18: [
        {
            "destination": "Alcampo",
            "direction": "Luz Shopping"
        },
        {
            "destination": "Diego F. Herrera",  
            "direction": "Corredera"
        }
    ]
}


non_regular_bus_stops = ['Garvey', 'Los Villares', 'Los Villares II', 'Ciudad del Transporte', 'IVECO', 'PCTA', 'Campo de la Juventud', 'Agrimensor',
    'Alvar Fañez', 'Rodrigo de Jerez', 'Media Markt', 'Guadabajaque', 'Campus El Sabio', 'Resid. Rancho Colores', 
    'Gta. de Guadabajaque', 'Media Markt', 'Rodrigo de Jerez', 'Carrefour Sur.'
]
