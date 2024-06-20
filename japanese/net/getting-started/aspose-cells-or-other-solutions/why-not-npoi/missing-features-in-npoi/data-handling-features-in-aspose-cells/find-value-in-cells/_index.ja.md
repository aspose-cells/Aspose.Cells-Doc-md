---
title: セル内の値の検索
type: docs
weight: 20
url: /ja/net/find-value-in-cells/
---

## **Aspose.Cells - セル内の値の検索**
Microsoft Excelでは、特定のデータを含むセルを検索できます。たとえば、**編集**をクリックし、**検索**を選択すると、検索ダイアログが開きます。ユーザーは値を入力し、**OK**をクリックして検索を実行できます。Excelは一致するフィールドを強調表示します。

**C#**

{{< highlight cs >}}

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
## **ランニングコードのダウンロード**
以下に挙げるいずれかのソーシャルコーディングサイトから**セル内の値の検索**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[データの検索](/cells/ja/net/find-or-search-data/)をご覧ください。

{{% /alert %}}
