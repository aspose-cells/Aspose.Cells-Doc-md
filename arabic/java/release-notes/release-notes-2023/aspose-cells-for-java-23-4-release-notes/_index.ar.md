---
title: Aspose.Cells for Java 23.4 ملاحظات الإصدار
type: docs
weight: 9
url: /ar/java/aspose-cells-for-java-23-4-release-notes/
---
{{% alert color="primary" %}}

 تحتوي هذه الصفحة على ملاحظات الإصدار لـ[Aspose.Cells for Java 23.4](https://releases.aspose.com/cells/java/).

{{% /alert %}}

|**مفتاح**|**ملخص**|**فئة**|
| :- | :- | :- |
|CELLSJAVA-45255|عرض النص من أعلى إلى أسفل باستخدام "وضع الكتابة" في CSS|
|CELLSJAVA-45227|يتعطل Aspose.Cells حفظ الملف باسم XLSB|
|CELLSJAVA-45241|النتيجة المحسوبة لـ MIRR غير صحيحة|
|CELLSJAVA-45296|Aspose Cells لا يقوم بإعادة حساب صيغة بعض القيم|
|CELLSJAVA-45223|رسم بياني للصورة - لم يتم عرض الحرف وارتفاع مفتاح الرسم بشكل صحيح|
|CELLSJAVA-45257| مقاييس الرسم البياني مفقودة في Excel حتى عرض PDF|
|CELLSJAVA-45054|لا يمكن تبديل ورقة العمل للملف المحدد من العميل|
|CELLSJAVA-45229|لا يمكن تحميل الملف في GridWeb لملف test.xlsx|
|CELLSJAVA-45231|لا تسري setRowHeightForCSV بعد تبديل ورقة العمل ، ولا يزال ارتفاع صف ملف csv صغيرًا|
|CELLSJAVA-45251|بعد ضبط عرض العمود ، يجب أيضًا ضبط موضع زر الفلتر في مكانه|
|CELLSJAVA-45082|يختلف تعبئة السطر المتموج بعد حفظ الملف في pdf|
|CELLSJAVA-45237|خطأ في عرض الصيغة عند حفظ الملف في SVG|
|CELLSJAVA-45236|خطأ في موضع الخط عند حفظ الملف في SVG|
|CELLSJAVA-45252|إزالة غير صحيحة للصفحات أثناء تحويل Excel إلى PDF عند استخدام خيار PrintingPageType.IGNORE_BLANK|
|CELLSJAVA-45273|بعض النصوص غير مرئية عند التحويل إلى svg|
|CELLSJAVA-45266|Cell خطأ في موقع المحتوى عند التحويل إلى html|
|CELLSJAVA-45279|تظهر مسافة بيضاء إضافية عند تصدير الملف إلى HTML|
|CELLSJAVA-45248| HTML إلى Excel: لا يمكن الاحتفاظ بالتنسيق المتعدد في نفس الوقت|
|CELLSJAVA-45304|قطعة الأرض مفقودة في المخططات الشريطية عند تحويل xlsx إلى ods|
|CELLSJAVA-45305|يتم تحويل شكل الشمس إلى شكل مستطيل عند تحويل ods إلى xlsx|
|CELLSJAVA-45308|لا تظهر قيم Cell للخلايا التي تحتوي على ورقة عرضية عند تحويل xlsx إلى ods|
|CELLSJAVA-45259|فقدان البيانات عند تحويل HTML مع القوائم إلى XLSX|
|CELLSJAVA-45260|HTML إلى XLSX: لم يتم الاحتفاظ بالمحاذاة|
|CELLSJAVA-45271| يحتوي ملف النتيجة على معرف مستخدم مختلف عند حفظ مصنف مرتين|
|CELLSJAVA-45283|يدعم تحديد PivotArea أنواع الحقول المحورية الأخرى غير PivotFieldType.Data|
|CELLSJAVA-45298|يجب الاحتفاظ بألوان المخططات الدائرية عند تحويل xlsx إلى ods|
|CELLSJAVA-45309|زاوية الشريحة الأولى للمخطط الدائري غير صحيحة عند تحويل Excel إلى ods|
|CELLSJAVA-45310|أضف تنسيق OneNote إلى FileFormatUtil API لاكتشاف نوع الملف|

##  **API العام والتغييرات غير المتوافقة مع الإصدارات السابقة**

فيما يلي قائمة بأي تغييرات تم إجراؤها على API العام مثل الأعضاء المضافين أو المعاد تسميتهم أو المحذوفون أو المهملون بالإضافة إلى أي تغيير غير متوافق مع الإصدارات السابقة تم إجراؤه على Aspose.Cells for Java. إذا كانت لديك مخاوف بشأن أي تغيير مدرج ، فيرجى رفعه في منتدى الدعم Aspose.Cells.

###  **يضيف خاصية XlsbSaveOptions.LightCellsDataProvider**

يسمح للمستخدم بحفظ ملف xlsb في وضع LightCell.

###  **يضيف أساليب Worksheet.CalculateArrayFormula (...)**

يسمح للمستخدم بحساب صيغة واحدة كصيغة صفيف ديناميكيًا دون تعيينها إلى خلية في البداية.

###  **يضيف خاصية CalculationOptions.CharacterEncoding**

يسمح للمستخدم بتحديد الترميز المستخدم لترميز / فك تشفير الأحرف عند حساب الصيغ مثل وظيفة CHAR و CODE.

###  **يضيف فئة EquationNode والفئات المشتقة منه**

يسمح للمستخدمين بإكمال بناء شكل المعادلة عن طريق إدراج العقد ذات الصلة خطوة بخطوة.

###  **إضافة تعدادات FileFormatType.XHtml و FileFormat.OneNote**

يمثل نوع تنسيق ملف xhtml و One Note.

###  **يضيف أسلوب FontConfigs.IsFontAvailable ()**

يُرجع ما إذا كان الخط متاحًا أم لا.

###  **إضافة خاصية LoadOptions.IgnoreUselessShapes**

الإشارة إلى ما إذا كان يتم تجاهل الأشكال عديمة الفائدة في ملفات xlsx أم لا.

###  **إضافة خصائص PivotArea.OnlyData و OnlyLabel.**

يمثل ما إذا كان تحديد البيانات فقط أو lable للمنطقة المحورية.

###  **يضيف تعداد SaveFormat.XHtml.**

يمثل تنسيق الحفظ.

###  **يضيف طريقة ListObject.PutCellFormula ()**

يضع الصيغة في الخلايا في الجدول.

###  **يضيف خاصية VbaProject.Encoding**

الحصول على وتعيين ترميز مشروع VBA في ملفات Excel.

###  **إضافة خاصية XmlSaveOptions.SheetNameAsElementName.**

يشير إلى ما إذا كان يتم حفظ اسم الورقة كاسم عنصر عند تحويل بيانات Excel إلى بيانات xml.

###  **يضيف خاصية XmlSaveOptions.DataAsAttribute.**

يشير إلى ما إذا كان يتم حفظ البيانات كسمة للعقدة عند تحويل بيانات Excel إلى بيانات xml.
