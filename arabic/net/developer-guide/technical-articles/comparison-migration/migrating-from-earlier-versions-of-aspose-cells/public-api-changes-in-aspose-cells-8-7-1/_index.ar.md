---
title: عام API التغييرات في Aspose.Cells 8.7.1
type: docs
weight: 240
url: /ar/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.0 إلى 8.7.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية LookInType.OriginalValues**
 Aspose.Cells تدعم واجهات برمجة التطبيقات بالفعل[البحث عن البيانات أو البحث عنها](/cells/ar/net/find-or-search-data/)ميزة لجداول البيانات من أجل العثور على جزء معين من المحتويات في قيمة الخلية وصيغتها. ومع ذلك ، كانت هذه الميزة تفتقر إلى جانب التنسيق المطبق على الخلية والذي قد يغير المظهر بالإضافة إلى قيمة المحتويات ، وبالتالي يجعل النص غير قابل للبحث باستخدام القيمة الأصلية. مع هذا الإصدار من Aspose.Cells APIs ، تم الكشف عن ثابت آخر باسم LookInType.OriginalValues للجمهور API مما يسمح بالتغلب على الموقف كما تمت مناقشته أعلاه.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[البحث في البيانات باستخدام القيم الأصلية](/cells/ar/net/search-data-using-original-values/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET كشف 8.7.1 عن حدث OnBeforeColumnFilter الذي يعمل بمثابة رد اتصال لآلية التصفية التي تتم من خلال GridWeb UI. كما يوحي الاسم ، يتم تشغيل الحدث قبل تطبيق تصفية العمود ويمكن استخدامه للحصول على معلومات التصفية مثل فهرس العمود والقيمة التي يجب تطبيق الفلتر عليها.

يبدو سيناريو الاستخدام البسيط على النحو التالي.

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

لا تنس تسجيل الحدث في GridWeb control<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
