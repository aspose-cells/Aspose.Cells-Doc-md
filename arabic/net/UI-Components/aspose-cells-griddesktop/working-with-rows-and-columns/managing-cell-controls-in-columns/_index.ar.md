---
title: إدارة Cell عناصر التحكم في الأعمدة
type: docs
weight: 100
url: /ar/net/managing-cell-controls-in-columns/
---
{{% alert color="primary" %}} 

يناقش هذا الموضوع بعض المفاهيم المهمة حول إدارة عناصر تحكم الخلية في الأعمدة باستخدام Aspose.Cells.GridDesktop API. سوف نشرح كيف يمكن للمطورين الوصول إلى عناصر تحكم الخلية وتعديلها وإزالتها من أعمدة أوراق العمل الخاصة بهم. دعونا نلقي نظرة عليه.

{{% /alert %}} 
## **الوصول إلى Cell الضوابط**
 للوصول إلى عنصر تحكم خلية موجود وتعديله في العمود ، يمكن للمطورين استخدام الخاصية CellControl في ملف**Aspose.Cells.GridDesktop.Data.GridColumn** . بمجرد الوصول إلى عنصر تحكم الخلية ، يمكن للمطورين تعديل خصائصه في وقت التشغيل. على سبيل المثال ، في المثال الموضح أدناه ، وصلنا إلى ملف**خانة الاختيار** التحكم في الخلية من ملف**Aspose.Cells.GridDesktop.Data.GridColumn** وتعديل خاصية التحقق الخاصة به.

**مهم:** توفر خاصية CellControl عنصر تحكم خلية في شكل**CellControl**هدف. لذلك ، إذا كنت بحاجة إلى الوصول إلى نوع معين من التحكم في الخلية ، على سبيل المثال**خانة الاختيار** ثم سوف تضطر إلى تلبيس ملف**CellControl** يعترض على**خانة الاختيار** صف دراسي.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **إزالة Cell الضوابط**
 لإزالة عنصر تحكم خلية موجود ، يمكن للمطورين ببساطة الوصول إلى ورقة العمل المطلوبة وبعد ذلك**إزالة** عنصر تحكم الخلية من عمود معين باستخدام**RemoveCellControl** طريقة**Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

 كل عمود في**الأعمدة** جمع**ورقة عمل** يتم تمثيله بمثيل**Aspose.Cells.GridDesktop.Data.GridColumn** صف دراسي.

{{% /alert %}}
