---
title: استخدام ميزة التراجع واعادة القيام
type: docs
weight: 120
url: /ar/net/aspose-cells-griddesktop/use-undo-and-redo-feature/
keywords: GridDesktop، التراجع، إعادة
description: يقدم هذا المقال ميزة التراجع وإعادة القيام في GridDesktop.
---

{{% alert color="primary" %}} 

ميزة التراجع/الإعادة في GridDesktop مفيدة للغاية. يشرح اسمها وظيفتها بمفرده، حيث تسمح لك بتراجع/إعادة الإجراءات الأخيرة في ورقة العمل. على سبيل المثال، إذا تم حذف الصيغة عن طريق الخطأ أو تحرير البيانات في خلية لا ترغب في ذلك فعلياً، يمكن تصحيح هذه الإجراءات باستخدام عمليات التراجع والإعادة المقدمة من العنصر التحكم.

{{% /alert %}} 
## **القيام بعملية التراجع والإعادة**
تتوفر الواجهات البرمجية التالية للمهمة. يتم تقديم الوصف مع كل واجهة برمجية، يرجى التحقق منها.

- **GridDesktop.EnableUndo** - سمة: تشير ما إذا كانت وظيفة التراجع ممكنة، القيمة الافتراضية "false".
- **UndoManager** – فئة: تُستخدم لإدارة عملية التراجع/الإعادة.
- **GridDesktop.UndoManager** – سمة: تحصل على مثيل لكائن **UndoManager**.
- **UndoManager.Undo** – طريقة: تنفذ عملية التراجع.
- **UndoManager.Redo -** طريقة: تنفذ عملية الإعادة.
- **UndoManager.ClearStack** – طريقة: تقوم بمسح مكدس التراجع/الإعادة.
- **UndoManager.UndoStepsCount** – سمة: تحصل على عدد الخطوات المتاحة حالياً للتراجع.
- **UndoManager.RedoStepsCount** – سمة: يحصل على عدد الخطوات التراجعية المتاحة حاليًا.
- **UndoManager.UndoStackSize** – سمة: يحصل على/يضبط حجم المكدس التراجعي.
### **تراجع**
الشيفرة العينية التالية توضح كيفية تنفيذ العملية التراجعية باستخدام واجهة برمجة التطبيقات لـ GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Undo.cs" >}}
### **إعادة**
الشيفرة العينية التالية توضح كيفية تنفيذ العملية الإعادة باستخدام واجهة برمجة التطبيقات لـ GridDesktop.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UndoRedoFeature-Redo.cs" >}}

{{% alert color="primary" %}} 

حاليًا، تشير عملية التراجع/الإعادة إلى التغيير في قيمة خلية.

{{% /alert %}}
