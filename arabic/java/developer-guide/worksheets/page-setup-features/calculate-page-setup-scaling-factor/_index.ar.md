---
title: حساب عامل تحجيم إعداد الصفحة
type: docs
weight: 260
url: /ar/java/calculate-page-setup-scaling-factor/
---

{{% alert color="primary" %}} 

عندما تقوم بتعيين تكبير إعداد الصفحة باستخدام خيار **تلائم n صفحة عريضة حسب m إرتفاعًا**، يقوم Microsoft Excel بحساب معامل تكبير إعداد الصفحة. يمكنك حساب الشيء نفسه باستخدام خاصية [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale). تقوم هذه الخاصية بإرجاع قيمة مزدوجة يمكن تحويلها إلى قيمة نسبة مئوية. على سبيل المثال، إذا أرجعت 0.5079621076 فإنه يعني أن معامل التكبير هو 51٪.

{{% /alert %}} 
## **حساب معامل تكبير إعداد الصفحة**
يوضح الكود العيني التالي كيفية حساب معامل تكبير إعداد الصفحة باستخدام خاصية [SheetRender.getPageScale()](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#PageScale).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculatePageSetupScalingFactor-CalculatePageSetupScalingFactor.java" >}}
## **مخرجات الوحدة**
فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.

{{< highlight java >}}

 0.5079621076583862

{{< /highlight >}}
