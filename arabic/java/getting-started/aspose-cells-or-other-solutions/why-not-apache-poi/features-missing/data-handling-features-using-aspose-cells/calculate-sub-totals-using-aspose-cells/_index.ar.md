---
title: حساب المجاميع الفرعية باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/calculate-sub-totals-using-aspose-cells/
---

## **Aspose.Cells - حساب الإجماليات الفرعية**
يمكنك إنشاء الإجماليات الفرعية تلقائيًا لأي قيم متكررة في جدول البيانات. توفر Aspose.Cells ميزات واجهة برمجة التطبيقات التي تساعدك في إضافة الإجماليات الفرعية لجداول البيانات بشكل برمجي.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook workbook = new Workbook("book1.xls");

//Get the Cells collection in the first worksheet

Cells cells = workbook.getWorksheets().get(0).getCells();

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn =1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.subtotal(ca, 0, ConsolidationFunction.SUM, new int[] { 1 });

//Save the excel file

workbook.save("AsposeTotal.xls");

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إنشاء مجاميع فرعية](/cells/ar/java/creating-subtotals).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
