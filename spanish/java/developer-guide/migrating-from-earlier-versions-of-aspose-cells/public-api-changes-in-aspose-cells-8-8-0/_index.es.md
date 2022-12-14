---
title: Público API Cambios en Aspose.Cells 8.8.0
type: docs
weight: 270
url: /es/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.2 a la 8.8.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Obtenga referencias Cell para conexión externa**
 Aspose.Cells for Java 8.8.0 ha expuesto las siguientes propiedades nuevas que son útiles para recuperar las referencias de celda de destino y salida para conexiones externas almacenadas en la hoja de cálculo.

1. QueryTable.ConnectionId: Obtiene el Id. de conexión de la tabla de consulta.
1. ExternalConnection.Id: Obtiene el Id de la conexión externa.
1. ListObject.QueryTable: Obtiene el QueryTable vinculado.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas](/cells/es/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Se agregó la propiedad HTMLLoadOptions.KeepPrecision**
Aspose.Cells for Java 8.8.0 agregó la propiedad HTMLLoadOptions.KeepPrecision para controlar la conversión de valores numéricos largos a notación exponencial al importar archivos HTML. De forma predeterminada, cualquier valor de más de 15 dígitos se convierte a notación exponencial si los datos se importan desde una cadena o un archivo HTML. Sin embargo, ahora los usuarios pueden controlar este comportamiento con la ayuda de la propiedad HTMLLoadOptions.KeepPrecision. Si dicha propiedad se establece en verdadero, los valores se importarán tal como están en la fuente.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[ Evite la conversión de valores numéricos grandes a notación exponencial](/cells/es/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Se agregó la propiedad HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for Java 8.8.0 ha expuesto la propiedad HTMLLoadOptions.DeleteRedundantSpaces para mantener o eliminar los espacios adicionales después de la etiqueta de salto de línea (<br>Tag) al importar los datos de la cadena o archivo HTML. La propiedad HTMLLoadOptions.DeleteRedundantSpaces tiene el valor predeterminado falso, lo que significa que todos los espacios adicionales se conservarán e importarán al objeto Libro de trabajo; sin embargo, cuando se establece en verdadero, API eliminará todos los espacios redundantes que vienen después de la etiqueta de salto de línea.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Eliminar espacios redundantes de HTML](/cells/es/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 El escenario de uso simple se ve de la siguiente manera.

**Java**

{{< highlight "csharp" >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[]byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Se agregó la propiedad Style.QuotePrefix**
 Aspose.Cells for Java 8.8.0 ha expuesto la propiedad Style.QuotePrefix para detectar si un valor de celda comienza con un símbolo de comilla simple.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Detectar comillas simples al comienzo del valor Cell](/cells/es/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 El escenario de uso simple se ve de la siguiente manera.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **API obsoletas**
### **Propiedad LoadOptions.ConvertNumericData obsoleta**
Aspose.Cells 8.8.0 marcó la propiedad LoadOptions.ConvertNumericData como obsoleta. Utilice la propiedad correspondiente de las clases HTMLLoadOptions o TxtLoadOptions.
