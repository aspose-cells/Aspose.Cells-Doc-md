---
title: إعدادات الحماية المتقدمة منذ Excel XP
type: docs
weight: 30
url: /ar/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

منذ إصدار Excel 2002 أو XP ، أضاف Microsoft العديد من إعدادات الحماية المتقدمة.

{{% /alert %}}

## **مقدمة**

تعمل إعدادات الحماية هذه على تقييد المستخدمين أو السماح لهم بما يلي:

- احذف الصفوف أو الأعمدة.
- تحرير المحتويات أو الكائنات أو السيناريوهات.
- تنسيق الخلايا أو الصفوف أو الأعمدة.
- قم بإدراج صفوف أو أعمدة أو ارتباطات تشعبية.
- حدد الخلايا المؤمنة أو غير المؤمنة.
- استخدم الجداول المحورية وغير ذلك الكثير.

يدعم Aspose.Cells كافة إعدادات الحماية المتقدمة التي يوفرها Excel XP أو الإصدارات الأحدث.

### **إعدادات الحماية المتقدمة باستخدام Excel XP والإصدارات الأحدث**

لعرض إعدادات الحماية المتوفرة في Excel XP:

1.  من**أدوات** القائمة ، حدد**حماية** تليها**ورقة حماية**. سيتم عرض مربع حوار.

لعرض إعدادات الحماية المتوفرة في Excel 2016

1.  من**ملف** القائمة ، حدد**حماية المصنف** تليها**حماية الورقة الحالية**.
1.  حدد ملف**ورقة حماية** في ال**إعادة النظر** قائمة.

باتباع الخطوات المذكورة أعلاه ، سيظهر مربع حوار حيث يمكنك السماح بميزات أوراق العمل أو تقييدها أو تطبيق كلمة مرور على ورقة العمل.

### **إعدادات الحماية المتقدمة باستخدام Aspose.Cells**

Aspose.Cells يدعم كل إعدادات الحماية المتقدمة.

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي.

 ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) الخاصية المستخدمة لتطبيق إعدادات الحماية المتقدمة هذه. ال[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) الخاصية هي في الواقع كائن من[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/protection)فئة تضم العديد من الخصائص المنطقية لتعطيل القيود أو تمكينها.

يوجد أدناه مثال صغير للتطبيق. يفتح ملف Excel ويستخدم معظم إعدادات الحماية المتقدمة التي يدعمها Excel XP والإصدارات الأحدث.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 من فضلك لا تتصل ب[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**يحمي**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) الطريقة عند استخدام[**حماية**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)منشأه. أيضًا ، احفظ الملف بتنسيق Excel97To2003 أو Xlsx لأن إعدادات الحماية المتقدمة مدعومة فقط بواسطة Excel XP والإصدارات الأحدث.

{{% /alert %}}

### **Cell مشكلة الإقفال**

إذا كنت تريد تقييد المستخدمين من تحرير الخلايا ، فيجب تأمين الخلايا قبل تطبيق أي إعدادات حماية. خلاف ذلك ، يمكن تحرير الخلايا حتى إذا كانت ورقة العمل محمية. في Microsoft Excel XP ، يمكن تأمين الخلايا من خلال مربع الحوار التالي:

|**مربع حوار لتأمين الخلايا في Excel XP**|
|:- |
|![ما يجب القيام به: image_بديل_نص](advanced-protection-settings-since-excel-xp_1.png)|

من الممكن قفل الخلايا باستخدام Aspose.Cells API أيضًا. يمكن أن تحصل كل خلية[**أسلوب**](https://reference.aspose.com/cells/net/aspose.cells/style) التنسيق الذي يحتوي على خاصية منطقية ،[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . تعيين[**مقفل**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) الملكية ل**حقيقي** أو**خاطئة** لقفل أو إلغاء قفل الخلية.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
