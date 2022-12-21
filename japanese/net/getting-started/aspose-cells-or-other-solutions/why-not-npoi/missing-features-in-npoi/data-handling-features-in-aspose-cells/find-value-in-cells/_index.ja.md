---
title: Cells で値を検索
type: docs
weight: 20
url: /ja/net/find-value-in-cells/
---
## **Aspose.Cells - Cells の値を検索**
Microsoft Excel では、ユーザーは特定のデータを含むセルを検索できます。たとえば、**編集**その後**探す**検索ダイアログを開きます。ユーザーが値を入力してクリック**わかった**それを検索します。 Excel で一致するフィールドが強調表示されます。

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Cells で値を検索**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[データの検索または検索](/cells/ja/net/find-or-search-data/).

{{% /alert %}}
