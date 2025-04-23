---
title: Öffentliche API Änderungen in Aspose.Cells 8.8.0
type: docs
weight: 270
url: /de/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an der Aspose.Cells-API von Version 8.7.2 auf 8.8.0, die für Modul-/Anwendungsentwickler interessant sein könnten. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte & entfernte Klassen usw., sondern auch eine Beschreibung etwaiger Änderungen im Verhalten hinter den Kulissen von Aspose.Cells.

{{% /alert %}} 
## **Hinzugefügte APIs**
### **Zellverweise für externe Verbindung abrufen**
Aspose.Cells for Java 8.8.0 hat die folgenden neuen Eigenschaften freigegeben, die bei der Abrufung der Ziel- und Ausgangszellverweise für externe Verbindungen in der Tabellenkalkulation hilfreich sind. 

1. QueryTable.ConnectionId: Ruft die Verbindungs-ID der Abfrage-Tabelle ab.
1. ExternalConnection.Id: Ruft die ID der externen Verbindung ab.
1. ListObject.QueryTable: Ruft die verknüpfte QueryTable ab.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel über [das Auffinden von Abfrage-Tabellen und List-Objekten, die mit externen Datenverbindungen zusammenhängen](/cells/de/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Hinzugefügte HTMLLoadOptions.KeepPrecision Eigenschaft**
Aspose.Cells for Java 8.8.0 hat die HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt, um die Konvertierung langer numerischer Werte in eine exponentielle Notation beim Import von HTML-Dateien zu steuern. Standardmäßig wird ein Wert länger als 15 Stellen in eine exponentielle Notation konvertiert, wenn die Daten aus einer HTML-Zeichenkette oder -datei importiert werden. Jetzt können Benutzer dieses Verhalten mit Hilfe der HTMLLoadOptions.KeepPrecision-Eigenschaft steuern. Wenn diese Eigenschaft auf true gesetzt ist, werden die Werte wie im Quelltext importiert.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel [Vermeiden der Umwandlung großer numerischer Werte in Exponentialnotation](/cells/de/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Im Folgenden wird das einfache Anwendungsszenario beschrieben.

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
### **Hinzugefügte Eigenschaft HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel [Überflüssige Leerzeichen aus HTML löschen](/cells/de/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus. 

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
### **Hinzugefügte Eigenschaft Style.QuotePrefix**
Aspose.Cells for Java 8.8.0 hat die Eigenschaft Style.QuotePrefix freigegeben, um zu erkennen, ob ein Zellenwert mit einem einzelnen Anführungszeichen beginnt. 

{{% alert color="primary" %}} 

Für weitere Details zu diesem Feature lesen Sie bitte den ausführlichen Artikel [Erkennen eines einzelnen Anführungszeichens am Anfang des Zellenwerts](/cells/de/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Das einfache Anwendungsszenario sieht wie folgt aus. 

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
## **Veraltete APIs**
### **Veraltete LoadOptions.ConvertNumericData-Eigenschaft**
Aspose.Cells 8.8.0 hat die LoadOptions.ConvertNumericData-Eigenschaft als veraltet markiert. Bitte verwenden Sie die entsprechende Eigenschaft der Klassen HTMLLoadOptions oder TxtLoadOptions.
{{< app/cells/assistant language="java" >}}
