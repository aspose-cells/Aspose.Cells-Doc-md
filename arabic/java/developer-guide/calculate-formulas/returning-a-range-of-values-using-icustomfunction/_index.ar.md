---
title: إرجاع نطاق من القيم باستخدام وظيفة ICustomFunction
type: docs
weight: 270
url: /ar/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 ال[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) منذ إصدار Aspose.Cells for Java 20.8. الرجاء استخدام[**الخلاصةحساب المحرك**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) صف دراسي. استخدام[**الخلاصةحساب المحرك**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) يتم وصف فئة في المقالة التالية.

[إرجاع نطاق من القيم باستخدام AbstractCalculationEngine](/cells/ar/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 يوفر Aspose.Cells[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)الواجهة التي تُستخدم لتنفيذ الوظائف المعرفة من قبل المستخدم أو الوظائف المخصصة التي لا يدعمها Microsoft Excel كوظائف مضمنة.

 في الغالب عند تنفيذ[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) طريقة الواجهة ، تحتاج إلى إرجاع قيمة خلية واحدة. لكن في بعض الأحيان ، تحتاج إلى إرجاع نطاق من القيم. تشرح هذه المقالة كيفية إرجاع نطاق القيم من[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **إرجاع نطاق من القيم باستخدام وظيفة ICustomFunction**

 يتم تنفيذ التعليمات البرمجية التالية[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) وإرجاع نطاق القيم عبر طريقته. رجاء تاكد من[ملف اكسل الناتج](5472922.xlsx) و[بي دي إف](5472925.pdf) ولدت مع رمز للرجوع اليها.

إنشاء فئة مع وظيفة*احسبدالة مخصصة*. هذه الفئة تنفذ[**وظيفة ICustom**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

الآن استخدم الوظيفة المذكورة أعلاه في برنامجك.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
