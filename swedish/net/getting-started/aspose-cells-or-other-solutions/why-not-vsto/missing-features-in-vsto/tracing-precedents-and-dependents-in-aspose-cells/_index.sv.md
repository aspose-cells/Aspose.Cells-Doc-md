---
title: Spåra precedenter och beroenden i Aspose.Cells
type: docs
weight: 130
url: /sv/net/tracing-precedents-and-dependents-in-aspose-cells/
---

{{% alert color="primary" %}} 

Komplexa finansiella arbetsblad, särskilt de som utvecklats i samarbete, kan dölja de mest pinsamma felen. Att kontrollera formler för noggrannhet och hitta felets källa kan vara svårt när formeln använder precedens- och beroendeceller.

- **Precedensceller** är celler som hänvisas till av en formel i en annan cell. Till exempel, om cell D10 innehåller formeln =B5, är cell B5 en precedens till cell D10.
- **Beroende celler** innehåller formler som hänvisar till andra celler. Till exempel, om cellen D10 innehåller formeln =B5, är cellen D10 beroende av cellen B5.

För att göra kalkylarket lättläst vill du kanske tydligt visa vilka celler på ett kalkylblad som används i en formel. På liknande sätt kan du vilja extrahera de beroende cellerna för andra celler.

Aspose.Cells låter dig spåra celler och ta reda på vilka som är länkade.

{{% /alert %}} 
## **Spåra precedens- och beroendeceller: Microsoft Excel**
Formler kan ändras baserat på ändringar som gjorts av en klient. Till exempel, om cell C1 är beroende av C3 och C4 som innehåller en formel, och C1 ändras (så att formeln åsidosätts), behöver C3 och C4, eller andra celler, ändras för att balansera kalkylbladet baserat på affärsregler.

Likaså, anta att C1 innehåller formeln "=(B1*22)/(M2*N32)". Jag vill hitta de celler som C1 är beroende av; det vill säga de precedente cellerna B1, M2 och N32.

Du kanske behöver spåra beroendet av en specifik cell till andra celler. Om affärsregler är inbäddade i formler, vill vi ta reda på beroendet och utföra vissa regler baserat på det. På samma sätt om värdet på en specifik cell ändras, vilka celler i arbetsbladet påverkas av den ändringen?

Microsoft Excel tillåter användare att spåra precedenser och beroenden.

1. På ** Visa verktygsfältet ** välj ** Formelgranskning **.
   Dialogrutan Formelgranskning visas. 
   ** Dialogrutan Formelgranskning ** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_1.png)

1. Spåra Precedenser:
   1. Välj den cell som innehåller formeln för vilken du vill hitta precedensceller.
   1. För att visa en spårpil till varje cell som direkt tillhandahåller data till den aktiva cellen, klicka på **Spåra Precedenser** på verktygsfältet för formelgranskning.
1. Spåra formler som refererar till en specifik cell (beroenden)
   1. Välj den cell för vilken du vill identifiera de beroende cellerna.
   1. För att visa en spårpil till varje cell som är beroende av den aktiva cellen, klicka på Spåra Beroenden på verktygsfältet för formelgranskning.
## **Spårar föregående och beroende celler: Aspose.Cells**
### **Spårar föregående**
Aspose.Cells gör det enkelt att få precedenter celler. Den kan inte bara hämta celler som tillhandahåller data till enkla formelprecedenter utan också hitta celler som tillhandahåller data till komplexa formelprecedenter med namngivna områden.

I exemplet nedan används en template excelfil, Book1.xls. Kalkylarket har data och formler på den första arbetsbladet.

** Ingående kalkylblad ** 

![todo:image_alt_text](tracing-precedents-and-dependents-in-aspose-cells_2.png)

Aspose.Cells tillhandahåller metoden GetPrecedents för Cellklassen som används för att spåra en cells precedenter. Den returnerar en ReferredAreaCollection. Som du kan se ovan, i Book1.xls, innehåller cellen B7 formeln "=SUM(A1:A3)". Så cellerna A1:A3 är de precedente cellerna till cellen B7. Följande exempel demonstrerar spåra-precedenter-funktionen med hjälp av mallfilen Book1.xls.

**C#**

{{< highlight csharp >}}

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
### **Spårar beroende**
Aspose.Cells låter dig få beroende celler i kalkylblad. Aspose.Cells kan inte bara hämta celler som tillhandahåller data för enkel formel utan också hitta celler som tillhandahåller data till komplexa formelberoenden med namngivna områden.

Aspose.Cells tillhandahåller metoden GetDependents för Cellklassen som används för att spåra en cells beroenden. Till exempel, i Book1.xlsx finns formlerna: "=A1+20" och "=A1+30" i cellerna B2 och C2. Följande exempel demonstrerar hur man spårar beroenden för cellen A1 med hjälp av mallfilen Book1.xlsx.

**C#**

{{< highlight csharp >}}

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
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Tracing%20Precedents%20and%20Dependents)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

{{< app/cells/assistant language="csharp" >}}
