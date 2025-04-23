---
title: Funciones de configuración de página
type: docs
weight: 40
url: /es/java/page-setup-features/
---

A veces, es necesario configurar la configuración de página para hojas de cálculo para controlar la impresión. Estas configuraciones ofrecen varias opciones.

**Opciones de página** 

![todo:image_alt_text](page-setup-features_1.png)

Las opciones de configuración de página son totalmente compatibles en Aspose.Cells. Este artículo explica cómo establecer opciones de página con Aspose.Cells.

## **Configurando Opciones de Página**

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase Workbook contiene una colección Worksheets que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La clase Worksheet proporciona la propiedad PageSetup, que se utiliza para establecer opciones de configuración de página. De hecho, la propiedad PageSetup es un objeto de la clase PageSetup que hace posible configurar opciones de diseño de página para una hoja de cálculo impresa. La clase PageSetup proporciona varias propiedades que se utilizan para establecer opciones de configuración de página. Algunas de estas propiedades se discuten a continuación.

### **Orientación de Página**

La orientación de página se puede establecer en vertical u horizontal usando el método [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). El método [**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) toma la enumeración [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) como parámetro. A continuación se enumeran los miembros de la enumeración [**PageOrientationType**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType).

|**Tipos de Orientación de Página**|**Descripción**|
| :- | :- |
|[**HORIZONTAL**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientación horizontal|
|[**VERTICAL**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientación vertical|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Factor de Escala**

Es posible reducir o ampliar el tamaño de una hoja de cálculo ajustando el factor de escala con el método [**setZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Opciones Ajustar a Páginas**

Para ajustar el contenido de la hoja de cálculo a un número específico de páginas, utiliza los métodos [**setFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) y [**setFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). También se utilizan estos métodos para escalar las hojas de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Tamaño de papel**

Establece el tamaño de papel al que se imprimirán las hojas de cálculo utilizando la propiedad [**PaperSize**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La propiedad PaperSize acepta uno de los valores predefinidos en la enumeración [**PaperSizeType**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType), que se enumeran a continuación.

|**Tipos de Tamaño de Papel**|**Descripción**|
| :- | :- |
|Paper10x14|10 in. x 14 in.|
|Paper11x17|11 in. x 17 in.|
|PaperA3|A3 (297 mm x 420 mm)|
|PaperA4|A4 (210 mm x 297 mm)|
|PaperA4Small|A4 Small (210 mm x 297 mm)|
|PaperA5|A5 (148 mm x 210 mm)|
|PaperB3|B3 (13.9 x 19.7 inches)|
|PaperB4|B4 (250 mm x 354 mm)|
|PaperB5|B5 (182 mm x 257 mm)|
|PaperBusinessCard|Business Card (90 mm x 55 mm)|
|PaperCSheet|C size sheet|
|PaperDSheet|D size sheet|
|PaperEnvelope10|Envelope #10 (4-1/8 in. x 9-1/2 in.)|
|PaperEnvelope11|Envelope #11 (4-1/2 in. x 10-3/8 in.)|
|PaperEnvelope12|Envelope #12 (4-1/2 in. x 11 in.)|
|PaperEnvelope14|Envelope #14 (5 in. x 11-1/2 in.)|
|PaperEnvelope9|Envelope #9 (3-7/8 in. x 8-7/8 in.)|
|PaperEnvelopeB4|Envelope B4 (250 mm x 353 mm)|
|PaperEnvelopeB5|Envelope B5 (176 mm x 250 mm)|
|PaperEnvelopeB6|Envelope B6 (176 mm x 125 mm)|
|PaperEnvelopeC3|Envelope C3 (324 mm x 458 mm)|
|PaperEnvelopeC4|Envelope C4 (229 mm x 324 mm)|
|PaperEnvelopeC5|Envelope C5 (162 mm x 229 mm)|
|PaperEnvelopeC6|Envelope C6 (114 mm x 162 mm)|
|PaperEnvelopeC65|Envelope C65 (114 mm x 229 mm)|
|PaperEnvelopeDL|Envelope DL (110 mm x 220 mm)|
|PaperEnvelopeItaly|Envelope Italy (110 mm x 230 mm)|
|PaperEnvelopeMonarch|Envelope Monarch (3-7/8 in. x 7-1/2 in.)|
|PaperEnvelopePersonal|Envelope (3-5/8 in. x 6-1/2 in.)|
|PaperESheet|E size sheet|
|PaperExecutive|Executive (7-1/2 in. x 10-1/2 in.)|
|PaperFanfoldLegalGerman|German Legal Fanfold (8-1/2 in. x 13 in.)|
|PaperFanfoldStdGerman|German Standard Fanfold (8-1/2 in. x 12 in.)|
|PaperFanfoldUS|U.S. Standard Fanfold (14-7/8 in. x 11 in.)|
|PaperFolio|Folio (8-1/2 in. x 13 in.)|
|PaperLedger|Ledger (17 in. x 11 in.)|
|PaperLegal|Legal (8-1/2 in. x 14 in.)|
|PaperLetter|Letter (8-1/2 in. x 11 in.)|
|PaperLetterSmall|Letter Small (8-1/2 in. x 11 in.)|
|PaperNote|Note (8-1/2 in. x 11 in.)|
|PaperQuarto|Quarto (215 mm x 275 mm)|
|PaperStatement|Statement (5-1/2 in. x 8-1/2 in.)|
|PaperTabloid|Tabloid (11 in. x 17 in.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Calidad de impresión**

Establece la calidad de impresión de las hojas de cálculo que se imprimirán con el método [**setPrintQuality**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). La unidad de medida de la calidad de impresión es puntos por pulgada (PPP).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Número de primera página**

Inicia la numeración de las páginas de la hoja de cálculo utilizando el método [**setFirstPageNumber**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). El método setFirstPageNumber establece el número de página de la primera página de la hoja de cálculo y las páginas siguientes se numeran en orden ascendente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Configurando Márgenes**

Aspose.Cells soporta completamente las opciones de configuración de página de Microsoft Excel. Los desarrolladores pueden necesitar configurar ajustes de configuración de página para hojas de cálculo para controlar el proceso de impresión. Este tema discute cómo usar Aspose.Cells para configurar márgenes de página.

**Márgenes de página en Microsoft Excel**

![todo:image_alt_text](page-setup-features_2.png)

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) que representa un archivo de Microsoft Excel. La clase Workbook contiene la colección Worksheets que permite acceder a cada hoja de cálculo en un archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

La clase Worksheet proporciona la propiedad PageSetup, que se utiliza para establecer opciones de configuración de página. El atributo PageSetup es un objeto de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup), lo que permite establecer diferentes opciones de diseño de página para una hoja de cálculo impresa. La clase PageSetup proporciona varias propiedades y métodos que se utilizan para establecer opciones de configuración de página.

### **Márgenes de Página**

Establece los márgenes (izquierdo, derecho, superior, inferior) de una página con los miembros de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). A continuación, se enumeran algunos de los métodos utilizados para especificar los márgenes de página:

- [**setLeftMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**setRightMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**setTopMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**setBottomMargin(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrar en la Página**

Es posible centrar algo en una página horizontal y verticalmente. La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) dispone de miembros con este propósito: [**setCenterHorizontally**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) y [**setCenterVertically**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Márgenes de Encabezado y Pie de Página**

Establece márgenes de encabezado y pie de página con miembros de [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tales como [**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) y [**setFooterMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Configuración de encabezados y pies de página**

Los encabezados y pies de página son secciones de texto e imágenes por encima del margen superior o por debajo del margen inferior de una página. También es posible agregar encabezados y pies de página a hojas de cálculo. Los encabezados y pies de página pueden utilizarse para mostrar cualquier tipo de información útil, como el número de página, nombre del autor, título del documento o fecha y hora. Los encabezados y pies de página también se gestionan utilizando el cuadro de diálogo Configuración de Página.

**El cuadro de diálogo Configuración de Página** 

![todo:image_alt_text](page-setup-features_3.png)

Aspose.Cells permite agregar encabezados y pies de página a las hojas de cálculo en tiempo de ejecución, pero se recomienda que los encabezados y pies de página se configuren manualmente en un archivo pre-diseñado para la impresión. Puedes utilizar Microsoft Excel como una herramienta gráfica para configurar fácilmente los encabezados y pies de página y así reducir el tiempo de desarrollo. Aspose.Cells puede importar el archivo y mantener estas configuraciones.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona clases especiales y algunos comandos de script para controlar el formato.

### **Comandos de Script**

Los comandos de script son comandos especiales proporcionados por Aspose.Cells que permiten a los desarrolladores dar formato a los encabezados y pies de página.

|**Comandos de Script**|**Descripción**|
| :- | :- |
|&P|El número de página actual.|
|&G|Una imagen.|
|&N|El número total de páginas.|
|&D|La fecha actual.|
|&T|La hora actual.|
|&A|El nombre de la hoja de cálculo.|
|&F|El nombre del archivo sin la ruta.|
|&&Texto|Muestra &Texto. Por ejemplo: &&WO será mostrado como &WO|
|&"\<FontName>"|Un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nombre de fuente con un estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de la fuente. Por ejemplo: “&14abc”. Sin embargo, si este comando va seguido de un número normal a imprimir en el encabezado, esto debe separarse con un carácter de espacio del tamaño de la fuente. Por ejemplo: “&14 123”.|

### **Establecer Encabezados y Pies de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) proporciona el método [**setHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader-int-java.lang.String-) para agregar un encabezado y [**setFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter-int-java.lang.String-) para agregar un pie de página a una hoja de cálculo. El script se utiliza como argumento para todos los métodos mencionados anteriormente. Representa el script a usar para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Insertar un Gráfico en un Encabezado o Pie de Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) tiene los métodos [**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture-int-byte[]-) y [**setFooterPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture-int-byte[]-) para agregar imágenes al encabezado y pie de página de una hoja de cálculo. Estos métodos reciben dos parámetros:

- **Sección**, la sección del encabezado o pie de página donde se colocará la imagen. Hay tres secciones: izquierda, centro y derecha, representadas por los valores numéricos 0, 1 y 2 respectivamente.
- **Flujo de Entrada de Archivo**, los datos gráficos. Los datos binarios deben ser escritos en el búfer de una matriz de bytes.

Después de ejecutar el código y abrir el archivo, verifica el encabezado de la hoja de cálculo en Microsoft Excel:

1. En el menú **Archivo**, selecciona **Configurar Página**.
1. En el cuadro de diálogo Configurar Página, selecciona la pestaña **Encabezado/Pie de Página**.

**Insertar un gráfico en un encabezado/pie de página** 

![todo:image_alt_text](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Insertar un Gráfico solo en el Encabezado de la Primera Página**

La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) también tiene otros métodos útiles, como [**setPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture-boolean-boolean-boolean-int-byte[]-), [**setFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader-int-java.lang.String-), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter-int-java.lang.String-), para agregar imágenes al encabezado/pie de página de la primera página de una hoja de cálculo. La primera página es especial: es común querer que muestre información especial, por ejemplo, un logotipo de empresa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Configuración de Opciones de Impresión**

Los ajustes de configuración de página de Microsoft Excel proporcionan varias opciones de impresión (también conocidas como opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo. Estas opciones de impresión permiten a los usuarios:

- Seleccionar un área de impresión específica en una hoja de cálculo.
- Títulos de impresión.
- Líneas de cuadrícula de impresión.
- Imprimir encabezados de filas y columnas
- Lograr calidad de borrador.
- Comentarios de impresión.
- Errores de celda de impresión.
- Definir el orden de páginas.

Todas estas opciones de impresión se muestran a continuación.

**Opciones de impresión (hoja)** 

![todo:image_alt_text](page-setup-features_5.png)

### **Configuración de opciones de impresión y hoja**

spose.Cells admite todas las opciones de impresión ofrecidas por Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para hojas de cálculo utilizando las propiedades ofrecidas por la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Cómo se utilizan estas propiedades se discute a continuación con más detalle.

### **Establecer Área de Impresión**

De forma predeterminada, solo el área de impresión incorpora todas las áreas de la hoja de trabajo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de trabajo.

Para seleccionar un área de impresión específica, utilice la propiedad [**setPrintArea**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup). Asigne un rango de celdas que defina el área de impresión a esta propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Establecer Títulos de Impresión**

Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de cálculo impresa. Para hacerlo, utilice las propiedades [**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) y [**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) de la clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup).

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Establecer Otras Opciones de Impresión**

La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) también proporciona varias otras propiedades para establecer opciones generales de impresión como sigue:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), una propiedad booleana que define si imprimir las líneas de la cuadrícula o no imprimir.
- [*setPrintHeadings*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), una propiedad booleana que define si imprimir los encabezados de fila y columna o no imprimirlos.
- [**setBlackAndWhite**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), una propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), define si mostrar los comentarios de impresión en la hoja de cálculo o al final de la hoja de cálculo.
- [**setPrintDraft**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), una propiedad booleana que define si imprimir la hoja de cálculo en calidad preliminar o no.
- [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), define si imprimir los errores de celda tal como se muestran, en blanco, con un guion o como N/A.

Para establecer las propiedades [**PrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) y [**PrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), Aspose.Cells también proporciona dos enumeraciones, [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) y [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType), que contienen valores predefinidos para ser asignados a las propiedades [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) y [**setPrintErrors**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) respectivamente.

Los valores predefinidos en la enumeración [**PrintCommentsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) se describen a continuación.

|**Tipos de Imprimir Comentarios**|**Descripción**|
| :- | :- |
|[**PRINT_IN_PLACE**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-IN-PLACE)|Especifica imprimir comentarios como se muestran en la hoja.|
|[**PRINT_NO_COMMENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-NO-COMMENTS)|Especifica no imprimir comentarios.|
|[**PRINT_SHEET_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT-SHEET-END)|Especifica imprimir comentarios al final de la hoja.|

Los valores predefinidos de la enumeración [**PrintErrorsType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) se describen a continuación.

|**Tipos de Imprimir Errores**|**Descripción**|
| :- | :- |
|[**PRINT_ERRORS_BLANK**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-BLANK)|Especifica no imprimir errores.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DASH)|Especifica imprimir errores como "--".|
|[**PRINT_ERRORS_DISPLAYED**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-DISPLAYED)|Especifica imprimir errores tal cual se muestran.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT-ERRORS-NA)|Especifica imprimir errores como "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Establecer Orden de Páginas**

La clase [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) proporciona la propiedad [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) que se utiliza para ordenar múltiples páginas de su hoja de cálculo para imprimir. Hay dos posibilidades de ordenar las páginas de la siguiente manera:

- **Abajo y luego a la derecha** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **A la derecha y luego hacia abajo** imprime las páginas de izquierda a derecha antes de imprimir cualquier página debajo.

Aspose.Cells proporciona una enumeración, [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType), que contiene todos los tipos de orden predefinidos para ser asignados al método [**setOrder**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order).

Los valores predefinidos de la enumeración [**PrintOrderType**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) se describen a continuación.

|**Tipos de Orden de Impresión**|**Descripción**|
| :- | :- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN-THEN-OVER)|Imprimir hacia abajo, luego a la derecha.|
|[**OVER_THEN_DOWN**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER-THEN-DOWN)|Imprimir sobre, luego abajo.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel**

Por favor, consulte este artículo relacionado con este tema.

## **Temas avanzados**
- [Calcular Factor de Escalado de la Configuración de Página](/cells/es/java/calculate-page-setup-scaling-factor/)
- [Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino](/cells/es/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Determinar si el tamaño de papel de la hoja de cálculo es automático](/cells/es/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Obtener Ancho y Alto del Papel desde la Configuración de Página de la Hoja de Trabajo](/cells/es/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementar Tamaño de Papel Personalizado de la Hoja de Cálculo para el Renderizado](/cells/es/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Configuración de página y opciones de impresión](/cells/es/java/page-setup-and-printing-options/)
- [Eliminar la configuración existente de PrinterSettings de las hojas de cálculo en el archivo de Excel](/cells/es/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
{{< app/cells/assistant language="java" >}}
