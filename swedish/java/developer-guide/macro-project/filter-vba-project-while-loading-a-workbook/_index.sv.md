---
title: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 70
url: /sv/java/filter-vba-project-while-loading-a-workbook/
---

## **Möjliga användningsscenario**
Vissa .xlsm/.xslb-filer har en extremt stor mängd makron (eller väldigt, väldigt långa makron). Aspose.Cells kommer ovillkorligen att ladda denna (meta)data när sådana arbetsböcker öppnas. Du kan behöva kontrollera detta genom LoadDataFilterOptions, när du verkligen bara behöver extrahera kalkylbladsnamn för ett stort antal arbetsböcker och därmed hoppa över sådan onödig innehåll. Denna filter tillhandahålls genom att introducera den nya LoadDataFilterOptions.VBA-optionen.
## **Exempelkod**
Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. Provfil för att testa denna funktion kan laddas ner från nedanstående länk:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Ange laddningsalternativen, vi vill inte ladda VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Skapa arbetsboksobjekt från provexcel-fil med laddningsalternativ
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Spara utmatningen i pdf-format
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
