---
title: Erweiterte Schutzeinstellungen seit Excel XP in Aspose.Cells
type: docs
weight: 20
url: /de/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- Zeilen oder Spalten löschen.
- Inhalte, Objekte oder Szenarien bearbeiten.
- Zellen, Zeilen oder Spalten formatieren.
- Zeilen, Spalten oder Hyperlinks einfügen.
- Gesperrte oder ungesperrte Zellen auswählen.
- Pivot-Tabellen verwenden und vieles mehr.

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen, die von Excel XP oder späteren Versionen angeboten werden.

{{% /alert %}}

## **Erweiterte Schutzeinstellungen mit Excel XP und späteren Versionen verwenden**

Um die Schutzeinstellungen in Excel XP anzuzeigen:

1. Wählen Sie im Menü **Extras** die Option **Schutz** und dann **Arbeitsblatt schützen**.
   Es wird ein Dialogfeld angezeigt.

   **Dialogfeld zur Anzeige von Schutzoptionen in Excel XP**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Arbeitsblattfunktionen erlauben oder einschränken oder ein Passwort anwenden.

### **Erweiterte Schutzeinstellungen mit Aspose.Cells verwenden**

Aspose.Cells unterstützt alle erweiterten Schutzeinstellungen.

Aspose.Cells stellt eine Klasse, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), bereit, die eine Microsoft Excel-Datei darstellt. Die Klasse [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) enthält eine [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)-Sammlung, die den Zugriff auf jedes Arbeitsblatt in der Excel-Datei ermöglicht. Ein Arbeitsblatt wird durch die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) repräsentiert.

Die Klasse [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) stellt die Eigenschaft [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) bereit, die verwendet wird, um diese erweiterten Schutzeinstellungen anzuwenden. Die Eigenschaft [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) ist tatsächlich ein Objekt der Klasse [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection), das mehrere boolesche Eigenschaften zum Deaktivieren oder Aktivieren von Beschränkungen umschließt.

Unten finden Sie eine kleine Beispielanwendung. Es öffnet eine Excel-Datei und verwendet die meisten von Excel XP und späteren Versionen unterstützten erweiterten Schutzeinstellungen.

**C#**

{{< highlight csharp >}}

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

## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
