---
title: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/python-net/advanced-protection-settings-since-excel-xp/
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

يدعم Aspose.Cells for Python via .NET جميع إعدادات الحماية المتقدمة التي تقدمها إكسل XP أو الإصدارات الأحدث.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات اللاحقة**

لعرض إعدادات الحماية المتاحة في Excel XP:

1. من القائمة **أدوات**, اختر **الحماية** ثم **حماية الورقة**. سيتم عرض مربع الحوار.

لاستعراض إعدادات الحماية المتوفرة في Excel 2016

1. من القائمة **ملف**, اختر **حماية الدفتر** ثم **حماية الورقة الحالية**.
1. حدد **حماية الورقة** في قائمة **مراجعة**.

باتباع الخطوات المذكورة أعلاه ستظهر مربع حوار حيث يمكنك السماح أو تقييد ميزات ورقات العمل أو تطبيق كلمة مرور على ورقة العمل.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells for Python via .NET**

يدعم Aspose.Cells for Python via .NET جميع إعدادات الحماية المتقدمة.

يوفر Aspose.Cells for Python via .NET فئة تسمى [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) تمثل ملف إكسل من Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) التي تتيح الوصول إلى كل ورقة عمل داخل الملف. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) الخاصية [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) المستخدمة لتطبيق هذه الإعدادات المتقدمة للحماية. الخاصية [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) في الواقع هي كائن من فئة [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) الذي يغلف العديد من الخصائص المنطقية لتعطيل أو تمكين القيود.

فيما يلي مثال تطبيقي صغير. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة المدعومة من Excel XP والإصدارات اللاحقة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

يرجى عدم استدعاء طريقة [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) لفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) عند استخدام خاصية [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection). كما يجب حفظ الملف بصيغة Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط من قبل Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **مشكلة قفل الخلية**

إذا كنت ترغب في تقييد المستخدمين من تحرير الخلايا يجب أن تكون الخلايا مقفلة قبل تطبيق أي إعدادات حماية. وإلا يمكن تحرير الخلايا حتى لو تم حماية ورقة العمل. في Microsoft Excel XP، يمكن قفل الخلايا من خلال المربع الحوار التالي:

|**مربع الحوار لقفل الخلايا في Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن أيضًا قفل الخلايا باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET. يمكن لكل خلية الحصول على تنسيق [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) الذي يحتوي على خاصية Boolean، [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). ضبط الخاصية [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) على **true** أو **false** لقفل أو إلغاء قفل الخلية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

