---
title: Configuración de encabezados y pies de página
type: docs
weight: 30
url: /es/python-net/setting-headers-and-footers/
description: Este artículo explica cómo insertar una imagen de forma programática en el encabezado y pie de página de las hojas de cálculo de Excel mediante comandos de script utilizando la API de Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel para Python, insertar imagen en encabezado y pie de página de Excel en Python, establecer comandos de script de encabezado y pie de página de Excel usando Python.
---

{{% alert color="primary" %}}

Los encabezados y pies de página son las líneas de texto que se muestran debajo del margen superior o encima del margen inferior, respectivamente. También es posible agregar encabezados y pies de página a las hojas de cálculo. Los encabezados y pies de página pueden utilizarse para mostrar información útil como el número de página, el nombre del autor, el nombre del tema o la fecha y hora. Los encabezados y pies de página se gestionan mediante la configuración del diseño de página.

{{% /alert %}}

## **Configuración de encabezados y pies de página**

Aspose.Cells para Python via .NET te permite añadir encabezados y pies de página a las hojas de cálculo en tiempo de ejecución, pero recomendamos establecer los encabezados y pies de página manualmente en un archivo pre-diseñado para la impresión. Puedes utilizar Microsoft Excel como herramienta GUI para establecer encabezados y pies de página y así ahorrar esfuerzo y tiempo de desarrollo. Aspose.Cells para Python via .NET puede importar el archivo y guardar los ajustes.

Para añadir encabezados y pies de página en tiempo de ejecución, Aspose.Cells para Python via .NET proporciona llamadas especiales de API y comandos de script para formatear los encabezados y pies de página.

### **Comandos de Script**

Los comandos de script son comandos especiales que le permiten configurar el formato de los encabezados y pies de página.

|**Comandos de Script**|**Descripción**|
| :- | :- |
|&P|Número de página actual|
|&G|Una imagen|
|&N|El número total de páginas|
|&D|La fecha actual|
|&T|La hora actual|
|&A|Nombre de la hoja de cálculo|
|&F|El nombre del archivo sin su ruta|
|&"\<FontName>"|Representa un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representa el nombre de la fuente con estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de la fuente. Por ejemplo: “&14abc”. Sin embargo, si este comando va seguido de un número normal a imprimir en el encabezado, esto debe separarse con un carácter de espacio del tamaño de la fuente. Por ejemplo: “&14 123”.|

### **Cómo establecer encabezados y pies de página**

La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) proporciona dos métodos, [**set_header**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header/#int-str) y [**set_footer**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer/#int-str), utilizados para agregar un encabezado y un pie de página a una hoja de trabajo. Estos métodos solo toman dos parámetros:

- **Sección** – la sección donde se debe colocar el encabezado o pie de página. Hay tres secciones: izquierda, centro y derecha, representadas respectivamente por 0, 1 y 2.
- **Script** – el script a utilizar para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.py" >}}

### **Cómo insertar una imagen en un encabezado o pie de página**

La clase [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup) tiene dos métodos adicionales, [**set_header_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_header_picture/#int-bytes) y [**set_footer_picture**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/set_footer_picture/#int-bytes), utilizados para agregar imágenes en el encabezado y pie de página. Estos métodos toman los siguientes parámetros:

- **Sección** – la sección de encabezado o pie de página donde se colocará la imagen. Hay tres secciones, izquierda, centro y derecha, representadas por los valores 0, 1 y 2 respectivamente.
- **Arreglo de bytes** – los datos gráficos (los datos binarios deben escribirse en el búfer de un arreglo de bytes).

Después de ejecutar el código a continuación y abrir el archivo, verificar el encabezado de la hoja de trabajo mediante:

1. En el menú **Archivo**, seleccionar **Configurar Página**. Se mostrará un cuadro de diálogo.
1. Seleccionar la pestaña **Encabezado/Pie de página**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.py" >}}
