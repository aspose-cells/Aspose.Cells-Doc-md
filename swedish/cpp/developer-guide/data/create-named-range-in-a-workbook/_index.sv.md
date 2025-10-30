---
title: Skapa namngivet område i en arbetsbok
type: docs
weight: 60
url: /sv/cpp/create-named-range-in-a-workbook/
---

## **Möjliga användningsscenario**
Aspose.Cells stödjer skapandet av ett namngivet område. Det finns olika sätt att skapa ett namngivet område. Ett av de enklaste sätten är att först skapa [Range](https://reference.aspose.com/cells/cpp/aspose.cells/range) objekt och sedan ställa in dess namn med hjälp av metoden [Range.SetName()](https://reference.aspose.com/cells/cpp/aspose.cells/range/setname). Du kan se alla namngivna områden i din excelfil via Microsoft Excel *Namnhanterare* gränssnittet.
## **Skapa namngivet område i en arbetsbok**
Följande exempel på kod förklarar hur man skapar ett *Namngivet område* via Aspose.Cells. När *Namngivet område* är skapat, är det synligt inne i [arbetsbok.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames) samlingen. Se den [utdata excelfilen](23167006.xlsx) genererad av koden för referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook-new.cpp" >}}
## **Konsoloutput**
Följande konsoloutput skriver ut värdena för [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) och [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) metoder för det skapade *Namngivna området* i ovanstående kod.

{{< highlight java >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
