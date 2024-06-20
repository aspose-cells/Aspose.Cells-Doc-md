---
title: تغييرات الواجهة العامة في Aspose.Cells 8.7.1
type: docs
weight: 240
url: /ar/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

توضح هذه الوثيقة التغييرات التي طرأت على واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.7.0 إلى 8.7.1 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. تتضمن ليس فقط الأساليب العامة الجديدة والمحدثة، وإضافة وإزالة الفئات وما إلى ذلك، ولكن أيضًا وصفاً لأي تغييرات في السلوك الخلفي في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية LookInType.OriginalValues**
تدعم APIs لـ Aspose.Cells بالفعل [البحث أو العثور على البيانات](/cells/ar/net/find-or-search-data/) لجداول البيانات بهدف إيجاد جزء معين من المحتويات في قيمة الخلية والصيغة. ومع ذلك، كان هذا الميزة يفتقد جانب التنسيق المطبق على الخلية الذي قد يغير المظهر وكذلك قيمة المحتويات، مما يجعل النص غير قابل للبحث باستخدام القيمة الأصلية. مع هذا الإصدار من APIs لـ Aspose.Cells، تمت إضافة ثابت آخر باسم LookInType.OriginalValues إلى الواجهة البرمجية العامة والذي يسمح بالتغلب على الوضع كما هو مناقش أعلاه.

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يُرجى مراجعة المقالة المفصلة حول [البحث عن البيانات باستخدام القيم الأصلية](/cells/ar/net/search-data-using-original-values/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **تمت إضافة حدث OnBeforeColumnFilter لـ GridWeb**
تمتكن Aspose.Cells.GridWeb for .NET 8.7.1 الـ OnBeforeColumnFilter والتي تعمل كإشارة إلى آلية التصفية التي تتم من خلال واجهة GridWeb UI. كما يوحي الاسم، يتم تشغيل الحدث قبل تطبيق تصفية العمود ويُمكن استخدامه للحصول على معلومات التصفية مثل فهرس العمود والقيمة التي يجب تطبيق التصفية عليها.

سيناريو الاستخدام البسيط يبدو كما يلي.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
