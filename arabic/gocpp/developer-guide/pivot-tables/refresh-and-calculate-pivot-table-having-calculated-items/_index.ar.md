---
title: تحديث وحساب جدول محوري يحتوي على عناصر محسوبة باستخدام Golang عبر C++
linktitle: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/go-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
description: تحديث وحساب الجدول المحوري مع العناصر المحسوبة باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}}

تدعم Aspose.Cells الآن تحديث وحساب الجدول المحوري الذي يحتوي على عناصر محسوبة. يرجى استخدام [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/go-cpp/pivottable/refreshdata/) و [**PivotTable.CalculateData()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) كالمعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

يحمّل الكود النموذجي التالي ملف إكسل المصدر والذي يحتوي على جدول محوري به ثلاثة عناصر محسوبة مثل "إضافة"، "قسمة"، "قسمة2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب الجدول المحوري باستخدام واجهات برمجة التطبيقات من Aspose.Cells وحفظ الملف بصيغة PDF. تظهر النتائج في ملف PDF المخرجات أن Aspose.Cells قام بتحديث وحساب الجدول المحوري بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel يدويًا بوضع القيمة 20 في الخلية D2 ثم تحديث الجدول المحوري بواسطة مفتاح الاختصار Alt+F5 أو النقر على زر تحديث الجدول المحوري.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshAndCalculatePivotTableHavingCalculatedItems.go" >}}
