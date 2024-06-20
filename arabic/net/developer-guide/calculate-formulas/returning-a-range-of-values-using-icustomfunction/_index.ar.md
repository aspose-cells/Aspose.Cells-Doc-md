---
title: إرجاع مجموعة من القيم باستخدام ICustomFunction
description: يصف هذا المقال كيفية استخدام مكتبة Aspose.Cells لإرجاع مجموعة من القيم باستخدام ICustomFunction في Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف Excel جديد، يمكننا استخدام الأساليب المقدمة من Aspose.Cells للحصول على مجموعة من القيم وإرجاع النتيجة. وأخيرًا، نقوم بحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، ICustomFunction، يُرجع سلسلة من القيم
type: docs
weight: 50
url: /ar/net/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

[**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) تمت إهماله منذ إصدار Aspose.Cells for Java 20.8. يرجى استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine). يتم وصف استخدام فئة [**AbstractCalculationEngine**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) في المقال التالي.

[إرجاع مجموعة من القيم باستخدام AbstractCalculationEngine](/cells/ar/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}}

{{% alert color="primary" %}}

توفر Aspose.Cells واجهة [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) التي تُستخدم لتنفيذ وظائف مخصصة أو مخصصة لا تدعمها Microsoft Excel كوظائف مدمجة.

عند تنفيذ طريقة واجهة [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) عادةً، تحتاج إلى إرجاع قيمة خلية واحدة. ولكن في بعض الأحيان، قد تحتاج إلى إرجاع مجموعة من القيم. سيشرح هذا المقال كيفية إرجاع مجموعة القيم من [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

الكود التالي ينفذ [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) ويُرجع مجموعة القيم من خلال طريقة الواجهة.

قم بإنشاء فئة تحتوي على وظيفة *CalculateCustomFunction*. تنفذ هذه الفئة [**ICustomFunction**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

الآن استخدم الوظيفة أعلاه في برنامجك

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
