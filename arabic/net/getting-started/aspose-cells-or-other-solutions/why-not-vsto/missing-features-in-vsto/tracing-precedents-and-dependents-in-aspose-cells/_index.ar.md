---
title: تتبع السوابق والتابعين Aspose.Cells
type: docs
weight: 130
url: /ar/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

أوراق العمل المالية المعقدة ، خاصة تلك التي تم تطويرها بالتعاون ، يمكن أن تخفي الأخطاء الأكثر إحراجًا. قد يكون التحقق من الصيغ للتأكد من دقتها وإيجاد مصدر الخطأ أمرًا صعبًا عندما تستخدم الصيغة خلايا سابقة وخلايا تابعة.

- **الخلايا السابقة** هي الخلايا المشار إليها بواسطة صيغة أخرى في Cell. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية B5 هي سابقة للخلية D10.
- **الخلايا التابعة** تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية D10 تكون تابعة للخلية B5.

لتسهيل قراءة جدول البيانات ، قد ترغب في إظهار الخلايا الموجودة في جدول البيانات والمستخدمة في الصيغة بوضوح. وبالمثل ، قد ترغب في استخراج الخلايا التابعة للخلايا الأخرى.

Aspose.Cells يسمح لك بتتبع الخلايا ومعرفة أي منها مرتبطة.

{{% /alert %}} 
## **تتبع السوابق والمعالين Cells: Microsoft Excel**
قد تتغير الصيغ بناءً على التعديلات التي يجريها العميل. على سبيل المثال ، إذا كانت الخلية C1 تعتمد على C3 و C4 التي تحتوي على صيغة ، وتم تغيير C1 (بحيث يتم تجاوز الصيغة) ، أو C3 و C4 ، أو خلايا أخرى ، فيجب تغييرها لموازنة جدول البيانات استنادًا إلى قواعد العمل.

وبالمثل ، افترض أن C1 تحتوي على الصيغة "= (B1*22) / (م 2*N32) ". أريد العثور على الخلايا التي تعتمد عليها C1 ، وهي الخلايا السابقة B1 و M2 و N32.

قد تحتاج إلى تتبع تبعية خلية معينة إلى خلايا أخرى. إذا تم تضمين قواعد العمل في الصيغ ، فنحن نرغب في معرفة التبعية وتنفيذ بعض القواعد بناءً عليها. وبالمثل ، إذا تم تعديل قيمة خلية معينة ، فما الخلايا في ورقة العمل التي ستتأثر بهذا التغيير؟

Microsoft Excel يسمح للمستخدمين بتتبع السوابق والتابعين.

1.  على ال**عرض شريط الأدوات** ، تحديد**تدقيق الصيغة**.
 يتم عرض مربع حوار تدقيق الصيغة.
   **مربع حوار تدقيق الصيغة** 

![ما يجب القيام به: image_بديل_نص](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. تتبع السوابق:
1. حدد الخلية التي تحتوي على الصيغة التي تريد البحث عن الخلايا السابقة لها.
 1. لعرض سهم التتبع لكل خلية توفر بيانات مباشرة إلى الخلية النشطة ، انقر فوق**تتبع السوابق** على ال**تدقيق الصيغة** شريط الأدوات.
1. تتبع الصيغ التي تشير إلى خلية معينة (التابعين)
 1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
 1. لعرض سهم التتبع لكل خلية تعتمد على الخلية النشطة ، انقر فوق تتبع التابعين على شريط أدوات تدقيق الصيغة.
## **تتبع السوابق والمعالين Cells: Aspose.Cells**
### **تتبع السوابق**
يسهل Aspose.Cells الحصول على الخلايا السابقة. لا يمكنها فقط استرداد الخلايا التي توفر بيانات إلى سوابق صيغة بسيطة ولكن أيضًا العثور على الخلايا التي توفر بيانات لسوابق صيغة معقدة ذات نطاقات مسماة.

في المثال أدناه ، يتم استخدام ملف Excel نموذجي ، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ في ورقة العمل الأولى.

**جدول الإدخال** 

![ما يجب القيام به: image_بديل_نص](tracing-precedents-and-dependents-in-aspose-cells_2.png)

يوفر Aspose.Cells فئة Cell 'GetPrecedents طريقة المستخدمة لتتبع السوابق في الخلية. تقوم بإرجاع RefifiedAreaCollection. كما ترى أعلاه ، في Book1.xls ، تحتوي الخلية B7 على صيغة "= SUM (A1: A3)". لذا فإن الخلايا A1: A3 هي الخلايا السابقة للخلية B7. يوضح المثال التالي ميزة سوابق التتبع باستخدام ملف القالب Book1.xls.

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("book1.xls");

Cells cells = workbook.Worksheets[0].Cells;

Aspose.Cells.Cell cell = cells["B7"];

//Tracing precedents of the cell B7.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.GetPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.Count; m++)

  {

    ReferredArea area = ret[m];

    StringBuilder stringBuilder = new StringBuilder();

    if (area.IsExternalLink)

    {

        stringBuilder.Append("[");

        stringBuilder.Append(area.ExternalFileName);

        stringBuilder.Append("]");

     }

     stringBuilder.Append(area.SheetName);

     stringBuilder.Append("!");

     stringBuilder.Append(CellsHelper.CellIndexToName(area.StartRow, area.StartColumn));

     if (area.IsArea)

      {

          stringBuilder.Append(":");

          stringBuilder.Append(CellsHelper.CellIndexToName(area.EndRow, area.EndColumn));

      }


      Console.WriteLine(stringBuilder.ToString());

   }

}



{{< /highlight >}}
### **تتبع المعالين**
يتيح لك Aspose.Cells الحصول على خلايا تابعة في جداول البيانات. لا يمكن لـ Aspose.Cells فقط استرداد الخلايا التي توفر بيانات تتعلق بصيغة بسيطة ولكن أيضًا العثور على الخلايا التي توفر البيانات إلى المعتمدين على صيغة معقدة ذات نطاقات مسماة.

يوفر Aspose.Cells فئة Cell 'طريقة GetDependents المستخدمة لتتبع التابعين للخلية. على سبيل المثال ، في Book1.xlsx توجد صيغ: "= A1 + 20" و "= A1 + 30" في الخلايا B2 و C2 على التوالي. يوضح المثال التالي كيفية تتبع التابعين لخلية A1 باستخدام ملف القالب Book1.xlsx.

**C#**

{{< highlight "csharp" >}}

 string path = "Book1.xlsx";

Workbook workbook = new Workbook(path);

Worksheet worksheet = workbook.Worksheets[0];

var c = worksheet.Cells["A1"];

var dependents = c.GetDependents(true);

foreach (var dependent in dependents)

{

     Debug.WriteLine(string.Format("{0} ---- {1} : {2}", dependent.Worksheet.Name, dependent.Name, dependent.Value));

}

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

