---
title: Aspose.Cells for Java 8.4.1 ملاحظات الإصدار
type: docs
weight: 70
url: /ar/java/aspose-cells-for-java-8-4-1-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 8.4.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.1/)

{{% /alert %}}

فيما يلي قائمة بالتحسينات والتغييرات في هذا الإصدار من Aspose.Cells

## Aspose.Cells

### **الميزات الرئيسية**

تم نقل قاعدة الكود الرئيسية إلى Java 6 (Java 7 و 8 مدعومة أيضًا). تم إسقاط الدعم for Java 5 و 1.4.

### **تحسينات وتغييرات أخرى**

### **ميزات جديدة**

(CELLSJAVA-41235) - دعم RenderToSize API لصورة ورقة العمل

(CELLSJAVA-41234) - دعم الرموز النقطية أثناء استخدام SmartMarkers أو طريقة Cell.setHtmlString

### **البق**

(CELLSJAVA-41229) - Aspose.Cells لا يقوم بإنشاء ملف HTMs و CSS فردي للأوراق في Excel لتحويل HTML

(CELLSJAVA-41170) - يعرض SheetRender.toImage الصورة مع تسميات "(فارغة)" على المحور x للمخطط

(CELLSJAVA-41270) - مشكلة مع Cells.insertRange () حيث لا يتم إزاحة المنطقة المدمجة بشكل جيد

(CELLSJAVA-41240) - يتم اقتطاع النص الموجود بخط Arial من الأعلى أثناء تحويل جدول البيانات إلى PDF

(CELLSJAVA-41238) - ورق_أ_2 لا يعمل كما هو متوقع عند الحفظ كـ PDF

(CELLSJAVA-41217) - عندما تحتوي بيانات فئة السلسلة على فاصلة ، لا تظهر وسيلة إيضاح الرسم البياني PIE بشكل صحيح

(CELLSJAVA-41194) - تداخل إدخالات وسيلة الإيضاح أثناء تحويل المخطط إلى صورة

(CELLSJAVA-41002) - الخط المنقط مفقود في الرسم البياني 1

(CELLSJAVA-40993) - خطوط الشبكة الأفقية مفقودة في مخطط النمو

(CELLSJAVA-41259) - يؤدي تعيين Name.setRefersTo وإعادة حساب الصيغ إلى قيمة غير صحيحة أثناء تحويل جدول البيانات إلى HTML

(CELLSJAVA-41258) - تحميل وحفظ XLSX مع Aspose.Cells يجعل جدول البيانات الناتج تالفًا

(CELLSJAVA-41255) - يتحول الزر المخصص إلى صورة ويختفي التسمية التوضيحية في الإخراج XLSX

(CELLSJAVA-41254) - Microsoft يتعطل Excel عند فتح ملف الإخراج XLSX

(CELLSJAVA-41253) - تختفي القائمة المنسدلة في ملف الإخراج XLSX

### **استثناءات**

(CELLSJAVA-41266) - حدث java.lang.NumberFormatException عند فتح ملف القالب XLSX

(CELLSJAVA-41248) - استثناء مؤشر فارغ عند فتح ملف XLSX المصدر

(CELLSJAVA-41265) - استثناء: "java.lang.NullPointerException" عند فتح ملف SpreadsheetML

(CELLSJAVA-41264) - استثناء أثناء استخدام Cell.getStringValueWithoutFormat

(CELLSJAVA-41246) - استثناء: صيغة ديناميكية غير صالحة ... تتضمن وظيفة الفهرس أثناء استخدام الصيغ الديناميكية للعلامات الذكية

## Aspose.Cells مجموعة الشبكة

### **تحسينات وتغييرات أخرى**

### **التحسينات**

(CELLSJAVA-41213) - Gridweb: تعيين حدود مختلفة من خلال عملية الويب

### **البق**

(CELLSJAVA-41261) - تم تغيير الأحرف متعددة البايت في قائمة التحقق من صحة البيانات إلى "؟؟" عند تحديده في FireFox

(CELLSJAVA-41260) - لا يمكن إظهار أو تحديد أو زيادة ارتفاع الصف المخفي في GridWeb

(CELLSJAVA-41257) - التنقل خاطئ عند الانتقال من الخلية C1 -> C3 باستخدام مفاتيح الأسهم

(CELLSJAVA-41256) - لا يمكن استخدام بعض قواعد التنسيق الشرطي أو استخدامها جزئيًا في ملف القالب عند استيرادها إلى GridWeb

## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

يضيف خاصية مصنف.

يشير إلى ما إذا تم تعيين الترخيص.

Obsoletes Workbook.ValidateFormula.

الرجاء استخدام خاصية Cell.Formula بدلاً من ذلك.

إضافة خاصية ImageOrPrintOptions.SVGFitToViewPort.

الإشارة إلى ما إذا كانت الصورة SVG التي تم إنشاؤها مناسبة لعرض المنفذ.

يضيف طريقة ImageOrPrintOptions.SetDesiredSize.

يضبط العرض والارتفاع المطلوبين للصورة.

يضيف Aspose.Cells.GridDesktop.WorksheetCollection.MoveTo

ينقل ورقة العمل في الفهرس المحدد إلى فهرس آخر.

**ملحوظة**

نظرًا لأن قاعدة الكود Aspose.Cells for Java تطابق رمز إصدار .NET ذي الصلة ، فإن معظم التغييرات والتحسينات والإصلاحات المضمنة في Aspose.Cells for .NET v8.4.1 مدرجة أيضًا في Aspose.Cells for Java v8.4.1.
