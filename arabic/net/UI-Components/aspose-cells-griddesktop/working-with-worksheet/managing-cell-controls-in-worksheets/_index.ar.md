﻿---
title: إدارة Cell الضوابط في أوراق العمل
type: docs
weight: 130
url: /ar/net/managing-cell-controls-in-worksheets/
---
{{% alert color="primary" %}} 

يناقش هذا الموضوع بعض المفاهيم المهمة حول إدارة عناصر التحكم في الخلايا باستخدام API من Aspose.Cells.GridDesktop. سنشرح كيف يمكن للمطورين الوصول إلى عناصر التحكم في الخلية وتعديلها وإزالتها من أوراق العمل الخاصة بهم. دعونا نلقي نظرة عليه.

{{% /alert %}} 
## **الوصول إلى Cell الضوابط**
 للوصول إلى عنصر تحكم خلية موجود وتعديله في ورقة العمل ، يمكن للمطورين الوصول إلى عنصر تحكم خلية معين من ملف**ضوابط** جمع**ورقة عمل** من خلال تحديد الخلية (باستخدام اسم الخلية أو موقعها من حيث أرقام الصفوف والأعمدة) التي يتم فيها عرض عنصر التحكم في الخلية. بمجرد الوصول إلى عنصر تحكم الخلية ، يمكن للمطورين تعديل خصائصه في وقت التشغيل. على سبيل المثال ، في المثال الموضح أدناه ، وصلنا إلى ملف**خانة الاختيار** التحكم في الخلية من**ورقة عمل** وتعديل خاصية التحقق الخاصة به.

**الأهمية:** **ضوابط** تحتوي المجموعة على جميع أنواع عناصر التحكم في الخلية في شكل**CellControl** أشياء. لذلك ، إذا كنت بحاجة إلى الوصول إلى نوع معين من التحكم في الخلية ، على سبيل المثال**خانة الاختيار** ثم سوف تضطر إلى تلبيس ملف**CellControl** يعترض على**خانة الاختيار** صف دراسي.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **إزالة Cell الضوابط**
 لإزالة عنصر تحكم خلية موجود ، يمكن للمطورين ببساطة الوصول إلى ورقة العمل المطلوبة وبعد ذلك**يزيل** التحكم في الخلية من**ضوابط** جمع**ورقة عمل** من خلال تحديد الخلية (باستخدام اسمها أو رقم الصف والعمود) التي تحتوي على عنصر تحكم الخلية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}