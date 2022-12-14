---
title: قم بإنشاء أزرار أوامر مخصصة
type: docs
weight: 100
url: /ar/net/create-custom-command-buttons/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb يحتوي على أزرار خاصة مثل**يُقدِّم**, **يحفظ** و**الغاء التحميل**. تؤدي كل هذه الأزرار مهامًا محددة لـ Aspose.Cells.GridWeb.
من الممكن أيضًا إضافة أزرار مخصصة تؤدي مهامًا مخصصة. يشرح هذا الموضوع كيفية استخدام هذه الميزة.

{{% /alert %}} 
## **إنشاء أزرار أوامر مخصصة**
لإنشاء زر أمر مخصص في Aspose.Cells.GridWeb:

1. أضف Aspose.Cells.GridWeb control إلى نموذج الويب.
1. قم بالوصول إلى ورقة العمل.
1. قم بإنشاء مثيل لفئة CustomCommandButton.
1. قم بتعيين أمر الزر إلى بعض القيمة. يتم استخدام هذه القيمة في معالج حدث الزر.
1. اضبط نص الزر.
1. قم بتعيين عنوان URL لصورة الزر.
1. أخيرًا ، قم بإضافة كائن CustomCommandButton إلى مجموعة CustomCommandButtons لعنصر التحكم GridWeb.

{{% alert color="primary" %}} 

يمكن أيضًا إضافة أزرار الأوامر المخصصة في وضع WYSIWYG باستخدام مربع حوار خصائص Visual Studio.

{{% /alert %}} 

يتم عرض إخراج مقتطف الشفرة أدناه:

**تمت إضافة زر أمر مخصص إلى عنصر تحكم GridWeb** 

![ما يجب القيام به: image_بديل_نص](create-custom-command-buttons_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitCustomCommandButton.aspx-InitCustomCommandButton.cs" >}}
### **معالجة الحدث لزر الأمر المخصص**
أهم جانب من جوانب أزرار الأوامر المخصصة هو الإجراء الذي يقومون به عند النقر فوقها. لتعيين الإجراء ، قم بإنشاء معالج حدث للحدث CustomCommand الخاص بعنصر التحكم GridWeb.

يتم تشغيل الحدث CustomCommand دائمًا عند النقر فوق زر أمر مخصص. لذلك يجب على معالج الحدث تحديد زر الأمر المخصص المحدد الذي ينطبق عليه بواسطة مجموعة الأوامر عند إضافة الزر إلى عنصر التحكم GridWeb. أخيرًا ، أضف التعليمات البرمجية المخصصة التي يتم تنفيذها عند النقر فوق الزر.

في مثال الرمز أدناه ، تتم إضافة رسالة نصية إلى الخلية A1 عند النقر فوق الزر.

**تمت إضافة النص إلى خلية A1 عند النقر فوق زر الأمر المخصص** 

![ما يجب القيام به: image_بديل_نص](create-custom-command-buttons_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleCustomCommandEvent.aspx-HandleCustomCommandEvent.cs" >}}
