---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 260
url: /ar/java/calculate-page-setup-scaling-factor/
---
{{% alert color="primary" %}} 

عندما تقوم بتعيين مقياس إعداد الصفحة باستخدام**يصلح ل n صفحة (ق) عرض في متر طول** الخيار ، Microsoft يقوم Excel بحساب عامل قياس إعداد الصفحة. يمكنك حساب نفس الشيء باستخدام[SheetRender.getPageScale ()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale) خاصية. تقوم هذه الخاصية بإرجاع قيمة مزدوجة يمكن تحويلها إلى قيمة نسبة مئوية. على سبيل المثال ، إذا كانت تُرجع 0.5079621076 ، فهذا يعني أن عامل القياس هو 51٪.

{{% /alert %}} 
## **حساب عامل تحجيم إعداد الصفحة**
 يوضح نموذج التعليمات البرمجية التالي كيفية حساب عامل تحجيم إعداد الصفحة باستخدام[SheetRender.getPageScale ()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale)خاصية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **إخراج وحدة التحكم**
هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه.

{{< highlight "java" >}}

 0.5079621076583862

{{< /highlight >}}
