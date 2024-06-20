---
title: محرك حساب الصيغ في Aspose.Cells
type: docs
weight: 30
url: /ar/net/formula-calculation-engine-in-aspose-cells/
---

## **أسبوز.خلايا - محرك حساب الصيغ**
يتم تضمين محرك حساب الصيغ في Aspose.Cells. يمكنه القيام ليس فقط بإعادة حساب الصيغة المستوردة من ملف ورقة بيانات المصمم ولكنه أيضًا يدعم حساب نتائج الصيغ الجديدة في وقت التشغيل.

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
## **تحميل رمز التشغيل**
تنزيل **محرك حساب الصيغ** من أي من مواقع التشفير الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [محرك حساب الصيغ](/cells/ar/net/formula-calculation-engine/).

{{% /alert %}}
