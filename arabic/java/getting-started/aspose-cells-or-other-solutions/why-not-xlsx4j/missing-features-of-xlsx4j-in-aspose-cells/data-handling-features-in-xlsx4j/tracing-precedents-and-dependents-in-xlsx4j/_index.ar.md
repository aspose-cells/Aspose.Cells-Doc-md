---
title: تتبع السوابق والمعالين في xlsx4j
type: docs
weight: 70
url: /ar/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - تتبع السوابق والتابعين**
أوراق العمل المالية المعقدة ، خاصة تلك التي تم تطويرها بالتعاون ، يمكن أن تخفي الأخطاء الأكثر إحراجًا. قد يكون التحقق من الصيغ للتأكد من دقتها وإيجاد مصدر الخطأ أمرًا صعبًا عندما تستخدم الصيغة خلايا سابقة وخلايا تابعة.

- **الخلايا السابقة**هي الخلايا المشار إليها بواسطة صيغة أخرى في Cell. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية B5 هي سابقة للخلية D10.
- **الخلايا التابعة**تحتوي على صيغ تشير إلى خلايا أخرى. على سبيل المثال ، إذا كانت الخلية D10 تحتوي على الصيغة = B5 ، فإن الخلية D10 تكون تابعة للخلية B5.

لتسهيل قراءة جدول البيانات ، قد ترغب في إظهار الخلايا الموجودة في جدول البيانات والمستخدمة في الصيغة بوضوح. وبالمثل ، قد ترغب في استخراج الخلايا التابعة للخلايا الأخرى.

Aspose.Cells يسمح لك بتتبع الخلايا ومعرفة أي منها مرتبطة.

تتبع السوابق

**Java**

{{< highlight "java" >}}

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

تتبع المعالين

**Java**

{{< highlight "java" >}}

 // احصل على الخلية A1

Cell ج = cell.get ("A5") ؛

// احصل على جميع التابعين لخلية A5

Cell [] المعالون = c.getDependents (صحيح) ؛

لـ (int i = 0 ؛ i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تتبع السوابق والمعالين](/java/tracing-precedents-and-dependents).

{{% /alert %}}
