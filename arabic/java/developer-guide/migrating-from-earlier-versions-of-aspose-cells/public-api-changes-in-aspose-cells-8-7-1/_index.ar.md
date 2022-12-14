---
title: عام API التغييرات في Aspose.Cells 8.7.1
type: docs
weight: 250
url: /ar/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

يصف هذا المستند التغييرات التي تم إجراؤها على Aspose.Cells API من الإصدار 8.7.0 إلى 8.7.1 والتي قد تهم مطوري الوحدة / التطبيق. لا يشمل فقط الأساليب العامة الجديدة والمحدثة ، والفئات المضافة والمحذوفة وما إلى ذلك ، بل يشمل أيضًا وصفًا لأي تغييرات في السلوك خلف الكواليس في Aspose.Cells.

{{% /alert %}} 
## **تمت إضافة واجهات برمجة التطبيقات**
### **تمت إضافة خاصية LookInType.ORIGINAL_VALUES**
 Aspose.Cells تدعم واجهات برمجة التطبيقات بالفعل[البحث عن البيانات أو البحث عنها](/cells/ar/java/find-or-search-data/)ميزة لجداول البيانات من أجل العثور على جزء معين من المحتويات في قيمة الخلية وصيغتها. ومع ذلك ، كانت هذه الميزة تفتقر إلى جانب التنسيق المطبق على الخلية والذي قد يغير المظهر بالإضافة إلى قيمة المحتويات ، وبالتالي يجعل النص غير قابل للبحث باستخدام القيمة الأصلية. مع هذا الإصدار من واجهات برمجة التطبيقات Aspose.Cells ، تم الكشف عن ثابت آخر باسم LookInType.ORIGINAL_VALUES للجمهور API والذي يسمح بالتغلب على الموقف كما تمت مناقشته أعلاه.

{{% alert color="primary" %}} 

 لمزيد من التفاصيل حول هذه الميزة ، يرجى مراجعة المقالة التفصيلية على[البحث في البيانات باستخدام القيم الأصلية](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
