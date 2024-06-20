---
title: تعطيل التفاف النص لتسميات البيانات في الرسم البياني
type: docs
weight: 60
url: /ar/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

يسمح Microsoft Excel 2013 للمستخدمين بلف النص داخل تسميات بيانات الرسم البياني أو فك اللف. بشكل افتراضي، يتم لف النص في تسميات البيانات.

{{% /alert %}}

توفر Aspose.Cells الطريقة [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). ضبط على **صحيح** أو **خطأ** لتمكين أو تعطيل لف النص على تسميات البيانات على التوالي.

بالمثل، استخدم الطريقة [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) لمعرفة ما إذا كانت تسمية بيانات ملفوفة بالفعل.

تُظهر هذه اللقطة الشاشة ملف Excel عيني يحتوي على رسم بياني يظهر فيه نص تسميات البيانات ملفوف. كما يمكنك التحقق أو إزالة الخيار **لف النص في الشكل** في قسم التوجيه في لوحة تنسيق تسميات البيانات في Microsoft Excel 2013.

**تجاويف تسميات البيانات**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

الكود العيني الذي يلي يحمل ملف Excel عيني باستخدام Aspose.Cells ويعطل لف النص في تسميات البيانات باستخدام الطريقة [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). عند تنفيذ الكود، يظهر الرسم البياني مثل هذا. يتم الآن فك النص الذي كان في السابق ملفوفًا.

**عرض تسميات البيانات على سطر واحد فقط**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
