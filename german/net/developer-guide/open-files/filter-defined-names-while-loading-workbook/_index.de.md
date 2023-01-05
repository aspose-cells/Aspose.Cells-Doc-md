---
title: Filtern Sie definierte Namen beim Laden der Arbeitsmappe
type: docs
weight: 50
url: /de/net/filter-defined-names-while-loading-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht es Ihnen, definierte Namen in der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwende[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)um definierte Namen zu laden und ~ zu verwenden[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)um sie beim Laden der Arbeitsmappe zu entfernen. Bitte beachten Sie, dass Formeln in der Arbeitsmappe möglicherweise aufgelöst werden, wenn Sie definierte Namen entfernen.

## **Filtern Sie definierte Namen beim Laden der Arbeitsmappe**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](61767860.xlsx) die eine Formel in der Zelle hat**C1** mit den definierten Namen dh*=SUMME(MeinName1, MeinName2)*. Da wir ~ verwenden[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, die Formel in Zelle C1 ein[Excel-Datei ausgeben](61767861.xlsx) bricht auf und du siehst*#NAME?*stattdessen. Bitte sehen Sie sich den folgenden Screenshot an, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo: Bild_alt_Text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
