---
title: Aspose.Cells for Java 20.8 ملاحظات الإصدار
type: docs
weight: 8
url: /ar/java/aspose-cells-for-java-20-8-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 20.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.8/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-43242|تم العثور على علامة نمط خارج علامة الرأس|خلل برمجي|
|CELLSJAVA-43157|لا يتم الاحتفاظ بلون سلسلة البيانات المخصصة عند إنشاء مخطط انحداري|خلل برمجي|
|CELLSJAVA-43240|فواصل الأسطر غير المقصودة في الأشكال / الكائنات عند تحويل Excel إلى PDF|خلل برمجي|
|CELLSJAVA-43255|مشكلة في الأداء في Excel لتحويل PDF|خلل برمجي|
|CELLSJAVA-43250|لا يتم دمج خلايا التسمية الموسعة في SmartMarker|خلل برمجي|
|CELLSJAVA-43253|يؤدي حفظ الملف باستخدام OoxmlSaveOptions بعد استبدال النص في SmartArt إلى تحويل XLS إلى XLSX|خلل برمجي|
CELLSJAVA-43170 | CellsException على طريقة calculateFormula | استثناء |

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

### **وضع علامة على واجهة ICustomFunction على أنها قديمة.**

 تسبب هذه الواجهة أحيانًا الغموض وسوء الفهم للمستخدمين. يجب على المستخدم استخدام**الخلاصةحساب المحرك** بدلاً من ذلك ، مما يوفر واجهات برمجة تطبيقات أكثر ملاءمة ومرونة لمعالجة الوظائف المخصصة.

### **وضع علامة CalculationOptions.CustomFunction على أنه خاصية قديمة.**

 الرجاء استخدام**الخلاصةحساب المحرك** بدلاً من**وظيفة ICustom** بواسطة CalculationOptions.CustomEngine property.

### **مصنف العلامات.**

 الرجاء استخدام**Workbook.CalculateFormula (خيارات الحساب)** بدلاً من.

### **وضع علامات على ورقة العمل .CalculateFormula (منطقي ، منطقي ، وظيفة ICustomFunction) عفا عليها الزمن.**

 الرجاء استخدام**Worksheet.CalculateFormula (CalculationOptions، Bool)** طريقة بدلا من ذلك.

### **علامات Cell.حسب (منطقي ، وظيفة ICustomFunction) على أنها قديمة.**

 الرجاء استخدام**Cell.حساب (خيارات الحساب)** طريقة بدلا من ذلك.

### **يضيف فئة DocxSaveOptions و SaveFormat.Docx enum**

يمثل الخيارات والتعداد لحفظ المصنف كملفات docx.

### **يضيف فئة PptxSaveOptions و SaveFormat.Pptx enum**

يمثل الخيارات والتعداد لحفظ المصنف كملفات .pptx.

### **إضافة فئة PowerQueryFormulaFunction**

يمثل وظيفة صيغة استعلام الطاقة.

### **يضيف SaveOptions.UpdateSmartArt ويحذف خاصية OoxmlSaveOptions.UpdateSmartArt**

يشير إلى ما إذا كان يتم تحديث نص الأشكال الفنية الذكية عند حفظ الملفات.

### **يضيف طريقة SlicerCollection.Add (جدول ListObject ، فهرس int ، سلسلة destCellName)**

إضافة Slicer جديد باستخدام ListObject كمصدر بيانات.

### **يضيف طريقة SlicerCollection.Add (جدول ListObject ، ListColumn listColumn ، سلسلة destCellName)**

إضافة Slicer جديد باستخدام ListObject كمصدر بيانات.

### **إضافة طريقة SlicerCollection.Add (جدول ListObject ، قائمة ListColumnColumn ، الصف int ، العمود int)**

إضافة Slicer جديد باستخدام ListObject كمصدر بيانات.
