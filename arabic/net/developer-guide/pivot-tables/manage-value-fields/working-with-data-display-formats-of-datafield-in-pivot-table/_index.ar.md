---
title: العمل مع تنسيقات عرض البيانات لحقل البيانات في جدول الإحصائيات المحورية
type: docs
weight: 140
url: /ar/net/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

تدعم Aspose.Cells جميع تنسيقات عرض البيانات لحقل البيانات.

{{% /alert %}}

## **"ترتيب من الأصغر إلى الأكبر" و "ترتيب من الأكبر إلى الأصغر" خيار شكل العرض**

يوفر ASpose.Cells القدرة على تعيين خيار تنسيق العرض لحقول الجدول المحوري. لهذا، توفر واجهة برمجة التطبيقات العقارية [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/). لتحديد الترتيب من الأكبر إلى الأصغر، قد تقوم بتعيين خاصية [**PivotField.ShowValuesSetting.CalculationType**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotshowvaluessetting/calculationtype/) إلى [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivotfielddatadisplayformat). المقتطف البرمجي التالي يوضح ضبط خيارات تنسيق العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف إكسل المصدر](101089332.xlsx)

[ملف إكسل الإخراج](101089333.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTables-PivotTableDataDisplayFormatRanking-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
