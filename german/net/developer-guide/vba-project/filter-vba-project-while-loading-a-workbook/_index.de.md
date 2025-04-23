---
title: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/net/filter-vba-project-while-loading-a-workbook/
---

## **Filtern Sie das VBA-Projekt beim Laden einer Excel-Arbeitsmappe in C#**

Einige .xlsm/.xslb-Dateien enthalten eine extrem große Anzahl von Makros (oder sehr, sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten bedingungslos, wenn solche Arbeitsmappen geöffnet werden. Es kann sein, dass Sie dies kontrollieren müssen, wenn Sie wirklich nur die Blattnamen für eine große Anzahl von Arbeitsmappen extrahieren müssen und daher solche unerwünschten Inhalte überspringen möchten. Dieser Filter wird durch Einführung einer neuen Option, [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions), bereitgestellt.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
