---
title: Öffentlich API Änderungen in Aspose.Cells 8.8.0
type: docs
weight: 270
url: /de/java/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt die Änderungen an Aspose.Cells API von Version 8.7.2 zu 8.8.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, hinzugefügte und entfernte Klassen usw., sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **APIs hinzugefügt**
### **Rufen Sie Cell-Referenzen für die externe Verbindung ab**
 Aspose.Cells for Java 8.8.0 hat die folgenden neuen Eigenschaften verfügbar gemacht, die beim Abrufen der Ziel- und Ausgabezellreferenzen für externe Verbindungen, die in der Tabelle gespeichert sind, hilfreich sind.

1. QueryTable.ConnectionId: Ruft die Verbindungs-ID der Abfragetabelle ab.
1. ExternalConnection.Id: Ruft die ID der externen Verbindung ab.
1. ListObject.QueryTable: Ruft die verknüpfte QueryTable ab.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Suchen Sie Abfragetabellen und listen Sie Objekte auf, die sich auf externe Datenverbindungen beziehen](/cells/de/java/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.0 hat die HTMLLoadOptions.KeepPrecision-Eigenschaft hinzugefügt, um die Konvertierung langer numerischer Werte in Exponentialschreibweise beim Importieren von HTML-Dateien zu steuern. Standardmäßig wird jeder Wert mit mehr als 15 Ziffern in die Exponentialschreibweise konvertiert, wenn die Daten aus einer HTML-Zeichenfolge oder -Datei importiert werden. Jetzt können die Benutzer dieses Verhalten jedoch mithilfe der HTMLLoadOptions.KeepPrecision-Eigenschaft steuern. Wenn die besagte Eigenschaft auf „true“ gesetzt ist, werden die Werte so importiert, wie sie in der Quelle sind.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[ Vermeiden Sie die Umwandlung großer numerischer Werte in die Exponentialschreibweise](/cells/de/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

Es folgt das einfache Nutzungsszenario.

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
### **HTMLLoadOptions.DeleteRedundantSpaces-Eigenschaft hinzugefügt**
Aspose.Cells for Java 8.8.0 hat die Eigenschaft HTMLLoadOptions.DeleteRedundantSpaces verfügbar gemacht, um die zusätzlichen Leerzeichen nach dem Zeilenumbruch-Tag (<br>-Tag) beim Importieren der Daten aus der HTML-Zeichenfolge oder -Datei. Die Eigenschaft „HTMLLoadOptions.DeleteRedundantSpaces“ hat den Standardwert „false“, was bedeutet, dass alle zusätzlichen Leerzeichen beibehalten und in das Workbook-Objekt importiert werden. Wenn sie jedoch auf „true“ gesetzt ist, löscht API alle überflüssigen Leerzeichen nach dem Zeilenumbruch-Tag.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Löschen Sie redundante Leerzeichen aus HTML](/cells/de/java/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

 Ein einfaches Nutzungsszenario sieht wie folgt aus.

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
### **Style.QuotePrefix-Eigenschaft hinzugefügt**
 Aspose.Cells for Java 8.8.0 hat die Style.QuotePrefix-Eigenschaft verfügbar gemacht, um zu erkennen, ob ein Zellenwert mit einem einfachen Anführungszeichen beginnt.

{{% alert color="primary" %}} 

 Weitere Einzelheiten zu dieser Funktion finden Sie im ausführlichen Artikel unter[Einfaches Anführungszeichen am Anfang des Werts Cell erkennen](/cells/de/java/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

 Ein einfaches Nutzungsszenario sieht wie folgt aus.

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
## **Veraltete APIs**
### **Veraltete LoadOptions.ConvertNumericData-Eigenschaft**
Aspose.Cells 8.8.0 hat die Eigenschaft LoadOptions.ConvertNumericData als veraltet markiert. Bitte verwenden Sie die entsprechende Eigenschaft aus den Klassen HTMLLoadOptions oder TxtLoadOptions.
