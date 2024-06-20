---
title: إدارة عناصر التحكم في الأعمدة
type: docs
weight: 100
url: /ar/net/aspose-cells-griddesktop/manage-cell-controls-in-columns/
keywords: GridDesktop، controls، control
description: يقدم هذا المقال كيفية ضبط العنصر التحكم في عمود GridDesktop.
---

{{% alert color="primary" %}} 

يناقش هذا الموضوع بعض المفاهيم الهامة حول إدارة عناصر التحكم في الخلايا في الأعمدة باستخدام واجهة برمجة التطبيقات Aspose.Cells.GridDesktop. سنشرح كيف يمكن للمطور الوصول إلى العناصر التحكم، وتعديلها، وإزالتها من الأعمدة في ورقة العمل الخاصة بهم. دعونا نلقي نظرة عليها.

{{% /alert %}} 
## **الوصول إلى تحكم الخلية**
يمكن للمطورين الوصول إلى وتعديل ضوابط الخلية الحالية في العمود ببساطة باستخدام خاصية CellControl لـ **Aspose.Cells.GridDesktop.Data.GridColumn**. وبمجرد الوصول إلى ضابط الخلية، يمكن للمطورين تعديل خصائصها أثناء التشغيل. على سبيل المثال، في المثال المعطى أدناه، لقد وصلنا إلى ضابط خلية **CheckBox** موجود من عمود معين لـ **Aspose.Cells.GridDesktop.Data.GridColumn** وقمنا بتعديل خاصيتها Checked.

**مهم:** خاصية CellControl توفر ضابط خلية في شكل كائن **CellControl**. لذا، إذا كنت بحاجة إلى الوصول إلى نوع محدد من ضابط الخلية، مثل **CheckBox** على سبيل المثال، فيجب على الشخص نوع المضيف لكائن **CellControl** إلى فئة **CheckBox**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-AccessCheckbox.cs" >}}
## **إزالة تحكم الخلية**
لإزالة ضابط خلية موجود، يمكن للمطورين ببساطة الوصول إلى ورقة العمل المطلوبة ثم **إزالة** ضابط الخلية من العمود المحدد باستخدام الطريقة **RemoveCellControl** في **Aspose.Cells.GridDesktop.Data.GridColumn**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ManagingControlsInColumns-RemoveCheckbox.cs" >}}

{{% alert color="primary" %}} 

يتم تمثيل كل عمود في مجموعة **Columns** لـ **Worksheet** بمثيل من فئة **Aspose.Cells.GridDesktop.Data.GridColumn**.

{{% /alert %}}
