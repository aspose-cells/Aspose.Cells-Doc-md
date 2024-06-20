---
title: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

منذ إصدار Excel 2002 أو XP، أضافت Microsoft العديد من إعدادات الحماية المتقدمة.

{{% /alert %}}

## **مقدمة**

تقييد أو السماح للمستخدمين بـ:

- حذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- إدراج الصفوف أو الأعمدة أو الروابط الفرعية.
- تحديد الخلايا المقفلة أو غير المقفلة.
- استخدام الجداول المحورية وأكثر من ذلك بكثير.

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة المقدمة من Excel XP أو الإصدارات اللاحقة.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **أدوات**, اختر **الحماية** ثم **حماية الورقة**. سيتم عرض مربع الحوار.

لاستعراض إعدادات الحماية المتوفرة في Excel 2016

1. من القائمة **ملف**, اختر **حماية الدفتر** ثم **حماية الورقة الحالية**.
1. حدد **حماية الورقة** في قائمة **مراجعة**.

باتباع الخطوات المذكورة أعلاه ستظهر مربع حوار حيث يمكنك السماح أو تقييد ميزات ورقات العمل أو تطبيق كلمة مرور على ورقة العمل.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

تدعم Aspose.Cells جميع إعدادات الحماية المتقدمة.

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Microsoft Excel. فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تحتوي على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) الخاصية [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) المستخدمة لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) في الواقع هي كائن من فئة [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) الذي يغلف العديد من الخصائص المنطقية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

يرجى عدم استدعاء طريقة [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) عند استخدام خاصية [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). كما يجب حفظ الملف بصيغة Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط من قبل Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد المستخدمين من تحرير الخلايا يجب أن تكون الخلايا مقفلة قبل تطبيق أي إعدادات حماية. وإلا يمكن تحرير الخلايا حتى لو تم حماية ورقة العمل. في Microsoft Excel XP، يمكن قفل الخلايا من خلال المربع الحوار التالي:

|**مربع الحوار لقفل الخلايا في Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن قفل الخلايا باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells أيضًا. يمكن أن تأخذ كل خلية تنسيقًا يحتوي على خاصية منطقية، [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style). ضبط خاصية [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) على **صحيح** أو **خطأ** لقفل أو فتح الخلية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
