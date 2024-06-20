---
title: تغييرات الواجهة العامة في Aspose.Cells 8.7.1
type: docs
weight: 250
url: /ar/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

توضح هذه الوثيقة التغييرات التي طرأت على واجهة برمجة التطبيقات Aspose.Cells من الإصدار 8.7.0 إلى 8.7.1 التي قد تكون مثيرة لاهتمام مطوري الوحدات/التطبيقات. تتضمن ليس فقط الأساليب العامة الجديدة والمحدثة، وإضافة وإزالة الفئات وما إلى ذلك، ولكن أيضًا وصفاً لأي تغييرات في السلوك الخلفي في Aspose.Cells.

{{% /alert %}} 
## **واجهات برمجة التطبيقات الجديدة**
### **تمت إضافة خاصية LookInType.ORIGINAL_VALUES.**
تدعم بالفعل واجهات برمجة التطبيقات Aspose.Cells ميزة [البحث أو البحث عن البيانات](/cells/ar/java/find-or-search-data/) لجداول البيانات من أجل العثور على قطعة معينة من المحتويات في قيمة الخلية والصيغة. ومع ذلك، كانت تفتقر هذه الميزة إلى جانب التنسيق الذي يُطبق على الخلية والذي قد يغيّر المظهر بالإضافة إلى قيمة المحتويات، مما يُجعل النص غير قابل للبحث باستخدام القيمة الأصلية. مع إصدار واجهات برمجة التطبيقات Aspose.Cells هذا، تمت تقديم ثابت آخر بالاسم LookInType.ORIGINAL_VALUES لواجهة البرمجة العامة والذي يسمح بتجاوز الوضع كما هو موضّح أعلاه. 

{{% alert color="primary" %}} 

لمزيد من التفاصيل حول هذه الميزة، يرجى مراجعة المقال المفصل حول [البحث عن البيانات باستخدام القيم الأصلية](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

فيما يلي سيناريو الاستخدام البسيط.

**Java**

{{< highlight csharp >}}

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
