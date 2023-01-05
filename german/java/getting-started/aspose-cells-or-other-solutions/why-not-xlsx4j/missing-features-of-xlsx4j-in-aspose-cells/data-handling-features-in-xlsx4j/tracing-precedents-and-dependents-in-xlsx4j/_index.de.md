---
title: Ablaufverfolgung von Präzedenzfällen und Abhängigkeiten in xlsx4j
type: docs
weight: 70
url: /de/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Rückverfolgung von Präzedenzfällen und Angehörigen**
Komplexe Finanzarbeitsblätter, insbesondere solche, die gemeinsam entwickelt wurden, können die peinlichsten Fehler verbergen. Das Überprüfen von Formeln auf Genauigkeit und das Auffinden der Fehlerquelle kann schwierig sein, wenn die Formel Vorgängerzellen und abhängige Zellen verwendet.

- **Vorhergehende Zellen**sind Zellen, auf die durch eine Formel in einem anderen Cell verwiesen wird. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle B5 ein Präzedenzfall für Zelle D10.
- **Abhängige Zellen**Formeln enthalten, die auf andere Zellen verweisen. Wenn beispielsweise Zelle D10 die Formel =B5 enthält, ist Zelle D10 von Zelle B5 abhängig.

Um die Tabellenkalkulation leicht lesbar zu machen, möchten Sie möglicherweise deutlich zeigen, welche Zellen in einer Tabellenkalkulation in einer Formel verwendet werden. Ebenso möchten Sie möglicherweise die abhängigen Zellen anderer Zellen extrahieren.

Aspose.Cells ermöglicht es Ihnen, Zellen zu verfolgen und herauszufinden, welche verknüpft sind.

Präzedenzfälle verfolgen

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

Abhängigkeiten verfolgen

**Java**

{{< highlight "java" >}}

 // Holen Sie sich die A1-Zelle

Cell c = Zellen. get ("A5");

// Holen Sie sich alle abhängigen Zellen der A5-Zelle

Cell[]abhängige = c.getDependents(true);

für (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Rückverfolgung von Präzedenzfällen und Angehörigen](/java/tracing-precedents-and-dependents).

{{% /alert %}}
