---
title: احسب المجاميع الفرعية باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/calculate-sub-totals-using-aspose-cells/
---
## **Aspose.Cells - احسب المجاميع الفرعية**
يمكنك إنشاء مجاميع فرعية تلقائيًا لأي قيم مكررة في جدول بيانات. يوفر Aspose.Cells ميزات API التي تساعدك على إضافة الإجماليات الفرعية إلى جداول البيانات برمجيًا.

**Java**

{{< highlight "java" >}}

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

cells.subtotal(ca, 0, ConsolidationFunction.SUM, new int[]{ 1 });

//Save the excel file

workbook.save("AsposeTotal.xls");

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/formula/AsposeCreateSubTotals.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تكوين المجاميع الفرعية](/cells/ar/java/creating-subtotals).

{{% /alert %}}
