---
title: احصل على تطبيق التحقق من الصحة على Cell
type: docs
weight: 80
url: /ar/java/get-validation-applied-on-a-cell/
description: توضح هذه المقالة كيفية تطبيق التحقق من الصحة على Cell مع Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 يمكنك استخدام Aspose.Cells API لتطبيق التحقق على أي خلية. يوفر Aspose.Cells ملف[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) طريقة لهذا الغرض. إذا لم يكن هناك تحقق في الخلية ، فإنها ترجع فارغة. وبالمثل ، يمكنك استخدام ملف[**Worksheet.getValidations (). getValidationInCell (الصف int ، العمود int)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) للحصول على التحقق المطبق على خلية من خلال توفير فهارس الصفوف والعمود.

{{% /alert %}}

 تُظهر اللقطة التالية نموذج ملف Excel Microsoft المستخدم في نموذج التعليمات البرمجية أدناه. Cell**C1** لديها**التحقق العشري** تم تطبيقها ويمكن أن تأخذ القيم فقط**بين 10 و 20**.

**خلية مع التحقق من الصحة**

![ما يجب القيام به: image_بديل_نص](get-validation-applied-on-a-cell_1.png)

يحصل نموذج التعليمات البرمجية أدناه على التحقق المطبق على C1 ويقرأ خصائصه المختلفة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية المنفذة مع نموذج الملف الموضح في اللقطة أعلاه.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## مقالات ذات صلة

- [تأكيد صحة البيانات](/cells/ar/java/data-validation/)
