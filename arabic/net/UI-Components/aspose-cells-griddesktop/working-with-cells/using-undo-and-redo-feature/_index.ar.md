---
title: استخدام ميزة التراجع والإعادة
type: docs
weight: 120
url: /ar/net/using-undo-and-redo-feature/
---
{{% alert color="primary" %}} 

ميزة GridDesktop's Undo / Redo مفيدة للغاية. يشرح الاسم وظائفه بنفسه ، ويسمح لك بالتراجع / إعادة الإجراء (الإجراءات) الأخير في ورقة العمل. على سبيل المثال ، إذا تم حذف صيغة عن طريق الخطأ أو قمت بتحرير بيانات في خلية لا تريدها بالفعل ، فيمكن تصحيح هذه الإجراءات باستخدام عمليتي التراجع والإعادة التي يوفرها عنصر التحكم.

{{% /alert %}} 
## **تنفيذ عملية التراجع والإعادة**
تتوفر للمهمة واجهات برمجة التطبيقات التالية. الوصف معطى مع كل API ، يرجى التحقق منها.

- **GridDesktop.EnableUndo** - السمة: تشير إلى تمكين وظيفة التراجع ، والقيمة الافتراضية هي "خطأ".
- **التراجع عن المدير** - فئة: تستخدم لإدارة عملية التراجع / الإعادة.
- **GridDesktop.UndoManager** - السمة: تحصل على مثيل**التراجع عن المدير** موضوع.
- **UndoManager.Undo** - الطريقة: تقوم بعملية تراجع.
- **UndoManager.Redo -** الطريقة: تقوم بعملية الإعادة.
- **UndoManager.ClearStack** - الطريقة: يمسح مكدس التراجع / الإعادة.
- **UndoManager.UndoStepsCount** - السمة: تحصل على عدد خطوات التراجع المتوفرة حاليًا.
- **UndoManager.RedoStepsCount** - السمة: تحصل على عدد خطوات الإعادة المتاحة الحالية.
- **UndoManager.UndoStackSize** - السمة: تحصل على / تحدد حجم مكدس التراجع.
### **الغاء التحميل**
يُظهر نموذج التعليمات البرمجية التالي كيفية تنفيذ عملية التراجع باستخدام GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **إعادة**
يوضح نموذج التعليمات البرمجية التالي كيفية تنفيذ عملية الإعادة باستخدام GridDesktop API.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

حاليًا ، تشير عملية التراجع / الإعادة إلى التغيير في قيمة الخلية.

{{% /alert %}}
