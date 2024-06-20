---
title: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 70
url: /de/java/filter-vba-project-while-loading-a-workbook/
---

## **Mögliche Verwendungsszenarien**
Einige .xlsm/.xslb-Dateien enthalten eine extrem große Anzahl von Makros (oder sehr, sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten bedingungslos beim Öffnen solcher Arbeitsmappen. Möglicherweise müssen Sie dies jedoch über LoadDataFilterOptions steuern, wenn Sie wirklich nur die Blattnamen für eine große Anzahl von Arbeitsmappen extrahieren müssen und somit über solchen unnötigen Inhalt hinwegspringen müssen. Dieser Filter wird eingeführt durch Einführung der neuen Option LoadDataFilterOptions.VBA.
## **Beispielcode**
Der folgende Beispielcode lädt eine Arbeitsmappe so, dass nur VBA gefiltert wird. Die Beispieldatei zum Testen dieses Features kann über folgenden Link heruntergeladen werden:

[sampleMacroEnabledWorkbook.xlsm](79527951.xlsm)

// Setzen Sie die Ladefilteroptionen, wir möchten das VBA nicht laden
LoadOptions loadOptions = new LoadOptions(LoadFormat.AUTO);
loadOptions.setLoadFilter(new LoadFilter(LoadDataFilterOptions.ALL & ~LoadDataFilterOptions.VBA));

// Erstellen Sie ein Arbeitsmappenobjekt aus der Beispieldatei mit den Ladefilteroptionen
Workbook book = new Workbook(srcDir + "sampleMacroEnabledWorkbook.xlsm", loadOptions);

// Speichern Sie die Ausgabe im PDF-Format
book.save(outDir + "OutputSampleMacroEnabledWorkbook.xlsm", SaveFormat.XLSM);
