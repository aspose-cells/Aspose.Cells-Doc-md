---
title: Öffentliche API Änderungen in Aspose.Cells 8.1.0
type: docs
weight: 40
url: /de/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.0.2 auf 8.1.0, die für Modul-/Anwendungs-Entwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse verfügt über das Attribut ExportHiddenWorksheet, das verwendet werden kann, um anzugeben, ob versteckte Arbeitsblätter im HTML-Format exportiert werden. Der Standardwert ist true. Wenn er jedoch auf false gesetzt wird, exportiert Aspose.Cells die Inhalte des versteckten Arbeitsblatts nicht.

{{% alert color="primary" %}} 

Bitte prüfen Sie den detaillierten Artikel zu [Verhindern des Exports von versteckten Arbeitsblattinhalten beim Speichern unter](/cells/de/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Hinzugefügtes Cell.StringValueWithoutFormat-Attribut**
Das StringValueWithoutFormat-Attribut wurde der Cell-Klasse hinzugefügt, um den Entwicklern das Abrufen des Zellenwerts ohne jegliche Formatierung zu ermöglichen.

Der unten bereitgestellte Codeausschnitt demonstriert die Verwendung der Cell.StringValueWithoutFormat-Eigenschaft im Vergleich zum cell.DisplayStringValue durch das Erstellen einer Tabelle von Grund auf und das Anwenden des Zahlenformats auf eine der Zellen.

**C#**

{{< highlight csharp >}}

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
## **Veraltete Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs-Eigenschaften**
Viele Eigenschaften der Klasse BuiltInDocumentPropertyCollection wurden ab Aspose.Cells for .NET 8.1.0 als veraltet markiert. Dazu gehören Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Der Grund dafür ist, dass die genannten Eigenschaften nicht zur Erhaltung von Excel-Arbeitsmappen geeignet sind, da Excel sie auslässt. Diese Eigenschaften wurden ursprünglich für Word-Dokumente und PowerPoint-Präsentationen geschrieben.
