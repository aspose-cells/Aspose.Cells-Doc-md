---
title: قم بتحديث قيم الأشكال المرتبطة
type: docs
weight: 3000
url: /ar/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

في بعض الأحيان ، يكون لديك شكل مرتبط في ملف Excel مرتبط ببعض الخلايا. في Microsoft Excel ، يؤدي تغيير قيمة الخلية المرتبطة أيضًا إلى تغيير قيمة الشكل المرتبط. يعمل هذا أيضًا بشكل جيد مع Aspose.Cells إذا كنت تريد حفظ المصنف بتنسيق XLS أو XLSX. ومع ذلك ، إذا كنت تريد حفظ المصنف بتنسيق PDF أو HTML ، فسيتعين عليك الاتصال[**Worksheet.getShapes (). updateSelectedValue ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) طريقة لتحديث قيمة الشكل المرتبط.

{{% /alert %}}

## مثال

 تُظهر لقطة الشاشة التالية ملف Excel المصدر المستخدم في نموذج التعليمات البرمجية أدناه. لها ارتباط**الصورة 1** مرتبط بالخلية A1. سنقوم بتغيير قيمة الخلية A1 مع Aspose.Cells ثم الاتصال[**Worksheet.getShapes (). updateSelectedValue ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) طريقة لتحديث قيمة**الصورة 1** وحفظه بتنسيق PDF.

![ما يجب القيام به: image_بديل_نص](refresh-values-of-linked-shapes_1.png)

يمكنك تنزيل ملف[ملف Excel المصدر](5472956.xlsx) و ال[الإخراج PDF](5472955.pdf) من الروابط المعطاة.

### كود Java لتجديد قيم الأشكال المرتبطة

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}
