---
title: إدارة قائمة سياق GridDesktops
type: docs
weight: 40
url: /ar/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop قائمة السياق التي تحتوي على جميع الأوامر شائعة الاستخدام. يسمح لك عنصر التحكم بإخفاء / إظهار عناصر القائمة. علاوة على ذلك ، من الممكن إضافة عناصر قائمة جديدة مع معالجات الأحداث إلى القائمة.

{{% /alert %}} 
## **مقدمة**
يتم استخدام فئة ContextMenuManager لإدارة عناصر قائمة السياق. تحصل السمة GridDesktop.ContextMenuManager على مثيل كائن ContextMenuManager. على سبيل المثال ، تحصل السمة ContextMenuManager.MenuItemAvailable_Copy على قيمة تشير إلى ما إذا كان عنصر قائمة السياق ** Copy ** متاحًا أم لا. وبالمثل ، لدينا جميع السمات المقابلة لعناصر قائمة السياق المختلفة.

**الأهمية:** بشكل افتراضي ، تكون جميع عناصر قائمة السياق مرئية في القائمة.
## **إدارة قائمة السياق**
### **إخفاء عناصر قائمة السياق**
لتنفيذ هذه المهمة ، نلقي أولاً نظرة على قائمة السياق الافتراضية الموجودة في GridDesktop.

**قائمة GridDeskop الافتراضية** 

![ما يجب القيام به: image_بديل_نص](managing-griddesktops-context-menu_1.png)

الآن ، قم بإخفاء بعض عناصر القائمة باستخدام الكود أدناه:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



بعد تنفيذ الكود أعلاه ، لن تظهر بعض عناصر القائمة للمستخدمين:

**بعض عناصر القائمة مخفية** 

![ما يجب القيام به: image_بديل_نص](managing-griddesktops-context-menu_2.png)
### **إضافة عناصر قائمة جديدة**
أضف عنصر قائمة سياق جديد إلى القائمة باستخدام مقتطف التعليمات البرمجية التالي.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


نحدد أيضًا معالج الحدث للأمر / الخيار الجديد.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



بعد تنفيذ الكود أعلاه ، يمكن رؤية عنصر قائمة جديد في قائمة السياق. ستظهر رسالة أيضًا عند النقر فوق الخلية.

**يتم إضافة عنصر قائمة جديد إلى القائمة** 

![ما يجب القيام به: image_بديل_نص](managing-griddesktops-context-menu_3.png)
