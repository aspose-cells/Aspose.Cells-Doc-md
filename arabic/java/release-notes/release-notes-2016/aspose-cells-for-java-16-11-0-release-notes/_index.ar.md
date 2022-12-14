---
title: Aspose.Cells for Java 16.11.0 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-16-11-0-release-notes/
---
|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-42042 | دعم Subtotal / Total تسميات بلغات أخرى| ميزة جديدة|
|CELLSJAVA-41994 | يتدفق نص Cell إلى الخلية التالية| حشرة|
|CELLSJAVA-42039 | توجد مشكلة في CalculateFormula في إعادة حساب الخلايا بالإشارة إلى الخلايا ذات الصيغ| حشرة|
|CELLSJAVA-42050 |لا يتم تقديم أحرف التحكم العبرية بشكل صحيح في PDF| حشرة|
|CELLSJAVA-42020 | يستغرق تحويل XLS إلى PDF الكثير من الوقت| حشرة|
|CELLSJAVA-42017 | مشكلة التخطيط عند تحويل جدول البيانات إلى PDF| حشرة|
|CELLSJAVA-42023 | تتداخل تسميات المحور X مع وسيلة الإيضاح عند تقديمها إلى PDF| حشرة|
|CELLSJAVA-42022 | الصورة لا تحجيم بشكل جيد وملف SVG غير صحيح| حشرة|
|CELLSJAVA-42003 | عرض غير صحيح للمخطط أثناء تحويل جدول البيانات إلى HTML| حشرة|
|CELLSJAVA-41986 | يتم حذف المسافات من النص في إخراج PNG من المخطط| حشرة|
|CELLSJAVA-41438 | لم يتم حفظ التحديد أو التحقق من الحالة عند الحفظ في PDF| حشرة|
|CELLSJAVA-41339 |تم إفساد محاذاة النص والنص في الملف (01_ال_السماد_أداة_البلطيق_20131215_ incl_logo.xlsx)| حشرة|
|CELLSJAVA-42056 | يؤدي تمديد كائن جدول / قائمة MS Excel إلى تغيير تنسيق الخلايا| حشرة|
|CELLSJAVA-42055 | تؤدي إضافة Arc إلى مصنف جديد إلى إنشاء جدول بيانات يحتمل أن يكون غير آمن| حشرة|
|CELLSJAVA-42038 |تم كسر حل عمود الجدول إذا كان يحتوي على "["]| حشرة|
|CELLSJAVA-42021 | مشكلة تتعلق بتوسيع محتوى جدول / قائمة Excel فيما يتعلق بالصيغ| حشرة|
|CELLSJAVA-42019 | تم إرجاع صيغة غير صحيحة من خلية ورقة عمل| حشرة|
|CELLSJAVA-42004 |java.lang.NullPointerException ، في Workbook ctor أثناء تحميل ملف XLSX| استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية Workbook.AbsolutePath**
الحصول على المسار المطلق للملف وتعيينه. تستخدم فقط للروابط الخارجية.
#### **إضافة فئة GlobalizationSettings و WorkbookSettings.GlobalizationSettings**
الحصول على إعدادات العولمة وتعيينها.
#### **يزيل Cell.GetConditionalStyle () طريقة قديمة**
استخدم طريقة Cell.GetConditionalFormattingResult () بدلاً من ذلك.
#### **يزيل Cells.MaxDataRowInColumn (عمود int) طريقة قديمة**
استخدم طريقة Cells.GetLastDataRow (int) بدلاً من ذلك.
#### **يزيل خاصية PageSetup.Draft القديمة**
استخدم خاصية PageSetup.PrintDraft بدلاً من ذلك.
#### **يزيل خاصية AutoFilter.FilterColumnCollection القديمة**
استخدم خاصية AutoFilter.FilterColumns بدلاً من ذلك.
#### **يتخلى عن مُنشئ النمط ويضيف فئة CellsFactory**
استخدم طريقة CellsFactory.CreateStyle () بدلاً من ذلك.
#### **يزيل خاصية TickLabels.Rotation القديمة**
استخدم خاصية TickLabels.RotationAngle بدلاً من ذلك.
#### **يضيف أسلوب GridHyperlinkCollection.GetHyperlink (خلية GridCell)**
الحصول على كائن الارتباط التشعبي للخلية. إذا لم يكن هناك ارتباط تشعبي للخلية ، فإنها ترجع فارغة.
#### **يضيف أسلوب GridHyperlinkCollection.GetHyperlink (صف int ، عمود int)**
الحصول على كائن الارتباط التشعبي للخلية. إذا لم يكن هناك ارتباط تشعبي للخلية ، فإنها ترجع فارغة.
