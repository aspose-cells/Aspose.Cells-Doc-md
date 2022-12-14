---
title: Filtern Sie VBA-Projekte beim Laden einer Arbeitsmappe
type: docs
weight: 70
url: /de/java/filter-vba-project-while-loading-a-workbook/
---
## **Mögliche Nutzungsszenarien**
Einige .xlsm/.xslb-Dateien enthalten extrem viele Makros (oder sehr, sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsmappen bedingungslos. Möglicherweise müssen Sie dies durch LoadDataFilterOptions steuern, wenn Sie wirklich nur Blattnamen für eine große Anzahl von Arbeitsmappen extrahieren müssen, wodurch solche nicht benötigten Inhalte übersprungen werden. Dieser Filter wird durch die Einführung der neuen Option LoadDataFilterOptions.VBA bereitgestellt.
## **Beispielcode**
Der folgende Beispielcode lädt eine Arbeitsmappe, sodass nur VBA gefiltert wird. Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Legen Sie die Ladeoptionen fest, wir wollen VBA nicht laden
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Arbeitsmappenobjekt aus Beispiel-Excel-Datei mit Ladeoptionen erstellen
Arbeitsmappenbuch = neue Arbeitsmappe (srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Speichern Sie die Ausgabe im PDF-Format
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
