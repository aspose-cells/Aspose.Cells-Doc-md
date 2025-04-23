---
title: حساب أو إعادة حساب الصيغ ديناميكياً
type: docs
weight: 10
url: /ar/net/calculate-or-recalculate-formulas-dynamically/
---

يتم تضمين محرك حساب الصيغ في Aspose.Cells. يمكنه ليس فقط إعادة حساب الصيغة المستوردة من ملف المصمم ولكن أيضاً يدعم حساب نتائج الصيغ المضافة أثناء التشغيل.
## **إضافة صيغ وحساب النتائج**
Aspose.Cells يدعم معظم الصيغ أو الوظائف التي تشكل جزءًا من Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ باستخدام واجهة برمجة التطبيقات أو جداول البيانات المصممة. تدعم Aspose.Excel مجموعة ضخمة من الصيغ الرياضية والنصية والمنطقية والتاريخ / الوقت والإحصائية وقاعدة البيانات والبحث والإشارة.

استخدم خاصية الصيغة في فئة Cell لإضافة صيغة إلى خلية. عند تطبيق صيغة على خلية، يجب دائمًا أن تبدأ السلسلة بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel. استخدم الفاصلة (،) لفصل معلمات الدالة.

لحساب نتائج الصيغ، قم باستدعاء طريقة CalculateFormula في فئة Excel والتي تقوم بمعالجة جميع الصيغ المضمنة في ملف Excel. اقرأ [الرابط: قائمة الدوال المدعومة بواسطة طريقة CalculateFormula](/cells/ar/net/supported-formula-functions/).

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int sheetIndex = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[sheetIndex];

//Adding a value to "A1" cell

worksheet.Cells["A1"].PutValue(1);

//Adding a value to "A2" cell

worksheet.Cells["A2"].PutValue(2);

//Adding a value to "A3" cell

worksheet.Cells["A3"].PutValue(3);

//Adding a SUM formula to "A4" cell

worksheet.Cells["A4"].Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

workbook.CalculateFormula();

//Get the calculated value of the cell

string value = worksheet.Cells["A4"].Value.ToString();

//Saving the Excel file

workbook.Save("Adding Formula.xls");

{{< /highlight >}}
## **حساب الصيغ مرة واحدة فقط**
عندما يقوم المستخدم بدعوة Workbook.CalculateFormula() لحساب قيم الصيغ داخل قالب المصنف، يقوم Aspose.Cells بإنشاء سلسلة حساب. يزيد الأداء عندما يتم حساب الصيغ للمرة الثانية أو الثالثة الخ.
ومع ذلك، إذا كان قالب المستخدم يحتوي على الكثير من الصيغ المتنوعة، فإن حساب الصيغ للمرة الأولى يمكن أن يستهلك الكثير من وقت معالجة وحدة المعالجة المركزية والذاكرة.

تسمح Aspose.Cells لك بإيقاف إنشاء سلسلة الحساب والتي تكون مفيدة في السيناريوهات عندما ترغب في حساب الصيغ مرة واحدة فقط من ملفك.

إذا كنت تسعى إلى تحسين أداء حساب الصيغ بواسطة Aspose.Cells ولا ترغب في إنشاء سلسلة حساب الصيغ، فيرجى ضبط **FormulaSettings.EnableCalculationChain** كـ **false**. بشكل افتراضي، يكون مضبوطًا على **true**.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Adding Formula.xlsx";

//Load the template workbook

Workbook workbook = new Workbook(FileName);

//Print the time before formula calculation

Console.WriteLine(DateTime.Now);

//Set the CreateCalcChain as false

workbook.Settings.FormulaSettings.EnableCalculationChain = false;

//Calculate the workbook formulas

workbook.CalculateFormula();

//Print the time after formula calculation

Console.WriteLine(DateTime.Now);

workbook.Save(FileName);

{{< /highlight >}}
## **حساب مباشر للصيغ**
محرك حساب الصيغ مضمن في Aspose.Cells. بالإضافة إلى إعادة حساب الصيغ المستوردة من ملف المصمم، تدعم Aspose.Cells أيضًا حساب نتائج الصيغ مباشرة.
أحيانًا، تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها فعليًا في ورقة عمل. قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة العمل وكل ما تحتاجه هو العثور على نتيجة تلك القيم استنادًا إلى بعض صيغة Ms-Excel دون إضافة الصيغة في ورقة العمل.

يمكنك استخدام واجهة برمجة التطبيقات لحساب الصيغ في Aspose.Cells أي **worksheet.Calculate(string formula)** لحساب نتائج مثل تلك الصيغ دون إضافتها فعليًا في ورقة العمل.

{{< highlight csharp >}}

 //Create a workbook

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Put 20 in cell A1

Cell cellA1 = worksheet.Cells["A1"];

cellA1.PutValue(20);

//Put 30 in cell A2

Cell cellA2 = worksheet.Cells["A2"];

cellA2.PutValue(30);

//Calculate the Sum of A1 and A2

var results = worksheet.CalculateFormula("=Sum(A1:A2)");

Cell cellA3 = worksheet.Cells["A3"];

cellA3.PutValue(results);

//Print the output

Debug.WriteLine("Value of A1: " + cellA1.StringValue);

Debug.WriteLine("Value of A2: " + cellA2.StringValue);

Debug.WriteLine("Result of Sum(A1:A2): " + results.ToString());

workbook.Save("Calulate Any Formulae.xls");

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
