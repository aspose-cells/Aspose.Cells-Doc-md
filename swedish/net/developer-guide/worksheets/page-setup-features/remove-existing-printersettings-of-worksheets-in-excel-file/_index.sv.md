---
title: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 60
url: /sv/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I den här artikeln kommer du att lära dig hur du tar bort befintliga skrivarinställningar för kalkylblad inuti Excel filen genom Page Setup objektet programmatiskt med exempelkod med användning av C# API eller .NET bibliotek.
keywords: ta bort skrivarinställningar för kalkylblad c#, ta bort skrivareinställningar för excel kalkylblad c#
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra Excel från att inkludera *.bin*-filer av skrivarinställningar i sparade XLSX-filer. Skrivarinställningsfiler finns under *“[fil "root"]\xl\printerSettings”.* I den här dokumentationen förklaras hur man tar bort befintliga skrivarinställningar med Aspose.Cells-API:er.
## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells möjliggör att ta bort befintliga skrivarinställningar som är specificerade för olika kalkylblad i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Se dess [exempelfil för Excel](45056020.xlsx), [utdata för Excel-fil](45056021.xlsx), konsolresultat samt skärmdumpen som referens.
## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
## **Konsoloutput**
{{< highlight java >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
