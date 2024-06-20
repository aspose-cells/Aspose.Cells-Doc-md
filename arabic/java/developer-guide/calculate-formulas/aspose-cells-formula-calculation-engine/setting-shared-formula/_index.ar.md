---
title: ضبط الصيغ المشتركة
type: docs
weight: 10
url: /ar/java/setting-shared-formula/
---

{{% alert color="primary" %}} 

من المفترض أن يكون لديك ورقة عمل مليئة بالبيانات بتنسيق يبدو مثل الورقة العمل النموذجية التالية.

**ملف الإدخال بعمود واحد أو بيانات** 

![todo:image_alt_text](setting-shared-formula_1.png)

ترغب في إضافة وظيفة في B2 التي ستقوم بحساب ضريبة المبيعات للصف الأول من البيانات. الضريبة **9%**. الصيغة التي تحسب ضريبة المبيعات هي: **"=A2*0.09"**. يشرح هذا المقال كيفية تطبيق هذه الصيغة باستخدام Aspose.Cells.

{{% /alert %}} 

Aspose.Cells يتيح لك تحديد الصيغة باستخدام [خاصية Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)، وتحديدًا [Cell.setFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) و [Cell.getFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

هناك خياران لإضافة الصيغ إلى الخلايا الأخرى (B3، B4، B5، وهلم جرا) في العمود.

إما أن تفعل ما فعلته للخلية الأولى، مضبطا الصيغة لكل خلية وتحديثها وفقًا للإشارة إلى الخلية (`A3*0.09`، `A4*0.09`، `A5*0.09`، وهلم جرا). هذا يتطلب تحديث الإشارات إلى الخلية في كل صف. كما يتطلب من Aspose.Cells معالجة كل صيغة بشكل فردي، مما يمكن أن يكون مستهلا لجداول بيانات كبيرة وصيغ معقدة. كما أنه يضيف أكواد إضافية على الرغم من أن الحلقات يمكن أن تقلصها إلى حد ما.

نهج آخر هو استخدام **الصيغة المشتركة**. مع الصيغة المشتركة، يتم تحديث الصيغ تلقائيًا للإشارات إلى الخلية في كل صف بحيث يتم حساب الضريبة بشكل صحيح. تعتبر طريقة [Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) أكثر كفاءة من الطريقة الأولى.

المثال التالي يوضح كيفية استخدامه. يظهر اللقطة الشاشية أدناه الملف الناتج.

**ملف الإخراج: تطبيق الصيغة المشتركة** 

![todo:image_alt_text](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
