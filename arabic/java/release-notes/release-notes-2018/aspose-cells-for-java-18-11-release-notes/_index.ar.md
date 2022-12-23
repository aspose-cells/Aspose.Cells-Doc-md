---
title: Aspose.Cells for Java 18.11 ملاحظات الإصدار
type: docs
weight: 20
url: /ar/java/aspose-cells-for-java-18-11-release-notes/
---
{{% alert color="primary" %}} 

تحتوي هذه الصفحة على ملاحظات إصدار Aspose.Cells for Java 18.11.

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-42738|تمت قراءة العد الخاطئ لقيم التحقق من الصحة من XLSX|التعزيز|
|CELLSJAVA-42734|مشكلة أثناء التعامل مع المحددات المتتالية على أنها مميزة|التعزيز|
|CELLSJAVA-42739|Aspose.Cells.GridWeb (Java) يتعطل عند استخدامه في نفس الوقت في بيئة متعددة المستخدمين|خلل برمجي|
|CELLSJAVA-42737|خط الرسم البياني مفقود في XLSX-> PNG التحويل|خلل برمجي|
|CELLSJAVA-42735|مشكلة في طريقة getActualChartSize|خلل برمجي|
|CELLSJAVA-40861|لا يتم نسخ SmartArt عند نسخ المصنف|خلل برمجي|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة خاصية PivotTable.RefreshedByWho**
الحصول على اسم المستخدم الذي قام بتحديث PivotTable آخر مرة.
### **إضافة خاصية PivotTable.RefreshDate**
الحصول على التاريخ الذي تم فيه تحديث PivotTable آخر مرة.
### **يضيف خصائص CalculationData.CellRow / CellColumn**
يوفر طريقة فعالة للمستخدم للحصول على فهارس صفوف وأعمدة الخلية بدلاً من جلب كائن Cell.
### **يضيف فئة CalculationCell**
يمثل بيانات الحساب حول خلية واحدة يتم حسابها.
### **يضيف طريقة AbstractCalculationMonitor.OnCircular (IEnumerator circularCellsData)**
يوفر طريقة للمستخدم لجمع ومعالجة المراجع الدائرية.
### **إضافة خاصية TxtLoadOptions.TreatConsecutiveDelimitersAsOne**
يسمح للمستخدم باختيار ما إذا كان يجب اعتبار المحددات المتتالية كواحد عند استيراد ملف CSV.
### **يضيف FormatCondition.SetFormulas (صيغة سلسلة 1 ، صيغة سلسلة 2 ، منطقي هو R1C1 ، طريقة منطقية isLocal)**
يوفر طريقة فعالة وملائمة للمستخدم لتعيين الصيغ لـ FormatCondition.
### **يضيف طريقة Validation.GetListValue (صف int ، عمود int)**
يسمح للمستخدم بالحصول على القيمة لإنتاج قائمة للتحقق من صحة خلية معينة.
### **Obsoletes ValidationCollection.Add (التحقق من الصحة)**
استخدم طريقة ValidationCollection.Add (CellArea) بدلاً من ذلك.
### **يضيف Validation.Copy (Aspose.Cells.Validation ، Aspose.Cells.CopyOptions) طريقة**
التحقق من النسخ.
### **يضيف خصائص CreatedUniversalTime و LastPrintedUniversalTime و LastSavedUniversalTime لمجموع BuiltInDocumentPropertyCollection**
إرجاع وقت UTC حول الخصائص المضمنة.
### **يضيف خاصية OoxmlSaveOptions.UpdateSmartArt**
يشير إلى ما إذا كان يتم تحديث الفن الذكي.
### **يضيف فئة SmartArtShape**
يمثل الشكل الفني الذكي.
