---
title: Filtern des VBA Projekts beim Laden einer Arbeitsmappe
type: docs
weight: 140
url: /de/python-net/filter-vba-project-while-loading-a-workbook/
---

## **VBA-Projekt beim Laden einer Excel-Arbeitsmappe in Python filtern**

Einige .xlsm/.xslb-Dateien enthalten eine äußerst große Anzahl an Makros (oder sehr lange Makros). Aspose.Cells for Python via .NET lädt diese (Meta-)Daten unbesehen beim Öffnen solcher Arbeitsmappen. Sie müssen dies möglicherweise durch [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) steuern, wenn Sie nur die Blattnamen aus einer großen Anzahl von Arbeitsmappen extrahieren möchten und solche unnötigen Inhalte überspringen.

## **Beispielcode**

Der folgende Beispielscode lädt eine Arbeitsmappe so, dass nur das VBA gefiltert wird. Eine Testdatei für dieses Feature können Sie über den folgenden Link herunterladen:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
