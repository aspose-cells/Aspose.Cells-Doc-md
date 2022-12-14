---
title: Funciones de configuración de página
type: docs
weight: 40
url: /es/java/page-setup-features/
---
A veces, es necesario configurar los ajustes de configuración de la página para que las hojas de trabajo controlen la impresión. Estos ajustes de configuración de página ofrecen varias opciones.

**Opciones de página** 

![todo:imagen_alternativa_texto](page-setup-features_1.png)

Las opciones de configuración de página son totalmente compatibles con Aspose.Cells. Este artículo explica cómo configurar las opciones de página con Aspose.Cells.

## **Configuración de opciones de página**

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , que representa un archivo de Excel Microsoft. La clase Libro de trabajo contiene una colección de Hojas de trabajo que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

La clase Worksheet proporciona la propiedad PageSetup, que se utiliza para configurar las opciones de configuración de la página. De hecho, la propiedad PageSetup es un objeto de la clase PageSetup que permite establecer opciones de diseño de página para una hoja de trabajo impresa. La clase PageSetup proporciona varias propiedades que se utilizan para establecer las opciones de configuración de la página. Algunas de estas propiedades se analizan a continuación.

### **Orientación de la página**

 La orientación de la página se puede establecer en vertical u horizontal mediante el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) método. los[**setOrientation(PageOrientationType)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Orientation) método toma el[**Tipo de orientación de página**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType) enumeración como parámetro. los miembros de la[**Tipo de orientación de página**](https://reference.aspose.com/cells/java/com.aspose.cells/PageOrientationType)enumeración se enumeran a continuación.

|**Tipos de orientación de página**|**Descripción**|
|:- |:- |
|[**PAISAJE**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#LANDSCAPE)|Orientación horizontal|
|[**RETRATO**](https://reference.aspose.com/cells/java/com.aspose.cells/pageorientationtype#PORTRAIT)|Orientación Vertical|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageOrientation-PageOrientation.java" >}}

### **Factor de escala**

 Es posible reducir o aumentar el tamaño de una hoja de trabajo ajustando el factor de escala con el[**establecerZoom**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Zoom) metodo de la[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ScalingFactor-ScalingFactor.java" >}}

### **Opciones de FitToPages**

 Para ajustar el contenido de la hoja de trabajo a un número específico de páginas, use el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**establecerFitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) y[**establecerFitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide) métodos. Estos métodos también se utilizan para escalar hojas de trabajo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FitToPagesOptions-FitToPagesOptions.java" >}}

### **Tamaño de papel**

 Establezca el tamaño de papel en el que se imprimirán las hojas de trabajo utilizando el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**Tamaño de papel**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PaperSize) propiedad. La propiedad PaperSize acepta uno de los valores predefinidos en el[**Tipo de tamaño de papel**](https://reference.aspose.com/cells/java/com.aspose.cells/PaperSizeType) enumeración, que se enumeran a continuación.

|**Tipos de tamaño de papel**|**Descripción**|
|:- |:- |
|Papel10x14|10 pulgadas x 14 pulgadas|
|Papel11x17|11 pulgadas x 17 pulgadas|
|PapelA3|A3 (297 mm x 420 mm)|
|PapelA4|A4 (210 mm x 297 mm)|
|PapelA4Pequeño|A4 pequeño (210 mm x 297 mm)|
|PapelA5|A5 (148 mm x 210 mm)|
|PapelB3|B3 (13,9 x 19,7 pulgadas)|
|PapelB4|B4 (250 mm x 354 mm)|
|PapelB5|B5 (182 mm x 257 mm)|
|PapelNegocioTarjeta|Tarjeta de visita (90 mm x 55 mm)|
|PapelCHoja|Hoja de tamaño C|
|PapelDHoja|Hoja de tamaño D|
|PapelSobre10|Sobre #10 (4-1/8 pulg. x 9-1/2 pulg.)|
|PapelSobre11|Sobre #11 (4-1/2 pulg. x 10-3/8 pulg.)|
|PapelSobre12|Sobre #12 (4-1/2 pulg. x 11 pulg.)|
|PapelSobre14|Sobre #14 (5 pulg. x 11-1/2 pulg.)|
|PapelSobre9|Sobre #9 (3-7/8 pulg. x 8-7/8 pulg.)|
|PapelSobreB4|Sobre B4 (250 mm x 353 mm)|
|PapelSobreB5|Sobre B5 (176 mm x 250 mm)|
|PapelSobreB6|Sobre B6 (176 mm x 125 mm)|
|PapelSobreC3|Sobre C3 (324 mm x 458 mm)|
|PapelSobreC4|Sobre C4 (229 mm x 324 mm)|
|PapelSobreC5|Sobre C5 (162 mm x 229 mm)|
|PapelSobreC6|Sobre C6 (114 mm x 162 mm)|
|PapelSobreC65|Sobre C65 (114 mm x 229 mm)|
|PapelSobreDL|Sobre DL (110 mm x 220 mm)|
|De PapelSobreItalia|Sobre Italia (110 mm x 230 mm)|
|De PapelSobreMonarca|Sobre monarca (3-7/8 pulg. x 7-1/2 pulg.)|
|De PapelSobrePersonal|Sobre (3-5/8 pulg. x 6-1/2 pulg.)|
|PapelEHoja|Hoja de tamaño E|
|PapelEjecutivo|Ejecutivo (7-1/2 pulg. x 10-1/2 pulg.)|
|PapelFanfoldLegalAlemán|Folleto en acordeón alemán legal (8-1/2 pulg. x 13 pulg.)|
|PaperFanfoldStdAlemán|Plegado estándar alemán (8-1/2 pulg. x 12 pulg.)|
|PaperFanfoldUS|Plegado estándar de EE. UU. (14-7/8 pulg. x 11 pulg.)|
|PapelFolio|Folio (8-1/2 pulg. x 13 pulg.)|
|libro mayor|Libro mayor (17 pulg. x 11 pulg.)|
|PapelLegal|Legal (8-1/2 pulg. x 14 pulg.)|
|PapelCarta|Carta (8-1/2 pulg. x 11 pulg.)|
|De PapelCartaPequeños|Carta pequeña (8-1/2 pulg. x 11 pulg.)|
|Nota de papel|Nota (8-1/2 pulg. x 11 pulg.)|
|PaperQuarto|Cuarto (215 mm x 275 mm)|
|PaperStatement|Declaración (5-1/2 pulg. x 8-1/2 pulg.)|
|Tabloide de papel|Tabloide (11 pulg. x 17 pulg.)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ManagePaperSize-ManagePaperSize.java" >}}

### **Calidad de impresión**

 Establezca la calidad de impresión de las hojas de trabajo que se imprimirán con el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**establecerCalidadDeImpresión**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintQuality) método. La unidad de medida de la calidad de impresión son los puntos por pulgada (DPI).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintQuality-SetPrintQuality.java" >}}

### **Número de la primera página**

 Inicie la numeración de las páginas de la hoja de trabajo usando el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**establecerNúmeroPrimeraPágina**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FirstPageNumber) método. El método setFirstPageNumber establece el número de página de la primera página de la hoja de trabajo y las siguientes páginas se numeran en orden ascendente.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetFirstPageNumber-SetFirstPageNumber.java" >}}

## **Configuración de márgenes**

Aspose.Cells es totalmente compatible con las opciones de configuración de página de Microsoft de Excel. Es posible que los desarrolladores necesiten configurar los ajustes de configuración de la página para que las hojas de trabajo controlen el proceso de impresión. Este tema trata sobre cómo usar Aspose.Cells para configurar los márgenes de página.

**Márgenes de página en Microsoft Excel**

![todo:imagen_alternativa_texto](page-setup-features_2.png)

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)que representa un archivo de Excel Microsoft. La clase Workbook contiene la colección Worksheets que permite el acceso a cada hoja de trabajo en un archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) clase.

 La clase Worksheet proporciona la propiedad PageSetup, que se utiliza para configurar las opciones de configuración de la página. El atributo PageSetup es un objeto del[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class que permite establecer diferentes opciones de diseño de página para una hoja de trabajo impresa. La clase PageSetup proporciona varias propiedades y métodos que se utilizan para configurar las opciones de configuración de la página.

### **Márgenes de página**

 Establecer los márgenes (izquierdo, derecho, superior, inferior) de una página con[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) miembros de la clase A continuación se enumeran algunos de los métodos utilizados para especificar los márgenes de página:

- [**establecerMargenIzquierdo(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#LeftMargin)
- [**establecerMargenDerecho(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#RightMargin)
- [**establecerMargenSuperior(int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#TopMargin)
- [**establecer margen inferior (int)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BottomMargin)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetMargins-SetMargins.java" >}}

### **Centrar en la página**

 Es posible centrar algo en una página horizontal y verticalmente. los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) La clase tiene miembros para este propósito:[**establecerCentroHorizontalmente**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterHorizontally) y[**establecerCentroVerticalmente**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#CenterVertically).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-CenterOnPage-CenterOnPage.java" >}}

### **Márgenes de encabezado y pie de página**

Establecer márgenes de encabezado y pie de página con[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) miembros como[**setHeaderMargin**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#HeaderMargin) y[**establecer Margen de pie de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FooterMargin).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HeaderAndFooterMargins-HeaderAndFooterMargins.java" >}}

## **Configuración de encabezados y pies de página**

Los encabezados y pies de página son las secciones de texto e imágenes que se encuentran sobre el margen superior o debajo del margen inferior de una página. También es posible agregar encabezados y pies de página a las hojas de trabajo. Los encabezados y pies de página se pueden usar para mostrar cualquier tipo de información útil, por ejemplo, el número de página, el nombre del autor, el título del documento o la fecha y la hora. Los encabezados y pies de página también se administran mediante el cuadro de diálogo Configuración de página.

**El cuadro de diálogo Configurar página** 

![todo:imagen_alternativa_texto](page-setup-features_3.png)

Aspose.Cells permite agregar encabezados y pies de página a las hojas de trabajo en tiempo de ejecución, pero se recomienda que los encabezados y pies de página se configuren manualmente en un archivo prediseñado para imprimir. Puede usar Microsoft Excel como una herramienta GUI para establecer encabezados y pies de página fácilmente para reducir el tiempo de desarrollo. Aspose.Cells puede importar el archivo y reservar estos ajustes.

Para agregar encabezados y pies de página en tiempo de ejecución, Aspose.Cells proporciona clases especiales y algunos comandos de script para controlar el formato.

### **Comandos de secuencia de comandos**

Los comandos de script son comandos especiales proporcionados por Aspose.Cells que permiten a los desarrolladores formatear encabezados y pies de página.

|**Comandos de secuencia de comandos**|**Descripción**|
|:- |:- |
|&PAGS|El número de página actual.|
|&GRAMO|Una foto.|
|&NORTE|El número total de páginas.|
|&D|La fecha actual.|
|&T|La hora actual.|
|&A|El nombre de la hoja de trabajo.|
|&F|El nombre del archivo sin la ruta.|
|&"\<FontName>"|Un nombre de fuente. Por ejemplo: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Un nombre de fuente con un estilo. Por ejemplo: &"Arial,Negrita"|
|&\<FontSize>|Representa el tamaño de fuente. Por ejemplo: “&14abc”. Pero, si este comando es seguido por un número simple para imprimir en el encabezado, este debe estar separado del tamaño de fuente con un carácter de espacio. Por ejemplo: “&14 123”.|

### **Establecer encabezados y pies de página**

 los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la clase proporciona el método[**establecerEncabezado**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeader(int,%20java.lang.String) para agregar un encabezado y[**establecer pie de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooter(int,%20java.lang.String)) para agregar un pie de página a una hoja de cálculo. El script se utiliza como argumento para todos los métodos mencionados anteriormente. Representa el script que se utilizará para el encabezado o pie de página. Este script contiene comandos de script para formatear encabezados o pies de página.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetHeadersAndFooters-SetHeadersAndFooters.java" >}}

### **Insertar un gráfico en un encabezado o pie de página**

 los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la clase tiene los métodos[**setHeadPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setHeaderPicture(int,%20byte[]) ) y[**establecer imagen de pie de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFooterPicture(int,%20byte[])) para agregar imágenes al encabezado y pie de página de una hoja de trabajo. Estos métodos toman dos parámetros:

- **Sección**, la sección del encabezado o pie de página donde se colocará la imagen. Hay tres secciones: izquierda, centro y derecha, representadas por los valores numéricos 0, 1 y 2 respectivamente.
- **Flujo de entrada de archivo**, los datos gráficos. Los datos binarios deben escribirse en el búfer de una matriz de bytes.

Después de ejecutar el código y abrir el archivo, verifique el encabezado de la hoja de trabajo en Microsoft Excel:

1.  Sobre el**Expediente** menú, seleccione**Configuración de página**.
1.  En el cuadro de diálogo Configurar página, seleccione el**Encabezado/Pie de página** pestaña.

**Insertar un gráfico en un encabezado/pie de página** 

![todo:imagen_alternativa_texto](page-setup-features_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertImageInHeaderFooter-InsertImageInHeaderFooter.java" >}}

### **Insertar un gráfico solo en el encabezado de la primera página**

 los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class también tiene otros métodos útiles, por ejemplo[**establecerImagen**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setPicture(boolean,%20boolean,%20boolean,%20int,%20byte[])), [**establecerFirstPageHeader**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageHeader(int,%20java.lang.String)), [**setFirstPageFooter**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#setFirstPageFooter(int,%20java.lang.String)), para agregar imágenes en el encabezado/pie de página de la primera página de una hoja de cálculo. La primera página es una página especial: es común querer que muestre información especial, por ejemplo, el logotipo de una empresa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-InsertGraphicinFirstPageHeaderOnly-InsertGraphicinFirstPageHeaderOnly.java" >}}

## **Configuración de las opciones de impresión**

Microsoft Los ajustes de configuración de página de Excel proporcionan varias opciones de impresión (también denominadas opciones de hoja) que permiten a los usuarios controlar cómo se imprimen las páginas de la hoja de cálculo. Estas opciones de impresión permiten a los usuarios:

- Seleccione un área de impresión específica en una hoja de trabajo.
- Imprimir títulos.
- Imprimir líneas de cuadrícula.
- Imprimir encabezados de filas y columnas
- Consiga calidad de borrador.
- Imprimir comentarios.
- Imprimir errores de celda.
- Definir el orden de las páginas.

Todas estas opciones de impresión se muestran a continuación.

**Opciones de impresión (hoja)** 

![todo:imagen_alternativa_texto](page-setup-features_5.png)

### **Configuración de las opciones de impresión y hoja**

 spose.Cells admite todas las opciones de impresión que ofrece Microsoft Excel y los desarrolladores pueden configurar fácilmente estas opciones para las hojas de trabajo utilizando las propiedades que ofrece el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup)clase. Cómo se utilizan estas propiedades se analiza a continuación con más detalle.

### **Establecer área de impresión**

De manera predeterminada, solo el área de impresión incorpora todas las áreas de la hoja de cálculo que contienen datos. Los desarrolladores pueden establecer un área de impresión específica de la hoja de trabajo.

 Para seleccionar un área de impresión específica, use el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**establecerárea de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintArea) propiedad. Asigne un rango de celdas que defina el área de impresión a esta propiedad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintArea-SetPrintArea.java" >}}

### **Establecer títulos de impresión**

 Aspose.Cells le permite designar encabezados de fila y columna para repetir en todas las páginas de una hoja de trabajo impresa. Para hacerlo, utilice el[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) clase'[**setPrintTitleColumns**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleColumns) y[**setPrintTitleRows**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintTitleRows) propiedades.

Las filas o columnas que se repetirán se definen pasando sus números de fila o columna. Por ejemplo, las filas se definen como $1:$2 y las columnas se definen como $A:$B.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPrintTitle-SetPrintTitle.java" >}}

### **Establecer otras opciones de impresión**

 los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) class también proporciona varias otras propiedades para establecer las opciones generales de impresión de la siguiente manera:

- [**setPrintGridlines**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintGridlines), una propiedad booleana que define si se imprimen líneas de cuadrícula o no.
- [*establecerEncabezados de impresión*](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintHeadings), una propiedad booleana que define si se imprimen o no los encabezados de fila y columna.
- [**conjuntoblancoynegro**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#BlackAndWhite), una propiedad booleana que define si imprimir la hoja de cálculo en modo blanco y negro o no.
- [**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments), define si mostrar los comentarios de impresión en la hoja de trabajo o al final de la hoja de trabajo.
- [**establecerImprimirBorrador**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintDraft), una propiedad booleana que define si imprimir la hoja de trabajo en calidad de borrador o no.
- [**establecer errores de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors), define si imprimir los errores de celda como mostrados, en blanco, guión o N/A.

 Para configurar el[**ImprimirComentarios**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) y[**Errores de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) properties, Aspose.Cells también proporciona dos enumeraciones,[**ImprimirComentariosTipo**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) y[**Tipo de error de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) que contienen valores predefinidos para ser asignados a la[**setPrintComments**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintComments) y[**establecer errores de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#PrintErrors) propiedades respectivamente.

 Los valores predefinidos en el[**ImprimirComentariosTipo**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintCommentsType) enumeración se describen a continuación.

|**Imprimir tipos de comentarios**|**Descripción**|
|:- |:- |
|[**IMPRIMIR_EN_LUGAR**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_IN_PLACE)|Especifica que se impriman los comentarios tal como se muestran en la hoja de trabajo.|
|[**IMPRIMIR_SIN_COMENTARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_NO_COMMENTS)|Especifica que no se impriman comentarios.|
|[**IMPRIMIR_HOJA_END**](https://reference.aspose.com/cells/java/com.aspose.cells/printcommentstype#PRINT_SHEET_END)|Especifica que se impriman comentarios al final de la hoja de trabajo.|

 Los valores predefinidos de la[**Tipo de error de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintErrorsType) enumeración se describen a continuación.

|**Tipos de errores de impresión**|**Descripción**|
|:- |:- |
|[*IMPRIMIR_ERRORS_BLANK*](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_BLANK)|Especifica que no se impriman errores.|
|[**PRINT_ERRORS_DASH**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DASH)|Especifica que se impriman errores como "--".|
|[**IMPRIMIR_ERRORS_VISUALIZADOS**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_DISPLAYED)|Especifica que se impriman los errores como se muestran.|
|[**PRINT_ERRORS_NA**](https://reference.aspose.com/cells/java/com.aspose.cells/printerrorstype#PRINT_ERRORS_NA)|Especifica que se impriman errores como "#N/A".|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-OtherPrintOptions-OtherPrintOptions.java" >}}

### **Establecer orden de página**

 los[**Configuración de página**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup) la clase proporciona la[**establecer orden**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) propiedad que se utiliza para ordenar que se impriman varias páginas de la hoja de trabajo. Hay dos posibilidades para ordenar las páginas de la siguiente manera:

- **Abajo y luego encima** imprime todas las páginas hacia abajo antes de imprimir cualquier página hacia la derecha.
- **arriba y luego abajo** imprime las páginas de izquierda a derecha antes de imprimir las siguientes páginas.

 Aspose.Cells proporciona una enumeración,[**Tipo de pedido de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) , que contiene todos los tipos de orden predefinidos que se asignarán a[**establecer orden**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#Order) método.

 Los valores predefinidos de[**Tipo de pedido de impresión**](https://reference.aspose.com/cells/java/com.aspose.cells/PrintOrderType) enumeración se describen a continuación.

|**Tipos de órdenes de impresión**|**Descripción**|
|:- |:- |
|[**DOWN_THEN_OVER**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#DOWN_THEN_OVER)|Imprime hacia abajo, luego hacia arriba.|
|[**SOBRE_ENTONCES_ABAJO**](https://reference.aspose.com/cells/java/com.aspose.cells/printordertype#OVER_THEN_DOWN)|Imprimir arriba, luego abajo.|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SetPageOrder-SetPageOrder.java" >}}

## **Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel**

Por favor, consulte este artículo relacionado con este tema.

## **Temas avanzados**
- [Calcular factor de escala de configuración de página](/cells/es/java/calculate-page-setup-scaling-factor/)
- [Copie la configuración de configuración de página de la hoja de trabajo de origen a la hoja de trabajo de destino](/cells/es/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/)
- [Determinar si el tamaño de papel de la hoja de trabajo es automático](/cells/es/java/determine-if-paper-size-of-worksheet-is-automatic/)
- [Obtenga el ancho y la altura del papel desde la configuración de la página de la hoja de trabajo](/cells/es/java/get-paper-width-and-height-from-pagesetup-of-worksheet/)
- [Implementar el tamaño de papel personalizado de la hoja de trabajo para la representación](/cells/es/java/implement-custom-paper-size-of-worksheet-for-rendering/)
- [Configuración de página y opciones de impresión](/cells/es/java/page-setup-and-printing-options/)
- [Eliminar la configuración de impresora existente de las hojas de trabajo en el archivo de Excel](/cells/es/java/remove-existing-printersettings-of-worksheets-in-excel-file/)
