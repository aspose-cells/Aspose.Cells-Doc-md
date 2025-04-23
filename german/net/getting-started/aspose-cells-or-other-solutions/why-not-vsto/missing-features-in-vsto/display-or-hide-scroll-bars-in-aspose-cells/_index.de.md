---
title: Scrollleisten in Aspose.Cells anzeigen oder ausblenden
type: docs
weight: 70
url: /de/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

Scrollleisten werden verwendet, um durch die Inhalte einer Datei zu navigieren. Normalerweise gibt es zwei Arten von Scrollleisten:

- Vertikale Scrollleisten
- Horizontale Scrollleisten

Microsoft Excel bietet auch horizontale und vertikale Scrollleisten an, damit Benutzer durch die Inhalte des Arbeitsblatts scrollen können. Mit Aspose.Cells können Entwickler die Sichtbarkeit beider Arten von Scrollleisten in Excel-Dateien steuern.

{{% /alert %}}

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bereit, die eine Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) bietet eine breite Palette von Eigenschaften und Methoden zur Verwaltung einer Excel-Datei. Um die Sichtbarkeit von Scrollleisten zu steuern, verwenden Sie die Eigenschaften [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) der Klasse [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings). [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) und [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sind boolsche Eigenschaften, was bedeutet, dass diese Eigenschaften nur **true** oder **false** Werte speichern können.

Im Folgenden finden Sie einen vollständigen Code, der eine Excel-Datei öffnet, book1.xls versteckt beide Scrollleisten und speichert dann die geänderte Datei als output.xls ab.

Das folgende Screenshot zeigt die Datei Book1.xls mit beiden Scrollleisten. Die geänderte Datei wird als output.xls Datei gespeichert, wie unten gezeigt.

**Book1.xls: Excel-Datei vor jeder Änderung**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Excel-Datei nach der Änderung**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Laufenden Code herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
