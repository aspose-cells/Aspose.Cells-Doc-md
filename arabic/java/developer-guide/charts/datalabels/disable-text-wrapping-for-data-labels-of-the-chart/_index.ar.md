---
title: تعطيل التفاف النص لتسميات البيانات في المخطط
type: docs
weight: 60
url: /ar/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft يسمح Excel 2013 للمستخدمين بالتفاف أو إلغاء التفاف النص داخل تسميات بيانات المخطط. بشكل افتراضي ، يتم التفاف نص تسمية البيانات.

{{% /alert %}}

يوفر Aspose.Cells ملف[**DataLabels.setTextWrapped ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) طريقة. ضبط ل**حقيقي** أو**خطأ شنيع** لتمكين التفاف النص على تسميات البيانات أو تعطيله على التوالي.

 وبالمثل ، استخدم ملف[**DataLabels.isTextWrapped ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)طريقة لمعرفة ما إذا كانت تسمية البيانات مغلفة بالفعل.

تُظهر لقطة الشاشة هذه نموذجًا من ملف Excel Microsoft يحتوي على مخطط يتم فيه التفاف نص ملصقات البيانات. كما ترى ، يمكنك التحقق من أو مسح**التفاف النص في الشكل** الخيار في قسم ALIGNMENT بلوحة Format Datalabels في Microsoft Excel 2013.

**تسميات التفاف البيانات**

![ما يجب القيام به: image_بديل_نص](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 نموذج التعليمة البرمجية التي تلي تحميل نموذج ملف Excel Microsoft باستخدام Aspose.Cells وتعطيل التفاف نص تسمية البيانات باستخدام[**DataLabels.setTextWrapped ()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)طريقة. عندما يتم تنفيذ الكود ، يبدو الرسم البياني هكذا. النص الذي تم تغليفه سابقًا غير ملفوف الآن.

**إظهار تسميات البيانات في سطر واحد فقط**

![ما يجب القيام به: image_بديل_نص](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
