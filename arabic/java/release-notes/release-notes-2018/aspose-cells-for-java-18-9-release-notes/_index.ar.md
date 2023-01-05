---
title: Aspose.Cells for Java 18.9 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-18-9-release-notes/
---
{{% alert color="primary" %}}

تحتوي هذه الصفحة على ملاحظات إصدار for Java Aspose.Cells 18.9.

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42715|لا يتم استرداد الصيغ كما هو الحال في ملف MS Excel|خلل برمجي|
|CELLSJAVA-42711|لا يتم إنشاء المخطط في PDF من قالب Excel|خلل برمجي|
|CELLSJAVA-42710|نص عنصر وسيلة الإيضاح مكرر في المخطط في Excel لتحويل PDF|خلل برمجي|
|CELLSJAVA-42706|PDF الإخراج لا يعرض تسمية المخطط|خلل برمجي|
|CELLSJAVA-42700|لم يتم عرض المخطط الانحداري بشكل صحيح بعد تغيير بيانات المخطط|خلل برمجي|
|CELLSJAVA-42717|Cells.deleteRow يعمل بشكل غير صحيح|خلل برمجي|
|CELLSJAVA-42716|تم استرداد قيمة خاطئة لنمط الحد|خلل برمجي|
|CELLSJAVA-42709|تم إرجاع نمط حد سفلي خاطئ للخلية المدمجة|خلل برمجي|
|CELLSJAVA-42705|يثير MS Excel خطأ أثناء تحميل الملف بعد ضبط التصفية التلقائية|خلل برمجي|
|CELLSJAVA-42703|لم يتم تقديم المخطط أثناء التحويل ODS إلى PDF|خلل برمجي|
|CELLSJAVA-42702|تظهر الحدود الرمادية بعد قراءة نمط الخلية في ورقة العمل|خلل برمجي|
|CELLSJAVA-42699|PasteType. القيم_و_NUMBER_FORMATS لا تعمل بشكل جيد|خلل برمجي|
|CELLSJAVA-42646|استثناء: "FormulaBuild Unknown الصيغة token0" في Name.getRefersTo ()|استثناء|
|CELLSJAVA-42707|يتسبب أسلوب Chart.calculate في حدوث OutOfMemoryError|استثناء|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **إضافة أساليب CellsHelper.CreateSafeSheetName (اسم سلسلة Proposal) / CreateSafeSheetName (اسم السلسلة Proposal ، char replaceChar)**

طرق لراحة المستخدم لإنشاء اسم ورقة صالح.

### **يضيف Row.FirstDataCell**

الحصول على أول خلية غير فارغة في الصف.

### **إضافة تعداد MapChartLabelLayout**

يمثل نوع تخطيط التسمية لمخطط الخريطة.

### **يضيف تعداد MapChartProjectType**

يمثل نوع الإسقاط لمخطط الخريطة.

### **إضافة تعداد MapChartRegionType**

يمثل نوع المنطقة في مخطط الخريطة.

### **إضافة تعداد QuartileCalculationType**

يمثل نوع الحساب الربعي للمخطط.

### **يضيف خاصية Series.LayoutProperties وفئة SeriesLayoutProperties**

يمثل خصائص تخطيط السلسلة.

### **يضيف خاصية TickLabels.SAutomaticRotation**

يشير إلى ما إذا كان تدوير تسميات التجزئة تلقائيًا.

### **يضيف FilterOperatorType.BeginsWith ، ويحتوي على ، وينتهي ، ولا يحتوي على التعداد**

يمثل نوع عامل تصفية النص.

### **يضيف Cell.GetDisplayStyle (bool) method**

يحصل على نمط عرض الخلية.

### **يضيف أسلوب GlobalizationSettings.GetStandardHeaderFooterFontStyleName (سلسلة localFontStyleName)**

الحصول على اسم نمط الخط الإنجليزي القياسي (عادي ، غامق ، مائل) للرأس / التذييل وفقًا لاسم نمط الخط المحلي المحدد.

### **يضيف تعداد PdfCustomPropertiesExport**

يحدد طريقة تصدير CustomDocumentPropertyCollection إلى ملف PDF.

### **يضيف خاصية PdfSaveOptions.CustomPropertiesExport**

الحصول على أو تحديد قيمة تحدد طريقة تصدير CustomDocumentPropertyCollection إلى ملف PDF. القيمة الافتراضية هي بلا.

### **يضيف فئة XmlDataBinding**

يمثل معلومات ربط بيانات Xml.

### **إضافة خاصية ListObject.XmlMap**

يحصل على خريطة XmlMap المستخدمة لهذه القائمة.

### **إضافة خاصية XmlDataBinding.Url**

يحصل على عنوان url لمصدر ربط البيانات هذا.

### **إضافة خاصية XmlMap.DataBinding**

يحصل على XmlDataBinding لهذه الخريطة.
