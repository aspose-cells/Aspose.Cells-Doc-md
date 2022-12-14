---
title: Filtrera VBA-projekt när en arbetsbok laddas
type: docs
weight: 70
url: /sv/java/filter-vba-project-while-loading-a-workbook/
---
## **Möjliga användningsscenarier**
Vissa .xlsm/.xslb-filer har extremt många makron (eller väldigt, väldigt långa makron). Aspose.Cells kommer ovillkorligen att ladda dessa (meta)data när sådana arbetsböcker öppnas. Du kan behöva kontrollera detta genom LoadDataFilterOptions, när du egentligen bara behöver extrahera arknamn för ett stort antal arbetsböcker och därmed hoppa över sådant onödigt innehåll. Detta filter tillhandahålls genom att introducera det nya alternativet LoadDataFilterOptions.VBA.
## **Exempelkod**
Följande exempelkod läser in en arbetsbok så att endast VBA filtreras. Exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Ställ in laddningsalternativen, vi vill inte ladda VBA
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(nytt LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Skapa arbetsboksobjekt från exempel i Excel-fil med laddningsalternativ
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Spara utdata i pdf-format
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
