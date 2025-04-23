---
title: تحديث قيم الأشكال المرتبطة
type: docs
weight: 3000
url: /ar/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تكون هناك شكل مرتبط في ملف Excel الخاص بك مرتبط ببعض الخلية. في Microsoft Excel، تغيير قيمة الخلية المرتبطة يؤدي أيضًا إلى تغيير قيمة الشكل المرتبط. هذا يعمل بشكل جيد أيضًا مع Aspose.Cells إذا كنت ترغب في حفظ دفتر العمل الخاص بك في تنسيق XLS أو XLSX. ومع ذلك، إذا كنت ترغب في حفظ دفتر العمل الخاص بك في تنسيق PDF أو HTML، فعليك أن تقوم بالاتصال بـ [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

تظهر اللقطة الشاشة التالية ملف Excel المصدر المستخدم في رمز العينة أدناه. لديها **صورة 1** مرتبطة بالخلية A1. سنقوم بتغيير قيمة الخلية A1 بواسطة Aspose.Cells، ثم نقوم بالاتصال بـ [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) لتحديث قيمة **صورة 1** وحفظها في تنسيق PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

يمكنك تنزيل [ملف Excel المصدر](5472956.xlsx) و [ملف PDF الناتج](5472955.pdf) من الروابط المعطاة.

### كود Java لتحديث قيم الأشكال المرتبطة

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
{{< app/cells/assistant language="java" >}}
