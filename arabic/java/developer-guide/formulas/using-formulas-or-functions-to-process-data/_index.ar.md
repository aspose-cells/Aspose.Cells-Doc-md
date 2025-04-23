---
title: استخدام الصيغ أو الوظائف لمعالجة البيانات
type: docs
weight: 5
url: /ar/java/get-and-set-formula/
---

{{% alert color="primary" %}}

إحدى الميزات المثيرة للاهتمام في Microsoft Excel هي قدرته على معالجة البيانات باستخدام الصيغ والوظائف. يوفر Microsoft Excel مجموعة من الوظائف والصيغ المضمّنة التي تساعد المستخدمين على إجراء الحسابات المعقدة بسرعة. كما يوفر Aspose.Cells مجموعة هائلة من الوظائف والصيغ المضمّنة التي تساعد المطوّرين على حساب القيم بسهولة. تدعم Aspose.Cells أيضًا الوظائف الإضافية. علاوة على ذلك، تدعم Aspose.Cells الصيغ الصفيفية وR1C1 في Aspose.Cells.

{{% /alert %}}

## **استخدام الصيغ والوظائف**

توفر Aspose.Cells فئةً، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يُمثل ورقة عمل كائن الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). يوفر الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). كل عنصر في مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) يمثل كائنًا من الفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

من الممكن تطبيق الصيغ على الخلايا باستخدام الخصائص والأساليب التي تقدمها الفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)، كما سيتم مناقشته بالتفصيل أدناه.

- [استخدام الوظائف المضمنة](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [استخدام الوظائف الإضافية](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [العمل مع الصيغ الصفيفية](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [إنشاء صيغة R1C1](/cells/ar/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **استخدام الوظائف المضمّنة**

تُوفّر الوظائف المضمّنة أو الصيغ كوظائف جاهزة لتقليل جهود ووقت المطوّرين. انظر [قائمة بالوظائف المضمّنة](/cells/ar/java/supported-formula-functions/). تُسرد الوظائف بترتيب أبجدي. ستُدعم المزيد من الوظائف في المستقبل.

تدعم Aspose.Cells معظم الصيغ أو الوظائف التي توفّرها Microsoft Excel. يمكن للمطوّرين استخدام هذه الصيغ من خلال واجهة البرمجة التطبيقية أو [جدول البيانات التصميمي](/cells/ar/java/what-is-a-designer-spreadsheet/). تدعم Aspose.Cells مجموعة هائلة من الصيغ الرياضية والنصية والبولية والتاريخ والوقت، الإحصائية، قواعد البيانات، البحث، والمراجع.

استخدم خاصية [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) للفئة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) لإضافة صيغة إلى خلية. **الصيغ المعقدة**، على سبيل المثال

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, مدعومة أيضًا في Aspose.Cells. عند تطبيق صيغة على خلية، يجب دائمًا بدء السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel واستخدام فاصلة (,) لفصل معلمات الوظيفة.

في المثال أدناه، يتم تطبيق صيغة معقدة على الخلية الأولى في مجموعة [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) لورقة العمل. تستخدم الصيغة وظيفة **IF** المضمّنة المقدّمة بواسطة Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **استخدام الوظائف الإضافية**

يمكن أن يحتوي على بعض الصيغ التي يعرفها المستخدم ونريد تضمينها كإضافة إكسل. عند ضبط [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) تعمل الوظائف المضمنة بشكل جيد ومع ذلك يوجد حاجة لضبط الوظائف أو الصيغ المخصصة باستخدام وظائف الإضافة.

توفر Aspose.Cells ميزات لتسجيل وظائف الوظيفة الإضافية باستخدام [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-). بعد ذلك عندما نقوم بتعيين [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn ، يحتوي ملف Excel الناتج على القيمة المحسوبة من وظيفة الإضافة.

سيتم تنزيل ملف XLAM لتسجيل وظيفة الإضافة في رمز العينة أدناه. بالمثل، يمكن تنزيل ملف الإخراج "test_udf.xlsx" للتحقق من الإخراج.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **استخدام الصيغة الصفيفية**

الصيغ الصفية هي صيغ تعمل مع المصفوفات بدلاً من الأرقام الفردية كمدخلات للوظائف التي تشكل الصيغة. عند عرض صيغة صفية، يتم لفها بقوسين مموجين ({}) كما هو موضح أدناه.

**ضبط صيغة صفية على الخلية G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

تعيد بعض وظائف Microsoft Excel مصفوفات القيم. لحساب نتائج متعددة باستخدام صيغة مصفوفة، أدخل المصفوفة في نطاق الخلايا بعدد الصفوف والأعمدة نفس معدلات الوسائط المصفوفات.

من الممكن تطبيق صيغة مصفوفة على خلية عن طريق استدعاء طريقة [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) لفئة [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-). تأخذ الطريقة [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) المعلمات التالية:

- **صيغة مصفوفة**, صيغة المصفوفة.
- **عدد الصفوف**, عدد الصفوف لملء نتيجة صيغة المصفوفة.
- **عدد الأعمدة**, عدد الأعمدة لملء نتيجة الصيغة الصفية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **استخدام صيغة R1C1**

تطبيق صيغة نمط المرجع R1C1 على خلية مع [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) الفئة الرئيسية' [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) الخاصية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
