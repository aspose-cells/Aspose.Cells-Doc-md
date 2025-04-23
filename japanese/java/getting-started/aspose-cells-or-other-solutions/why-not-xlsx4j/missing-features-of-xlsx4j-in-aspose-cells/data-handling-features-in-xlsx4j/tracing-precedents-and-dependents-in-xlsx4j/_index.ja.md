---
title: xlsx4j での Precedents および Dependents のトレース
type: docs
weight: 70
url: /ja/java/tracing-precedents-and-dependents-in-xlsx4j/
---

## **Aspose.Cells - Precedents および Dependents のトレース**
特に共同で開発された複雑な財務ワークシートは、最も恥ずかしいエラーを隠すことがあります。式の正確さをチェックし、エラーの原因を特定することは、先行セルおよび従属セルを使用する式をチェックする際に困難になるかもしれません。

- **Precedent cells** とは、他のセルの数式で参照されるセルのことです。例えば、セル D10 が数式 =B5 を含んでいる場合、セル B5 はセル D10 の先行要素です。
- **Dependent cells** とは、他のセルを参照する数式を含んでいるセルのことです。例えば、セル D10 が数式 =B5 を含んでいる場合、セル D10 はセル B5 の依存要素です。

スプレッドシートをわかりやすくするために、スプレッドシートに含まれるセルが式で使用されているかを明確に表示することがあります。同様に、他のセルの従属セルを抽出することがあります。

Aspose.Cells を使用すると、セルをトレースしてリンクされているセルを特定することができます。

先行をトレース

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

従属をトレース

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
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

詳細については、[Precedents および Dependents のトレース](/java/tracing-precedents-and-dependents) をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
