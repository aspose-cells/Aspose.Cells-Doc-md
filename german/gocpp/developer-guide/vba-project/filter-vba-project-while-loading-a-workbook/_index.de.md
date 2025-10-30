---
title: Filtern des VBA Projekts beim Laden einer Arbeitsmappe mit Golang via C++
linktitle: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Lernen, wie man VBA Projekte beim Laden einer Excel Arbeitsmappe mit Aspose.Cells mit Golang via C++ filtert.
---

## **Filtern Sie VBA-Projekte beim Laden eines Excel-Arbeitsbuchs in C++**

Einige .xlsm/.xslb Dateien haben eine extrem große Anzahl an Makros (oder sehr lange Makros). Aspose.Cells lädt diese (Meta-)Daten beim Öffnen solcher Arbeitsbücher unbeding. Sie müssen dies jedoch mit [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) kontrollieren, wenn Sie nur Sheet-Namen extrahieren möchten, um so unnötigen Inhalt zu überspringen. Dieser Filter wird durch die Einführung einer neuen Option, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions), bereitgestellt.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
