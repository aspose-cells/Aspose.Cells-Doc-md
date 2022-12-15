---
title: Manipulera namngivet område i en arbetsbok
type: docs
weight: 90
url: /sv/cpp/manipulate-named-range-in-a-workbook/
---
## **Möjliga användningsscenarier**
 Aspose.Cells stöder manipulering av befintliga namngivna intervall. Alla befintliga namngivna intervall kan nås från[IWorkbook.GetIWorksheets().GetINames()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa9e7bc07917a152a2c0de161cca133fa) samling. När du väl kommer åt det namngivna området kan du ändra dess olika metoder, t.ex[GetFullText](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)och[GetRefersTo](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36).
## **Manipulera namngivet område i en arbetsbok**
 Följande exempelkod läser det första namngivna intervallet inuti[källkod excel-fil](23167008.xlsx) och skriver ut sin[Full text](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)och[Refererar till](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) egenskaper på konsolen. Efter det ändrar den `RefersTo`-egenskapen och sparar[output excel-fil](23167009.xlsx).
## **Exempelkod**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ManipulateNamedRangeInWorkbook.cpp" >}}
## **Konsolutgång**
 Följande konsolutdata skriver ut värdena för[Full text](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#a5b450ef193365dec035c58280fbe9563)och[Refererar till](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_name#afdb10a12d8d395ae81de231f017eba36) medlemmar av det befintliga*Namngiven Range*i ovanstående kod.

{{< highlight "java" >}}

 Full Text: TestRange

Refers To: =Sheet1!$D$3:$G$6

{{< /highlight >}}
