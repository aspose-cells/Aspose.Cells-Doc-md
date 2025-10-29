---
title: العمل مع تنسيقات عرض البيانات لحقل البيانات في جدول الإحصائيات المحورية
type: docs
weight: 140
url: /ar/python-net/working-with-data-display-formats-of-datafield-in-pivot-table/
description: كيفية العمل مع صيغ عرض البيانات لحقل البيانات في جدول البيانات المحوري باستخدام Aspose.Cells لـ Python via .NET.
keywords: Aspose.Cells for Python Excel، مكتبة Excel Python، العمل مع صيغ عرض البيانات لحقل البيانات في جدول البيانات المحوري.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET يدعم جميع صيغ عرض بيانات حقل البيانات.

{{% /alert %}}

## **كيفية تعيين خيار "تصنيفات من الأصغر إلى الأكبر" و "تصنيفات من الأكبر إلى الأصغر" لخيار صيغة العرض**

Aspose.Cells for Python via .NET يوفر القدرة على تعيين خيارات صيغة العرض لحقول Pivot. لهذا، يقدم الواجهة البرمجية الخاصية [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/). لتصنيف من الأكبر إلى الأصغر، يمكنك تعيين الخاصية [**PivotField.data_display_format**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/data_display_format/)  إلى [**PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfielddatadisplayformat/). يوضح مقتطف الكود التالي تعيين خيارات صيغة العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف إكسل المصدر](101089332.xlsx)

[ملف إكسل الإخراج](101089333.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-PivotTableDataDisplayFormatRanking-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
