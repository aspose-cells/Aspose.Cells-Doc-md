---
title: تتبع مسبقات ومراحل Aspose.Cells
type: docs
weight: 130
url: /ar/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

ورق العمل المالي المعقد، خصوصًا تلك التي تم تطويرها بالتعاون، يمكن أن تخفي الأخطاء الأكثر إحراجًا. فحص الصيغ لضمان الدقة والعثور على مصدر الخطأ يمكن أن يكون صعبًا عندما تستخدم الصيغ خلايا سابقة وخلايا معولة.

- **الخلايا المسبقة** هي الخلايا التي يشير إليها صيغة في خلية أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية B5 هي مسبقة للخلية D10.
- **الخلايا المعتمدة** تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية D10 هي معتمدة على الخلية B5.

لجعل ورق العمل سهل القراءة، قد ترغب في إظهار بشكل واضح الخلايا المستخدمة في صيغة. بالمثل، قد ترغب في استخراج الخلايا المعولة لخلايا أخرى.

تتيح Aspose.Cells لك تتبع الخلايا ومعرفة الخلايا المرتبطة.

{{% /alert %}} 
## **تتبع خلايا السابقة والتابعة: مايكروسوفت إكسل**
الصيغ قد تتغير استناداً إلى التعديلات التي يقوم بها العميل. على سبيل المثال، إذا كانت الخلية C1 تعتمد على وجود صيغ في C3 وC4، وتم تغيير C1 (بحيث يتم تجاوز الصيغة)، فإنه يجب أن تتغير C3 و C4، أو غيرها من الخلايا، لتحقيق توازن الجدول الإلكتروني استناداً إلى قواعد العمل.

بالمثل، لنفترض أن الخلية C1 تحتوي على الصيغة "=(B1*22)/(M2*N32)". أريد العثور على الخلايا التي تعتمد عليها C1، أي الخلايا السابقة B1، M2 وN32.

قد تحتاج إلى تتبع تبعية خلية معينة إلى خلايا أخرى. إذا كانت قواعد العمل مضمنة في الصيغ، نود أن نعرف التبعية وتنفيذ بعض القواعد استناداً إليها. وبالمثل إذا تم تعديل قيمة خلية معينة، فأي الخلايا في ورقة العمل تتأثر بهذا التغيير؟

تسمح مايكروسوفت إكسل للمستخدمين بتتبع الخلايا السابقة والتابعة.

1. على شريط أدوات **عرض**, حدد **تدقيق الصيغ**.
   يتم عرض مربع حوار تدقيق الصيغ. 
   **مربع حوار تدقيق الصيغ** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. تتبع السابقين:
   1. حدد الخلية التي تحتوي الصيغة التي تريد العثور على الخلايا السابقة لها.
   1. لعرض السهم التتبع إلى كل خلية توفر بيانات مباشرة للخلية النشطة، انقر على **تتبع السابقين** على شريط أدوات **تدقيق الصيغ**.
1. تتبع الصيغ التي تشير إلى خلية معينة (التوابع)
   1. حدد الخلية التي تريد تحديد الخلايا التابعة لها.
   1. لعرض السهم التتبع إلى كل خلية تعتمد على الخلية النشطة، انقر على تتبع التوابع على شريط أدوات تدقيق الصيغ.
## **تتبع خلايا السابقة والتابعة: Aspose.Cells**
### **تتبع السابقين**
يجعل Aspose.Cells من السهل الحصول على الخلايا السابقة. فهو لا يمكن أن يسترد الخلايا السابقة التي توفر بيانات لصيغة بسيطة فقط ولكن أيضا يمكنه أن يجد الخلايا التي توفر بيانات لصيغة معقدة مع النطاقات المسماة.

في المثال أدناه، يتم استخدام ملف إكسل نموذجي، Book1.xls. يحتوي جدول البيانات على بيانات وصيغ على ورقة العمل الأولى.

**جدول البيانات الداخلية** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

يوفر Aspose.Cells طريقة GetPrecedents في فئة الخلية المستخدمة لتتبع الخلايا السابقة. يعيد ReferredAreaCollection. كما يمكنك رؤية أعلاه، في Book1.xls، تحتوي الخلية B7 على الصيغة "=SUM(A1:A3)". لذا فإن الخلايا A1:A3 هي الخلايا السابقة للخلية B7. يظهر المثال التالي توضيح ميزة تتبع السابقة باستخدام ملف النموذج Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **تتبع المعتمدين**
تتيح Aspose.Cells لك الحصول على الخلايا التابعة في جداول البيانات. يمكن ل Aspose.Cells لا يقوم فقط باسترجاع الخلايا التي توفر بيانات حول صيغة بسيطة بل يمكنه أيضًا العثور على الخلايا التي توفر بيانات لتبعيات صيغة معقدة باسماء معرفة.

توفر Aspose.Cells طريقة GetDependents في فئة Cell تُستخدم لتتبع تبعيات الخلية. على سبيل المثال، في Book1.xlsx هناك صيغ: "=A1+20" و "=A1+30" في الخلايا B2 و C2 على التوالي. يوضح المثال التالي كيفية تتبع التبعيات للخلية A1 باستخدام ملف القالب Book1.xlsx.

**C#**

{{< highlight csharp >}}

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
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

{{< app/cells/assistant language="csharp" >}}
