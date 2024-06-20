---
title: Kopiera siduppsättning inställningar från kälark till destinationsark
type: docs
weight: 10
url: /sv/java/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
---

## **Möjliga användningsscenario**

När du lägger till en ny kalkylblad till en arbetsbok innehåller den standard siduppsättningsinställningar. Det kan finnas tillfällen då du behöver överföra inställningarna ([**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)) från ett kalkylblad till ett annat kalkylblad. Den här dokumentationen förklarar hur man kopierar siduppsättningsinställningar från ett kalkylblad till ett annat med hjälp av Aspose.Cells API:er.

## **Kopiera siduppsättning inställningar från källkalkylblad till destinations kalkylblad**

Följande exempelkod illustrerar hur man kopierar siduppsättningsinställningar från ett kalkylblad till ett annat med hjälp av [**PageSetup.Copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#copy(com.aspose.cells.PageSetup,%20com.aspose.cells.CopyOptions))-metoden. Se följande exempelkod och dess konsolresultat för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Worksheets-PageSetupFeatures-CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Before Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

Before Paper Size: PAPER_LETTER

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

After Paper Size: PAPER_A_3_EXTRA_TRANSVERSE

{{< /highlight >}}
