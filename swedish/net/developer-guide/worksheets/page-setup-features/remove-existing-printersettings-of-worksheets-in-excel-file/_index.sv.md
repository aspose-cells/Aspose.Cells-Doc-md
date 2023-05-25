---
title: Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil
type: docs
weight: 60
url: /sv/net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I den här artikeln kommer du att lära dig hur du tar bort befintliga skrivarinställningar för kalkylblad i Excel-filen via Utskriftsformatsobjektet programmatiskt med exempelkod med hjälp av C# API eller .NET Library.
keywords: remove printer settings of worksheet c#, remove printer settings of excel worksheet c#
---
##  **Möjliga användningsscenarier**
Ibland vill utvecklare hindra Excel från att inkludera*.bin* filer med skrivarinställningar i de sparade XLSX-filerna. Skrivarinställningar finns under*"[fil "root"]\xl\skrivarinställningar".* Det här dokumentet förklarar hur du tar bort befintliga skrivarinställningar med Aspose.Cells API:er.
##  **Ta bort befintliga skrivarinställningar för arbetsblad i Excel-fil**
Aspose.Cells låter dig ta bort befintliga skrivarinställningar som anges för olika ark i Excel-filen. Följande exempelkod illustrerar hur du tar bort befintliga skrivarinställningar för alla kalkylblad i arbetsboken. Vänligen se den[exempel på Excel-fil](45056020.xlsx), [utdata Excel-fil](45056021.xlsx)konsolutgång samt skärmdumpen för en referens.
##  **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)
##  **Exempelkod**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.cs" >}}
##  **Konsolutgång**
{{< highlight "java" >}}

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
