---
title: حساب الإجماليات الفرعية
type: docs
weight: 10
url: /ar/net/calculate-sub-totals/
---

## **Aspose.Cells - حساب الإجماليات الفرعية**
يمكنك إنشاء الإجماليات الفرعية تلقائيًا لأي قيم متكررة في جدول البيانات. توفر Aspose.Cells ميزات واجهة برمجة التطبيقات التي تساعدك في إضافة الإجماليات الفرعية لجداول البيانات بشكل برمجي.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **حساب الإجماليات الفرعية** من أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إنشاء المجاميع](/cells/ar/net/creating-subtotals/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
