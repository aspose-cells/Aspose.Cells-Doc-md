---
title: Manipulera namngivet område i en arbetsbok
type: docs
weight: 90
url: /sv/cpp/manipulate-named-range-in-a-workbook/
---
##  **Möjliga användningsscenarier**
 Aspose.Cells stöder manipulering av befintliga namngivna intervall. Alla befintliga namngivna intervall kan nås från[Workbook.GetWorksheets().GetNames()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getnames/) samling. När du väl kommer åt det namngivna området kan du ändra dess olika metoder, t.ex[GetFullText](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)och[GetRefersTo](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/).
##  **Manipulera namngivet område i en arbetsbok**
 Följande exempelkod läser det första namngivna intervallet inuti[source excel-fil](23167008.xlsx) och skriver ut sin[Full text](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)och[Refererar till](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) egenskaper på konsolen. Efter det ändrar den `RefersTo`-egenskapen och sparar[output excel-fil](23167009.xlsx).
##  **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook-new.cpp" >}}
##  **Konsolutgång**
 Följande konsolutdata skriver ut värdena för[Full text](https://reference.aspose.com/cells/cpp/aspose.cells/name/getfulltext/)och[Refererar till](https://reference.aspose.com/cells/cpp/aspose.cells/name/getrefersto/) medlemmar av det befintliga*Namngiven Range*ovanstående kod.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
