---
title: تتبع سابقين ومعاول في xlsx4j
type: docs
weight: 70
url: /ar/java/tracing-precedents-and-dependents-in-xlsx4j/
---

## **Aspose.Cells - تتبع السابقين والمعاول**
ورق العمل المالي المعقد، خصوصًا تلك التي تم تطويرها بالتعاون، يمكن أن تخفي الأخطاء الأكثر إحراجًا. فحص الصيغ لضمان الدقة والعثور على مصدر الخطأ يمكن أن يكون صعبًا عندما تستخدم الصيغ خلايا سابقة وخلايا معولة.

- الخلايا السابقة هي الخلايا التي يشير إليها صيغة في خلية أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية B5 هي سابقة للخلية D10.
- الخلايا المعولة تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال، إذا كانت الخلية D10 تحتوي على الصيغة =B5، فإن الخلية D10 هي معولة للخلية B5.

لجعل ورق العمل سهل القراءة، قد ترغب في إظهار بشكل واضح الخلايا المستخدمة في صيغة. بالمثل، قد ترغب في استخراج الخلايا المعولة لخلايا أخرى.

تتيح Aspose.Cells لك تتبع الخلايا ومعرفة الخلايا المرتبطة.

تتبع السابقين

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook(dataDir + "workbook.xls");

Cells cells = workbook.getWorksheets().get(0).getCells();

Cell cell = cells.get("A12");

//Tracing precedents of the cell A12.

//The return array contains ranges and cells.

ReferredAreaCollection ret = cell.getPrecedents();

//Printing all the precedent cells' name.

if(ret != null)

{

  for(int m = 0 ; m < ret.getCount(); m++)

  {

    ReferredArea area = ret.get(m);

    StringBuilder stringBuilder = new StringBuilder();

    if (area.isExternalLink())

    {

        stringBuilder.append("[");

        stringBuilder.append(area.getExternalFileName());

        stringBuilder.append("]");

     }

     stringBuilder.append(area.getSheetName());

     stringBuilder.append("!");

     stringBuilder.append(CellsHelper.cellIndexToName(area.getStartRow(), area.getStartColumn()));

     if (area.isArea())

      {

          stringBuilder.append(":");

          stringBuilder.append(CellsHelper.cellIndexToName(area.getEndRow(), area.getEndColumn()));

      }

      System.out.println("Tracing Precedents: " + stringBuilder.toString());

   }

}

{{< /highlight >}}

تتبع المعتمدين

**Java**

{{< highlight java >}}

 //Get the A1 cell

Cell c = cells.get("A5");

//Get the all the Dependents of A5 cell

Cell[] dependents = c.getDependents(true);

for (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تتبع مسبق ومرتبط](/java/tracing-precedents-and-dependents).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
