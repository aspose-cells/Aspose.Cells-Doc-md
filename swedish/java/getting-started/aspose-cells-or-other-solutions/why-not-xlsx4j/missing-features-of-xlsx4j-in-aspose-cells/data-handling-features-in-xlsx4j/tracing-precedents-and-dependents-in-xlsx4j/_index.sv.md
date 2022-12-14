---
title: Spåra prejudikat och beroende i xlsx4j
type: docs
weight: 70
url: /sv/java/tracing-precedents-and-dependents-in-xlsx4j/
---
## **Aspose.Cells - Spåra prejudikat och beroende**
Komplexa ekonomiska kalkylblad, särskilt sådana som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta källan till ett fel kan vara svårt när formeln använder prejudikatceller och beroende celler.

- **Prejudikatceller**är celler som refereras till av en formel i en annan Cell. Om cell D10 till exempel innehåller formeln =B5, är cell B5 ett prejudikat till cell D10.
- **Beroende celler**innehåller formler som refererar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är cell D10 ett beroende av cell B5.

För att göra kalkylarket lätt att läsa, kanske du vill tydligt visa vilka celler i ett kalkylblad som används i en formel. På liknande sätt kanske du vill extrahera de beroende cellerna från andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.

Spåra prejudikat

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

Spåra beroende

**Java**

{{< highlight "java" >}}

 //Hämta A1-cellen

Cell c = cells.get("A5");

//Hämta alla beroenden i A5-cellen

Cell[]beroende = c.getDependents(true);

för (int i = 0; i< dependents.length; i++)

{

     System.out.println("Tracing Dependents: " + dependents[i].getWorksheet().getName() +dependents[i].getName() + ":" + dependents[i].getIntValue());

}

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/tracingprecedentsanddependents/AsposeTracingPrecedentsAndDependents.java)

{{% alert color="primary" %}} 

 För mer information, besök[Spåra prejudikat och beroende](/java/tracing-precedents-and-dependents).

{{% /alert %}}
