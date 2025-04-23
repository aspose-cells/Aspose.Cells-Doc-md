---
title: Ta bort befintliga utskriftsinställningar för kalkylblad i Excel filen
type: docs
weight: 60
url: /sv/python-net/remove-existing-printersettings-of-worksheets-in-excel-file/
description: I denna artikel lär du dig hur du tar bort befintliga PrinterSettings för kalkylbladet inuti Excel filen via Page Setup objektet programmässigt med exempelcode med hjälp av Aspose.Cells för Python Excel Library.
keywords: Python Excel Library, Python ta bort skrivareinställningar för kalkylblad, Python ta bort skrivareinställningar för Excel kalkylblad.
---

## **Möjliga användningsscenario**
Ibland vill utvecklare förhindra att Excel inkluderar *.bin* filer med skrivareinställningar i de sparade XLSX-filerna. Skrivareinställningsfiler finns under *“[fil "root"]\xl\printerSettings”.* Denna dokumentation förklarar hur man tar bort befintliga skrivareinställningar med Aspose.Cells för Python via .NET API:er.

## **Ta bort befintliga skrivareinställningar för arbetsblad i Excel-fil**
Aspose.Cells för Python via .NET låter dig ta bort befintliga skrivareinställningar som anges för olika blad i Excel-filen. Följande exempel visar hur man tar bort befintliga skrivareinställningar för alla kalkylblad i arbetsboken. Se dess [exempel-Excel-fil](45056020.xlsx), [utdata-Excel-fil](45056021.xlsx), konsolutdata samt screenshot för referens.

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
