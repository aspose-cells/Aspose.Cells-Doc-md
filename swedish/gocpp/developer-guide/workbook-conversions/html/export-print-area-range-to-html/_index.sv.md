---
title: Exportera utskriftsområdeinterval till HTML med Golang via C++
linktitle: Exportera utskriftsområdet till HTML
type: docs
weight: 60
url: /sv/go-cpp/export-print-area-range-to/
description: Lär dig hur du exporterar utskriftsområdet till HTML med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**

Detta är ett vanligt scenario där vi behöver exportera endast utskriftsområdet, dvs. ett valt cellintervall, istället för hela bladet till HTML. Denna funktion är redan tillgänglig för PDF-rendering; nu kan du även göra detta för HTML. Först, ställ in utskriftsområdet i arbetsbladets siduppsättningsobjekt. Därefter, använd [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/)-flaggan för att exportera endast det valda området.

## **Exempelkod**

Följande exempel kod hjälper dig att ladda en arbetsbok och sedan exportera utskriftsområdet till HTML. Testfilen för denna funktion kan laddas ner via länken:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
