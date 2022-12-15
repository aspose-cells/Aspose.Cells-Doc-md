---
title: Spåra prejudikat och beroende i Aspose.Cells
type: docs
weight: 130
url: /sv/net/tracing-precedents-and-dependents-in-aspose-cells/
---
{{% alert color="primary" %}} 

Komplexa ekonomiska kalkylblad, särskilt sådana som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta källan till ett fel kan vara svårt när formeln använder prejudikatceller och beroende celler.

- **Prejudikatceller** är celler som refereras till av en formel i en annan Cell. Om cell D10 till exempel innehåller formeln =B5, är cell B5 ett prejudikat till cell D10.
- **Beroende celler** innehåller formler som refererar till andra celler. Till exempel, om cell D10 innehåller formeln =B5, är cell D10 ett beroende av cell B5.

För att göra kalkylarket lätt att läsa, kanske du vill tydligt visa vilka celler i ett kalkylblad som används i en formel. På liknande sätt kanske du vill extrahera de beroende cellerna från andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.

{{% /alert %}} 
## **Spåra prejudikat och beroende Cells: Microsoft Excel**
Formler kan ändras baserat på ändringar gjorda av en kund. Till exempel, om cell C1 är beroende av att C3 och C4 innehåller en formel, och C1 ändras (så att formeln åsidosätts), måste C3 och C4, eller andra celler, ändras för att balansera kalkylbladet baserat på affärsregler.

På samma sätt, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta cellerna som C1 beror på, det vill säga prejudikatcellerna B1, M2 och N32.

Du kan behöva spåra beroendet av en viss cell till andra celler. Om affärsregler är inbäddade i formler vill vi ta reda på beroendet och exekvera några regler baserat på det. På samma sätt om värdet på en viss cell ändras, vilka celler i kalkylbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra prejudikat och beroende.

1.  På**Visa verktygsfält** , Välj**Formelrevision**.
 Dialogrutan Formelrevision visas.
   **Dialogrutan Formelrevision** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Spåra prejudikat:
1. Välj cellen som innehåller formeln som du vill hitta prejudikatceller för.
 1. För att visa en spårningspil för varje cell som direkt tillhandahåller data till den aktiva cellen, klicka**Spåra prejudikat** på**Formelrevision** verktygsfältet.
1. Spåra formler som refererar till en viss cell (beroende)
 1. Välj den cell som du vill identifiera de beroende cellerna för.
 1. För att visa en spårningspil för varje cell som är beroende av den aktiva cellen, klicka på Spåra beroende i verktygsfältet Formula Auditing.
## **Spårande prejudikat och beroende Cells: Aspose.Cells**
### **Spåra prejudikat**
Aspose.Cells gör det enkelt att få prejudikatceller. Den kan inte bara hämta celler som tillhandahåller data till en enkel formelprejudikat utan också hitta celler som tillhandahåller data till komplexa formelprejudikat med namngivna intervall.

I exemplet nedan används en excel-mall, Book1.xls. Kalkylarket har data och formler på det första kalkylbladet.

**Indatakalkylarket** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells tillhandahåller Cell-klassens GetPrecedents-metod som används för att spåra en cells prejudikat. Den returnerar en ReferredAreaCollection. Som du kan se ovan, i Book1.xls, innehåller cell B7 en formel "=SUMMA(A1:A3)". Så cellerna A1:A3 är prejudikatcellerna till cell B7. Följande exempel visar spårningsprejudikatfunktionen med hjälp av mallfilen Book1.xls.

**C#**

{{< highlight "csharp" >}}

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
### **Spåra beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data om en enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoende med namngivna intervall.

Aspose.Cells tillhandahåller Cell-klassens GetDependents-metod som används för att spåra en cells beroende. Till exempel, i Book1.xlsx finns formler: "=A1+20" och "=A1+30" i B2- respektive C2-cellerna. Följande exempel visar hur man spårar beroenden för A1-cellen med hjälp av mallfilen Book1.xlsx.

**C#**

{{< highlight "csharp" >}}

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
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

