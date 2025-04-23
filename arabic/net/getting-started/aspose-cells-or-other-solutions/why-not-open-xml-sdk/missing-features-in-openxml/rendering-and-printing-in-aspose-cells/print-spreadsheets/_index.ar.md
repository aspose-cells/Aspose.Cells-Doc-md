---
title: طباعة جداول بيانات
type: docs
weight: 20
url: /ar/net/print-spreadsheets/
---

إعدادات تخطيط الصفحة توفر أيضًا عدة خيارات طباعة (تُشار إليها أيضًا بالخيارات الورقية) تسمح للمستخدمين بالتحكم في صفحاتهم المطبوعة لورقات العمل. تتيح هذه الخيارات تحكم المستخدمين في:

- تحديد منطقة طباعة معينة في ورقة العمل
- طباعة العناوين
- طباعة خطوط الشبكة
- طباعة عناوين الصفوف / الأعمدة
- تحقيق جودة مسودة
- طباعة التعليقات
- طباعة أخطاء الخلية
- تعريف ترتيب الصفحات
  **ضبط خيارات الطباعة / الورقة**

تدعم Aspose.Cells جميع هذه الخيارات للطباعة ويمكن للمطورين تكوين هذه الخيارات بسهولة لورقات العمل المرغوبة باستخدام الخصائص المتعددة التي تقدمها فئة PageSetup. يتم مناقشة استخدام هذه الخصائص لفئة PageSetup بالتفصيل أدناه.
## **تعيين منطقة الطباعة**
افتراضيًا، يتم تحديد منطقة الطباعة التي تضم مساحة الورقة بأكملها التي تحتوي على البيانات ولكن يمكن للمطورين أيضًا تحديد منطقة الطباعة المحددة لورقة العمل حسب رغبتهم.

لتحديد منطقة طباعة معينة، يمكن للمطورين استخدام طريقة **PrintArea** في فئة **PageSetup**. يمكنك توفير نطاق الخلايا الذي تريد طباعته لهذه الطريقة كوسيط.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **تحديد عناوين الطباعة**
تسمح Aspose.Cells لك بتعيين عناوين الصف والعمود التي ترغب في تكرارها على جميع الصفحات لورقة العمل المطبوعة. للقيام بذلك، يمكن للمطورين استخدام طرق **setPrintTitleColumns** و **setPrintTitleRows** في فئة **PageSetup**.

يتم تحديد الصفوف أو الأعمدة (التي يتم تكرارها على جميع الصفحات لورقة العمل المطبوعة) عن طريق تمرير أرقام الصف أو العمود الخاصة بهم. على سبيل المثال، يتم تعريف الصفوف بما يلي \ $1: \ $2 ويتم تعريف الأعمدة بما يلي \ $A: \ $B.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows = "$1:$2";

{{< /highlight >}}
## **تحديد خيارات الطباعة الأخرى**
توفر فئة **PageSetup** أيضًا العديد من الطرق الأخرى لتحديد خيارات الطباعة العامة كما يلي:

- **setPrintGridlines method**، يتم تمرير معلمة بوليانية إلى هذه الطريقة التي تحدد ما إذا كان يتم طباعة خطوط الشبكة أم لا
- **setPrintHeadings method**، يتم تمرير معلمة بوليانية إلى هذه الطريقة التي تحدد ما إذا كان يتم طباعة أعناوين الصف والعمود أم لا
- **setBlackAndWhite method**، يتم تمرير معلمة بوليانية إلى هذه الطريقة التي تحدد ما إذا كان يتم طباعة ورقة العمل في وضع أسود وأبيض أم لا
- **setPrintComments method**، تحدد ما إذا كان عرض تعليقات الطباعة على ورقة العمل أم في نهاية ورقة العمل
- **setPrintDraft method**، يتم تمرير معلمة بوليانية إلى هذه الطريقة التي تحدد ما إذا كان يتم طباعة ورقة العمل بجودة مسودة أم لا
- **setPrintErrors method**، تحدد ما إذا كان يتم طباعة أخطاء الخلية كما هو معروض، فارغ، علامة شرط أو N/A

لاستخدام طرق **setPrintComments** و **setPrintErrors**، توفر Aspose.Cells أيضًا تعميمين، PrintCommentsType & PrintErrorsType التي تحتوي على قيم محددة مسبقًا لتمريرها كمعلمات إلى طرق set PrintComments و set PrintErrors على التوالي.

{{< highlight csharp >}}

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
## **تحديد ترتيب الصفحة**
توفر فئة **PageSetup** طريقة set Order التي تُستخدم لترتيب عدة صفحات من ورقة العمل الخاصة بك للطباعة. هناك احتمالان لترتيب الصفحات كما يلي:

تحديد النزول ثم الانتقال بحيث سيتم طباعة جميع الصفحات لأسفل قبل طباعة الصفحات إلى اليمين
الانتقال ثم النزول بحيث ستتم طباعة الصفحات من اليسار إلى اليمين قبل طباعة الصفحات أدناه
توفر Aspose.Cells تعميمًا، PrintOrderType الذي يحتوي على جميع أنواع الترتيب المحددة مسبقًا لتعيينها لطريقة setPage Order.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **تحميل رمز عينة**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
