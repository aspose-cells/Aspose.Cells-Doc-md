---
title: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 80
url: /sv/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Den här artikeln förklarar hur man använder C# API eller .NET bibliotekets exempelkod för att kopiera sidlayoutinställningar från källark till destinationsark programmatiskt.
keywords: kopiera sidlayoutinställningar c#, kopiera sidlayoutinställningar till målock c#
---

## **Möjliga användningsscenario**

När du lägger till ett nytt blad i en arbetsbok innehåller den standard *Sidlayoutinställningar*. Det kan finnas tillfällen när du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) från ett blad till ett annat blad. Detta dokument förklarar hur man kopierar sidlayoutinställningar från ett blad till ett annat med hjälp av Aspose.Cells API:er.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar *sidlayoutinställningar* från ett blad till ett annat med hjälp av [**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)-metoden. Se följande exempelkod och dess konsolresultat som referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
