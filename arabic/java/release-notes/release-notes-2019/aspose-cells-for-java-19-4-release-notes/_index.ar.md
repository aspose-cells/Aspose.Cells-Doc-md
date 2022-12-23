---
title: Aspose.Cells for Java 19.4 ملاحظات الإصدار
type: docs
weight: 90
url: /ar/java/aspose-cells-for-java-19-4-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 19.4.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42838|تعطيل خاصية العرض التلقائي لجزء المهام.|ميزة جديدة|
|CELLSJAVA-42853|مشكلة في الأداء أثناء تحويل XLSX إلى HTML|التعزيز|
|CELLSJAVA-42852|لا يتم عرض التسمية الموجودة على كلا المحورين|خلل برمجي|
|CELLSJAVA-42856|Excel إلى HTML مشكلة التحويل|خلل برمجي|
|CELLSJAVA-42872|صورة الورقة ، الأسطر اليمنى والسفلى مفقودة|خلل برمجي|
|CELLSJAVA-42873|تحتوي الورقة المشروطة مسبقًا على العديد من خلفيات الخلايا والنصوص المفقودة وهي مخفية.|خلل برمجي|
|CELLSJAVA-42874|فقد العمود عند تصدير الملف إلى HTML|خلل برمجي|
|CELLSJAVA-42875|العرض خاطئ والشاشة خارج الشكل|خلل برمجي|
|CELLSJAVA-42878|نتيجة حساب الصيغ غير صحيحة|خلل برمجي|
|CELLSJAVA-40419|لا يمكن إنشاء PDF بعلامات أثناء التصدير من Excel إلى PDF|خلل برمجي|
|CELLSJAVA-40570|التحويل الخاطئ إلى PDF و JPG للصفحات ذات الأحجام المختلفة|خلل برمجي|
|CELLSJAVA-42833|حدثت مشكلة أثناء تضمين نفس الملف PDF في أوراق متعددة في مصنف|خلل برمجي|
|CELLSJAVA-42858|مشكلة عند إضافة صورة إلى خلايا مدمجة باستخدام علامات ذكية مع صورة: خيار FitToCell|خلل برمجي|
|CELLSJAVA-42862|تمت إعادة تسمية اسم الورقة في الصيغ بعد استيراد CSV|خلل برمجي|
|CELLSJAVA-42865|وقت غير صحيح للقراءة من خلية في ملف ODS|خلل برمجي|
|CELLSJAVA-42879|تلف ملف Excel بعد الحفظ بواسطة Aspose.Cells|خلل برمجي|
|CELLSJAVA-42860|java.lang.NullPointerException عند تحميل تنسيق ملف ODS|استثناء|
|CELLSJAVA-42871|java.lang.Exception: استنساخ غير مدعوم للتيار المدعوم أثناء التحويل XLSX إلى PDF|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف واجهات برمجة التطبيقات لحفظ مستند Markdown: SaveFormat.Markdown ، FileFormatType.Markdown ، MarkdownSaveOptions**
يدعم حفظ محتوى الخلايا كجدول تخفيض السعر. باستخدام طريقة Workbook.Save () ، سيتم تصدير جميع محتويات الخلية في الورقة النشطة كجدول في مستند العلامات.
### **يزيل الخصائص القديمة لـ TxtLoadOptions**
الرجاء استخدام خاصية LoadStyleStrategy بدلاً من KeepExactFormat.
### **يزيل LoadDataOption فئة قديمة**
الرجاء استخدام فئة LoadFilter وخاصية LoadOptions.LoadFilter بدلاً من ذلك.
### **يزيل الخصائص القديمة لخيارات LoadOptions**
LoadOptions.ConvertNumericData: الرجاء استخدام هذه الخاصية مع الفئة الفرعية المقابلة من LoadOptions ، مثل TxtLoadOptions.
LoadOptions.LoadDataOptions: الرجاء استخدام خاصية LoadOptions.LoadFilter مع التنفيذ المخصص لـ LoadFilter.
LoadOptions.LoadDataFilterOptions: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions بدلاً من ذلك.
LoadOptions.OnlyLoadDocumentProperties: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions = LoadDataFilterOptions.DocumentProperties.
LoadOptions.LoadDataAndFormatting / LoadDataOnly: الرجاء استخدام LoadOptions.LoadFilter.LoadDataFilterOptions = LoadDataFilterOptions.CellData | LoadDataFilterOptions.DefinedNames.
### **يضيف خاصية PdfSaveOptions.ExportDocumentStructure**
الحصول على أو تحديد قيمة تحدد ما إذا كان سيتم تصدير بنية المستند أم لا.
### **إضافة فئات من مساحة الاسم Aspose.Cells.WebExtensions**
يمثل WebExtensions و WebExtensionTasks.
### **إضافة خصائص WorksheetCollection.WebExtensions و WorksheetCollection.WebExtensionTaskPanes.**
يمثل جميع WebExtensions و WebExtensionTasks.
### **يضيف فئة WebExtensionShape.**
يمثل شكل WebExtension.
### **يضيف Cells.InsertCutCells () طريقة.**
إدراج قطع الخلايا.
### **يضيف Cells.SetViewColumnWidthPixel.**
يضبط عرض عرض العمود.
### **يضيف فئات ThreadedCommentCollection و ThreadedComment.**
يمثل التعليق المترابط.
### **يضيف الخاصية WorksheetCollection.ThreadedCommentAuthors.**
يحصل على وتعيين مؤلفي التعليقات المترابطة.
### **يضيف تعليقًا.**
يمثل التعليقات المترابطة على التعليق.
### **يضيف أساليب CommentCollection.AddThreadedComment () و CommentCollection.GetThreadedComments ().**
يضيف ويحصل على التعليقات المترابطة.
### **يضيف خاصية Chart.SubTitle.**
الحصول على العنوان الفرعي للرسم البياني. فقط لملف تنسيق ODS.
