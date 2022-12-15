---
title: Отслеживание прецедентов и зависимостей в xlsx4j
type: docs
weight: 70
url: /ru/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Отслеживание прецедентов и иждивенцев**
Сложные финансовые таблицы, особенно разработанные совместно, могут скрывать самые неприятные ошибки. Проверка формул на точность и поиск источника ошибки могут быть затруднены, если в формуле используются предшествующие ячейки и зависимые ячейки.

- **Предыдущие ячейки**— это ячейки, на которые ссылается формула в другом Cell. Например, если ячейка D10 содержит формулу =B5, ячейка B5 является предшествующей ячейке D10.
- **Зависимые ячейки**содержат формулы, которые ссылаются на другие ячейки. Например, если ячейка D10 содержит формулу =B5, ячейка D10 зависит от ячейки B5.

Чтобы электронную таблицу было легко читать, вы можете четко показать, какие ячейки в электронной таблице используются в формуле. Точно так же вы можете захотеть извлечь зависимые ячейки других ячеек.

Aspose.Cells позволяет отслеживать ячейки и выяснять, какие из них связаны.

Отслеживание прецедентов

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

Отслеживание иждивенцев

**Java**

{{< highlight "java" >}}

 //Получить ячейку A1

Cell c = Cells.get("A5");

//Получить все зависимые ячейки A5

Cell[]зависимые = c.getDependents(true);

для (целое я = 0; я< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Отслеживание прецедентов и иждивенцев](/java/tracing-precedents-and-dependents).

{{% /alert %}}
