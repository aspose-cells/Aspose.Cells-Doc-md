---
title: xlsx4j でセル内の値を検索
type: docs
weight: 30
url: /ja/java/find-value-in-cells-in-xlsx4j/
---

## **Aspose.Cells - セル内の値の検索**
Microsoft Excelでは、特定のデータを含むセルを検索できます。たとえば、**編集**をクリックし、**検索**を選択すると、検索ダイアログが開きます。ユーザーは値を入力し、**OK**をクリックして検索を実行できます。Excelは一致するフィールドを強調表示します。

**Java**

{{< highlight java >}}

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/findvalueincells/AsposeFindValueInCells.java)

{{% alert color="primary" %}} 

詳細については、[データの検索](/cells/ja/java/find-or-search-data)を参照してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
