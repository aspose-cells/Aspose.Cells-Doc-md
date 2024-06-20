---
title: تحديث قيم الأشكال المرتبطة
type: docs
weight: 3200
url: /ar/net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

أحيانًا، يمكن أن يكون لديك شكل مرتبط في ملف Excel يرتبط بخلية ما. في Microsoft Excel، يؤدي تغيير قيمة الخلية المرتبطة أيضًا إلى تغيير قيمة الشكل المرتبط. ويعمل هذا أيضًا بشكل جيد مع Aspose.Cells إذا كنت ترغب في حفظ سجل العمل الخاص بك في تنسيق XLS أو XLSX. ومع ذلك، إذا كنت ترغب في حفظ سجل العمل الخاص بك في تنسيق PDF أو HTML، فيجب عليك استدعاء الطريقة [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

اللقطة الملتقطة التالية تظهر ملف Excel المصدر المستخدم في الكود العيني أدناه. يحتوي على صورة مرتبطة مرتبطة بخلايا من A1 إلى E4. سنقوم بتغيير قيمة الخلية B4 باستخدام Aspose.Cells ومن ثم استدعاء الطريقة [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) لتحديث قيمة الصورة وحفظها في تنسيق PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

يمكنك تنزيل الملف الأصلي [ملف الإكسل المصدر](95584291.xlsx) و[PDF الناتج](95584292.pdf) من الروابط المعطاة.

### كود C# لتحديث قيم الأشكال المرتبطة

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
