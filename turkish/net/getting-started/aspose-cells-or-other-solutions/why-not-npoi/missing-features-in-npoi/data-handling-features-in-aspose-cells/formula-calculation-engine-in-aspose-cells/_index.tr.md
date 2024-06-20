---
title: Aspose.Cells te Elektronik Tabloyu PDF ye Dönüştürme
type: docs
weight: 30
url: /tr/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Elektronik Tabloyu PDF'ye Dönüştürme**
PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinin standart formatı olarak geniş bir şekilde kullanılmaktadır. Yazılım geliştiricileri genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürme yolu bulmaları istenir. Aspose.Cells bu özellikleri destekler.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.Worksheets.Add();

Worksheet worksheet = book.Worksheets[sheetIndex];

Cells cells = worksheet.Cells;

Cell cell = null;

//Adding a value to "A1" cell

cell = cells["A1"];

cell.Value = 1;

//Adding a value to "A2" cell

cell = cells["A2"];

cell.Value = 2;

//Adding a value to "A3" cell

cell = cells["A3"];

cell.Value = 3;

//Adding a SUM formula to "A4" cell

cell = cells["A4"];

cell.Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

book.CalculateFormula();

//Saving the Excel file

book.Save("AsposeFormulaEngine.xls");

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi aşağıdaki sosyal kodlama sitelerinden **Elektronik Tabloyu PDF'ye Dönüştürme** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Formül Hesaplama Motoru](/cells/tr/net/formula-calculation-engine/) ziyaret edin.

{{% /alert %}}
