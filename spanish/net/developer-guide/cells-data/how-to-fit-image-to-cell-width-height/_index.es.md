---
title: Cómo ajustar una imagen al ancho y alto de la celda
type: docs
weight: 130
url: /es/net/how-to-fit-image-to-cell-width-height/
description: Aprenda cómo ajustar la imagen al ancho de la celda con Aspose.Cells.
keywords: Cómo ajustar la imagen al ancho de la celda, ajustar imagen al ancho de la celda, cómo ajustar la imagen al ancho y alto de la celda, cómo ajustar la imagen a la altura de la celda.
---


## **Por qué ajustar la imagen al ancho y alto de la celda**
Ajustar una imagen al ancho y alto de una celda específica no solo se trata de estética. Es fundamentalmente una cuestión de precisión, automatización y organización de datos.

1. Para Presentación Profesional y Legibilidad: Cuando construyes un panel de control, a menudo necesitas iconos, banderas o imágenes de productos para que se alineen perfectamente con los puntos de datos. Una imagen mal alineada se ve descuidada y poco profesional. Si estás diseñando una plantilla para que otros la usen (por ejemplo, un catálogo de productos, un directorio de empleados), quieres que las imágenes se ajusten automáticamente a los espacios designados, asegurando la coherencia cada vez que se utilice la plantilla. Las imágenes que desbordan las celdas pueden causar saltos inesperados en la página y problemas de formato al imprimir. Una imagen ajustada se comporta de manera predecible en la página impresa.

2. Para Organización y Estructura de Datos: Esta es la razón funcional más importante. Excel es una cuadrícula para datos. Cuando una imagen se "coloca" en la cuadrícula en lugar de "ajustarse" a una celda, causa problemas. Problemas con Imágenes Flotantes Libres: No se Mueven con las Celdas: Si ordenas, filtras o insertas/eliminar filas, la imagen permanece en su posición absoluta en la hoja, desconectándose completamente de los datos que debería representar. No se Redimensionan con las Celdas: Si cambias la altura de fila o el ancho de columna, una imagen flotante libre permanece del mismo tamaño, rompiendo el diseño. Beneficio de Ajustar a una Celda: La Celda se convierte en el "contenedor" de la imagen: Cuando una imagen se ajusta a una celda, su posición y tamaño están definidos por las coordenadas de la cuadrícula de la celda. Si mueves los datos (por ejemplo, ordenas una tabla), la imagen se mueve con su fila correspondiente. Crea un Verdadero par de Imagen-Dato: Esto te permite tratar la imagen como un atributo visual de los datos en esa fila, lo cual es esencial para la automatización.

3. Para Automatización y Funcionalidad Avanzada: Aquí es donde ajustar imágenes a celdas se convierte en un superpoder. Vincular Imágenes Dinámicamente: Puedes usar una fórmula para extraer la ruta de la imagen de una celda y luego usar una macro (VBA) para dimensionar automáticamente e insertar la imagen en una celda adyacente. Así es como creas un catálogo de productos dinámico donde cambiar un ID de producto actualiza automáticamente el nombre, precio y la imagen. Integración con Bases de Datos: Cuando exportas datos o vinculas Excel a una base de datos, tener imágenes contenidas dentro de celdas específicas hace que todo el conjunto de datos, incluidos sus elementos visuales, sea más estructurado y portable.

## **Cómo Ajustar una Imagen al Ancho y Alto de la Celda usando Excel**
Puedes ajustar una imagen al ancho y alto de la celda en Excel usando las siguientes dos formas.

### **Ajustar Imagen al Ancho y Alto de la Celda usando Ubicación en la Celda**
Acerca de cómo insertar una imagen en una celda en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar en celda**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="1.png" width=60% />
3. Selecciona la imagen e insértala en una celda.
<br>
<img src="8.png" width=60% />

### **Ajustar Imagen al Ancho y Alto de la Celda usando Ubicación sobre las Celdas**
Acerca de cómo insertar una imagen sobre celdas en Excel, sigue estos pasos:

1. Ve a la pestaña Insertar y haz clic en la opción Imágenes.
2. Selecciona **Colocar sobre celdas**. Selecciona una de las siguientes fuentes en el menú desplegable Insertar imagen de (**Este dispositivo**, **Imágenes de stock** y **Imágenes en línea**). Este dispositivo para insertar una imagen desde tu dispositivo. Imágenes de stock para insertar una imagen desde imágenes de stock. Imágenes en línea para insertar una imagen desde la web.
<br>
<img src="2.png" width=60% />
3. Selecciona la imagen e insértala sobre las celdas.
<br>
<img src="3.png" width=60% />
4. Ajusta manualmente el ancho y alto de la imagen para que coincidan con el ancho y alto de las celdas.
<br>
<img src="6.png" width=60% />

## **Cómo Ajustar Imagen al Ancho y Alto de la Celda usando Aspose.Cells**
Debido a variaciones en el ancho y alto de filas y columnas dependiendo del idioma y la relación de pantalla, ajustar el ancho y alto de una imagen puede resultar en pequeñas diferencias, y a veces puede no ser completamente coherente con el ancho y alto de las celdas. Puedes ajustar la imagen al ancho y alto de la celda en Aspose.Cells usando las siguientes dos formas.

### **Cómo Ajustar Imagen al Ancho y Alto de la Celda usando Ubicación en la Celda**
Insertar imagen en celda usando Aspose.Cells. Consulte el siguiente código de ejemplo. Después de ejecutar el código de ejemplo, se insertará una imagen en una celda.
1. Instanciar un objeto Workbook. 
2. Obtener la celda donde desea insertar la imagen.
3. Establecer la propiedad Cell.EmbeddedImage. 
4. Finalmente, guarda el libro en formato [XLSX de salida](out.xlsx). 

### ** Código de ejemplo para Ubicación en la Celda**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-in-cell.cs" >}}
{{< app/cells/assistant language="csharp" >}}

### **Cómo Ajustar Imagen al Ancho y Alto de la Celda usando Ubicación sobre las Celdas**
Agregar imágenes a una hoja de cálculo es muy fácil. Solo toma unas pocas líneas de código:
Simplemente llama al método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) de la colección [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) (encapsulado en el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). Luego ajusta el ancho y alto de la imagen en función del ancho y alto de las celdas. Finalmente, guarda el archivo en formato [XLSX de salida](out_net.xlsx). El método [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) toma los siguientes parámetros:

- **Índice de fila superior izquierda**, el índice de la fila superior izquierda.
- **Índice de columna superior izquierda**, el índice de la columna superior izquierda.
- **Nombre del archivo de imagen**, el nombre del archivo de imagen, completo con la ruta.


### **Código de ejemplo para Ubicación sobre las Celdas**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-place-image-over-cells-fit-cell-width-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
