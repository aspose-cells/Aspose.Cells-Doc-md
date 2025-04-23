---
title: Aspose.Cells te Elektronik Tabloyu PDF ye Dönüştürme
type: docs
weight: 50
url: /tr/java/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Elektronik Tabloyu PDF'ye Dönüştürme**
PDF belgeleri, kuruluşlar, devlet sektörleri ve bireyler arasında belge alışverişinin standart formatı olarak geniş bir şekilde kullanılmaktadır. Yazılım geliştiricileri genellikle Microsoft Excel dosyalarını kolayca PDF belgelerine dönüştürme yolu bulmaları istenir. Aspose.Cells bu özellikleri destekler.

**Java**

{{< highlight java >}}

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
## **Çalışan Kodu İndir**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Formül Hesaplama Motoru](/cells/tr/java/aspose-cells-formula-calculation-engine) sayfasını ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
