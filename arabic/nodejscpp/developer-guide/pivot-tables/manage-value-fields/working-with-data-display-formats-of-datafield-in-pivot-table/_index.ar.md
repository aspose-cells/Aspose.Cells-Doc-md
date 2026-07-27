---
title: العمل مع تنسيقات عرض البيانات لحقل البيانات في جدول الإحصائيات المحورية
type: docs
weight: 140
url: /ar/nodejs-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells for Node.js via C++ جميع تنسيقات عرض البيانات الخاصة بـ DataField.

{{% /alert %}}

## **"ترتيب من الأصغر إلى الأكبر" و "ترتيب من الأكبر إلى الأصغر" خيار شكل العرض**

يوفر ASpose.Cells القدرة على تعيين خيار تنسيق العرض لحقول الجدول المحوري. لهذا، توفر واجهة برمجة التطبيقات العقارية [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-). لتحديد الترتيب من الأكبر إلى الأصغر، قد تقوم بتعيين خاصية [**PivotShowValuesSetting.setCalculationType**](https://reference.aspose.com/cells/nodejs-cpp/pivotshowvaluessetting/#setCalculationType-pivotfielddatadisplayformat-) إلى [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/nodejs-cpp/pivotfielddatadisplayformat/). المقتطف البرمجي التالي يوضح ضبط خيارات تنسيق العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف إكسل المصدر](101089332.xlsx)

[ملف إكسل الإخراج](101089333.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-PivotTableDataDisplayFormatRanking-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
