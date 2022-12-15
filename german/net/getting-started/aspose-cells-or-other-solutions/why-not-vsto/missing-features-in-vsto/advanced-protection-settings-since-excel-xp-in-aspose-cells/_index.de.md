---
title: Erweiterte Schutzeinstellungen seit Excel XP in Aspose.Cells
type: docs
weight: 20
url: /de/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Zeilen oder Spalten löschen.
- Bearbeiten Sie Inhalte, Objekte oder Szenarien.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Wählen Sie gesperrte oder entsperrte Zellen aus.
- Verwenden Sie Pivot-Tabellen und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

{{% /alert %}}

## **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen**

So zeigen Sie die in Excel XP verfügbaren Schutzeinstellungen an:

1.  Von dem**Werkzeug** Menü, auswählen**Schutz** gefolgt von**Schutzblatt**.
 Ein Dialogfeld wird angezeigt.

   **Dialog zum Anzeigen von Schutzoptionen in Excel XP**

![todo: Bild_alt_Text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Erlauben oder beschränken Sie Arbeitsblattfunktionen oder wenden Sie ein Passwort an.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells**

Aspose.Cells unterstützen alle erweiterten Schutzeinstellungen.

 Aspose.Cells bietet eine Klasse,[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , die eine Microsoft Excel-Datei darstellt. Das[**Arbeitsmappe**](https://reference.aspose.com/cells/net/aspose.cells/workbook) Klasse enthält a[**Arbeitsblätter**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch dargestellt[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse.

 Das[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Klasse bietet die[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)-Eigenschaft, die zum Anwenden dieser erweiterten Schutzeinstellungen verwendet wird. Das[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) Eigentum ist in der Tat ein Objekt der[**Schutz**](https://reference.aspose.com/cells/net/aspose.cells/protection) Klasse, die mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Einschränkungen kapselt.

Unten ist eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten erweiterten Schutzeinstellungen, die von Excel XP und späteren Versionen unterstützt werden.

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
