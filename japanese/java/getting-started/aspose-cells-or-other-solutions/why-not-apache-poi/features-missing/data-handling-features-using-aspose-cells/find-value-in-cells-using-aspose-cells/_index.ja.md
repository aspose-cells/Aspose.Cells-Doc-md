---
title: Aspose.Cells を使用して Cells の値を検索
type: docs
weight: 10
url: /ja/java/find-value-in-cells-using-aspose-cells/
---
## **Aspose.Cells - Cells の値を検索**
Microsoft Excel では、ユーザーは特定のデータを含むセルを検索できます。たとえば、**編集**その後**探す**検索ダイアログを開きます。ユーザーが値を入力してクリック**わかった**それを検索します。 Excel で一致するフィールドが強調表示されます。

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[データの検索または検索](/cells/ja/java/find-or-search-data).

{{% /alert %}}
