---
title: العمل مع تنسيقات عرض البيانات لحقل البيانات في جدول الإحصائيات المحورية
type: docs
weight: 150
url: /ar/java/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells جميع تنسيقات عرض البيانات لحقل البيانات.

{{% /alert %}}

## **"ترتيب من الأصغر إلى الأكبر" و "ترتيب من الأكبر إلى الأصغر" خيار شكل العرض**

توفر Aspose.Cells القدرة على تعيين خيار شكل العرض لحقول الجدول المحوري. لهذا الغرض، يوفر الواجهة البرمجية الخاصية [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat). لتصنيف من الأكبر إلى الأصغر، يمكنك تعيين الخاصية [**PivotField.DataDisplayFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfield#DataDisplayFormat) على [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/java/com.aspose.cells/pivotfielddatadisplayformat#RANK-LARGEST-TO-SMALLEST). كود البرنامج التالي يوضح كيفية تعيين خيارات شكل العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف Excel الأصل](PivotTableSample.xlsx)

[ملف Excel الإخراج](PivotTableDataDisplayFormatRanking_out.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-PivotTables-PivotTableDataDisplayFormatRanking-1.java" >}}
{{< app/cells/assistant language="java" >}}
