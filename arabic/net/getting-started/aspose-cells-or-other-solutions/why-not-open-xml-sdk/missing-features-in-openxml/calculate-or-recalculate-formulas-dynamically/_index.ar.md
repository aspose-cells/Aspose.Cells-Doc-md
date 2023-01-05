---
title: حساب أو إعادة حساب الصيغ ديناميكيًا
type: docs
weight: 10
url: /ar/net/calculate-or-recalculate-formulas-dynamically/
---
**حساب الصيغة** المحرك مضمن في**Aspose.Cells**. لا يمكنه فقط إعادة حساب الصيغة المستوردة من ملف المصمم ولكنه يدعم أيضًا حساب نتائج الصيغ المضافة في وقت التشغيل.
## **إضافة الصيغ وحساب النتائج**
يدعم Aspose.Cells معظم الصيغ أو الوظائف التي تشكل جزءًا من Microsoft Excel. يمكن للمطورين استخدام هذه الصيغ باستخدام API أو جداول البيانات المصممة. يدعم Aspose.Excel مجموعة ضخمة من الصيغ الرياضية ، والسلسلة ، والمنطقية ، والتاريخ / الوقت ، والإحصاء ، وقاعدة البيانات ، والبحث والمراجع.

استخدم الخاصية Formula لفئة Cell لإضافة صيغة إلى خلية. عند تطبيق صيغة على خلية ، ابدأ السلسلة دائمًا بعلامة يساوي (=) كما تفعل عند إنشاء صيغة في Microsoft Excel. استخدم فاصلة (،) لتحديد معلمات الوظيفة.

 لحساب نتائج الصيغ ، اتصل بفئة Excel 'CalculateFormula طريقة تعالج جميع الصيغ المضمنة في ملف Excel. إقرأ ال[url: قائمة الوظائف التي تدعمها طريقة CalculateFormula](/cells/ar/net/supported-formula-functions/).

{{< highlight "csharp" >}}

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
عندما يقوم المستخدم باستدعاء Workbook.CalculateFormula () لحساب قيم الصيغ داخل قالب المصنف ، يقوم Aspose.Cells بإنشاء سلسلة حساب. يزيد من الأداء عند حساب الصيغ للمرة الثانية أو الثالثة وما إلى ذلك.
ومع ذلك ، إذا كان قالب المستخدم يحتوي على الكثير من الصيغ المتنوعة ، فإن المرة الأولى لحساب الصيغة يمكن أن تستهلك الكثير من وقت معالجة وحدة المعالجة المركزية والذاكرة.

يسمح لك Aspose.Cells بإيقاف إنشاء سلسلة الحساب التي تكون مفيدة في السيناريوهات عندما تريد حساب الصيغ لملفك مرة واحدة فقط.

 إذا كنت تسعى إلى تحسين أداء حسابات الصيغة بواسطة Aspose.Cells ولا تريد إنشاء سلسلة حساب الصيغة ، فيرجى تعيين**FormulaSettings.EnableCalculationChain** مثل**خاطئة** . بشكل افتراضي ، يتم تعيينه على أنه**حقيقي**.

{{< highlight "csharp" >}}

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
## **الحساب المباشر للصيغة**
تم تضمين محرك حساب الصيغة في Aspose.Cells. بالإضافة إلى ذلك ، فإن إعادة حساب الصيغة المستوردة من ملف المصمم ، يدعم Aspose.Cells أيضًا حساب نتائج الصيغ مباشرةً.
في بعض الأحيان ، تحتاج إلى حساب نتائج الصيغ مباشرة دون إضافتها فعليًا في ورقة العمل. قيم الخلايا المستخدمة في الصيغة موجودة بالفعل في ورقة عمل وكل ما تحتاجه هو العثور على نتيجة هذه القيم بناءً على صيغة MS-Excel دون إضافة الصيغة في ورقة العمل.

 يمكنك استخدام Aspose.Cells محرك حساب الصيغة API ie**ورقة عمل. احسب (صيغة سلسلة)**لحساب نتائج هذه الصيغ دون إضافتها فعليًا في ورقة العمل.

{{< highlight "csharp" >}}

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
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Direct%20Formulae%20Call%20%28Aspose.Cells%29.zip)
