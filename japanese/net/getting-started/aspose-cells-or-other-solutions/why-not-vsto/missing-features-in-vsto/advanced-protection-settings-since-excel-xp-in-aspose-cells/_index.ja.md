---
title: Aspose.CellsにおけるExcel XP以降の高度な保護設定
type: docs
weight: 20
url: /ja/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- 行または列の削除。
- 内容、オブジェクト、またはシナリオの編集。
- セル、行、または列の書式設定。
- 行、列、またはハイパーリンクの挿入。
- ロックされたセルまたはロックされていないセルの選択。
- ピボットテーブルなどの使用。

Aspose.CellsはExcel XP以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

{{% /alert %}}

## **Excel XPおよびそれ以降のバージョンを使用した高度な保護設定**

Excel XPで利用可能な保護設定を表示するには：

1. **ツール** メニューから **保護** を選択し、続いて **シートを保護** を選択します。
   ダイアログが表示されます。

   **Excel XPで保護オプションを表示するためのダイアログ**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. ワークシートの機能の許可または制限、またはパスワードを適用します。

### **Aspose.Cellsを使用した高度な保護設定**

Aspose.Cellsはすべての高度な保護設定をサポートしています。

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) を提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) クラスには、Excelファイル内の各ワークシートにアクセスできる [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) コレクションが含まれています。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスによって表されます。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) クラスは、これらの高度な保護設定を適用するために使用される [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) プロパティを提供します。[**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) プロパティは実際には、いくつかの制限を無効または有効にするためのいくつかのブーリアンプロパティをカプセル化した [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) クラスのオブジェクトです。

以下は小さなサンプルアプリケーションです。それはExcelファイルを開いて、Excel XPおよびそれ以降のバージョンでサポートされる高度な保護設定のほとんどを使用します。

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

## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
