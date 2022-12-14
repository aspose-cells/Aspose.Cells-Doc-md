---
title: Aspose.Cells for .NET 17.10 ملاحظات الإصدار
type: docs
weight: 30
url: /ar/net/aspose-cells-for-net-17-10-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for .NET 17.10](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.10/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSNET-45695|قم بتعيين تنسيق الأرقام للخلايا في جدول بيانات المخطط|ميزة جديدة|
|CELLSNET-45666|الحصول على حقل SheetId في ورقة عمل Excel|ميزة جديدة|
|CELLSNET-45664|قراءة وكتابة الاتصال الخارجي لملف XLSB|ميزة جديدة|
|CELLSNET-45660|عرض الورقة إلى الصورة - مشكلة المحاذاة للخطوط الآسيوية|التعزيز|
|CELLSNET-45408|تختفي القيمة أو يتغير لونها عند التحويل إلى PDF|حشرة|
|CELLSNET-45696|القطاعة لا تتحرك لأسفل في الورقة عند إدخال الصفوف|حشرة|
|CELLSNET-45675|خطأ في حساب الصيغ (التي تتضمن "SUMPRODUCT" و "TRANSPOSE")|حشرة|
|CELLSNET-45651|يتغير حجم TextBox عند استخدام الخط الصيني في المصنف في التقديم إلى PDF|حشرة|
|CELLSNET-45678|الأحرف المفقودة جزئيًا عند التحويل إلى صورة|حشرة|
|CELLSNET-45667|لا يتم تحديث تسميات خط الاتجاه في MS Excel عندما نغير قيمة المصدر يدويًا في الخلايا|حشرة|
|CELLSNET-45620|يختلف اللون والفاصل الزمني بين المقياس للمخطط ثلاثي الأبعاد|حشرة|
|CELLSNET-45397|يتعرف Aspose.Cells على الخطوط في المخطط بشكل غير صحيح|حشرة|
|CELLSNET-45700|تمت إزالة جزء الوظيفة الإضافية لبرنامج MS Excel 2016 من الملف بعد فتحه / حفظه بواسطة Aspose.Cells|حشرة|
|CELLSNET-45693|لم تعد ورقة العمل محمية في ملف الإخراج في تحويل SpreadsheetML إلى XLSX|حشرة|
|CELLSNET-45691|المستند تالف عند إعادة حفظه|حشرة|
|CELLSNET-45690|يبدو أن الأنماط يتم نقلها بشكل خاطئ لبعض الخلايا - تحويل SpreadsheetML إلى XLSX|حشرة|
|CELLSNET-45688|لم يتم فرز عمود التاريخ بشكل صحيح|حشرة|
|CELLSNET-45687|لا يتم نقل خصائص حماية أوراق العمل من SpreadsheetML|حشرة|
|CELLSNET-45683|لا يعمل عنصر SpreadsheetML AllowSort في إخراج XLSX|حشرة|
|CELLSNET-45682|يطالبك MS Excel برسالة خطأ "عثر Excel على محتوى غير قابل للقراءة ...."|حشرة|
|CELLSNET-45676|المستند تالف عند إعادة الحفظ بسبب عدم وجود مساحة في اسم ورقة العمل|حشرة|
|CELLSNET-45673|يتم تطبيق نمط المحاذاة على SpredsheetML|حشرة|
|CELLSNET-45670|Cells يتم فقد اللون عند التحويل إلى صورة|حشرة|
|CELLSNET-45692|لا يقوم GridWeb بفك تجميع الصفوف عند النقر فوق الزر "+"|حشرة|
|CELLSNET-45654|لا يتم استرداد التعليق المضاف إلى الخلية من جانب العميل - Aspose.Cells.GridWeb|حشرة|
|CELLSNET-45645|يحدث الاستثناء عند فتح BUDGET RH 3_0.xlsm في GridWeb|حشرة|
|CELLSNET-45657|لم تكن سلسلة الإدخال بتنسيق صحيح - استثناء في أسلوب Pivot.CalculateData ()|استثناء|
|CELLSNET-45703|استثناء عند تحويل ملف XLSM مرة أخرى إلى تنسيق ملف XLS|استثناء|
### **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for .NET. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
#### **يضيف طريقة AbstractCalculationMonitor.Interrupt (سلسلة)**
يسمح للمستخدمين بمقاطعة تقدم حسابات الصيغة.
#### **يضيف HtmlCrossType.MSExport التعداد**
تعرض السلسلة مثل تصدير MS Excel بتنسيق HTML.
#### **يضيف خاصية Worksheet.TabId**
يحصل على المعرف الداخلي للورقة.
#### **يضيف تعداد OLEDBCommandType**
نوع الأمر غير محدد.
#### **يضيف تعداد ConnectionDataSourceType**
يمثل نوع مصدر البيانات للاتصال.
#### **تقادم ExternalConnection.Credentials and ExternalConnection.ReConnectionMethod property**
استخدم خاصية ExternalConnection.CredentialsMethodType و ExternalConnection.ReconnectionMethodType بدلاً من ذلك.
#### **حذف خاصية WebQueryConnection.EditPage القديمة**
استخدم خاصية WebQueryConnection.EditWebPage بدلاً من ذلك.
#### **إضافة خاصية Seris.ValuesFormatCode**
يمثل رمز تنسيق الرقم لقيم السلسلة.
#### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [قم بتعيين رمز تنسيق القيم لسلسلة التخطيطات](/cells/ar/net/set-the-values-format-code-of-chart-series/)
- [استخدم خاصية Sheet.SheetId الخاصة بـ OpenXml باستخدام Aspose.Cells](/cells/ar/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [قراءة وكتابة الاتصال الخارجي لملف XLSB](/cells/ar/net/read-and-write-external-connection-of-xls-and-xlsb-files/)
- [مقاطعة أو إلغاء حساب صيغة المصنف](/cells/ar/net/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [حدد كيفية عبور السلسلة في إخراج HTML باستخدام HtmlCrossType](/cells/ar/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
