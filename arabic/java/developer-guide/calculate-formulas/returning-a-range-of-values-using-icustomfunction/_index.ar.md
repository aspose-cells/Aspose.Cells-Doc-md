---
title: إرجاع مجموعة من القيم باستخدام ICustomFunction
type: docs
weight: 270
url: /ar/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) تمت إهماله منذ إصدار Aspose.Cells for Java 20.8. يرجى استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). يتم وصف استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) في المقال التالي.

[إعادة مجموعة القيم باستخدام AbstractCalculationEngine](/cells/ar/java/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

توفر Aspose.Cells واجهة [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) التي تُستخدم لتنفيذ وظائف مخصصة أو مخصصة لا تدعمها Microsoft Excel كوظائف مدمجة.

عند تنفيذ طريقة واجهة [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) عادةً، تحتاج إلى إرجاع قيمة خلية واحدة. ولكن في بعض الأحيان، قد تحتاج إلى إرجاع مجموعة من القيم. سيشرح هذا المقال كيفية إرجاع مجموعة القيم من [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **إرجاع مجموعة من القيم باستخدام ICustomFunction**

الكود التالي ينفذ [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) ويُرجع مجموعة القيم عبر طريقة القيام به. يُرجى التحقق من [ملف الإكسل الناتج](5472922.xlsx) و[PDF](5472925.pdf) الذي تم إنشاؤه بالكود للرجوع إليه.

إنشاء فئة بوظيفة *CalculateCustomFunction*. تنفذ هذه الفئة [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

الآن استخدم الوظيفة أعلاه في برنامجك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
