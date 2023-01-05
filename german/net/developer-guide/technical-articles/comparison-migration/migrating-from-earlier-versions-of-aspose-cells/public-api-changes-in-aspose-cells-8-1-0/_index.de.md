---
title: Öffentlich API Änderungen in Aspose.Cells 8.1.0
type: docs
weight: 40
url: /de/net/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an Aspose.Cells API von Version 8.0.2 zu 8.1.0, die für Modul-/Anwendungsentwickler von Interesse sein könnten. Es enthält nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung aller Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse hat die ExportHiddenWorksheet-Eigenschaft verfügbar gemacht, die verwendet werden kann, um anzugeben, ob ausgeblendete Arbeitsblätter in das HTML-Format exportiert werden. Der Standardwert ist wahr. wohingegen, wenn auf „false“ gesetzt, Aspose.Cells keine versteckten Arbeitsblattinhalte exportiert.

{{% alert color="primary" %}} 

 Bitte lesen Sie den ausführlichen Artikel auf[Verhindern Sie den Export von versteckten Arbeitsblättern](/cells/de/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Eigenschaft Cell.StringValueWithoutFormat hinzugefügt**
Die Eigenschaft „StringValueWithoutFormat“ wurde der Klasse „Cell“ hinzugefügt, um den Entwicklern das Abrufen des Zellenwerts ohne angewendete Formatierung zu erleichtern.

Das unten bereitgestellte Code-Snippet demonstriert die Verwendung der Eigenschaft Cell.StringValueWithoutFormat im Vergleich zu cell.DisplayStringValue, indem eine Tabelle von Grund auf neu erstellt und das Zahlenformat auf eine der Zellen angewendet wird.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

Die Ausgabe des obigen Codes ist wie folgt

123,456

123456

{{% /alert %}}
## **Veraltete Eigenschaften von Bytes, Zeichen, CharactersWithSpaces, Zeilen, Absätzen**
Viele Eigenschaften der Klasse BuiltInDocumentPropertyCollection wurden ab Aspose.Cells for .NET 8.1.0 als veraltet markiert. Zu diesen Eigenschaften gehören Bytes, Zeichen, CharactersWithSpaces, Zeilen und Absätze. Der Grund dafür ist, dass die oben genannten Eigenschaften bei der Konservierung von Excel-Tabellen nicht von Nutzen sind, da Excel sie weglässt. Wobei diese Eigenschaften ursprünglich für Word-Dokumente und PowerPoint-Präsentationen geschrieben wurden.
