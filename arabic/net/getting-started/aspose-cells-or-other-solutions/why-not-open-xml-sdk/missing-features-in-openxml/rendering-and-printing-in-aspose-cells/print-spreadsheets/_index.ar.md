---
title: طباعة جداول البيانات
type: docs
weight: 20
url: /ar/net/print-spreadsheets/
---
توفر إعدادات إعداد الصفحة أيضًا العديد من خيارات الطباعة (يشار إليها أيضًا باسم خيارات الورقة) التي تتيح للمستخدمين التحكم في صفحات أوراق العمل المطبوعة الخاصة بهم. تتيح خيارات الطباعة هذه للمستخدمين:

- حدد ناحية طباعة معينة لورقة العمل
- عناوين الطباعة
- طباعة خطوط الشبكة
- طباعة عناوين الصفوف / الأعمدة
- تحقيق جودة المسودة
- طباعة التعليقات
- طباعة Cell أخطاء
- تحديد ترتيب الصفحة
  **ضبط خيارات الطباعة / الورقة**

يدعم Aspose.Cells كل خيارات الطباعة هذه ويمكن للمطورين تكوين هذه الخيارات بسهولة لأوراق العمل المطلوبة باستخدام الخصائص العديدة التي توفرها فئة PageSetup. تمت مناقشة استخدام هذه الخصائص لفئة PageSetup أدناه بمزيد من التفصيل.
## **تعيين ناحية الطباعة**
بشكل افتراضي ، يتم تحديد منطقة الطباعة فقط التي تتضمن المنطقة بأكملها من ورقة العمل ، والتي تحتوي على بيانات ولكن يمكن للمطورين أيضًا إنشاء منطقة طباعة معينة من ورقة العمل وفقًا لرغبتهم.

 لتحديد منطقة طباعة معينة ، يمكن للمطورين استخدام المجموعة**منطقة الطباعة** طريقة**اعداد الصفحة** صف دراسي. يمكنك توفير نطاق خلايا منطقة الطباعة لهذه الطريقة كوسيطة.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **تعيين عناوين الطباعة**
 يسمح لك Aspose.Cells بتعيين رؤوس الصفوف والأعمدة التي تريد تكرارها في كافة صفحات ورقة العمل المطبوعة. للقيام بذلك ، يمكن للمطورين استخدام مجموعة**PrintTitleColumns** و**setPrintTitleRows** طرق**اعداد الصفحة** صف دراسي.

يتم تحديد الصفوف أو الأعمدة (المراد تكرارها في كافة صفحات ورقة العمل المطبوعة) بتمرير أرقام الصفوف أو الأعمدة. على سبيل المثال ، يتم تعريف الصفوف على أنها \ $ 1: \ $ 2 ويتم تعريف الأعمدة على أنها \ $ A: \ $ B.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **قم بتعيين خيارات الطباعة الأخرى**
**اعداد الصفحة** توفر class أيضًا عدة طرق أخرى لتعيين خيارات الطباعة العامة على النحو التالي:

- **طريقة setPrintGridline** ، يتم تمرير معلمة منطقية إلى هذه الطريقة التي تحدد ما إذا كنت تريد طباعة خطوط الشبكة أم لا
- **طريقة setPrintHeadings**، يتم تمرير معلمة منطقية إلى هذه الطريقة التي تحدد ما إذا كنت تريد طباعة عناوين الصفوف والأعمدة أم لا
- **طريقة setBlackAndWhite** ، يتم تمرير معلمة منطقية إلى هذه الطريقة التي تحدد ما إذا كنت تريد طباعة ورقة العمل في الوضع الأسود والأبيض أم لا
- **طريقة setPrintComments** ، يحدد ما إذا كان سيتم عرض تعليقات الطباعة في ورقة العمل أو في نهاية ورقة العمل
- **طريقة setPrintDraft** ، يتم تمرير معلمة منطقية إلى هذه الطريقة التي تحدد ما إذا كنت تريد طباعة ورقة العمل بجودة المسودة أم لا
- **طريقة setPrintErrors** ، يحدد ما إذا كان سيتم طباعة أخطاء الخلية كما هي معروضة أو فارغة أو شرطة أو غير متوفرة

 لاستخدام المجموعة**PrintComments** وحدد**أخطاء الطباعة** يوفر Aspose.Cells أيضًا عددين ، PrintCommentsType & PrintErrorsType الذي يحتوي على قيم محددة مسبقًا ليتم تمريرها إلى معلمات لتعيين PrintComments وتعيين أساليب PrintErrors على التوالي.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines

pageSetup.PrintGridlines = true;

//Allowing to print row/column headings

pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode

pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet

pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality

pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A

pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;

{{< /highlight >}}
## **تعيين ترتيب الصفحة**
**اعداد الصفحة**توفر class طريقة ترتيب المجموعة التي تُستخدم لطلب طباعة صفحات متعددة من ورقة العمل الخاصة بك. هناك احتمالان لترتيب الصفحات على النحو التالي:

لأسفل ثم فوق وبالتالي ستطبع جميع الصفحات لأسفل قبل طباعة الصفحات إلى اليمين
ومن ثم لأسفل ، ستتم طباعة الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أدناه
يوفر Aspose.Cells تعدادًا ، PrintOrderType يحتوي على كافة أنواع الأوامر المحددة مسبقًا التي سيتم تخصيصها لطريقة ترتيب الصفحة.

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
