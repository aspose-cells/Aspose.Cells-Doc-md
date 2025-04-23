---
title: Отслеживание предшественников и зависимостей в xlsx4j
type: docs
weight: 70
url: /ru/java/tracing-precedents-and-dependents-in-xlsx4j/
---

## **Aspose.Cells - Отслеживание предшественников и зависимостей**
Сложные финансовые рабочие листы, особенно те, которые разработаны в сотрудничестве, могут скрывать наиболее нелестные ошибки. Проверка формул на точность и поиск источника ошибки может быть сложной, когда формула использует предшествующие и зависимые ячейки.

- **Предшествующие ячейки** - это ячейки, на которые ссылается формула в другой ячейке. Например, если в ячейке D10 содержится формула =B5, ячейка B5 является предшественником для ячейки D10.
- **Зависимые ячейки** содержат формулы, которые ссылается на другие ячейки. Например, если в ячейке D10 содержится формула =B5, ячейка D10 является зависимой от ячейки B5.

Чтобы сделать таблицу удобной для чтения, вы можете явно показать, какие ячейки в таблице используются в формулах. Точно так же, вы можете извлечь зависимые ячейки других ячеек.

Aspose.Cells позволяет отслеживать ячейки и выяснять, какие из них связаны между собой.

Отслеживание предшественников

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

Отслеживание зависимых

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
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

Дополнительные сведения см. на [Отслеживание предшественников и зависимостей](/java/tracing-precedents-and-dependents).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
