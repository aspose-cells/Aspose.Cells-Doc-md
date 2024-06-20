---
title: إدارة قائمة سياق GridDesktops
type: docs
weight: 40
url: /ar/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, سياق, قائمة السياق
description: يقدم هذا المقال كيفية تخصيص قائمة السياق في GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop يحتوي على قائمة سياق تحتوي على جميع الأوامر الشائعة المستخدمة. يسمح لك التحكم بإخفاء/إظهار عناصر القائمة. علاوة على ذلك، من الممكن إضافة عناصر جديدة للقائمة مع معالجي الأحداث إليها.

{{% /alert %}} 
## **مقدمة**
تستخدم فئة ContextMenuManager لإدارة عناصر قائمة السياق. يحصل السمة GridDesktop.ContextMenuManager على مثيل من كائن ContextMenuManager. على سبيل المثال، تحصل السمة ContextMenuManager.MenuItemAvailable_Copy على قيمة تشير ما إذا كانت عنصر قائمة السياق **نسخ** متاحة أم لا. بالمثل، لدينا جميع السمات المقابلة لعناصر قائمة السياق المختلفة.

**مهم:** بشكل افتراضي، جميع عناصر قائمة السياق مرئية في القائمة.
## **إدارة قائمة السياق**
### **إخفاء عناصر قائمة السياق**
لأداء هذه المهمة، نلقي أولا نظرة على قائمة السياق الافتراضية التي يحتوي عليها GridDesktop.

**قائمة GridDesktop الافتراضية** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

الآن، قم بإخفاء بعض عناصر القائمة باستخدام الكود التالي:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



بعد تنفيذ الكود أعلاه، لن تكون بعض عناصر القائمة مرئية للمستخدمين:

**تم إخفاء بعض عناصر القائمة** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **إضافة عناصر قائمة جديدة**
أضف عنصر قائمة سياق جديد إلى القائمة باستخدام مقتطف الكود التالي.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


نحدد أيضًا معالج حدث للأمر/الخيار الجديد.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



بعد تشغيل الكود أعلاه ، يمكن رؤية عنصر قائمة جديد في قائمة السياق. سيظهر أيضًا رسالة عند النقر على الخلية.

**تمت إضافة عنصر قائمة جديد إلى القائمة** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
