---
title: محرك حساب الصيغة في xlsx4j
type: docs
weight: 40
url: /ar/java/formula-calculation-engine-in-xlsx4j/
---
## **Aspose.Cells - محرك حساب الصيغة**
تم تضمين محرك حساب الصيغة في Aspose.Cells. لا يمكنه فقط إعادة حساب الصيغة المستوردة من ملف جدول بيانات مصمم ولكنه يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.

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
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/formulacalculationengine/AsposeFormulaCalculationEngine.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[محرك حساب الصيغة](/cells/ar/java/formula-calculation-engine-in-aspose-cells).

{{% /alert %}}
