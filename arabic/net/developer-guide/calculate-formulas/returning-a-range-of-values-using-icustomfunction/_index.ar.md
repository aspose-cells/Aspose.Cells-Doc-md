---
title: إرجاع نطاق من القيم باستخدام وظيفة ICustomFunction
type: docs
weight: 50
url: /ar/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 ال[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) منذ إصدار Aspose.Cells for Java 20.8. الرجاء استخدام[**الخلاصةحساب المحرك**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) صف دراسي. استخدام[**الخلاصةحساب المحرك**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) يتم وصف فئة في المقالة التالية.

[إرجاع نطاق من القيم باستخدام AbstractCalculationEngine](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 يوفر Aspose.Cells[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)الواجهة التي تُستخدم لتنفيذ الوظائف المعرفة من قبل المستخدم أو الوظائف المخصصة التي لا يدعمها Microsoft Excel كوظائف مضمنة.

 في الغالب عند تنفيذ[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) طريقة الواجهة ، تحتاج إلى إرجاع قيمة خلية واحدة. لكن في بعض الأحيان ، تحتاج إلى إرجاع نطاق من القيم. تشرح هذه المقالة كيفية إرجاع نطاق القيم من[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 يتم تنفيذ التعليمات البرمجية التالية[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)وإرجاع نطاق القيم عبر طريقته.

إنشاء فئة مع وظيفة*احسبدالة مخصصة*. هذه الفئة تنفذ[**وظيفة ICustom**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

الآن استخدم الوظيفة المذكورة أعلاه في برنامجك

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
