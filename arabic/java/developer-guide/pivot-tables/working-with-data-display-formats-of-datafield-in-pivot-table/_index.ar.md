---
title: العمل مع تنسيقات عرض البيانات DataField في Pivot Table
type: docs
weight: 150
url: /ar/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---
{{% alert color="primary" %}}

يدعم Aspose.Cells كل تنسيقات عرض البيانات الخاصة بـ DataField.

{{% /alert %}}

## **خيار تنسيق العرض "الترتيب من الأصغر إلى الأكبر" و "الترتيب من الأكبر إلى الأصغر"**

يوفر Aspose.Cells القدرة على تحديد اختيار نسق العرض للمجالات المحورية. لهذا ، يوفر API الامتداد[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) منشأه. لترتيب من الأكبر إلى الأصغر ، يمكنك تعيين[**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat)الملكية ل[**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK_LARGEST_TO_SMALLEST). يوضح مقتطف التعليمات البرمجية التالي تعيين خيارات تنسيق العرض.

يمكن تنزيل عينة من ملفات المصدر والمخرجات من هنا لاختبار نموذج التعليمات البرمجية:

[مصدر ملف Excel](PivotTableSample.xlsx)

[إخراج ملف Excel](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
