---
title: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 80
url: /sv/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Den här artikeln förklarar hur man använder Aspose.Cells för Python via .NET exempelkoden för att kopiera Sidlayout inställningar från källkalkylbladet till målkalkylbladet programmatiskt.
keywords: Python Excel bibliotek, Python kopiera sidlayout inställningar, kopiera sidlayout inställningar till målkalkylblad i Python.
---

## **Möjliga användningsscenario**

När du lägger till ett nytt blad i en arbetsbok innehåller det standard *Sidlayout inställningar*. Det kan finnas tillfällen när du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) från ett kalkylblad till ett annat kalkylblad. Det här dokumentet förklarar hur man kopierar Sidlayout inställningar från ett kalkylblad till ett annat med hjälp av Aspose.Cells för Python via .NET APIer.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar *sidlayoutinställningar* från ett blad till ett annat med hjälp av [**PageSetup.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/copy/#aspose.cells.PageSetup-aspose.cells.CopyOptions)-metoden. Se följande exempelkod och dess konsolresultat som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
