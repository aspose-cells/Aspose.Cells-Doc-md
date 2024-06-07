---
title: 在xlsx4j中跟踪前驱和依赖项
type: docs
weight: 70
url: /zh/java/tracing-precedents-and-dependents-in-xlsx4j/
---

## **Aspose.Cells - 跟踪前驱和依赖项**
特别是在协作开发的复杂财务工作表中，可能会隐藏最尴尬的错误。当公式使用前置单元格和后置单元格时，检查公式的准确性并找到错误来源可能会变得困难。

- **前驱单元格**是被另一个单元格公式引用的单元格。例如，如果单元格D10包含公式=B5，则单元格B5是单元格D10的前导。
- **依赖单元格**包含引用其他单元格的公式。例如，如果单元格D10包含公式=B5，则单元格D10是单元格B5的依赖项。

为了使电子表格易于阅读，您可能希望清楚地显示电子表格上使用的公式单元格。同样，您可能希望提取其他单元格的后置单元格。

Aspose.Cells允许您跟踪单元格并找出哪些单元格是链接的。

跟踪先行

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

跟踪从属

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

有关更多详细信息，请访问【跟踪前驱和依赖项】(/java/tracing-precedents-and-dependents)。

{{% /alert %}}
