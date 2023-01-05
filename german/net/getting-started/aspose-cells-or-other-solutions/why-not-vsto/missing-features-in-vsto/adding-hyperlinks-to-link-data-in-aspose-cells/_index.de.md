---
title: Hinzufügen von Hyperlinks zu Linkdaten in Aspose.Cells
type: docs
weight: 10
url: /de/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

Ein Hyperlink wird verwendet, um eine Verknüpfung zwischen zwei Entitäten herzustellen. Jeder kennt die Verwendung von Hyperlinks, insbesondere auf Websites.

Mit Aspose.Cells können Entwickler verschiedene Arten von Hyperlinks in Microsoft Excel-Dateien erstellen. In diesem Thema wird erläutert, welche Arten von Hyperlinks von Aspose.Cells unterstützt werden und wie sie in unseren Excel-Dateien verwendet werden können.

{{% /alert %}}

## **Hinzufügen von Hyperlinks**

Mit Aspose.Cells können einer Zelle drei Arten von Hyperlinks hinzugefügt werden:

- [Hinzufügen eines Links zu einer URL](#adding-link-to-a-url).
- [Hinzufügen eines Links zu einer anderen Zelle in derselben Datei](#adding-a-link-to-a-cell-in-the-same-file).
- [Hinzufügen eines Links zu einer externen Datei](#adding-a-link-to-an-external-file).

 Aspose.Cells ermöglicht Entwicklern das Hinzufügen von Hyperlinks zu Excel-Dateien entweder mit API oder[Designer-Tabellen](/cells/de/net/what-is-a-designer-spreadsheet/)(Tabellenkalkulationen, in denen Hyperlinks manuell erstellt werden und Aspose.Cells verwendet wird, um sie in andere Tabellenkalkulationen zu importieren).

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) das stellt eine Microsoft Excel-Datei dar. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblattsammlung**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse. Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) -Klasse bietet verschiedene Methoden zum Hinzufügen verschiedener Hyperlinks zu Excel-Dateien.

### **Link zu einer URL hinzufügen**

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse enthält a[**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks) Sammlung. Jedes Element in der Hyperlinks-Auflistung stellt einen Hyperlink dar. Fügen Sie Hyperlinks zu URLs hinzu, indem Sie die Add-Methode der Hyperlinks-Auflistung aufrufen. Die Add-Methode übernimmt die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich
- URL, die URL-Adresse.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Hinzufügen eines Links zu Cell in derselben Datei**

Es ist möglich, Hyperlinks zu Zellen in derselben Excel-Datei hinzuzufügen, indem die Add-Methode der Hyperlink-Auflistung aufgerufen wird. Die Add-Methode funktioniert sowohl für interne als auch für externe Hyperlinks. Eine Version der überladenen Methode akzeptiert die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse der Zielzelle.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **Hinzufügen eines Links zu einer externen Datei**

Es ist möglich, Hyperlinks zu externen Excel-Dateien hinzuzufügen, indem die Add-Methode der Hyperlinks-Auflistung aufgerufen wird. Die Add-Methode übernimmt die folgenden Parameter:

- Cell Name, der Name der Zelle, zu der der Hyperlink hinzugefügt wird.
- Zeilenanzahl, die Anzahl der Zeilen in diesem Hyperlinkbereich.
- Anzahl der Spalten, die Anzahl der Spalten in diesem Hyperlinkbereich.
- URL, die Adresse des Ziels, externe Excel-Datei.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
