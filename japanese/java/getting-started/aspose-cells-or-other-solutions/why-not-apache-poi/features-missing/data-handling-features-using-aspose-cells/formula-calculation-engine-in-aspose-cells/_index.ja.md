---
title: Aspose.Cells の数式計算エンジン
type: docs
weight: 50
url: /ja/java/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - 数式計算エンジン**
数式計算エンジンは Aspose.Cells に組み込まれています。デザイナー スプレッドシート ファイルからインポートされた数式を再計算できるだけでなく、実行時に追加された数式の結果を計算することもサポートします。

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.getWorksheets().add();

Worksheet worksheet = book.getWorksheets().get(sheetIndex);

Cells cells = worksheet.getCells();

Cell cell = null;

//Adding a value to "A1" cell

cell = cells.get("A1");

cell.setValue(1);

//Adding a value to "A2" cell

cell = cells.get("A2");

cell.setValue(2);

//Adding a value to "A3" cell

cell = cells.get("A3");

cell.setValue(3);

//Adding a SUM formula to "A4" cell

cell = cells.get("A4");

cell.setFormula("=SUM(A1:A3)");

//Calculating the results of formulas

book.calculateFormula();

//Saving the Excel file

book.save(dataDir + "AsposeFormulaEngine.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[式計算エンジン](/cells/ja/java/aspose-cells-formula-calculation-engine).

{{% /alert %}}
