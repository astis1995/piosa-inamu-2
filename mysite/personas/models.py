from django.db import models
from datetime import date
from django import forms

PROVINCIAS = (
('sanjose', 'San Jose'),
('alajuela', 'Alajuela'),
('heredia', 'Heredia'),
('cartago', 'Cartago'),
('limon', 'Limón'),
('puntarenas', 'Puntarenas'),
('guanacaste', 'Guanacaste'),
)
ACTIVIDADES  = (('agroindustria','Agroindustria'),('agropecuaria','Agropecuaria'),('servicios','Servicios')
,('artesania','Artesanía'),('turismo','Turismo'),('otro','Otro'))

CANTONES = (('San Carlos' , 'San Carlos')
,('Talamanca' , 'Talamanca')
,('Pococí' , 'Pococí')
,('Buenos Aires' , 'Buenos Aires')
,('Sarapiquí' , 'Sarapiquí')
,('Osa' , 'Osa')
,('Pérez Zeledón' , 'Pérez Zeledón')
,('Puntarenas' , 'Puntarenas')
,('Limón' , 'Limón')
,('Golfito' , 'Golfito')
,('Turrialba' , 'Turrialba')
,('Upala' , 'Upala')
,('Liberia' , 'Liberia')
,('La Cruz' , 'La Cruz')
,('Los Chiles' , 'Los Chiles')
,('Nicoya' , 'Nicoya')
,('Santa Cruz' , 'Santa Cruz')
,('Bagaces' , 'Bagaces')
,('San Ramón' , 'San Ramón')
,('Coto Brus' , 'Coto Brus')
,('Siquirres' , 'Siquirres')
,('Matina' , 'Matina')
,('Guatuso' , 'Guatuso')
,('Cañas' , 'Cañas')
,('Abangares' , 'Abangares')
,('Tilarán' , 'Tilarán')
,('Corredores' , 'Corredores')
,('Carrillo' , 'Carrillo')
,('Guácimo' , 'Guácimo')
,('Nandayure' , 'Nandayure')
,('Puriscal' , 'Puriscal')
,('Quepos' , 'Quepos')
,('Parrita' , 'Parrita')
,('Turrubares' , 'Turrubares')
,('Paraíso' , 'Paraíso')
,('Dota' , 'Dota')
,('Alajuela' , 'Alajuela')
,('Acosta' , 'Acosta')
,('Garabito' , 'Garabito')
,('Tarrazú' , 'Tarrazú')
,('Cartago' , 'Cartago')
,('Jiménez' , 'Jiménez')
,('Heredia' , 'Heredia')
,('Hojancha' , 'Hojancha')
,('Río Cuarto' , 'Río Cuarto')
,('Montes de Oro' , 'Montes de Oro')
,('Vázquez de Coronado' , 'Vázquez de Coronado')
,('Esparza' , 'Esparza')
,('Oreamuno' , 'Oreamuno')
,('El Guarco' , 'El Guarco')
,('Aserrí' , 'Aserrí')
,('Mora' , 'Mora')
,('Zarcero' , 'Zarcero')
,('Orotina' , 'Orotina')
,('Grecia' , 'Grecia')
,('Atenas' , 'Atenas')
,('Naranjo' , 'Naranjo')
,('San Mateo' , 'San Mateo')
,('León Cortés' , 'León Cortés')
,('Sarchí' , 'Sarchí')
,('Desamparados' , 'Desamparados')
,('Alvarado' , 'Alvarado')
,('Poás' , 'Poás')
,('Santa Ana' , 'Santa Ana')
,('Barva' , 'Barva')
,('Santa Bárbara' , 'Santa Bárbara')
,('San Rafael' , 'San Rafael')
,('La Unión' , 'La Unión')
,('San José' , 'San José')
,('Palmares' , 'Palmares')
,('Escazú' , 'Escazú')
,('Goicoechea' , 'Goicoechea')
,('Moravia' , 'Moravia')
,('San Isidro' , 'San Isidro')
,('Santo Domingo' , 'Santo Domingo')
,('Alajuelita' , 'Alajuelita')
,('Curridabat' , 'Curridabat')
,('Montes de Oca' , 'Montes de Oca')
,('Belén' , 'Belén')
,('Tibás' , 'Tibás')
,('San Pablo' , 'San Pablo')
,('Flores' , 'Flores')
)
DISTRITOS = (('Carmen' , 'Carmen')
,('Merced' , 'Merced')
,('Hospital' , 'Hospital')
,('Catedral' , 'Catedral')
,('Zapote' , 'Zapote')
,('San Francisco de Dos Ríos' , 'San Francisco de Dos Ríos')
,('La Uruca' , 'La Uruca')
,('Mata Redonda' , 'Mata Redonda')
,('Pavas' , 'Pavas')
,('Hatillo' , 'Hatillo')
,('San Sebastián' , 'San Sebastián')
,('San Miguel' , 'San Miguel')
,('San Antonio' , 'San Antonio')
,('San Rafael' , 'San Rafael')
,('Desamparados' , 'Desamparados')
,('San Juan de Dios' , 'San Juan de Dios')
,('San Rafael Arriba' , 'San Rafael Arriba')
,('Frailes' , 'Frailes')
,('Patarrá' , 'Patarrá')
,('San Cristóbal' , 'San Cristóbal')
,('Rosario' , 'Rosario')
,('Damas' , 'Damas')
,('San Rafael Abajo' , 'San Rafael Abajo')
,('Gravilias' , 'Gravilias')
,('Los Guido' , 'Los Guido')
,('Santiago' , 'Santiago')
,('Mercedes Sur' , 'Mercedes Sur')
,('Barbacoas' , 'Barbacoas')
,('Grifo Alto' , 'Grifo Alto')
,('Candelarita' , 'Candelarita')
,('Desamparaditos' , 'Desamparaditos')
,('Chires' , 'Chires')
,('San Marcos' , 'San Marcos')
,('San Lorenzo' , 'San Lorenzo')
,('San Carlos' , 'San Carlos')
,('Aserrí' , 'Aserrí')
,('Tarbaca' , 'Tarbaca')
,('Vuelta de Jorco' , 'Vuelta de Jorco')
,('San Gabriel' , 'San Gabriel')
,('Legua' , 'Legua')
,('Monterrey' , 'Monterrey')
,('Salitrillos' , 'Salitrillos')
,('Colón' , 'Colón')
,('Guayabo' , 'Guayabo')
,('Tabarcia' , 'Tabarcia')
,('Piedras Negras' , 'Piedras Negras')
,('Picagres' , 'Picagres')
,('Jaris' , 'Jaris')
,('Quitirrisí' , 'Quitirrisí')
,('Guadalupe' , 'Guadalupe')
,('San Francisco' , 'San Francisco')
,('Calle Blancos' , 'Calle Blancos')
,('Mata de Plátano' , 'Mata de Plátano')
,('Ipís' , 'Ipís')
,('Rancho Redondo' , 'Rancho Redondo')
,('Purral' , 'Purral')
,('Santa Ana' , 'Santa Ana')
,('Salitral' , 'Salitral')
,('Pozos' , 'Pozos')
,('Uruca' , 'Uruca')
,('Piedades' , 'Piedades')
,('Brasil' , 'Brasil')
,('Alajuelita' , 'Alajuelita')
,('San Josecito' , 'San Josecito')
,('Concepción' , 'Concepción')
,('San Felipe' , 'San Felipe')
,('San Isidro' , 'San Isidro')
,('Dulce Nombre de Jesús' , 'Dulce Nombre de Jesús')
,('Patalillo' , 'Patalillo')
,('Cascajal' , 'Cascajal')
,('San Ignacio' , 'San Ignacio')
,('Guaitil' , 'Guaitil')
,('Palmichal' , 'Palmichal')
,('Cangrejal' , 'Cangrejal')
,('Sabanillas' , 'Sabanillas')
,('San Juan' , 'San Juan')
,('Cinco Esquinas' , 'Cinco Esquinas')
,('Anselmo llorente' , 'Anselmo llorente')
,('León XIII' , 'León XIII')
,('Colima' , 'Colima')
,('San Vicente' , 'San Vicente')
,('San Jerónimo' , 'San Jerónimo')
,('La Trinidad' , 'La Trinidad')
,('San Pedro' , 'San Pedro')
,('Sabanilla' , 'Sabanilla')
,('Mercedes' , 'Mercedes')
,('San Pablo' , 'San Pablo')
,('San Juan de Mata' , 'San Juan de Mata')
,('San Luis' , 'San Luis')
,('Carara' , 'Carara')
,('Santa María' , 'Santa María')
,('Jardín' , 'Jardín')
,('Copey' , 'Copey')
,('Curridabat' , 'Curridabat')
,('Granadilla' , 'Granadilla')
,('Sánchez' , 'Sánchez')
,('Tirrases' , 'Tirrases')
,('San Isidro de El General' , 'San Isidro de El General')
,('El General' , 'El General')
,('Daniel Flores' , 'Daniel Flores')
,('Rivas' , 'Rivas')
,('Platanares' , 'Platanares')
,('Pejibaye' , 'Pejibaye')
,('Cajón' , 'Cajón')
,('Barú' , 'Barú')
,('Río Nuevo' , 'Río Nuevo')
,('Páramo' , 'Páramo')
,('La Amistad' , 'La Amistad')
,('San Andrés' , 'San Andrés')
,('Llano Bonito' , 'Llano Bonito')
,('Santa Cruz' , 'Santa Cruz')
,('Oriental' , 'Oriental')
,('Occidental' , 'Occidental')
,('San Nicolás' , 'San Nicolás')
,('Agua Caliente' , 'Agua Caliente')
,('Corralillo' , 'Corralillo')
,('Tierra Blanca' , 'Tierra Blanca')
,('Dulce Nombre' , 'Dulce Nombre')
,('Llano Grande' , 'Llano Grande')
,('Quebradilla' , 'Quebradilla')
,('Paraíso' , 'Paraíso')
,('Orosi' , 'Orosi')
,('Cachí' , 'Cachí')
,('Llanos de Santa Lucía' , 'Llanos de Santa Lucía')
,('Tres Ríos' , 'Tres Ríos')
,('San Diego' , 'San Diego')
,('San Ramón' , 'San Ramón')
,('Río Azul' , 'Río Azul')
,('Juan Viñas' , 'Juan Viñas')
,('Tucurrique' , 'Tucurrique')
,('Turrialba' , 'Turrialba')
,('La Suiza' , 'La Suiza')
,('Peralta' , 'Peralta')
,('Santa Teresita' , 'Santa Teresita')
,('Pavones' , 'Pavones')
,('Tuis' , 'Tuis')
,('Tayutic' , 'Tayutic')
,('Santa Rosa' , 'Santa Rosa')
,('Tres Equis' , 'Tres Equis')
,('La Isabel' , 'La Isabel')
,('Chirripó' , 'Chirripó')
,('Pacayas' , 'Pacayas')
,('Cervantes' , 'Cervantes')
,('Capellades' , 'Capellades')
,('Cot' , 'Cot')
,('Potrero Cerrado' , 'Potrero Cerrado')
,('Cipreses' , 'Cipreses')
,('El Tejar' , 'El Tejar')
,('Tobosi' , 'Tobosi')
,('Patio de Agua' , 'Patio de Agua')
,('Heredia' , 'Heredia')
,('Ulloa' , 'Ulloa')
,('Varablanca' , 'Varablanca')
,('Barva' , 'Barva')
,('San Roque' , 'San Roque')
,('Santa Lucía' , 'Santa Lucía')
,('San José de la Montaña' , 'San José de la Montaña')
,('Santo Domingo' , 'Santo Domingo')
,('Paracito' , 'Paracito')
,('Santo Tomás' , 'Santo Tomás')
,('Tures' , 'Tures')
,('Pará' , 'Pará')
,('Santa Bárbara' , 'Santa Bárbara')
,('Jesús' , 'Jesús')
,('Purabá' , 'Purabá')
,('Ángeles' , 'Ángeles')
,('San José' , 'San José')
,('La Ribera' , 'La Ribera')
,('La Asunción' , 'La Asunción')
,('San Joaquín' , 'San Joaquín')
,('Barrantes' , 'Barrantes')
,('Llorente' , 'Llorente')
,('Rincón de Sabanilla' , 'Rincón de Sabanilla')
,('Puerto Viejo' , 'Puerto Viejo')
,('La Virgen' , 'La Virgen')
,('Horquetas' , 'Horquetas')
,('Llanuras del Gaspar' , 'Llanuras del Gaspar')
,('Cureña' , 'Cureña')
,('Liberia' , 'Liberia')
,('Cañas Dulces' , 'Cañas Dulces')
,('Mayorga' , 'Mayorga')
,('Nacascolo' , 'Nacascolo')
,('Curubandé' , 'Curubandé')
,('Nicoya' , 'Nicoya')
,('Mansión' , 'Mansión')
,('Quebrada Honda' , 'Quebrada Honda')
,('Sámara' , 'Sámara')
,('Nosara' , 'Nosara')
,('Belén de Nosarita' , 'Belén de Nosarita')
,('Bolsón' , 'Bolsón')
,('Veintisiete de Abril' , 'Veintisiete de Abril')
,('Tempate' , 'Tempate')
,('Cartagena' , 'Cartagena')
,('Cuajiniquil' , 'Cuajiniquil')
,('Diriá' , 'Diriá')
,('Cabo Velas' , 'Cabo Velas')
,('Tamarindo' , 'Tamarindo')
,('Bagaces' , 'Bagaces')
,('La Fortuna' , 'La Fortuna')
,('Mogote' , 'Mogote')
,('Río Naranjo' , 'Río Naranjo')
,('Filadelfia' , 'Filadelfia')
,('Palmira' , 'Palmira')
,('Sardinal' , 'Sardinal')
,('Belén' , 'Belén')
,('Cañas' , 'Cañas')
,('Bebedero' , 'Bebedero')
,('Porozal' , 'Porozal')
,('Las Juntas' , 'Las Juntas')
,('Sierra' , 'Sierra')
,('Colorado' , 'Colorado')
,('Tilarán' , 'Tilarán')
,('Quebrada Grande' , 'Quebrada Grande')
,('Tronadora' , 'Tronadora')
,('Líbano' , 'Líbano')
,('Tierras Morenas' , 'Tierras Morenas')
,('Arenal' , 'Arenal')
,('Cabeceras' , 'Cabeceras')
,('Carmona' , 'Carmona')
,('Santa Rita' , 'Santa Rita')
,('Zapotal' , 'Zapotal')
,('Porvenir' , 'Porvenir')
,('Bejuco' , 'Bejuco')
,('La Cruz' , 'La Cruz')
,('Santa Cecilia' , 'Santa Cecilia')
,('La Garita' , 'La Garita')
,('Santa Elena' , 'Santa Elena')
,('Hojancha' , 'Hojancha')
,('Monte Romo' , 'Monte Romo')
,('Puerto Carrillo' , 'Puerto Carrillo')
,('Huacas' , 'Huacas')
,('Matambú' , 'Matambú')
,('Limón' , 'Limón')
,('Valle La Estrella' , 'Valle La Estrella')
,('Río Blanco' , 'Río Blanco')
,('Matama' , 'Matama')
,('Guápiles' , 'Guápiles')
,('Jiménez' , 'Jiménez')
,('La Rita' , 'La Rita')
,('Roxana' , 'Roxana')
,('Cariari' , 'Cariari')
,('La Colonia' , 'La Colonia')
,('Siquirres' , 'Siquirres')
,('Pacuarito' , 'Pacuarito')
,('Florida' , 'Florida')
,('Germania' , 'Germania')
,('Cairo' , 'Cairo')
,('Alegría' , 'Alegría')
,('Reventazón' , 'Reventazón')
,('Bratsi' , 'Bratsi')
,('Sixaola' , 'Sixaola')
,('Cahuita' , 'Cahuita')
,('Telire' , 'Telire')
,('Matina' , 'Matina')
,('Batán' , 'Batán')
,('Carrandi' , 'Carrandi')
,('Guácimo' , 'Guácimo')
,('Pocora' , 'Pocora')
,('Río Jiménez' , 'Río Jiménez')
,('Duacarí' , 'Duacarí')
,('Puntarenas' , 'Puntarenas')
,('Pitahaya' , 'Pitahaya')
,('Chomes' , 'Chomes')
,('Lepanto' , 'Lepanto')
,('Paquera' , 'Paquera')
,('Manzanillo' , 'Manzanillo')
,('Guacimal' , 'Guacimal')
,('Barranca' , 'Barranca')
,('Monte Verde' , 'Monte Verde')
,('Isla del Coco' , 'Isla del Coco')
,('Cóbano' , 'Cóbano')
,('Chacarita' , 'Chacarita')
,('Chira' , 'Chira')
,('Acapulco' , 'Acapulco')
,('El Roble' , 'El Roble')
,('Arancibia' , 'Arancibia')
,('Espíritu Santo' , 'Espíritu Santo')
,('San Juan Grande' , 'San Juan Grande')
,('Macacona' , 'Macacona')
,('Caldera' , 'Caldera')
,('Buenos Aires' , 'Buenos Aires')
,('Volcán' , 'Volcán')
,('Potrero Grande' , 'Potrero Grande')
,('Boruca' , 'Boruca')
,('Pilas' , 'Pilas')
,('Colinas' , 'Colinas')
,('Chánguena' , 'Chánguena')
,('Biolley' , 'Biolley')
,('Brunka' , 'Brunka')
,('Miramar' , 'Miramar')
,('La Unión' , 'La Unión')
,('Puerto Cortés' , 'Puerto Cortés')
,('Palmar' , 'Palmar')
,('Sierpe' , 'Sierpe')
,('Bahía Ballena' , 'Bahía Ballena')
,('Piedras Blancas' , 'Piedras Blancas')
,('Bahía Drake' , 'Bahía Drake')
,('Quepos' , 'Quepos')
,('Savegre' , 'Savegre')
,('Naranjito' , 'Naranjito')
,('Golfito' , 'Golfito')
,('Puerto Jiménez' , 'Puerto Jiménez')
,('Guaycará' , 'Guaycará')
,('Pavón' , 'Pavón')
,('San Vito' , 'San Vito')
,('Sabalito' , 'Sabalito')
,('Aguabuena' , 'Aguabuena')
,('Limoncito' , 'Limoncito')
,('Pittier' , 'Pittier')
,('Gutiérrez Braun' , 'Gutiérrez Braun')
,('Parrita' , 'Parrita')
,('Corredor' , 'Corredor')
,('La Cuesta' , 'La Cuesta')
,('Canoas' , 'Canoas')
,('Laurel' , 'Laurel')
,('Jacó' , 'Jacó')
,('Tárcoles' , 'Tárcoles')
)

class ProvinciasActivasModel(models.Model):

    provincia = models.CharField(max_length=140, choices=PROVINCIAS)
    def __str__(self):
        return self.provincia


class CantonesActivosModel(models.Model):
    canton = models.CharField(max_length=140, choices=CANTONES)
    provincia = models.ForeignKey(ProvinciasActivasModel, on_delete= models.CASCADE)
    def __str__(self):
        return self.canton

class DistritosActivosModel(models.Model):
    distrito = models.CharField(max_length=140, choices=DISTRITOS)
    canton = models.ForeignKey(CantonesActivosModel, on_delete= models.CASCADE)
    def __str__(self):
        return self.distrito

class ActividadesActivasModel(models.Model):
    actividad = models.CharField(max_length=140, choices=ACTIVIDADES)
    def __str__(self):
        return self.actividad

class ImagenesModel(models.Model):
    nombre = models.CharField(max_length=140)
    cedula = models.CharField(max_length=10)
    foto_de_perfil = models.BooleanField(default=False)
    foto_de_producto =models.BooleanField(default=False)
    imagen = models.ImageField()
    fecha = date.today().strftime("%d/%m/%Y")

    def __str__(self):

        return self.nombre + "_"+ self.fecha


class PersonaModel(models.Model):
    ACTIVIDADES  = (('agroindustria','Agroindustria'),('agropecuaria','Agropecuaria'),('servicios','Servicios')
    ,('artesania','Artesanía'),('turismo','Turismo'),('otro','Otro'))
    PREFERENCIAS_CONTACTO = (('whatsapp','Whatsapp'),('sms','Mensaje SMS convencional'),('email','Correo Electrónico'),('otro','Otro'))
    PROVINCIAS = (
    ('sanjose', 'San Jose'),
    ('alajuela', 'Alajuela'),
    ('heredia', 'Heredia'),
    ('cartago', 'Cartago'),
    ('limon', 'Limón'),
    ('puntarenas', 'Puntarenas'),
    ('guanacaste', 'Guanacaste'),
    )
    CANTONES = (('San Carlos' , 'San Carlos')
,('Talamanca' , 'Talamanca')
,('Pococí' , 'Pococí')
,('Buenos Aires' , 'Buenos Aires')
,('Sarapiquí' , 'Sarapiquí')
,('Osa' , 'Osa')
,('Pérez Zeledón' , 'Pérez Zeledón')
,('Puntarenas' , 'Puntarenas')
,('Limón' , 'Limón')
,('Golfito' , 'Golfito')
,('Turrialba' , 'Turrialba')
,('Upala' , 'Upala')
,('Liberia' , 'Liberia')
,('La Cruz' , 'La Cruz')
,('Los Chiles' , 'Los Chiles')
,('Nicoya' , 'Nicoya')
,('Santa Cruz' , 'Santa Cruz')
,('Bagaces' , 'Bagaces')
,('San Ramón' , 'San Ramón')
,('Coto Brus' , 'Coto Brus')
,('Siquirres' , 'Siquirres')
,('Matina' , 'Matina')
,('Guatuso' , 'Guatuso')
,('Cañas' , 'Cañas')
,('Abangares' , 'Abangares')
,('Tilarán' , 'Tilarán')
,('Corredores' , 'Corredores')
,('Carrillo' , 'Carrillo')
,('Guácimo' , 'Guácimo')
,('Nandayure' , 'Nandayure')
,('Puriscal' , 'Puriscal')
,('Quepos' , 'Quepos')
,('Parrita' , 'Parrita')
,('Turrubares' , 'Turrubares')
,('Paraíso' , 'Paraíso')
,('Dota' , 'Dota')
,('Alajuela' , 'Alajuela')
,('Acosta' , 'Acosta')
,('Garabito' , 'Garabito')
,('Tarrazú' , 'Tarrazú')
,('Cartago' , 'Cartago')
,('Jiménez' , 'Jiménez')
,('Heredia' , 'Heredia')
,('Hojancha' , 'Hojancha')
,('Río Cuarto' , 'Río Cuarto')
,('Montes de Oro' , 'Montes de Oro')
,('Vázquez de Coronado' , 'Vázquez de Coronado')
,('Esparza' , 'Esparza')
,('Oreamuno' , 'Oreamuno')
,('El Guarco' , 'El Guarco')
,('Aserrí' , 'Aserrí')
,('Mora' , 'Mora')
,('Zarcero' , 'Zarcero')
,('Orotina' , 'Orotina')
,('Grecia' , 'Grecia')
,('Atenas' , 'Atenas')
,('Naranjo' , 'Naranjo')
,('San Mateo' , 'San Mateo')
,('León Cortés' , 'León Cortés')
,('Sarchí' , 'Sarchí')
,('Desamparados' , 'Desamparados')
,('Alvarado' , 'Alvarado')
,('Poás' , 'Poás')
,('Santa Ana' , 'Santa Ana')
,('Barva' , 'Barva')
,('Santa Bárbara' , 'Santa Bárbara')
,('San Rafael' , 'San Rafael')
,('La Unión' , 'La Unión')
,('San José' , 'San José')
,('Palmares' , 'Palmares')
,('Escazú' , 'Escazú')
,('Goicoechea' , 'Goicoechea')
,('Moravia' , 'Moravia')
,('San Isidro' , 'San Isidro')
,('Santo Domingo' , 'Santo Domingo')
,('Alajuelita' , 'Alajuelita')
,('Curridabat' , 'Curridabat')
,('Montes de Oca' , 'Montes de Oca')
,('Belén' , 'Belén')
,('Tibás' , 'Tibás')
,('San Pablo' , 'San Pablo')
,('Flores' , 'Flores')
)
    DISTRITOS = (('Carmen' , 'Carmen')
,('Merced' , 'Merced')
,('Hospital' , 'Hospital')
,('Catedral' , 'Catedral')
,('Zapote' , 'Zapote')
,('San Francisco de Dos Ríos' , 'San Francisco de Dos Ríos')
,('La Uruca' , 'La Uruca')
,('Mata Redonda' , 'Mata Redonda')
,('Pavas' , 'Pavas')
,('Hatillo' , 'Hatillo')
,('San Sebastián' , 'San Sebastián')
,('San Miguel' , 'San Miguel')
,('San Antonio' , 'San Antonio')
,('San Rafael' , 'San Rafael')
,('Desamparados' , 'Desamparados')
,('San Juan de Dios' , 'San Juan de Dios')
,('San Rafael Arriba' , 'San Rafael Arriba')
,('Frailes' , 'Frailes')
,('Patarrá' , 'Patarrá')
,('San Cristóbal' , 'San Cristóbal')
,('Rosario' , 'Rosario')
,('Damas' , 'Damas')
,('San Rafael Abajo' , 'San Rafael Abajo')
,('Gravilias' , 'Gravilias')
,('Los Guido' , 'Los Guido')
,('Santiago' , 'Santiago')
,('Mercedes Sur' , 'Mercedes Sur')
,('Barbacoas' , 'Barbacoas')
,('Grifo Alto' , 'Grifo Alto')
,('Candelarita' , 'Candelarita')
,('Desamparaditos' , 'Desamparaditos')
,('Chires' , 'Chires')
,('San Marcos' , 'San Marcos')
,('San Lorenzo' , 'San Lorenzo')
,('San Carlos' , 'San Carlos')
,('Aserrí' , 'Aserrí')
,('Tarbaca' , 'Tarbaca')
,('Vuelta de Jorco' , 'Vuelta de Jorco')
,('San Gabriel' , 'San Gabriel')
,('Legua' , 'Legua')
,('Monterrey' , 'Monterrey')
,('Salitrillos' , 'Salitrillos')
,('Colón' , 'Colón')
,('Guayabo' , 'Guayabo')
,('Tabarcia' , 'Tabarcia')
,('Piedras Negras' , 'Piedras Negras')
,('Picagres' , 'Picagres')
,('Jaris' , 'Jaris')
,('Quitirrisí' , 'Quitirrisí')
,('Guadalupe' , 'Guadalupe')
,('San Francisco' , 'San Francisco')
,('Calle Blancos' , 'Calle Blancos')
,('Mata de Plátano' , 'Mata de Plátano')
,('Ipís' , 'Ipís')
,('Rancho Redondo' , 'Rancho Redondo')
,('Purral' , 'Purral')
,('Santa Ana' , 'Santa Ana')
,('Salitral' , 'Salitral')
,('Pozos' , 'Pozos')
,('Uruca' , 'Uruca')
,('Piedades' , 'Piedades')
,('Brasil' , 'Brasil')
,('Alajuelita' , 'Alajuelita')
,('San Josecito' , 'San Josecito')
,('Concepción' , 'Concepción')
,('San Felipe' , 'San Felipe')
,('San Isidro' , 'San Isidro')
,('Dulce Nombre de Jesús' , 'Dulce Nombre de Jesús')
,('Patalillo' , 'Patalillo')
,('Cascajal' , 'Cascajal')
,('San Ignacio' , 'San Ignacio')
,('Guaitil' , 'Guaitil')
,('Palmichal' , 'Palmichal')
,('Cangrejal' , 'Cangrejal')
,('Sabanillas' , 'Sabanillas')
,('San Juan' , 'San Juan')
,('Cinco Esquinas' , 'Cinco Esquinas')
,('Anselmo llorente' , 'Anselmo llorente')
,('León XIII' , 'León XIII')
,('Colima' , 'Colima')
,('San Vicente' , 'San Vicente')
,('San Jerónimo' , 'San Jerónimo')
,('La Trinidad' , 'La Trinidad')
,('San Pedro' , 'San Pedro')
,('Sabanilla' , 'Sabanilla')
,('Mercedes' , 'Mercedes')
,('San Pablo' , 'San Pablo')
,('San Juan de Mata' , 'San Juan de Mata')
,('San Luis' , 'San Luis')
,('Carara' , 'Carara')
,('Santa María' , 'Santa María')
,('Jardín' , 'Jardín')
,('Copey' , 'Copey')
,('Curridabat' , 'Curridabat')
,('Granadilla' , 'Granadilla')
,('Sánchez' , 'Sánchez')
,('Tirrases' , 'Tirrases')
,('San Isidro de El General' , 'San Isidro de El General')
,('El General' , 'El General')
,('Daniel Flores' , 'Daniel Flores')
,('Rivas' , 'Rivas')
,('Platanares' , 'Platanares')
,('Pejibaye' , 'Pejibaye')
,('Cajón' , 'Cajón')
,('Barú' , 'Barú')
,('Río Nuevo' , 'Río Nuevo')
,('Páramo' , 'Páramo')
,('La Amistad' , 'La Amistad')
,('San Andrés' , 'San Andrés')
,('Llano Bonito' , 'Llano Bonito')
,('Santa Cruz' , 'Santa Cruz')
,('Oriental' , 'Oriental')
,('Occidental' , 'Occidental')
,('San Nicolás' , 'San Nicolás')
,('Agua Caliente' , 'Agua Caliente')
,('Corralillo' , 'Corralillo')
,('Tierra Blanca' , 'Tierra Blanca')
,('Dulce Nombre' , 'Dulce Nombre')
,('Llano Grande' , 'Llano Grande')
,('Quebradilla' , 'Quebradilla')
,('Paraíso' , 'Paraíso')
,('Orosi' , 'Orosi')
,('Cachí' , 'Cachí')
,('Llanos de Santa Lucía' , 'Llanos de Santa Lucía')
,('Tres Ríos' , 'Tres Ríos')
,('San Diego' , 'San Diego')
,('San Ramón' , 'San Ramón')
,('Río Azul' , 'Río Azul')
,('Juan Viñas' , 'Juan Viñas')
,('Tucurrique' , 'Tucurrique')
,('Turrialba' , 'Turrialba')
,('La Suiza' , 'La Suiza')
,('Peralta' , 'Peralta')
,('Santa Teresita' , 'Santa Teresita')
,('Pavones' , 'Pavones')
,('Tuis' , 'Tuis')
,('Tayutic' , 'Tayutic')
,('Santa Rosa' , 'Santa Rosa')
,('Tres Equis' , 'Tres Equis')
,('La Isabel' , 'La Isabel')
,('Chirripó' , 'Chirripó')
,('Pacayas' , 'Pacayas')
,('Cervantes' , 'Cervantes')
,('Capellades' , 'Capellades')
,('Cot' , 'Cot')
,('Potrero Cerrado' , 'Potrero Cerrado')
,('Cipreses' , 'Cipreses')
,('El Tejar' , 'El Tejar')
,('Tobosi' , 'Tobosi')
,('Patio de Agua' , 'Patio de Agua')
,('Heredia' , 'Heredia')
,('Ulloa' , 'Ulloa')
,('Varablanca' , 'Varablanca')
,('Barva' , 'Barva')
,('San Roque' , 'San Roque')
,('Santa Lucía' , 'Santa Lucía')
,('San José de la Montaña' , 'San José de la Montaña')
,('Santo Domingo' , 'Santo Domingo')
,('Paracito' , 'Paracito')
,('Santo Tomás' , 'Santo Tomás')
,('Tures' , 'Tures')
,('Pará' , 'Pará')
,('Santa Bárbara' , 'Santa Bárbara')
,('Jesús' , 'Jesús')
,('Purabá' , 'Purabá')
,('Ángeles' , 'Ángeles')
,('San José' , 'San José')
,('La Ribera' , 'La Ribera')
,('La Asunción' , 'La Asunción')
,('San Joaquín' , 'San Joaquín')
,('Barrantes' , 'Barrantes')
,('Llorente' , 'Llorente')
,('Rincón de Sabanilla' , 'Rincón de Sabanilla')
,('Puerto Viejo' , 'Puerto Viejo')
,('La Virgen' , 'La Virgen')
,('Horquetas' , 'Horquetas')
,('Llanuras del Gaspar' , 'Llanuras del Gaspar')
,('Cureña' , 'Cureña')
,('Liberia' , 'Liberia')
,('Cañas Dulces' , 'Cañas Dulces')
,('Mayorga' , 'Mayorga')
,('Nacascolo' , 'Nacascolo')
,('Curubandé' , 'Curubandé')
,('Nicoya' , 'Nicoya')
,('Mansión' , 'Mansión')
,('Quebrada Honda' , 'Quebrada Honda')
,('Sámara' , 'Sámara')
,('Nosara' , 'Nosara')
,('Belén de Nosarita' , 'Belén de Nosarita')
,('Bolsón' , 'Bolsón')
,('Veintisiete de Abril' , 'Veintisiete de Abril')
,('Tempate' , 'Tempate')
,('Cartagena' , 'Cartagena')
,('Cuajiniquil' , 'Cuajiniquil')
,('Diriá' , 'Diriá')
,('Cabo Velas' , 'Cabo Velas')
,('Tamarindo' , 'Tamarindo')
,('Bagaces' , 'Bagaces')
,('La Fortuna' , 'La Fortuna')
,('Mogote' , 'Mogote')
,('Río Naranjo' , 'Río Naranjo')
,('Filadelfia' , 'Filadelfia')
,('Palmira' , 'Palmira')
,('Sardinal' , 'Sardinal')
,('Belén' , 'Belén')
,('Cañas' , 'Cañas')
,('Bebedero' , 'Bebedero')
,('Porozal' , 'Porozal')
,('Las Juntas' , 'Las Juntas')
,('Sierra' , 'Sierra')
,('Colorado' , 'Colorado')
,('Tilarán' , 'Tilarán')
,('Quebrada Grande' , 'Quebrada Grande')
,('Tronadora' , 'Tronadora')
,('Líbano' , 'Líbano')
,('Tierras Morenas' , 'Tierras Morenas')
,('Arenal' , 'Arenal')
,('Cabeceras' , 'Cabeceras')
,('Carmona' , 'Carmona')
,('Santa Rita' , 'Santa Rita')
,('Zapotal' , 'Zapotal')
,('Porvenir' , 'Porvenir')
,('Bejuco' , 'Bejuco')
,('La Cruz' , 'La Cruz')
,('Santa Cecilia' , 'Santa Cecilia')
,('La Garita' , 'La Garita')
,('Santa Elena' , 'Santa Elena')
,('Hojancha' , 'Hojancha')
,('Monte Romo' , 'Monte Romo')
,('Puerto Carrillo' , 'Puerto Carrillo')
,('Huacas' , 'Huacas')
,('Matambú' , 'Matambú')
,('Limón' , 'Limón')
,('Valle La Estrella' , 'Valle La Estrella')
,('Río Blanco' , 'Río Blanco')
,('Matama' , 'Matama')
,('Guápiles' , 'Guápiles')
,('Jiménez' , 'Jiménez')
,('La Rita' , 'La Rita')
,('Roxana' , 'Roxana')
,('Cariari' , 'Cariari')
,('La Colonia' , 'La Colonia')
,('Siquirres' , 'Siquirres')
,('Pacuarito' , 'Pacuarito')
,('Florida' , 'Florida')
,('Germania' , 'Germania')
,('Cairo' , 'Cairo')
,('Alegría' , 'Alegría')
,('Reventazón' , 'Reventazón')
,('Bratsi' , 'Bratsi')
,('Sixaola' , 'Sixaola')
,('Cahuita' , 'Cahuita')
,('Telire' , 'Telire')
,('Matina' , 'Matina')
,('Batán' , 'Batán')
,('Carrandi' , 'Carrandi')
,('Guácimo' , 'Guácimo')
,('Pocora' , 'Pocora')
,('Río Jiménez' , 'Río Jiménez')
,('Duacarí' , 'Duacarí')
,('Puntarenas' , 'Puntarenas')
,('Pitahaya' , 'Pitahaya')
,('Chomes' , 'Chomes')
,('Lepanto' , 'Lepanto')
,('Paquera' , 'Paquera')
,('Manzanillo' , 'Manzanillo')
,('Guacimal' , 'Guacimal')
,('Barranca' , 'Barranca')
,('Monte Verde' , 'Monte Verde')
,('Isla del Coco' , 'Isla del Coco')
,('Cóbano' , 'Cóbano')
,('Chacarita' , 'Chacarita')
,('Chira' , 'Chira')
,('Acapulco' , 'Acapulco')
,('El Roble' , 'El Roble')
,('Arancibia' , 'Arancibia')
,('Espíritu Santo' , 'Espíritu Santo')
,('San Juan Grande' , 'San Juan Grande')
,('Macacona' , 'Macacona')
,('Caldera' , 'Caldera')
,('Buenos Aires' , 'Buenos Aires')
,('Volcán' , 'Volcán')
,('Potrero Grande' , 'Potrero Grande')
,('Boruca' , 'Boruca')
,('Pilas' , 'Pilas')
,('Colinas' , 'Colinas')
,('Chánguena' , 'Chánguena')
,('Biolley' , 'Biolley')
,('Brunka' , 'Brunka')
,('Miramar' , 'Miramar')
,('La Unión' , 'La Unión')
,('Puerto Cortés' , 'Puerto Cortés')
,('Palmar' , 'Palmar')
,('Sierpe' , 'Sierpe')
,('Bahía Ballena' , 'Bahía Ballena')
,('Piedras Blancas' , 'Piedras Blancas')
,('Bahía Drake' , 'Bahía Drake')
,('Quepos' , 'Quepos')
,('Savegre' , 'Savegre')
,('Naranjito' , 'Naranjito')
,('Golfito' , 'Golfito')
,('Puerto Jiménez' , 'Puerto Jiménez')
,('Guaycará' , 'Guaycará')
,('Pavón' , 'Pavón')
,('San Vito' , 'San Vito')
,('Sabalito' , 'Sabalito')
,('Aguabuena' , 'Aguabuena')
,('Limoncito' , 'Limoncito')
,('Pittier' , 'Pittier')
,('Gutiérrez Braun' , 'Gutiérrez Braun')
,('Parrita' , 'Parrita')
,('Corredor' , 'Corredor')
,('La Cuesta' , 'La Cuesta')
,('Canoas' , 'Canoas')
,('Laurel' , 'Laurel')
,('Jacó' , 'Jacó')
,('Tárcoles' , 'Tárcoles')
)

    nombre                          = models.CharField(max_length=140)
    cedula_fisica                   = models.CharField(max_length=10,blank=True)
    nombre_emprendimiento           = models.CharField(max_length =140,blank=True)
    imagen_emprendimiento           = models.ImageField(blank=True)
    persona_indigena                = models.BooleanField(default = False,blank=True)
    formal                          = models.BooleanField(default = False,blank=True)
    cedula_juridica                 = models.CharField(max_length = 140,blank=True)
    actividad                       = models.CharField(max_length =140,blank=True,choices = ACTIVIDADES) #Puede ser multioption

    nombre_producto                 = models.CharField(max_length = 140,blank=True)
    trueque                         = models.BooleanField(default=False)
    telefono                        = models.CharField(max_length = 8,blank=True)
    email                           = models.CharField(max_length =140,blank=True)
    preferencia_contacto            = models.CharField(max_length =140,blank=True, choices = PREFERENCIAS_CONTACTO)

    horario_contacto                = models.CharField(max_length = 140,blank=True)
    provincia                       = models.CharField(max_length=10, choices=PROVINCIAS,blank=True)
    canton                          = models.CharField(max_length = 140, choices =  CANTONES,blank=True)
    distrito                        = models.CharField(max_length = 140, choices = DISTRITOS,blank=True)
    direccion                      = models.CharField(max_length=140,blank=True)
    a_domicilio                     = models.BooleanField(default=False,blank=True)
    a_domicilio_cantones            = models.CharField(max_length = 140, choices = CANTONES,blank=True) #MULTICHOICE
    fotos_productos                 = models.ImageField(blank=True)
    sitio_web                       = models.CharField(max_length=140,blank=True)
    rrss_link                       = models.CharField(max_length=140,blank=True)
    rrss_link_2                     = models.CharField(max_length=140,blank=True)
    comentarios                     = models.CharField(max_length=1500,blank=True)


    def __str__(self):
        return self.nombre
# Create your models here.
