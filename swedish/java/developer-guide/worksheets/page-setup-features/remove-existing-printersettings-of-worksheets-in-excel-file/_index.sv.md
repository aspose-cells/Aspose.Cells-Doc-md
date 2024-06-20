---
title: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 40
url: /sv/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra att Excel inkluderar *.bin* -filer för skrivareinställningar i de sparade XLSX-filerna. Skrivareinställningsfiler finns under *"[fil "rot"]\xl\printerSettings"*. Denna dokumentation förklarar hur man tar bort befintliga utskriftsinställningar med Aspose.Cells API: er.
## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells tillåter dig att ta bort befintliga utskriftsinställningar specificerade för olika blad i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga utskriftsinställningar för alla kalkylbladen i arbetsboken. Se dess [prov Excel-fil](45056023.xlsx), [utmatnings Excel-fil](45056024.xlsx), konsolresultat samt en skärmdump för referens.
## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Konsoloutput**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: 5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: 34

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: 70

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: 8

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
