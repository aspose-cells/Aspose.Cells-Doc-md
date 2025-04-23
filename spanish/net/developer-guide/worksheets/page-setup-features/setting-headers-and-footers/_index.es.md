---
title: Configuración de encabezados y pies de página
type: docs
weight: 30
url: /es/net/setting-headers-and-footers/
description: Este artículo explica cómo insertar programáticamente una imagen en el encabezado y pie de página de las hojas de cálculo de Excel mediante la configuración del encabezado y pie de página con comandos de script utilizando la API de C# o .NET Library.
keywords: insertar imagen en encabezado y pie de página de excel c#, establecer comandos de script de encabezado y pie de página de excel c#
---

{{% alert color="primary" %}}

Los encabezados y pies de página son las líneas de texto que se muestran debajo del margen superior o encima del margen inferior, respectivamente. También es posible agregar encabezados y pies de página a las hojas de cálculo. Los encabezados y pies de página pueden utilizarse para mostrar información útil como el número de página, el nombre del autor, el nombre del tema o la fecha y hora. Los encabezados y pies de página se gestionan mediante la configuración del diseño de página.

{{% /alert %}}

## **Configuración de encabezados y pies de página**

Aspose.Cells le permite agregar encabezados y pies de página a las hojas de cálculo en tiempo de ejecución, pero recomendamos configurar los encabezados y pies de página manualmente en un archivo pre-diseñado para imprimir. Puede utilizar Microsoft Excel como una herramienta GUI para configurar los encabezados y pies de página y ahorrar esfuerzo y tiempo de desarrollo. Aspose.Cells puede importar el archivo y guardar la configuración.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona llamadas de API especiales y comandos de script para formatear encabezados y pies de página.

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
|&&Texto|Muestra &Texto. Por ejemplo: &&WO será mostrado como &WO|
|&"\<FontName>"|Representa un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representa el nombre de la fuente con estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de la fuente. Por ejemplo: “&14abc”. Sin embargo, si este comando va seguido de un número normal a imprimir en el encabezado, esto debe separarse con un carácter de espacio del tamaño de la fuente. Por ejemplo: “&14 123”.|

### **Establecer Encabezados y Pies de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) proporciona dos métodos, [**SetHeader**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) y [**SetFooter**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), utilizados para agregar un encabezado y un pie de página a una hoja de trabajo. Estos métodos solo toman dos parámetros:

- **Sección** – la sección donde se debe colocar el encabezado o pie de página. Hay tres secciones: izquierda, centro y derecha, representadas respectivamente por 0, 1 y 2.
- **Script** – el script a utilizar para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Insertar una Imagen en un Encabezado o Pie de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) tiene dos métodos adicionales, [**SetHeaderPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) y [**SetFooterPicture**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), utilizados para agregar imágenes en el encabezado y pie de página. Estos métodos toman los siguientes parámetros:

- **Sección** – la sección de encabezado o pie de página donde se colocará la imagen. Hay tres secciones, izquierda, centro y derecha, representadas por los valores 0, 1 y 2 respectivamente.
- **Arreglo de bytes** – los datos gráficos (los datos binarios deben escribirse en el búfer de un arreglo de bytes).

Después de ejecutar el código a continuación y abrir el archivo, verificar el encabezado de la hoja de trabajo mediante:

1. En el menú **Archivo**, seleccionar **Configurar Página**. Se mostrará un cuadro de diálogo.
1. Seleccionar la pestaña **Encabezado/Pie de página**.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
