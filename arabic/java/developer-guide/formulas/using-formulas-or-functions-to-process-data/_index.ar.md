---
title: استخدام الصيغ أو الوظائف لمعالجة البيانات
type: docs
weight: 5
url: /ar/java/get-and-set-formula/
---
{{% alert color="primary" %}}

تتمثل إحدى ميزات Microsoft الجذابة في Excel في قدرته على معالجة البيانات باستخدام الصيغ والوظائف. يوفر Microsoft Excel مجموعة من الوظائف والصيغ المضمنة التي تساعد المستخدمين على إجراء العمليات الحسابية المعقدة بسرعة. يوفر Aspose.Cells أيضًا مجموعة ضخمة من الوظائف والصيغ المضمنة التي تساعد المطورين على حساب القيم بسهولة. يدعم Aspose.Cells أيضًا الوظائف الإضافية. علاوة على ذلك ، يدعم Aspose.Cells صفيف وصيغ R1C1 في Aspose.Cells.

{{% /alert %}}

## **استخدام الصيغ والوظائف**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) مجموعة. كل عنصر في[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) تمثل المجموعة كائنًا من[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)صف دراسي.

 من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والطرق التي يوفرها[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)الفصل ، بمزيد من التفصيل أدناه.

- [استخدام وظائف مدمجة](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [استخدام الوظائف الإضافية](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [العمل مع صيغ الصفيف](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [إنشاء صيغة R1C1](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **استخدام وظائف مدمجة**

 يتم توفير الوظائف أو الصيغ المضمنة كوظائف جاهزة لتقليل جهود المطورين والوقت. نرى[قائمة الوظائف المضمنة](/cells/ar/java/supported-formula-functions/). يتم سرد الوظائف بالترتيب الأبجدي. سيتم دعم المزيد من الوظائف في المستقبل.

 يدعم Aspose.Cells معظم الصيغ أو الوظائف التي يوفرها Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ من خلال API أو[جدول بيانات المصمم](/cells/ar/java/what-is-a-designer-spreadsheet/). يدعم Aspose.Cells مجموعة ضخمة من الصيغ الرياضية ، والجمل ، والمنطقية ، والتاريخ / الوقت ، والإحصائية ، وقاعدة البيانات ، والبحث ، والصيغ المرجعية.

 استخدم ال[**معادلة**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)ممتلكات[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) فئة لإضافة صيغة إلى خلية.**الصيغ المعقدة**، فمثلا

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

، يتم دعمها أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية ، ابدأ دائمًا السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدم فاصلة (،) لتحديد معاملات الدالة.

 في المثال أدناه ، يتم تطبيق صيغة معقدة على الخلية الأولى من ورقة العمل[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) مجموعة. تستخدم الصيغة ملف**إذا** الوظيفة المقدمة من Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **استخدام الوظائف الإضافية**

 يمكن أن يكون لدينا بعض الصيغ التي يحددها المستخدم والتي نريد تضمينها كوظيفة إضافية في Excel. عند ضبط ملف[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) تعمل الوظائف المدمجة للوظيفة بشكل جيد ولكن هناك حاجة لتعيين الوظائف أو الصيغ المخصصة باستخدام وظائف الوظيفة الإضافية.

 يوفر Aspose.Cells ميزات لتسجيل الوظائف الإضافية باستخدام[**أوراق العمل.**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). بعد ذلك عندما وضعنا[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn ، يحتوي ملف Excel الناتج على القيمة المحسوبة من الوظيفة الإضافية.

يجب تنزيل ملف XLAM التالي لتسجيل وظيفة الوظيفة الإضافية في نموذج التعليمات البرمجية أدناه. وبالمثل ، يمكن تنزيل ملف الإخراج "test_udf.xlsx" للتحقق من الإخراج.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **باستخدام صيغة المصفوفة**

صيغ الصفيف هي صيغ تعمل مع المصفوفات ، بدلاً من الأرقام الفردية ، كوسائط للدوال التي تشكل الصيغة. عندما يتم عرض صيغة مصفوفة ، فإنها محاطة بأقواس ({}) كما هو موضح أدناه.

**تعيين صيغة صفيف في الخلية G2** 

![ما يجب القيام به: image_بديل_نص](using-formulas-or-functions-to-process-data_1.png)

تقوم بعض دالات Microsoft Excel بإرجاع مصفوفات من القيم. لحساب نتائج متعددة باستخدام صيغة صفيف ، أدخل الصفيف في نطاق من الخلايا بنفس عدد الصفوف والأعمدة مثل وسيطات الصفيف.

 من الممكن تطبيق صيغة صفيف على خلية عن طريق استدعاء[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) طريقة. ال[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) تأخذ الطريقة المعلمات التالية:

- **صيغة المصفوفة**، صيغة الصفيف.
- **عدد الصفوف**، هو عدد الصفوف المراد نشرها نتيجة صيغة الصفيف.
- **عدد الأعمدة**، هو عدد الأعمدة المطلوب ملء نتيجة صيغة الصفيف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **باستخدام صيغة R1C1**

 تطبيق**R1C1** صيغة نمط مرجعي لخلية بامتداد[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) صف دراسي'[**الصيغة**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)منشأه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

