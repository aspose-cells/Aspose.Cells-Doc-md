---
title: Aspose.Cells for Java 9.0.0 ملاحظات الإصدار
type: docs
weight: 40
url: /ar/java/aspose-cells-for-java-9-0-0-release-notes/
---
## **1) Aspose.Cells**

|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-41947 | القدرة على اكتشاف ما إذا كانت DataPoint موجودة في Pie أو Bar|ميزة جديدة|
|CELLSJAVA-41827 | يستغرق جدول البيانات أكثر من 3 دقائق لحساب الصيغ عند استخدام طريقة Workbook.calculateFormula ()| التعزيز|
|CELLSJAVA-41969 | التظليل Cell مفقود أثناء تحويل تنسيق ملف HTML إلى تنسيق ملف XLSX| حشرة|
|CELLSJAVA-41955 | يظهر المصنف إلى HTML "#" في الخلايا| حشرة|
|CELLSJAVA-41942 |الحدود المفقودة وتظليل الخلية والصور - عرض HTML إلى Excel| حشرة|
|CELLSJAVA-41967 | يكون Cells مفقودًا في PDF عند تحديد مناطق طباعة متعددة في ورقة واحدة| حشرة|
|CELLSJAVA-41958 | يتم اقتطاع وسيلة إيضاح الجانب الأيمن في صورة المخطط| حشرة|
|CELLSJAVA-41953 | وضع النص في غير مكانه في الرسم التخطيطي بعد تحويله إلى تنسيق HTML| حشرة|
|CELLSJAVA-41948 | تم تغيير الرسم البياني أثناء تحويل جدول البيانات إلى HTML| حشرة|
|CELLSJAVA-41981 | الموضع غير الصحيح للخط العمودي في ملف PDF للمخطط| حشرة|
|CELLSJAVA-41964 | لا يعتبر Autoofit مستوى المسافة البادئة| حشرة|
|CELLSJAVA-40260 | تغيير نص WordArt موجود في ملف Excel| حشرة|
|CELLSJAVA-41971 | Cell.getValiationValue () يطرح NullPointerException لنوع التحقق المخصص| استثناء|
|CELLSJAVA-41963 | يحدث استثناء غير قانوني لحجم المفتاح أثناء فتح المصدر a5.xlsx| استثناء|
|CELLSJAVA-41962 | يحدث استثناء ArrayIndexOutOfBoundsException أثناء فتح المصدر a4.xls| استثناء|
|CELLSJAVA-41961 | تحدث سلسلة غير صالحة في ملف الاستثناء أثناء فتح المصدر a3.xls| استثناء|
|CELLSJAVA-41960 | يحدث استثناء NegativeArraySizeException أثناء فتح المصدر a2.xls| استثناء|
|CELLSJAVA-41959 | يحدث استثناء NullPointerException أثناء فتح المصدر a1.xlsx| استثناء|
## **2) مجموعة الشبكة Aspose.Cells**

|**مفتاح** |**ملخص** |**فئة** |
|:- |:- |:- |
|CELLSJAVA-41965 |احصل على الإصدار مثل CELLSNET-44565 و CELLSNET-44676 المطلوب أيضًا لـ GridWeb (Java)| التعزيز|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف خاصية Shape.TextOptions**
يمثل خيارات النص للشكل.
### **ورقة عمل عفا عليها الزمن. طريقة SetBackground**
الرجاء استخدام الخاصية Worksheet.BackgroundImage بدلاً من ذلك.
### **عفا عليها الزمن LineShape.Begin ArrowheadStyle و ArcShape.BeginArrowheadStyle**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadStyle بدلاً من ذلك.
### **Obsoletes LineShape.Begin ArrowheadWidth and ArcShape.BeginArrowheadWidth**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadWidth بدلاً من ذلك.
### **تقادم LineShape.Begin ArrowheadLength و ArcShape.Begin ArrowheadLength**
الرجاء استخدام خاصية Shape.Line.BeginArrowheadLength بدلاً من ذلك.
### **عفا عليها الزمن LineShape.EndArrowheadStyle و ArcShape.EndArrowheadStyle**
الرجاء استخدام خاصية Shape.Line.EndArrowheadStyle بدلاً من ذلك.
### **Obsoletes LineShape.EndArrowheadWidth and ArcShape.EndArrowheadWidth**
الرجاء استخدام خاصية Shape.Line.EndArrowheadWidth بدلاً من ذلك.
### **تقادم الخط الشكل.السهم النهائيالطول وشكل القوس.النهايةالسهمالطول**
الرجاء استخدام خاصية Shape.Line.EndArrowheadLength بدلاً من ذلك.
### **يحذف طريقة Worksheet.CopyConditionalFormatting () القديمة**
### **يحذف Workbook.CheckWriteProtectedPassword () طريقة قديمة**
الرجاء استخدام طريقة WorkbookSettings.WriteProtection.ValidatePassword بدلاً من ذلك.
### **إعادة تسمية المصنف .RemoveDigitallySign as Workbook.RemoveDigitalSignature method**
تمت إعادة تسمية طريقة Workbook.RemoveDigitallySign إلى Workbook.RemoveDigitalSignature.
### **يضيف خاصية ChartSplitType.Auto**
يجب أن يتم تقسيم يمثل نقاط البيانات باستخدام الآلية الافتراضية لهذا النوع من الرسم البياني.
### **إضافة خاصية ChartPoint.IsInSecondaryPlot**
الحصول على قيمة أو تعيينها يشير إلى ما إذا كانت نقاط البيانات هذه موجودة في المخطط الدائري الثاني أو الشريط على دائري من المخطط الدائري أو شريط مخطط دائري.
### **إضافة خاصية OleObject.ClassIdentifier**
الحصول على أو تحديد معرف فئة الكائن المضمن.
