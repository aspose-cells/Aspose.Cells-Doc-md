---
title: تحديث قيم الأشكال المرتبطة باستخدام Golang عبر C++
linktitle: تحديث قيم الأشكال المرتبطة
type: docs
weight: 3200
url: /ar/go-cpp/refresh-values-of-linked-shapes/
description: تعلم كيفية تحديث قيم الأشكال المرتبطة في ملفات إكسل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا، يمكن أن يكون لديك شكل مرتبط في ملف Excel يرتبط بخلية ما. في Microsoft Excel، يؤدي تغيير قيمة الخلية المرتبطة أيضًا إلى تغيير قيمة الشكل المرتبط. ويعمل هذا أيضًا بشكل جيد مع Aspose.Cells إذا كنت ترغب في حفظ سجل العمل الخاص بك في تنسيق XLS أو XLSX. ومع ذلك، إذا كنت ترغب في حفظ سجل العمل الخاص بك في تنسيق PDF أو HTML، فيجب عليك استدعاء الطريقة [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

يظهر لقطة الشاشة التالية ملف إكسل المصدر المستخدم في الشفرة أدناه. يحتوي على صورة مرتبطة مرتبطة بخلايا A1 إلى E4. سنغير قيمة الخلية B4 باستخدام Aspose.Cells ثم نستدعي طريقة [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/go-cpp/shapecollection/updateselectedvalue/) لتحديث قيمة الصورة وحفظها بتنسيق PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

يمكنك تنزيل [ملف إكسل المصدر](95584291.xlsx) و [ملف PDF الناتج](95584292.pdf) من الروابط المعطاة.

### كود C++ لتحديث قيم الأشكال المرتبطة

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RefreshValuesOfLinkedShapes.go" >}}
