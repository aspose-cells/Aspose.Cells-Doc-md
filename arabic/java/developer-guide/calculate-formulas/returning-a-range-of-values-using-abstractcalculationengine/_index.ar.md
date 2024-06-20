---
title: إرجاع مجموعة من القيم باستخدام محرك الحساب النموذجي
type: docs
weight: 275
url: /ar/java/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

توفر Aspose.Cells فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) التي تستخدم لتنفيذ وظائف مخصصة غير مدعومة من قبل Microsoft Excel كوظائف مدمجة.

سيشرح هذا المقال كيفية إرجاع مجموعة القيم من [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

يُظهر الكود التالي استخدام [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) ويعيد مجموعة القيم عبر طريقته.

إنشاء فئة بوظيفة *CalculateCustomFunction*. تمتد هذه الفئة من [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

الآن استخدم الوظيفة أعلاه في برنامجك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
