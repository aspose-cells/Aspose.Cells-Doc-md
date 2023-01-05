---
title: Öffentlich API Änderungen in Aspose.Cells 8.1.0
type: docs
weight: 50
url: /de/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.0.2 zu 8.1.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse hat die ExportHiddenWorksheet-Eigenschaft verfügbar gemacht, die verwendet werden kann, um anzugeben, ob ausgeblendete Arbeitsblätter in das HTML-Format exportiert werden. Der Standardwert ist wahr. wohingegen, wenn auf „false“ gesetzt, Aspose.Cells keine versteckten Arbeitsblattinhalte exportiert.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Verhindern Sie den Export von versteckten Arbeitsblättern](/cells/de/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Eigenschaft Cell.StringValueWithoutFormat hinzugefügt**
 Die Eigenschaft „StringValueWithoutFormat“ wurde der Klasse „Cell“ hinzugefügt, um den Entwicklern das Abrufen des Zellenwerts ohne angewendete Formatierung zu erleichtern.

Das unten bereitgestellte Code-Snippet demonstriert die Verwendung der Methode Cell.getStringValueWithoutFormat im Vergleich zu cell.getDisplayStringValue, indem eine Tabelle von Grund auf neu erstellt und das Zahlenformat auf eine der Zellen angewendet wird.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Die Ausgabe des obigen Codes ist wie folgt

Wert der formatierten Zeichenfolge: 123.456
Unformatierter Zeichenfolgenwert: 123456

{{% /alert %}}
## **Veraltete Eigenschaften von Bytes, Zeichen, CharactersWithSpaces, Zeilen, Absätzen**
 Viele Eigenschaften der Klasse BuiltInDocumentPropertyCollection wurden ab Aspose.Cells for .NET 8.1.0 als veraltet markiert. Zu diesen Eigenschaften gehören Bytes, Zeichen, CharactersWithSpaces, Zeilen und Absätze. Der Grund dafür ist, dass die oben genannten Eigenschaften bei der Konservierung von Excel-Tabellen nicht von Nutzen sind, da Excel sie weglässt. Wobei diese Eigenschaften ursprünglich für Word-Dokumente und PowerPoint-Präsentationen geschrieben wurden.
