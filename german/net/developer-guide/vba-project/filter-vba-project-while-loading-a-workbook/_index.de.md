---
title: Filtern Sie VBA-Projekte beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/net/filter-vba-project-while-loading-a-workbook/
---
## **Filtern Sie VBA-Projekt beim Laden einer Excel-Arbeitsmappe in C#**

Einige .xlsm/.xslb-Dateien enthalten extrem viele Makros (oder sehr, sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsmappen bedingungslos. Möglicherweise müssen Sie dies jedoch kontrollieren[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) wenn Sie wirklich nur Blattnamen für eine große Anzahl von Arbeitsmappen extrahieren müssen, wodurch solche nicht benötigten Inhalte übersprungen werden. Dieser Filter wird durch die Einführung einer neuen Option bereitgestellt,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Beispielcode**

Der folgende Beispielcode lädt eine Arbeitsmappe, sodass nur VBA gefiltert wird. Eine Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
