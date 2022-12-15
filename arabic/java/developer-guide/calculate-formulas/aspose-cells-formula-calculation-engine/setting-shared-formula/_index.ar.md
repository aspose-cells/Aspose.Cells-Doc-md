---
title: إعداد الصيغة المشتركة
type: docs
weight: 10
url: /ar/java/setting-shared-formula/
---
{{% alert color="primary" %}} 

افترض أن لديك ورقة عمل مليئة بالبيانات بالتنسيق الذي يشبه نموذج ورقة العمل التالية.

**ملف الإدخال بعمود واحد أو بيانات** 

![ما يجب القيام به: image_بديل_نص](setting-shared-formula_1.png)

 تريد إضافة دالة في B2 تحسب ضريبة المبيعات للصف الأول من البيانات. الضريبة**9%** الصيغة التي تحسب ضريبة المبيعات هي:**"= A2 * 0.09"**. تشرح هذه المقالة كيفية تطبيق هذه الصيغة مع Aspose.Cells.

{{% /alert %}} 

 Aspose.Cells يتيح لك تحديد معادلة باستخدام[Cell.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) الملكية ، على وجه التحديد[Cell.setFormula ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) و[Cell.getFormula ()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula).

يوجد خياران لإضافة الصيغ إلى الخلايا الأخرى (B3 و B4 و B5 وما إلى ذلك) في العمود.

إما أن تفعل ما فعلته للخلية الأولى ، وتعيين الصيغة لكل خلية بشكل فعال ، وتحديث مرجع الخلية وفقًا لذلك (A3*0.09 ، A4*0.09 و A5 * 0.09 وما إلى ذلك). يتطلب هذا تحديث مراجع الخلايا لكل صف. يتطلب أيضًا Aspose.Cells لتحليل كل صيغة على حدة ، مما قد يستغرق وقتًا طويلاً لجداول البيانات الكبيرة والصيغ المعقدة. يضيف أيضًا سطورًا إضافية من الرموز على الرغم من أن الحلقات يمكن أن تقللها إلى حد ما.

 نهج آخر هو استخدام**صيغة مشتركة** باستخدام صيغة مشتركة ، يتم تحديث الصيغ تلقائيًا لمراجع الخلية في كل صف بحيث يتم حساب الضريبة بشكل صحيح. ال[Cell.setSharedFormula](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setSharedFormula\(java.lang.String,%20int,%20int\)) الطريقة أكثر كفاءة من الطريقة الأولى.

يوضح المثال التالي كيفية استخدامه. تظهر لقطة الشاشة أدناه ملف الإخراج.

**ملف الإخراج: تم تطبيق الصيغة المشتركة** 

![ما يجب القيام به: image_بديل_نص](setting-shared-formula_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingSharedFormula-SettingSharedFormula.java" >}}
