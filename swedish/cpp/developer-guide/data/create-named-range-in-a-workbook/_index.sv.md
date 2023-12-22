---
title: Skapa namngivna intervall i en arbetsbok
type: docs
weight: 60
url: /sv/cpp/create-named-range-in-a-workbook/
---
##  **Möjliga användningsscenarier**
 Aspose.Cells stöder skapandet av ett namngivet intervall. Det finns olika sätt att skapa ett namngivet intervall. Ett av de enklaste sätten är att först skapa[Räckvidd](https://reference.aspose.com/cells/cpp/aspose.cells/range) objekt och ställ sedan in dess namn med[Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname) metod. Du kan se alla namngivna intervall i din excel-fil via Microsoft Excel*Namnchef*gränssnitt.
##  **Skapa namngivna intervall i en arbetsbok**
 Följande exempelkod förklarar hur du skapar en*Namngiven Range* via Aspose.Cells. En gång, den*Namngiven Range* skapas, är det synligt inuti[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) samling. Vänligen se[output excel-fil](23167006.xlsx) genereras av koden för en referens.
##  **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsolutgång**
 Följande konsolutdata skriver ut värdena för[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) och[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) metoder för det skapade*Namngiven Range*ovanstående kod.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
