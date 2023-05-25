---
title: Kopiera inställningar för sidinställningar från källarbetsbladet till målarbetsbladet
type: docs
weight: 80
url: /sv/net/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Den här artikeln förklarar hur du använder C# API eller .NET biblioteksexempelkod för att kopiera inställningar för utskriftsformat från källarbetsbladet till målarbetsbladet programmatiskt.
keywords: copy page setup settings c#, copy page setup settings to target worksheet c#
---
##  **Möjliga användningsscenarier**

När du lägger till ett nytt ark i en arbetsbok innehåller det standardinställningarna för *Sidinställningar*. Det kan finnas tillfällen då du behöver överföra inställningarna ([**Utskriftsformat**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)) från ett kalkylblad till ett annat kalkylblad. Det här dokumentet förklarar hur du kopierar inställningar för sidinställningar från ett kalkylblad till ett annat med hjälp av Aspose.Cells API:er.

##  **Kopiera inställningar för sidinställningar från källarbetsbladet till målarbetsbladet**

Följande exempelkod illustrerar hur du kopierar*Utskriftsinställningar*från ett kalkylblad till ett annat med hjälp av[**PageSetup.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/copy)metod. Se följande exempelkod och dess konsolutgång för en referens.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.cs" >}}

##  **Konsolutgång**

{{< highlight "java" >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
