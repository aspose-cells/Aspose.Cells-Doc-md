---
title: Aspose.Cells لملاحظات إصدار CPP 18.4
type: docs
weight: 30
url: /ar/cpp/aspose-cells-for-cpp-18-4-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells لـ CPP 18.4.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSCPP-53|دعم ميزات الرسم / الوحدات|ميزة جديدة|
|CELLSCPP-57|تطبيق System.Drawing Library|ميزة جديدة|
|CELLSCPP-68|نظام التصحيح. وحدة الرسم|ميزة جديدة|
|CELLSCPP-69|حل المشكلات في حالات اختبار C ++|ميزة جديدة|
|CELLSCPP-70|حل مشكلة تسرب الذاكرة في فئات وحدة الرسم System.Drawing|ميزة جديدة|
|CELLSCPP-73|اكتب طريقة في نشر ملفات h|ميزة جديدة|
|CELLSCPP-75|تنفيذ وظيفة C ++: رسم صورة من الدفق|ميزة جديدة|
|CELLSCPP-76|تنفيذ فئات C ++: ComIStreamWrapper و Metafile|ميزة جديدة|
|CELLSCPP-77|حالة اختبار التصحيح C ++: نُسخ|ميزة جديدة|
|CELLSCPP-78|حل المشكلات في حالات اختبار C ++: DigitalSignature و EnumTypes و Finds و Formulas و Hyperlinks Modules|ميزة جديدة|
|CELLSCPP-79|حل مشكلة ارتباط نسخة إصدار C ++|ميزة جديدة|
|CELLSCPP-81|إصلاح مشكلة FillPath في وحدة الرسم|ميزة جديدة|
|CELLSCPP-82|إصلاح مشكلة وحدة الرسم System.Drawing حسب حالة الاختبار|ميزة جديدة|
|CELLSCPP-83|إصلاح مشكلة gppoint FillPath في وحدة الرسم|ميزة جديدة|
|CELLSCPP-89|ترجمة وتصحيح حالة الاختبار في دليل المخططات / EnumTypes|ميزة جديدة|
|CELLSCPP-91|ترجمة حالة الاختبار في Finds|ميزة جديدة|
|CELLSCPP-96|ترجمة حالة الاختبار وتصحيحها في دليل الصيغ / الارتباطات التشعبية / ImpHtml / ImportExports / إدراج|ميزة جديدة|
|CELLSCPP-97|تصحيح الأخطاء وإصلاحها فيما يتعلق بعرض XLSX / XLS إلى PDF|ميزة جديدة|
|CELLSCPP-98|ترجمة حالة الاختبار وتصحيحها في دليل LightCells|ميزة جديدة|
|CELLSCPP-100|ترجمة وتصحيح حالة الاختبار في دليل Merges / OpenSaves / PageSetups / PDF|ميزة جديدة|
|CELLSCPP-101|ترجمة وتصحيح حالة الاختبار في دليل PivotTables|ميزة جديدة|
|CELLSCPP-102|لا يتم تحليل المخططات (الاحتفاظ بها) عند فتح / حفظ تنسيق ملف XLSX|ميزة جديدة|
|CELLSCPP-103|ترجمة وتصحيح حالة الاختبار في دليل الأشكال|ميزة جديدة|
|CELLSCPP-105|ترجمة وتصحيح حالة الاختبار في دليل XlsxTest|ميزة جديدة|
|CELLSCPP-108|افتح الملفات وتحقق من المشكلات المتعلقة بالمخططات|ميزة جديدة|
|CELLSCPP-106|مشكلة تسرب الذاكرة|حشرة|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for C++. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يعيد تسمية جميع الطرق مثل "SetIs *" إلى أساليب "Set *"**
يعيد تسمية الأساليب ، مثل SetIsOutlineShown to SetIsOutlineShown و SetIsSelected إلى SetSelected في IWorksheet وما إلى ذلك. لمزيد من التفاصيل ، راجع API الدليل المرجعي.
#### **يغير اللون إلى النظام :: الرسم :: اللون**
على سبيل المثال ، يقوم بتغيير Color :: GetBlue () إلى System :: Drawing :: Color :: GetBlue (). نظرًا لأن اللون هو رمز غامض هنا ، فقد يكون Aspose :: Cells :: System :: Drawing :: Color أو Gdiplus :: Color. لاستخدام اللون في Aspose Cells ، يجب إضافة مساحة الاسم System :: Drawing.
#### **يعيد تسمية ICells :: AddRange إلى AddIRange**
يضيف مرجع كائن النطاق إلى الخلايا.
#### **يعيد تسمية ICells :: ApplyColumnStyle إلى ApplyColumnIStyle**
يطبق التنسيق على عمود بأكمله.
#### **يعيد تسمية ICells :: ApplyRowStyle to ApplyRowIStyle**
يطبق التنسيق على صف كامل.
#### **يعيد تسمية ICells :: ApplyStyle to ApplyIStyle**
يطبق التنسيق على ورقة عمل كاملة.
#### **يعيد تسمية ICells :: CopyColumn إلى CopyIColumn**
نسخ البيانات وتنسيق العمود بأكمله.
#### **يعيد تسمية ICells :: CopyColumns إلى CopyIColumns**
نسخ البيانات وتنسيق الأعمدة المحددة.
#### **يعيد تسمية ICells :: CopyColumns إلى CopyIColumns**
نسخ البيانات وتنسيق الأعمدة المحددة.
#### **يعيد تسمية ICells :: CopyRow إلى CopyIRow**
نسخ البيانات وتنسيق صف كامل.
#### **يعيد تسمية ICells :: CopyRows إلى CopyIRows**
نسخ البيانات وتنسيق الصفوف المحددة.
#### **يعيد تسمية ICells :: MoveRange إلى MoveIRange**
ينقل النطاق إلى موقع الوجهة.
#### **يعيد تسمية ICells :: InsertRange إلى InsertIRange**
يُدرج نطاقًا من الخلايا وينقل الخلايا وفقًا لخيار الإزاحة.
#### **يعيد تسمية IColumn :: ApplyStyle إلى ApplyIStyle**
يطبق التنسيق على عمود بأكمله.
#### **يعيد تسمية IErrorCheckOption :: AddRange إلى AddIRange**
يضيف نطاقًا متأثرًا بهذا الإعداد.
#### **يعيد تسمية IRange :: ApplyStyle to ApplyIStyle**
يطبق التنسيق على نطاق كامل.
#### **يعيد تسمية IRow :: ApplyStyle to ApplyIStyle**
يطبق التنسيق على صف كامل.
#### **يعيد تسمية IPivotField :: GetNumberFormat إلى Get_NumberFormat**
يمثل تنسيق العرض المخصص للأرقام والتواريخ. نظرًا لأن اسم الأسلوب GetNumberFormat يتعارض مع وظيفة النظام Windows ، لذلك يتعين علينا إعادة تسميته.
#### **يعيد تسمية IStyleFlag :: GetNumberFormat إلى Get_NumberFormat**
نظرًا لأن اسم الأسلوب GetNumberFormat يتعارض مع وظيفة النظام Windows ، لذلك يتعين علينا إعادة تسميته وهو ما يمثل الحصول على إعداد تنسيق الرقم.
#### **يعيد تسمية IWorkbook :: CopyTheme إلى CopyITheme**
ينسخ النسق من مصنف آخر.
#### **يعيد تسمية IWorksheet :: SetBackground إلى SetBackgroundImage**
يضبط صورة خلفية ورقة العمل.
