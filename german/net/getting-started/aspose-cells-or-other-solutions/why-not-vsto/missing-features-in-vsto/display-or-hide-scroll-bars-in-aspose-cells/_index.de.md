---
title: Bildlaufleisten in Aspose.Cells anzeigen oder ausblenden
type: docs
weight: 70
url: /de/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Bildlaufleisten werden häufig verwendet, um durch den Inhalt einer Datei zu navigieren. Normalerweise gibt es zwei Arten von Bildlaufleisten:

- Vertikale Bildlaufleisten
- Horizontale Bildlaufleisten

Microsoft Excel bietet auch horizontale und vertikale Bildlaufleisten, damit Benutzer durch Arbeitsblattinhalte blättern können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Bildlaufleisten in Excel-Dateien steuern.

{{% /alert %}}

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) die eine Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) -Klasse bietet eine Vielzahl von Eigenschaften und Methoden zum Verwalten einer Excel-Datei. Um die Sichtbarkeit von Bildlaufleisten zu steuern, verwenden Sie die[**Arbeitsmappeneinstellungen**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) Klasse'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Eigenschaften.[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sind boolesche Eigenschaften, was bedeutet, dass diese Eigenschaften nur speichern können**Stimmt** oder**FALSCH** Werte.

Unten ist ein vollständiger Code, der eine Excel-Datei, book1.xls, öffnet, beide Bildlaufleisten ausblendet und dann die geänderte Datei als output.xls speichert.

Der folgende Screenshot zeigt die Datei Book1.xls, die beide Bildlaufleisten enthält. Die geänderte Datei wird als output.xls-Datei gespeichert, die auch unten gezeigt wird.

**Book1.xls: Excel-Datei vor jeder Änderung**

![todo: Bild_alt_Text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Excel-Datei nach der Änderung**

![todo: Bild_alt_Text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
