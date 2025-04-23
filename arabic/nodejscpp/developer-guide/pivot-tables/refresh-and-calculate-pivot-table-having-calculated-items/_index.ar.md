---
title: تحديث وحساب جدول البيانات المحوري الذي يحتوي على عناصر محسوبة
type: docs
weight: 40
url: /ar/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

يدعم Aspose.Cells for Node.js via C++ الآن تحديث وحساب جدول Pivot الذي يحتوي على عناصر حسابية. يرجى استخدام [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) و [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) كما المعتاد لأداء هذه الوظيفة.

{{% /alert %}}

## **تحديث وحساب الجدول الدوري الذي يحتوي على عناصر محسوبة**

يقوم الكود النموذجي التالي بتحميل ملف إكسل المصدر الذي يحتوي على جدول Pivot يحتوي على ثلاثة عناصر محسوبة مثل "add"، "div"، "div2". نقوم أولاً بتغيير قيمة الخلية D2 إلى 20 ثم نقوم بتحديث وحساب جدول Pivot باستخدام واجهات برمجة التطبيقات Aspose.Cells for Node.js via C++ وحفظ المصنف بصيغة PDF. تظهر النتائج في ملف PDF المخرجات أن Aspose.Cells for Node.js via C++ قام بتحديث وحساب جدول Pivot بنجاح. يمكنك التحقق من ذلك باستخدام Microsoft Excel عن طريق وضع القيمة 20 يدويًا في الخلية D2 ثم تحديث جدول Pivot عبر اختصار Alt+F5 أو بالنقر على زر تحديث جدول Pivot.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

