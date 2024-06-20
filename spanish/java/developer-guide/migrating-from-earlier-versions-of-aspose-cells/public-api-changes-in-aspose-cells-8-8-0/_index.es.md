---
title: Cambios en la API pública en Aspose.Cells 8.8.0
type: docs
weight: 270
url: /es/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.7.2 hasta la 8.8.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Obtener referencias de celda para conexión externa**
Aspose.Cells for Java 8.8.0 ha expuesto las siguientes nuevas propiedades que son útiles para recuperar las referencias de celdas de destino y de salida para las conexiones externas almacenadas en la hoja de cálculo. 

1. QueryTable.ConnectionId: Obtiene el Id de conexión de la tabla de consulta.
1. ExternalConnection.Id: Obtiene el Id de la conexión externa.
1. ListObject.QueryTable: Obtiene la QueryTable vinculada.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Buscar Tablas de consulta y Objetos de lista relacionados con las Conexiones de datos externas](/cells/es/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Propiedad HTMLLoadOptions.KeepPrecision agregada**
Aspose.Cells for Java 8.8.0 ha agregado la propiedad HTMLLoadOptions.KeepPrecision para controlar la conversión de valores numéricos largos a notación exponencial durante la importación de archivos HTML. Por defecto, cualquier valor mayor de 15 dígitos se convierte a notación exponencial si los datos se importan de una cadena o archivo HTML. Sin embargo, ahora los usuarios pueden controlar este comportamiento con la ayuda de la propiedad HTMLLoadOptions.KeepPrecision. Si dicha propiedad se establece en verdadero, los valores se importarán tal como están en la fuente.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Evitar la Conversión de Valores Numéricos Grandes a Notación Exponencial](/cells/es/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

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
### **Propiedad HTMLLoadOptions.DeleteRedundantSpaces agregada**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Eliminar Espacios Redundantes de HTML](/cells/es/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Un escenario de uso simple se ve como sigue. 

**Java**

{{< highlight csharp >}}

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

byte[] byteArray = html.getBytes();

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
### **Propiedad Style.QuotePrefix agregada**
Aspose.Cells for Java 8.8.0 ha expuesto la propiedad Style.QuotePrefix para detectar si un valor de celda comienza con un solo símbolo de comilla. 

{{% alert color="primary" %}} 

Para más detalles sobre esta característica, por favor revise el artículo detallado en [Detectar Comilla Simple al Inicio del Valor de Celda](/cells/es/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Un escenario de uso simple se ve como sigue. 

**Java**

{{< highlight csharp >}}

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
## **APIs obsoletas**
### **Propiedad Obsoleta LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 ha marcado la propiedad LoadOptions.ConvertNumericData como obsoleta. Por favor, utilice la propiedad correspondiente de las clases HTMLLoadOptions o TxtLoadOptions.
