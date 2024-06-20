---
title: الحصول على التحقق المطبق على خلية ما
type: docs
weight: 80
url: /ar/java/get-validation-applied-on-a-cell/
description: يوضح هذا المقال كيفية تطبيق التحقق على خلية بستخدام جافا
keywords: تطبيق التحقق من الخلية في Excel باستخدام جافا، تطبيق التحقق على خلية ما في Excel باستخدام جافا، تطبيق التحقق في Excel باستخدام جافا، التحقق من الخلية في Excel باستخدام جافا، جافا تطبيق التحقق من الخلية في Excel، جافا تطبيق التحقق على خلية في Excel، جافا التحقق من الخلية في Excel، جافا التحقق من الخلية
---

{{% alert color="primary" %}}

يمكنك استخدام واجهة برمجة تطبيقات Aspose.Cells للحصول على التحقق المطبق على أي خلية. توفر Aspose.Cells الطريقة [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) لهذا الغرض. إذا لم يكن هناك أي تحقق على الخلية، فإنها تُعيد قيمة فارغة. بالمثل، يمكنك استخدام الطريقة [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) للحصول على التحقق المطبق على خلية عن طريق توفير مؤشرات صف وعمود الخلية.

{{% /alert %}}

تظهر اللقطة الفوتوغرافية التالية الملف النموذجي لمايكروسوفت إكسل المستخدم في الشيفرة البرمجية النموذجية أدناه. الخلية **C1** لديها **تحقق عشري** مطبق ويمكنها فقط قبول القيم **بين 10 و 20**.

**خلية ذات تحقق**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

تحصل الشيفرة النموذجية أدناه على التحقق المطبق على C1 وتقرأ خصائصها المتنوعة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

هنا ناتج الوحدة من الشيفرة النموذجية تم تنفيذه مع الملف النموذجي الموضح في اللقطة الفوتوغرافية أعلاه.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## مقالات ذات صلة

- [التحقق من البيانات](/cells/ar/java/data-validation/)
