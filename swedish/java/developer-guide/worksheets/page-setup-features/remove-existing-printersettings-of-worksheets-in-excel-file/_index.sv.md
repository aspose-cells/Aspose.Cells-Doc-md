---
title: Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil
type: docs
weight: 40
url: /sv/java/remove-existing-printersettings-of-worksheets-in-excel-file/
---
## **Möjliga användningsscenarier**
Ibland vill utvecklare hindra Excel från att inkludera*.bin* filer med skrivarinställningar i de sparade XLSX-filerna. Skrivarinställningar finns under*“[fil "root"]\xl\skrivarinställningar”*. Det här dokumentet förklarar hur du tar bort befintliga skrivarinställningar med Aspose.Cells API:er.
## **Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil**
Aspose.Cells låter dig ta bort befintliga skrivarinställningar som anges för olika ark i Excel-filen. Följande exempelkod illustrerar hur du tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Vänligen se den[exempel på Excel-fil](45056023.xlsx), [utdata Excel-fil](45056024.xlsx)konsolutgång samt en skärmdump som referens.
## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.java" >}}
## **Konsolutgång**
{{< highlight "java" >}}

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
