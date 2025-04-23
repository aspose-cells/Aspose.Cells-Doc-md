---
title: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 80
url: /sv/python-net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Denna artikel förklarar hur man använder exempel kod för Aspose.Cells för Python via .NET för att kopiera sidinställning från ett kälvarsarbetsblad till ett destinationsarbetsblad programmässigt.
keywords: Python Excel bibliotek, Python kopiera sidinställningar, kopiera sidinställningar till målblad i Python.
---

## **Möjliga användningsscenario**

När du lägger till ett nytt ark i en arbetsbok innehåller det standard *Sidinställningar*. Det kan finnas situationer när du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup)) från ett arbetsblad till ett annat. Denna dokument förklarar hur man kopierar sidinställningar från ett arbetsblad till ett annat med Aspose.Cells för Python via .NET API:er.

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
