---
title: إنشاء أزرار الأوامر المخصصة
type: docs
weight: 100
url: /ar/net/aspose-cells-gridweb/create-custom-command-buttons/
keywords: GridWeb, الأمر, أزرار الأوامر, مخصص
description: يقدم هذا المقال كيفية إنشاء أزرار الأوامر المخصصة في GridWeb.
---

{{% alert color="primary" %}} 

تحتوي Aspose.Cells.GridWeb على أزرار خاصة مثل **مقدمة**، **حفظ** و **تراجع**. جميع هذه الأزرار تقوم بمهام محددة لـ Aspose.Cells.GridWeb.
من الممكن أيضًا إضافة أزرار مخصصة تقوم بأداء مهام مخصصة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.

{{% /alert %}} 
## **إنشاء أزرار أوامر مخصصة**
لإنشاء زر أمر مخصص في Aspose.Cells.GridWeb:

1. أضف تحكم Aspose.Cells.GridWeb إلى نموذج الويب.
1. الوصول إلى ورقة العمل.
1. إنشاء مثيل من فئة CustomCommandButton.
1. تعيين الأمر الخاص بالزر إلى قيمة معينة. يتم استخدام هذه القيمة في معالج الحدث الخاص بالزر.
1. تعيين نص الزر.
1. تعيين عنوان URL للصورة الخاصة بالزر.
1. أخيرًا، أضف كائن CustomCommandButton إلى مجموعة CustomCommandButtons لتحكم GridWeb.

{{% alert color="primary" %}} 

يمكن أيضًا إضافة أزرار أوامر مخصصة في وضع WYSIWYG باستخدام مربع حوار الخصائص في Visual Studio.

{{% /alert %}} 

يتم عرض إخراج مقطع الكود أدناه:

**تمت إضافة زر أمر مخصص إلى تحكم GridWeb** 

![todo:image_alt_text](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **معالجة الأحداث لزر أمر مخصص**
أهم جانب في أزرار الأوامر المخصصة هو الإجراء الذي تقوم به عند النقر. لتعيين الإجراء، أنشئ معالج حدث لحدث CustomCommand لتحكم GridWeb.

يتم تشغيل حدث CustomCommand دائمًا عند النقر على زر الأمر المخصص. لذا يتعين على معالج الحدث تحديد زر الأمر المخصص المعين الذي ينطبق عليه عن طريق الأمر المعين عند إضافة الزر إلى تحكم GridWeb. أخيرًا، أضف كود مخصص يتم تنفيذه عند النقر على الزر.

في المثال الكودي أدناه، يتم إضافة رسالة نصية إلى الخلية A1 عند النقر على الزر.

**تمت إضافة نص إلى الخلية A1 عند النقر على زر الأمر المخصص** 

![todo:image_alt_text](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
