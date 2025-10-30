---
title: Cómo Agregar Cámara para Alcance
type: docs
weight: 10
url: /es/net/how-to-add-camera-for-range/
description: Este artículo presentará cómo agregar una cámara para contenido de rango API Aspose.Cells for .NET.
keywords: Cómo Usar la Función de la Cámara, Cómo agregar Cámara para contenido de rango, Cómo Usar la herramienta Cámara, Función de Cámara en Excel, Cómo Usar la Función de Cámara en Aspose.Cells for .NET
---

## **Escenarios de uso posibles**
La herramienta Cámara en Excel es una función oculta pero poderosa que permite crear una instantánea en vivo y vinculada de cualquier rango de celdas. Aquí te explicamos por qué y cuándo podrías usarla.

Qué Hace la Herramienta Cámara:
1. Toma una "foto" de un rango de celdas seleccionado.
2. La "foto" es un enlace en vivo — si las celdas fuente cambian, la imagen se actualiza automáticamente.
3. Puedes mover o cambiar el tamaño de la imagen en cualquier lugar de la hoja o incluso a otra hoja.


## **Cómo Usar la Función de Cámara en Excel**
Aquí tienes una guía paso a paso para usar la Herramienta Cámara en Excel, una forma poderosa de crear imágenes dinámicas y en vivo de rangos de celdas.

### Habilitar la Herramienta Cámara

La herramienta Cámara está oculta por defecto. Aquí te explicamos cómo agregarla:

1. Haz clic en la flecha hacia abajo en la Barra de Acceso Rápido (esquina superior izquierda de Excel).
2. Elige Más Comandos....
3. En el cuadro de diálogo: En el menú desplegable “Elegir comandos de”, selecciona Comandos no en la cinta. Desliza hacia abajo y selecciona Cámara. Haz clic en Agregar >> para agregarla a la barra de herramientas.
4. Haz clic en Aceptar. Ahora verás un pequeño ícono de cámara en tu barra de herramientas.

### Usar la Herramienta Cámara
1. Selecciona el rango de celdas que deseas capturar (por ejemplo, A1:C5).
2. Haz clic en el ícono de Cámara en la Barra de Acceso Rápido.
3. Tu cursor cambiará a una cruz.
4. Haz clic en cualquier parte de la hoja de cálculo donde quieras colocar la imagen. Se inserta una imagen en vivo del rango seleccionado.

### Enlace dinámico
La imagen está vinculada a las celdas originales. Si cambian los valores o el formato en el rango fuente, la imagen se actualiza automáticamente.


## **Cómo agregar Cámara para rango en Aspose.Cells for .NET**
Aspose.Cells soporta mostrar el contenido de una celda o rango en una forma de imagen. Puedes vincular la imagen a la celda o rango que contiene los datos que deseas mostrar. Dado que la celda o rango está vinculado al objeto gráfico, los cambios que hagas en los datos de esa celda o rango aparecen automáticamente en el objeto gráfico. 

Aquí hay un ejemplo básico de cómo usar la función de Cámara usando el [archivo de muestra](camera.xlsx) en Aspose.Cells for .NET:

1. Carga el archivo de muestra usando la clase [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook).
1. Añade una imagen a la hoja de cálculo llamando al método [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) de la colección [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (envuelto en el objeto [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). 
1. Especifica el rango de celdas usando el atributo [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) del objeto [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).
1. Actualiza el valor seleccionado de las formas en la hoja de cálculo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Resultado de salida**
La siguiente captura de pantalla muestra la cámara del rango (A1:E12) creada por Aspose.Cells for .NET en el archivo Excel de salida.
<br>
Antes de añadir datos:
<br>
<img src="1.png" width=70% />
<br>
Después de añadir datos:
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
