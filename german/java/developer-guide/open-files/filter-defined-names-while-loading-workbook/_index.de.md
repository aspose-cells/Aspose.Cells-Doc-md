---
title: Filtern Sie definierte Namen beim Laden der Arbeitsmappe
type: docs
weight: 50
url: /de/java/filter-defined-names-while-loading-workbook/
---
## **Mögliche Nutzungsszenarien**

Aspose.Cells ermöglicht es Ihnen, definierte Namen in der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwende[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)um definierte Namen zu laden und ~ zu verwenden[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)um sie beim Laden der Arbeitsmappe zu entfernen. Bitte beachten Sie, dass Formeln in der Arbeitsmappe möglicherweise aufgelöst werden, wenn Sie definierte Namen entfernen.

## **Filtern Sie definierte Namen beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](61767873.xlsx)die eine Formel in Zelle C1 hat, die die definierten Namen enthält, dh*=SUMME(MeinName1, MeinName2)*. Da verwenden wir ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED_NAMES)um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, die Formel in Zelle C1 ein[Excel-Datei ausgeben](61767872.xlsx)bricht auf und du siehst*#NAME?*stattdessen. Bitte sehen Sie sich den folgenden Screenshot an, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo: Bild_alt_Text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
