---
title: إدارة تحكم الخلية في الأوراق العمل
type: docs
weight: 130
url: /ar/net/aspose-cells-griddesktop/manage-cell-controls-in-worksheets/
keywords: GridDesktop، تحكم الخلية، التحكم، التحكمات
description: تقدم هذه المقالة كيفية العمل مع تحكم الخلية في GridDesktop.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع بعض المفاهيم الهامة حول إدارة تحكم الخلية باستخدام واجهة برمجة التطبيقات (API) في Aspose.Cells.GridDesktop. سنشرح كيف يمكن للمطور الوصول إلى التحكم بالخلية وتعديله وإزالته من أوراق العمل الخاصة بهم. دعنا نلقي نظرة عليه.

{{% /alert %}} 
## **الوصول إلى تحكم الخلية**
للوصول إلى تحكم الخلية الحالي وتعديله في ورقة العمل، يمكن للمطورين الوصول إلى تحكم خلية محدد من مجموعة **Controls** لورقة العمل بتحديد الخلية (باستخدام اسم الخلية أو موقعها في صف وعمود الأرقام) الذي يتم عرض تحكم الخلية فيها. بمجرد الوصول إلى تحكم الخلية، يمكن للمطورين تعديل خصائصها أثناء التشغيل. على سبيل المثال، في المثال الوارد أدناه، قمنا بالوصول إلى تحكم خلية **CheckBox** موجود من **Worksheet** وقمنا بتعديل Checked خاصيته.

**مهم:** مجموعة **Controls** تحتوي على جميع أنواع تحكم الخلية في شكل كائنات **CellControl**. لذا، إذا كنت بحاجة للوصول إلى نوع محدد من تحكم الخلية، مثل **CheckBox** على سبيل المثال، فيجب عليك قم بتحويل نوع الكائن **CellControl** إلى فئة **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-AccessCheckbox.cs" >}}
## **إزالة تحكم الخلية**
لإزالة تحكم الخلية الحالي، يمكن للمطورين الوصول ببساطة إلى ورقة العمل المطلوبة ثم **إزالة** تحكم الخلية من مجموعة **Controls** في **Worksheet** بتحديد الخلية (باستخدام اسمها أو رقم الصف والعمود) الذي يحتوي على تحكم الخلية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingCellControls-RemoveCheckbox.cs" >}}
