---
title: Configuración de encabezados y pies de página
type: docs
weight: 30
url: /es/net/setting-headers-and-footers/
---
{{% alert color="primary" %}}

Los encabezados y pies de página son las líneas de texto que se muestran debajo del margen superior o encima del margen inferior, respectivamente. También es posible agregar encabezados y pies de página a las hojas de trabajo. Los encabezados y pies de página se pueden usar para mostrar información útil, como el número de página, el nombre del autor, el nombre del tema o la fecha y la hora. Los encabezados y pies de página se administran mediante la configuración de la página.

{{% /alert %}}

## **Configuración de encabezados y pies de página**

Aspose.Cells le permite agregar encabezados y pies de página a las hojas de trabajo en tiempo de ejecución, pero le recomendamos que configure los encabezados y pies de página manualmente en un archivo prediseñado para imprimir. Puede usar Microsoft Excel como una herramienta GUI para configurar encabezados y pies de página para ahorrar esfuerzo y tiempo de desarrollo. Aspose.Cells puede importar el archivo y guardar la configuración.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona llamadas API especiales y comandos de script para formatear encabezados y pies de página.

### **Comandos de secuencia de comandos**

Los comandos de script son comandos especiales que le permiten configurar el formato de encabezado y pie de página.

|**Comandos de secuencia de comandos**|**Descripción**|
|:- |:- |
|&PAGS|El número de página actual|
|&GRAMO|Una foto|
|&NORTE|El número total de páginas|
|&D|la fecha actual|
|&T|la hora actual|
|&A|El nombre de la hoja de trabajo|
|&F|El nombre del archivo sin su ruta|
|&"\<FontName>"|Representa un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representa el nombre de la fuente con estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de fuente. Por ejemplo: “&14abc”. Pero, si este comando es seguido por un número simple para imprimir en el encabezado, este debe estar separado del tamaño de fuente con un carácter de espacio. Por ejemplo: “&14 123”.|

### **Establecer encabezados y pies de página**

 los[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) La clase proporciona dos métodos,[**EstablecerEncabezado**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheader) y[**Establecer pie de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooter), que se usa para agregar un encabezado y un pie de página a una hoja de cálculo. Estos métodos toman sólo dos parámetros:

- **Sección** – la sección donde se debe colocar el encabezado o pie de página. Hay tres secciones: izquierda, centro y derecha, representadas por 0, 1 y 2 respectivamente.
- **Guion** – el guión que se utilizará para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-SetHeadersAndFooters-1.cs" >}}

### **Insertar una imagen en un encabezado o pie de página**

 los[**Configuración de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) La clase tiene dos métodos adicionales,[**EstablecerImagenDeEncabezado**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setheaderpicture) y[**Establecer imagen de pie de página**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/setfooterpicture), utilizado para agregar imágenes en el encabezado y pie de página. Estos métodos toman los parámetros:

- **Sección**– la sección de encabezado o pie de página donde se colocará la imagen. Hay tres secciones, izquierda, centro y derecha, representadas por los valores 0, 1 y 2 respectivamente.
- **matriz de bytes** – los datos gráficos (los datos binarios deben escribirse en el búfer de una matriz de bytes).

Después de ejecutar el código a continuación y abrir el archivo, verifique el encabezado de la hoja de trabajo de la siguiente manera:

1.  Sobre el**Expediente** menú, seleccione**Configuración de página**. Se mostrará un cuadro de diálogo.
1.  Selecciona el**Encabezado/Pie de página** pestaña.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-InsertImageInHeaderFooter-1.cs" >}}
