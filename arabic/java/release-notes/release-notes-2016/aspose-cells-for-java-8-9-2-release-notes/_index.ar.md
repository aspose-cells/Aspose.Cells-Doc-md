---
title: Aspose.Cells for Java 8.9.2 ملاحظات الإصدار
type: docs
weight: 50
url: /ar/java/aspose-cells-for-java-8-9-2-release-notes/
---
## **1) Aspose.Cells**

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41925|زاد وقت الحساب مع مراجعات API الأخيرة|ميزة جديدة|
|CELLSJAVA-40958|مطلوب آلية استبدال الخطوط القابلة للتكوين من قبل المستخدم|ميزة جديدة|
|CELLSJAVA-41936|لا تنتهي طريقة Workbook.calculateFormula () مطلقًا لملف Excel المصدر|التعزيز|
|CELLSJAVA-41928|تعذر التقاط مصدر الصورة أثناء تقديم جدول البيانات إلى HTML باستخدام IStreamProvider|خلل برمجي|
|CELLSJAVA-41841|مشكلة في تحويل CheckBoxes إلى HTML|خلل برمجي|
|CELLSJAVA-41932|مشكلة في getDisplayStringValue () لقيم تنسيق التاريخ|خلل برمجي|
|CELLSJAVA-41930|باستخدام Light Cells APIs لمعالجة ملف XLS ، تتم دائمًا معالجة الخلية الأولى من الورقة الأولى|خلل برمجي|
|CELLSJAVA-41931|تباعد الحروف وفصلها غير صحيحين للنص الرأسي أثناء تحويل جدول البيانات إلى PDF|خلل برمجي|
|CELLSJAVA-41709|يختلف عرض العمود في CentOS عنه في Windows|خلل برمجي|
|CELLSJAVA-41933|تم إزاحة مقياس الرسم البياني أثناء تقديم جدول البيانات إلى PDF|خلل برمجي|
|CELLSJAVA-41934|مشكلة المحاذاة عند تقديم ملف Excel إلى PDF|خلل برمجي|
|CELLSJAVA-41935|تم تعطيل تنسيق إدخالات وسيلة الإيضاح أثناء تقديم جدول البيانات إلى PDF|خلل برمجي|
|CELLSJAVA-41943|لم يتم تقديم تسميات المحور الأفقي بالكامل ، أي ؛ تفتقد جميع التصنيفات إلى بعض المحتويات في الصورة المعروضة.|خلل برمجي|
|CELLSJAVA-41940|الملف تالف بعد حساب الصيغة وحفظها|خلل برمجي|
|CELLSJAVA-41952|نتيجة الحساب غير صحيحة|خلل برمجي|
|CELLSJAVA-41941|لم يتم حساب صيغة المصفوفة بشكل صحيح|خلل برمجي|
|CELLSJAVA-41937|بعض القيم من ملف Excel مفقودة في التحويل HTML-XLS إلى HTML|خلل برمجي|
|CELLSJAVA-41927|استثناء: "java.lang.OutOfMemoryError" أثناء الحفظ بتنسيق ملف HTML|استثناء|
|CELLSJAVA-41945|CellsException: خطأ في حساب Cell [0Sheet1! E5] في Workbook.CalculateFormula أثناء حساب دالة TREND|استثناء|
|CELLSJAVA-41946|يؤدي فتح ملف Excel إلى java.lang.NumberFormatException: لسلسلة الإدخال: "80000020"|استثناء|
|CELLSJAVA-41922|IndexOutOfBoundsException أثناء نسخ الخلايا|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **إضافة خاصية CopyOptions.ReferToDestinationSheet و Cells.CopyRows (Cells sourceCells ، int sourceRowIndex ، int destinationRowIndex ، int rowNumber ، CopyOptions copyOptions)**
يحدد ما إذا كان سيتم الإشارة إلى ورقة العمل الوجهة (كمصدر بيانات للمخطط) أثناء نسخ الصفوف / النطاق.
عند نسخ النطاق والمخطط يشير إلى الورقة المصدر ، فإن خطأ يعني أن مصدر بيانات المخطط المنسوخ لن يتغير. صحيح يعني أن مصدر بيانات المخطط المنسوخ يشير إلى الورقة الوجهة.
### **إضافة خاصية HtmlSaveOptions.FilePathProvider**
الحصول على IFilePathProvider أو تعيينه لتصدير ورقة العمل إلى html بشكل منفصل.
### **يضيف واجهة IFilePathProvider**
يمثل موفر مسار الملف الذي تم تصديره.
### **يضيف فئة FontConfigs**
يحدد إعدادات الخط.
### **يضيف فئة FontSourceBase**
هذه فئة أساسية مجردة للفئات التي تسمح للمستخدم بتحديد مصادر الخطوط المختلفة.
### **يضيف فئة FileFontSource**
يمثل ملف خط تروتايب الفردي المخزن في نظام الملفات.
### **يضيف فئة FolderFontSource**
يمثل المجلد الذي يحتوي على ملفات خطوط تروتايب.
### **يضيف فئة MemoryFontSource**
يمثل ملف خط تروتايب الفردي المخزن في الذاكرة.
### **يضيف تعداد FontSourceType**
يحدد نوع مصدر الخط.
### **يضيف CalculationOptions.Recursive property**
يحدد ما إذا كان سيتم حساب الخلايا التابعة بشكل متكرر عند حساب خلية واحدة ويعتمد ذلك على الخلايا الأخرى.
### **خاصية Obsoletes CellsHelper.FontDir**
استخدم طريقة FontConfigs.SetFontFolder (سلسلة ، منطقية) مع المجلد العودي إلى false بدلاً من ذلك.
### **خاصية Obsoletes CellsHelper.FontDirs**
استخدم أسلوب FontConfigs.SetFontFolders (سلسلة [] ، منطقي) مع مجلد متكرر إلى خطأ بدلاً من ذلك.
### **خاصية Obsoletes CellsHelper.FontFiles**
استخدم FontConfigs.SetFontSources (FontSourceBase []) بدلاً من ذلك.
### **Obsoletes Shape.LineFormat ويضيف خاصية Shape.Line**
الرجاء استخدام خاصية Shape.Line بدلاً من ذلك.
### **Obsoletes Shape.FillFormat ويضيف خاصية Shape.Fill**
الرجاء استخدام خاصية Shape.Fill بدلاً من ذلك.
### **عفا عليها الزمن فئة ShapeFormat و Shape.Format الخاصية**
الرجاء استخدام خصائص Shape.Fill و Shape.Line مباشرةً.
### **Obsoletes ShapeFont class ويضيف فئة TextOptions**
الرجاء استخدام فئة TextOptions بدلاً من ذلك.
### **يضيف TextOptions.Fill property و TextOptions.Outline و TextOptions.Shadow property**
يمثل التعبئة والمخطط والظل للنص.
### **تقادم FontSetting.ShapeFont الخاصية ويضيف خاصية FontSetting.TextOptions**
الرجاء استخدام الخاصية FontSetting.TextOptions بدلاً من ذلك.
