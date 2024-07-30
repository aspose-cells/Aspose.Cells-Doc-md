---
title: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 60
url: /sv/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I den här artikeln kommer du att lära dig hur man tar bort befintliga PrinterSettings på arbetsbladet i Excel filen genom siduppsättningsobjektet programmatiskt med exempelkod med hjälp av Aspose.Cells för Python Excel biblioteket.
keywords: Python Excel bibliotek, Python ta bort skrivarens inställningar på arbetsbladet, Python ta bort skrivarens inställningar på excel ark.
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra Excel från att inkludera *.bin*-filer av skrivarens inställningar i de sparade XLSX-filerna. Skrivarens inställningsfiler finns under *"[fil "root"]\xl\printerSettings".* Detta dokument förklarar hur man tar bort befintliga skrivarens inställningar med hjälp av Aspose.Cells för Python via .NET API:er.

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells för Python via .NET låter dig ta bort befintliga skrivarens inställningar som angetts för olika ark i Excel-filen. Följande exempelkod illustrerar hur man tar bort befintliga skrivarens inställningar för alla arbetsblad i arbetsboken. Se dess [exempelfil av Excel](45056020.xlsx), [utdata-Excel-filen](45056021.xlsx), konsolresultat samt skärmdump för en referens.

## **Skärmdump**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-RemoveExistingPrinterSettingsOfWorksheets.py" >}}

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
