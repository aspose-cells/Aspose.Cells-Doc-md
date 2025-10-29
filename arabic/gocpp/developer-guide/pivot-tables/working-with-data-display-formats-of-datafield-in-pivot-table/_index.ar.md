---
title: العمل مع تنسيقات عرض البيانات في حقل البيانات في الجدول المحوري باستخدام Golang عبر C++
linktitle: العمل مع تنسيقات عرض البيانات لحقل البيانات في Pivot Table
type: docs
weight: 140
url: /ar/go-cpp/working-with-data-display-formats-of-datafield-in-pivot-table/
description: تعلم كيفية العمل مع تنسيقات عرض البيانات لحقل البيانات في Pivot Table باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells جميع تنسيقات عرض البيانات لحقل البيانات.

{{% /alert %}}

## **خيار تنسيق العرض "ترتيب الأصغر إلى الأكبر" و"ترتيب الأكبر إلى الأصغر"**

يوفر Aspose.Cells القدرة على تعيين خيار تنسيق العرض لحقول pivot. لهذا، يوفر API الخاص بـ [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) الخاصية. لترتيب الأكبر إلى الأصغر، يمكنك ضبط الخاصية [**PivotField.GetCalculationType()**](https://reference.aspose.com/cells/go-cpp/pivotshowvaluessetting/getcalculationtype/) إلى [**PivotFieldDataDisplayFormat.RankLargestToSmallest**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotfielddatadisplayformat/). يوضح مقتطف الكود التالي إعداد خيارات تنسيق العرض.

يمكن تنزيل ملفات الأصل والإخراج العينية من هنا لاختبار كود العينة:

[ملف إكسل المصدر](101089332.xlsx)

[ملف إكسل الإخراج](101089333.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithDataDisplayFormatsOfDatafieldInPivotTable.go" >}}
