---
title: Öffentliche API Änderungen in Aspose.Cells 8.1.0
type: docs
weight: 50
url: /de/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

Dieses Dokument beschreibt Änderungen an der Aspose.Cells API von Version 8.0.2 auf 8.1.0, die für Modul-/Anwendungs-Entwickler von Interesse sein können. Es umfasst nicht nur neue und aktualisierte öffentliche Methoden, sondern auch eine Beschreibung von Änderungen im Verhalten hinter den Kulissen in Aspose.Cells.

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet-Eigenschaft hinzugefügt**
Die HtmlSaveOptions-Klasse verfügt über das Attribut ExportHiddenWorksheet, das verwendet werden kann, um anzugeben, ob versteckte Arbeitsblätter im HTML-Format exportiert werden. Der Standardwert ist true. Wenn er jedoch auf false gesetzt wird, exportiert Aspose.Cells die Inhalte des versteckten Arbeitsblatts nicht.

{{% alert color="primary" %}} 

Bitte überprüfen Sie den ausführlichen Artikel zu [Verhindern des Exports von versteckten Arbeitsblattinhalten](/cells/de/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Hinzugefügtes Cell.StringValueWithoutFormat-Attribut**
Das StringValueWithoutFormat-Attribut wurde der Cell-Klasse hinzugefügt, um den Entwicklern das Abrufen des Zellenwerts ohne jegliche Formatierung zu ermöglichen. 

Der unten bereitgestellte Codeauszug zeigt die Verwendung der Cell.getStringValueWithoutFormat-Methode im Vergleich zum cell.getDisplayStringValue durch das Erstellen einer Tabelle von Grund auf und das Anwenden des Zahlenformats auf eine der Zellen. 

**Java**

{{< highlight csharp >}}

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

Formatierter Zeichenfolgenwert: 123,456
Unformatierter Zeichenfolgenwert: 123456

{{% /alert %}}
## **Veraltete Bytes, Characters, CharactersWithSpaces, Lines, Paragraphs-Eigenschaften**
Viele Eigenschaften der Klasse BuiltInDocumentPropertyCollection wurden ab Aspose.Cells for .NET 8.1.0 als veraltet markiert. Dazu gehören Bytes, Characters, CharactersWithSpaces, Lines & Paragraphs. Der Grund dafür ist, dass die genannten Eigenschaften nicht zur Erhaltung von Excel-Arbeitsmappen geeignet sind, da Excel sie auslässt. Diese Eigenschaften wurden ursprünglich für Word-Dokumente und PowerPoint-Präsentationen geschrieben. 
{{< app/cells/assistant language="java" >}}
