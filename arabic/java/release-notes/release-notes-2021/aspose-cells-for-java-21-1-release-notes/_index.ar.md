---
title: Aspose.Cells for Java 21.1 ملاحظات الإصدار
type: docs
weight: 12
url: /ar/java/aspose-cells-for-java-21-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 21.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.1/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43375|تحقق من كلمة مرور Excel VBA|
|CELLSJAVA-43371|XLSX إلى PDF توقف التحويل|
|CELLSJAVA-43353|مخططات مختلفة على Excel لقوات الدفاع الشعبي|
|CELLSJAVA-43377|مشاكل وضع الصور أثناء تحويل Excel إلى Html|
|CELLSJAVA-43381|خطأ في حساب دالة DAYS|
|CELLSJAVA-43342|لا يمكن عرض مخطط التحرير والسرد بشكل صحيح في Excel إلى pdf|
|CELLSJAVA-43354|لم تظهر النسب المئوية في الرسوم البيانية الصغيرة|
|CELLSJAVA-40264|خطأ في عناصر تحكم النموذج أو عناصر تحكم ActiveX عند الحفظ كـ EXCEL_97_TO_2003|
|CELLSJAVA-43372|تم إنشاء ملف تالف أثناء تحويل ODS إلى XLSX|
|CELLSJAVA-43378|يتغير العرض على أنه فارغ من صواب إلى خطأ بعد استنساخ المصنف|
|CELLSJAVA-43379|تم رفع الاستثناء أثناء حفظ المصنف كـ HTML|
|CELLSJAVA-43376|استثناء "java.lang.ClassCastException: تجاوز في تحويل int إلى بايت. قيمة int: 144" عند تحميل ملف XLSX|

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

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
