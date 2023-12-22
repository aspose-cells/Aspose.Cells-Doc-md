---
title: إرجاع نطاق من القيم باستخدام ICustomFunction
description: توضح هذه المقالة كيفية استخدام مكتبة Aspose.Cells لإرجاع نطاق من القيم باستخدام ICustomFunction في Microsoft Excel. عن طريق تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الطرق التي يوفرها Aspose.Cells للحصول على نطاق من القيم وإرجاع النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells, Excel, ICustomFunction, returns a series of values
type: docs
weight: 50
url: /ar/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 ال[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) تم إهماله منذ إصدار Aspose.Cells for Java 20.8. الرجاء استخدام[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) فصل. استخدام[**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) تم وصف الطبقة في المقالة التالية.

[إرجاع نطاق من القيم باستخدام AbstractCalculationEngine](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells يوفر[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)الواجهة التي يتم استخدامها لتنفيذ الوظائف المحددة من قبل المستخدم أو المخصصة التي لا يدعمها Microsoft Excel كوظائف مدمجة.

 في الغالب عند تنفيذ[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) طريقة الواجهة، تحتاج إلى إرجاع قيمة خلية واحدة. لكن في بعض الأحيان، تحتاج إلى إرجاع نطاق من القيم. تشرح هذه المقالة كيفية إرجاع نطاق القيم من[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 يتم تنفيذ التعليمات البرمجية التالية[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)وإرجاع نطاق القيم عبر طريقته.

قم بإنشاء فئة باستخدام دالة *CalculateCustomFunction*. تنفذ هذه الفئة[**IcustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

الآن استخدم الوظيفة المذكورة أعلاه في برنامجك

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
