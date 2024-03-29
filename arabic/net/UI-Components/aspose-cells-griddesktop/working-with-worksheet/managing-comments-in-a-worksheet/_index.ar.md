﻿---
title: إدارة التعليقات في ورقة عمل
type: docs
weight: 110
url: /ar/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

في MS Excel ، يجب أن تكون على دراية بميزة التعليقات التي تتيح للمستخدمين إضافة تعليقات إلى الخلايا. هذه الميزة مفيدة في تلك الحالات عندما تكون مطلوبة لتوفير بعض المعلومات للمستخدمين عندما يكونون على وشك إدخال القيم في الخلايا. عندما يضع المستخدم مؤشر الماوس الخاص به على خلية تم التعليق عليها ، تظهر رسالة منبثقة صغيرة لتوفير بعض المعلومات للمستخدم. باستخدام Aspose.Cells.GridDesktop ، يمكن للمطورين تكوين تعليقات على الخلايا. في هذا الموضوع ، سنشرح استخدام هذه الميزة بالتفصيل.

{{% /alert %}} 
## **إضافة التعليقات**
لإضافة تعليق إلى خلية باستخدام Aspose.Cells.GridDesktop ، يرجى اتباع الخطوات التالية:

-  أضف Aspose.Cells.GridDesktop control إلى ملف**استمارة**
-  الوصول إلى أي ملفات**ورقة عمل**
-  يضيف**تعليق** إلى ورقة العمل عن طريق تحديد الخلية (باستخدام اسمها أو رقم الصف والعمود) التي سيتم إضافة التعليق إليها.

 سيضيف الكود أدناه تعليقات إلى**ب 2** و**ب 4** خلايا ورقة العمل.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**تعليقات** جمع في**ورقة عمل** يوفر الكائن فوق طاقته**يضيف** طريقة. يمكن للمطورين استخدام أي إصدار محمّل فوق طاقته من**يضيف** الطريقة وفقًا لاحتياجاتهم الخاصة.
## **الوصول إلى التعليقات**
للوصول إلى تعليق موجود وتعديله في ورقة العمل ، يمكن للمطورين الوصول إلى التعليق من ملف**تعليقات** جمع**ورقة عمل** من خلال تحديد الخلية (باستخدام اسم الخلية أو موقعها من حيث رقم الصف والعمود) التي يتم إدراج التعليق فيها. بمجرد الوصول إلى التعليق ، يمكن للمطورين تعديل نصه في وقت التشغيل.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **إزالة التعليقات**
 لإزالة تعليق موجود ، يمكن للمطورين ببساطة الوصول إلى ورقة العمل المطلوبة وبعد ذلك**يزيل** تعليق من**تعليقات** جمع**ورقة عمل** من خلال تحديد الخلية (باستخدام اسمها أو الصف ورقم العمود) التي تحتوي على تعليق.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
