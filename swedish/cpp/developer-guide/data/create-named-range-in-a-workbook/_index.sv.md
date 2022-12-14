---
title: Skapa namngivna intervall i en arbetsbok
type: docs
weight: 60
url: /sv/cpp/create-named-range-in-a-workbook/
---
## **Möjliga användningsscenarier**
 Aspose.Cells stöder skapandet av ett namngivet intervall. Det finns olika sätt att skapa ett namngivet intervall. Ett av de enklaste sätten är att först skapa[IRange](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range) objekt och ställ sedan in dess namn med[IRange.SetName()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_range#a78480b6b6db0f24cffc8acc2b06552eb) metod. Du kan se alla namngivna intervall i din excel-fil via Microsoft Excel*Namnchef*gränssnitt.
## **Skapa namngivna intervall i en arbetsbok**
 Följande exempelkod förklarar hur du skapar en*Namngiven Range* via Aspose.Cells. En gång, den*Namngiven Range* skapas, är det synligt inuti[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) samling. Vänligen se[output excel-fil](23167006.xlsx) genereras av koden för en referens.
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-CreateNamedRangeInWorkbook.cpp" >}}
## **Konsolutgång**
 Följande konsolutdata skriver ut värdena för[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563) och `GetRefersTo` metoder för den skapade*Namngiven Range*i ovanstående kod.

{{< highlight "java" >}}

 Full Text: MyNamedRange

Refers To: =Sheet1!$A$5:$C$10

{{< /highlight >}}
