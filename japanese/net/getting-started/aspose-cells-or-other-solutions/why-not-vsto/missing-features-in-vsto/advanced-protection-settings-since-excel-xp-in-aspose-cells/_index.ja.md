---
title: Aspose.Cells の Excel XP 以降の高度な保護設定
type: docs
weight: 20
url: /ja/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- 行または列を削除します。
- コンテンツ、オブジェクト、またはシナリオを編集します。
- セル、行、または列をフォーマットします。
- 行、列、またはハイパーリンクを挿入します。
- ロックまたはロック解除されたセルを選択します。
- ピボット テーブルなどを使用します。

Aspose.Cells は、Excel XP 以降のバージョンで提供されるすべての高度な保護設定をサポートしています。

{{% /alert %}}

## **Excel XP 以降のバージョンを使用した高度な保護設定**

Excel XP で使用可能な保護設定を表示するには:

1. から**ツール**メニュー、選択**保護**に続く**プロテクトシート**.
ダイアログが表示されます。

   **Excel XP の保護オプションを表示するダイアログ**

![todo:画像_代替_文章](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. ワークシート機能を許可または制限するか、パスワードを適用します。

### **Aspose.Cells を使用した高度な保護設定**

Aspose.Cells は、すべての高度な保護設定をサポートしています。

Aspose.Cells はクラスを提供し、[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)、Microsoft Excel ファイルを表します。の[**ワークブック**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)Excel ファイル内の各ワークシートにアクセスできるコレクション。ワークシートは、[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラス。

の[**ワークシート**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスが提供する[**保護**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)これらの高度な保護設定を適用するために使用されるプロパティ。の[**保護**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)プロパティは実際にはのオブジェクトです[**保護**](https://reference.aspose.com/cells/net/aspose.cells/protection)制限を無効または有効にするためのいくつかのブール型プロパティをカプセル化するクラス。

以下は小さなアプリケーション例です。 Excel ファイルを開き、Excel XP 以降のバージョンでサポートされている高度な保護設定のほとんどを使用します。

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

## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
