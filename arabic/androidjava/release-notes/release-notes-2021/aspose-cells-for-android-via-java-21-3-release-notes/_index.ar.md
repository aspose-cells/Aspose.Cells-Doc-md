---
title: Aspose.Cells for Android via Java 21.3 ملاحظات الإصدار
type: docs
weight: 10
url: /ar/java/aspose-cells-for-android-via-java-21-3-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Android via Java 21.3.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43375|تحقق من كلمة مرور Excel VBA|
|CELLSJAVA-43400|دعم وظيفة UNIQUE ()|
|CELLSJAVA-42863|إحضار العنوان الفرعي للمخطط|
|CELLSJAVA-43401|دعم نتيجة التنسيق الموحدة للعصر الياباني لجميع JDKs|
|CELLSJAVA-43398|لا يتم تقديم التنسيق الشرطي بشكل صحيح في تحويل ODS إلى HTML|
|CELLSJAVA-43371|توقف تحويل XLSX إلى PDF|
|CELLSJAVA-43353|مخططات مختلفة على Excel لقوات الدفاع الشعبي|
|CELLSJAVA-43377|مشاكل وضع الصور أثناء تحويل Excel إلى Html|
|CELLSJAVA-43381|خطأ في حساب دالة DAYS|
|CELLSJAVA-43342|لا يمكن عرض مخطط التحرير والسرد بشكل صحيح في Excel إلى pdf|
|CELLSJAVA-43354|لم تظهر النسب المئوية في الرسوم البيانية الصغيرة|
|CELLSJAVA-40264|خطأ في عناصر تحكم النموذج أو عناصر تحكم ActiveX عند الحفظ كـ EXCEL_97_TO_2003|
|CELLSJAVA-43372|تم إنشاء ملف تالف أثناء تحويل ODS إلى XLSX|
|CELLSJAVA-43378|يتغير العرض على أنه فارغ من صواب إلى خطأ بعد استنساخ المصنف|
|CELLSJAVA-43382|ينتج عن النسخ مصنف تالف|
|CELLSJAVA-43364|مشكلة عند حفظ الرسم البياني الذي يحتوي على صورة في العلامة على الصورة|
|CELLSJAVA-43389|تفقد إعدادات حماية كلمة مرور المصنف / ورقة العمل عند الحفظ بتنسيق ملف XLSB|
|CELLSJAVA-43392|ينتج عن نسخ الورقة مصنف تالف|
|CELLSJAVA-43388|ملف الإخراج تالف بعد نسخ المصنف|
|CELLSJAVA-43406|مشاكل أثناء تحويل HTML إلى Excel|
|CELLSJAVA-43399|تنشئ CalculateFormula () الكثير من قيم نوع الخطأ #VALUE|
|CELLSJAVA-43362|مشكلة النسبة المئوية للملصقات عند طباعة المخططات|
|CELLSJAVA-43384|مشكلة النسب المئوية لبعض الملصقات عند التقديم إلى PDF وطباعة المخططات|
|CELLSJAVA-43402|قم بإنشاء صورة مخطط دقيقة من ملف Excel|
|CELLSJAVA-43408|يتم قطع الجزء العلوي من الرسم البياني ويرتفع الخط المائل|
|CELLSJAVA-43379|تم رفع الاستثناء أثناء حفظ المصنف بتنسيق HTML|
|CELLSJAVA-43376|استثناء "java.lang.ClassCastException: تجاوز في تحويل int إلى بايت. قيمة int: 144" عند تحميل ملف XLSX|
|CELLSJAVA-43387|يؤدي تصدير ورقة واحدة إلى HTML إلى زيادة الاستثناء|
|CELLSJAVA-43412|CellsException في تحويل xlsx إلى html|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على via Java for Android Aspose.Cells Aspose.Cells. في منتدى الدعم Aspose.Cells.

### **مُنشئ PdfSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ PdfSaveOptions () بدلاً من ذلك.

### **مُنشئ XlsbSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ XlsbSaveOptions () بدلاً من ذلك.

### **مُنشئ XlsSaveOptions (SaveFormat) قديم.**

استخدم مُنشئ XlsSaveOptions () بدلاً من ذلك.

### **مُنشئ SpreadsheetML2003SaveOptions (SaveFormat) المتقادم.**

استخدم مُنشئ SpreadsheetML2003SaveOptions () بدلاً من ذلك.

### **يضيف طريقة Chart.GetChartDataRange ().**

يحصل على مصدر نطاق البيانات للرسم البياني.

### **يضيف طريقة Chart.SwitchRowColumn ().**

يقوم بتبديل الصف / العمود لمصدر نطاق بيانات المخطط.

### **يضيف أسلوب OleObject.SetEmbeddedObject ().**

يضبط الكائن المضمّن.

### **يضيف طريقة VbaProject.ValidatePassword ().**

يتحقق من صحة كلمة مرور مشروع VBA.

### **حذف خصائص ChartPoint.MarkerBackgroundColor و Series.MarkerBackgroundColor القديمة ، وإضافة خاصية Marker.BackgroundColor.**

يستخدم Marker.BackgroundColor بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerForegroundColor و Series.MarkerForegroundColor القديمة ، وإضافة خاصية Marker.ForegroundColor.**

يستخدم Marker.ForegroundColor بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerBackgroundColorSetType و Series.MarkerBackgroundColorSetType القديمة ، وإضافة خاصية Marker.BackgroundColorSetType.**

يستخدم Marker.BackgroundColorSetType بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerForegroundColorSetType القديمة و Series.MarkerForegroundColorSetType ، وإضافة خاصية Marker.ForegroundColorSetType.**

يستخدم Marker.ForegroundColorSetType بدلاً من ذلك.

### **حذف خصائص ChartPoint.MarkerSize و Series.MarkerSize المتقادمة.**

يستخدم Marker.MarkerSize بدلاً من ذلك.

### **يحذف خصائص ChartPoint.MarkerStyle و Series.MarkerStyle القديمة.**

يستخدم Marker.MarkerStyle بدلاً من ذلك.

### **يغير سلوك Cells.DeleteBlankRows () / Cells.DeleteBlankRows (DeleteOptions)**

في الإصدارات القديمة ، نحذف جميع إعدادات الأعمدة أثناء حذف الصفوف الفارغة إذا كانت ورقة العمل فارغة (لا توجد بيانات للخلايا). هذا يجعل من المستحيل على المستخدم حذف الصفوف الفارغة فقط والاحتفاظ بجميع إعدادات الأعمدة. من 21.2 ، لم نعد نقوم بمسح إعدادات العمود. إذا احتاج المستخدم إلى حذف إعدادات العمود لورقة العمل الفارغة ، فعليه التحقق من عدم وجود بيانات في الورقة ثم مسح ColumnCollection يدويًا.
في الإصدارات القديمة ، لا نحذف الصفوف الفارغة تحت الشكل. هذا يجعل من المستحيل على المستخدم حذف جميع الصفوف الفارغة كما يتوقعون. من 12.2 ، نحذف تلك الصفوف الفارغة تحت الشكل مع الصفوف الفارغة الشائعة الأخرى.

### **خاصية Range.CellCount قديمة.**

الرجاء استخدام Range.RowCount و Range.ColumnCount للحصول على إجمالي عدد الخلايا بدلاً من ذلك.

### **يضيف خاصية AutoFilter.ShowFilterButton.**

يشير إلى ما إذا كان سيتم إظهار زر الفلتر الخاص بالفلتر التلقائي.

### **يحذف خاصية SeriesCollection.SecondCatergoryData.**

الرجاء استخدام الخاصية SeriesCollection.SecondCategoryData بدلاً من ذلك.

### **يحذف StyleModifyFlag. تعداد المسافات.**

لا تستخدم.

### **يضيف خاصية SignatureLine.Id.**

الحصول على أو تعيين معرف لسطر التوقيع هذا.

### **يضيف خاصية DigitalSignature.Id.**

يحدد UUID الذي يمكن الرجوع إليه باستخدام UUID الخاص بسطر التوقيع المخزن في محتوى المستند.

### **يضيف خاصية DigitalSignature.ProviderId.**

يحدد معرف فئة موفر التوقيع.

### **يضيف خاصية DigitalSignature.Image.**

يحدد صورة للتوقيع الرقمي.

### **يضيف خاصية DigitalSignature.Text.**

يحدد نص التوقيع الفعلي في التوقيع الرقمي.

### **يضيف Cells.ClearMergedCells () طريقة.**

يزيل كل الخلايا المدمجة.

### **يضيف طريقة Workbook.RemovePersonalInformation ().**

يزيل جميع المعلومات الشخصية.

### **إضافة خاصية WorkbookSettings.ForceFullCalculate.**

ترشد الخاصية ms excel إلى الحساب بالكامل في كل مرة يتم فيها تشغيل عملية حسابية.

### **يضيف مُنشئ DocxSaveOptions (منطقي).**

يمثل خيارات حفظ ملفات .docx.

### **يحذف خاصية WorkbookSettings.IsWriteProtected القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.IsWriteProtected بدلاً من ذلك.

### **يحذف WorkbookSettings القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.RecommendReadOnly بدلاً من ذلك.

### **يحذف WorkbookSettings.WriteProtectedPassword الخاصية القديمة.**

استخدم خاصية WorkbookSettings.WriteProtection.Password بدلاً من ذلك.
