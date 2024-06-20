---
title: Manipulera namngivet område i en arbetsbok
type: docs
weight: 90
url: /sv/cpp/manipulate-named-range-in-a-workbook/
---

## **Möjliga användningsscenario**
Aspose.Cells stödjer manipulation av befintliga namngivna områden. Alla befintliga namngivna områden kan kommas åt från [arbetsbok.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) samlingen. När du har åtkomst till det namngivna området, kan du ändra dess olika metoder som t.ex. [GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) och [GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
## **Manipulera namngivet område i en arbetsbok**
Följande exempelkod läser det första namngivna området i [käll excelfilen](23167008.xlsx) och skriver ut dess [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) och [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) egenskaper på konsolen. Efter det modifierar det `RefersTo` egenskapen och sparar den [utdata excelfilen](23167009.xlsx).
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
## **Konsoloutput**
Följande konsoloutput skriver ut värdena för [FullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/) och [RefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) medlemmar av det befintliga *Namngivna området* i ovanstående kod.

{{< highlight java >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
