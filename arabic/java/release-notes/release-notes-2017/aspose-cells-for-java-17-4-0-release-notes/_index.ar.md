---
title: Aspose.Cells for Java 17.4.0 ملاحظات الإصدار
type: docs
weight: 90
url: /ar/java/aspose-cells-for-java-17-4-0-release-notes/
---
{{% alert color="primary" %}} 

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 17.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.4.0/).

{{% /alert %}} 

|**مفتاح**|**ملخص**|**فئة**|
|:- |:- |:- |
|CELLSJAVA-41975|دعم تنسيق DBNum (نمط مخصص)|ميزة جديدة|
|CELLSJAVA-42237|يؤدي الوصول إلى الخلية إلى إنشاء HTML بصفوف فارغة|التعزيز|
|CELLSJAVA-42236|مشكلة في الأداء مع بيئة متعددة مؤشرات الترابط|التعزيز|
|CELLSJAVA-42226|حدد لمجلد ومجلداته الفرعية لاستخدام الخطوط في عرض الصور / PDF|التعزيز|
|CELLSJAVA-42239|خطأ في تنسيق سلسلة الإدخال عند تحميل HTML|حشرة|
|CELLSJAVA-42230|يتم إنشاء سمة محاذاة إضافية عند تحويل XLSX إلى HTML|حشرة|
|CELLSJAVA-42229|تصدير XLSX إلى HTML - يتم إنشاء رموز التجزئة بدلاً من قيم Cell الفعلية|حشرة|
|CELLSJAVA-42218|لم يتم تحويل HTML بشكل صحيح إلى ملف Excel|حشرة|
|CELLSJAVA-42210|بعض التنسيقات الشرطية لـ DataBar مفقودة في HTML الناتج|حشرة|
|CELLSJAVA-41783|يجب أن تكون صورة الخلفية بتنسيق SVG ولكن بتنسيق PNG|حشرة|
|CELLSJAVA-42253|تؤدي قيمة الخلية التابعة إلى حدوث خطأ في XLS|حشرة|
|CELLSJAVA-42222|المجموع غير صحيح بعد حساب المصنف|حشرة|
|CELLSJAVA-42254|GridWebServlet؟ acw_أياكس_حدث خطأ في الاتصال أثناء تحميل GridWeb|حشرة|
|CELLSJAVA-42243|Excel إلى PDF - مربع يشبه المستطيل|حشرة|
|CELLSJAVA-42242|Excel إلى PDF - تبدو الدائرة مثل الشكل البيضاوي|حشرة|
|CELLSJAVA-42227|ملف الصورة "x1.png" له حد علوي إضافي وحد سفلي مفقود|حشرة|
|CELLSJAVA-42212|مشكلة في الأداء عند تصدير XLS إلى PDF|حشرة|
|CELLSJAVA-42246|Excel إلى HTML - محاذاة النص في تسمية المحور ص للمخطط خاطئة|حشرة|
|CELLSJAVA-42223|نقاط مخطط الرادار xy px ترجع 0|حشرة|
|CELLSJAVA-42216|تتغير القيم المضمنة للمحور ص للمخطط الفقاعي عندما يتم تحويل AxisScalingValuesIssue-2.xlsx إلى PDF|حشرة|
|CELLSJAVA-42250|خطأ في التحويل البرمجي إذا احتوت التعليمات البرمجية على تعريف متغير من النوع CommandBar|حشرة|
|CELLSJAVA-42241|Excel إلى PDF - تأتي الأقواس في السطر التالي|حشرة|
|CELLSJAVA-42234|يزيل حفظ ملف XLSM بتنسيق XLS إجراء الماكرو من الزر|حشرة|
|CELLSJAVA-42233|قم بترقية الكود - تطبيق تنسيق ثلاثي الأبعاد على الرسم البياني|حشرة|
|CELLSJAVA-42225|تعذر تعيين نطاق إدخال الشكل|حشرة|
|CELLSJAVA-42224|مشكلة في فرز التعليقات|حشرة|
|CELLSJAVA-42221|الانحدار الحرج مع الضوابط المخصصة|حشرة|
|CELLSJAVA-42220|مشكلة تتعلق بتعيين عرض تخطيط الصفحة لملفات XLSB|حشرة|
|CELLSJAVA-42217|بعد الوصول إلى VbaModule عبر Aspose API ، تسبب ملف Excel الناتج في كسر مشروع vba|حشرة|
|CELLSJAVA-42213|يقوم الخط عن غير قصد بتغيير حجمه في التعليق مع تضمين CR مضمن فيه|حشرة|
|CELLSJAVA-42231|يحدث الاستثناء عند إدراج الصفوف|استثناء|
## **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**
فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.
### **يضيف طريقة VbaProject.Protect (bool islockedForViewing، string password)**
يحمي أو يلغي حماية مشروع VBA.
### **يضيف خاصية VbaProject.SProtected**
يشير إلى ما إذا كان مشروع vba محميًا.
### **يضيف خاصية VbaProject.IslockedForViewing**
يشير إلى ما إذا كان مشروع VBA مغلقًا للعرض.
### **إضافة خاصية CopyOptions.ExtendToAdjacentRange**
يشير إلى ما إذا كان يتم تمديد النطاقات عند نسخ النطاق إلى النطاق المجاور.

{{< highlight "java" >}}

 Workbook wb = new Workbook("sample.xlsx");

Worksheet ws = wb.getWorksheets().get("Sheet1");

CopyOptions co = new CopyOptions();

co.setExtendToAdjacentRange(true);

Cells cells = ws.getCells();

cells.copyRows(cells, 0, 1, 1, co);

{{< /highlight >}}
### **يحذف طريقة Workbook.ValidateFormula (صيغة السلسلة) التي عفا عليها الزمن**
### **يضيف خاصية DataSorter.SortAsNumber**
يشير إلى ما إذا كان يتم فرز أي شيء يشبه الرقم.
### **أمثلة على الاستخدام**
يرجى التحقق من قائمة مواضيع المساعدة المضافة في Aspose.Cells مستندات Wiki:

- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/java/specifying-sort-warning-while-sorting-data/)
- [حماية كلمة المرور لمشروع VBA من مصنف Excel](/cells/ar/java/password-protect-the-vba-project-of-excel-workbook/)
- [اكتشف ما إذا كان VBA Project محميًا](/cells/ar/java/find-out-if-vba-project-is-protected/)
- [تحقق مما إذا كان VBA Project محميًا ومؤمنًا للعرض](/cells/ar/java/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [تحديد تنسيق نمط مخصص DBNum](/cells/ar/java/specifying-dbnum-custom-pattern-formatting/)
