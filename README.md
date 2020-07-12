# Restaurador-de-imagenes-rotas
Restaurar imágenes dañadas y/o viejas con image inpainting

Se plantea un programa capaz de: 

1- Borrar marcas de agua indeseables en imágenes.
2- Restaurar imágenes que se han deteriorado a través de los años.
3- Eliminar graffitis o elementos no deseados en esculturas, murales, estatuas, etc.
4- Eliminar pequeños tatuajes.

Se utilizan dos algoritmos:

El primero se basa en el documento 'Una técnica de pintura de imágenes basada en el método de marcha rápida' por Alexandru Telea en 2004. Se basa en el método de marcha rápida o Fast Marching Method. Con ésto obtenemos la imagen: "restauracion1.jpg"

El segundo algoritmo se basa en el artículo 'Navier-Stokes, Fluid Dynamics, and Image and Video Inpainting' de Bertalmio, Marcelo, Andrea L. Bertozzi y Guillermo Sapiro en 2001. Con ésto obtenemos la imagen: "restauracion2.jpg"

Para más información sobre éstos dos algoritmos recurrir a la documentación OpenCv: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_photo/py_inpainting/py_inpainting.html.

Ambos algoritmos son relativamente rápidos. Cuando la región de la imagen se quiere rellenar es relativamente grande, el acabo final que se obtiene en la imagen no es muy bueno.

La máscara o mask se obtiene mediante el uso de Photopea. Se crean 3 capas: una para la imagen original, la siguiente para el fondo totalmente negro y por último las regiones donde queremos aplicar el inpainting. Para un mejor acabado en la imagen final, se puede utilizar un array con los pixeles precisamente donde se quiere hacer el inpainting o un proceso más minucioso en la 3er capa cuando se utiliza Photopea.

Imágenes obtenidas de Pixabay. La licencia ampara gratis para usos omerciales y no es necesario reconocimiento.
