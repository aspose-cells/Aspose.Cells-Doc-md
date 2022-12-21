---
title: xlsx4j での前例と依存関係のトレース
type: docs
weight: 70
url: /ja/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - 前例と扶養家族の追跡**
複雑な財務ワークシート、特に共同で開発されたものは、最も厄介なエラーを隠すことができます。数式が参照元セルと従属セルを使用している場合、数式の正確性をチェックし、エラーの原因を見つけることが難しい場合があります。

- **先行細胞**別の Cell の数式によって参照されるセルです。たとえば、セル D10 に数式 =B5 が含まれている場合、セル B5 はセル D10 の参照元になります。
- **依存セル**他のセルを参照する数式が含まれています。たとえば、セル D10 に数式 =B5 が含まれている場合、セル D10 はセル B5 の依存セルです。

スプレッドシートを読みやすくするために、スプレッドシートのどのセルが数式で使用されているかを明確に示したい場合があります。同様に、他のセルの依存セルを抽出することもできます。

Aspose.Cells を使用すると、セルをトレースして、リンクされているセルを見つけることができます。

前例をたどる

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

依存関係のトレース

**Java**

{{< highlight "java" >}}

 //A1セルを取得

Cell c = セル.get("A5");

//A5 セルのすべての依存関係を取得します

Cell[]依存 = c.getDependents(真);

for (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[前例と依存関係のトレース](/java/tracing-precedents-and-dependents).

{{% /alert %}}
