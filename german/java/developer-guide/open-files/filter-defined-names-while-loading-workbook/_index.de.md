---
title: Definierte Namen filtern beim Laden einer Arbeitsmappe
type: docs
weight: 50
url: /de/java/filter-defined-names-while-loading-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, definierte Namen in der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwenden Sie [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) zum Laden der definierten Namen und verwenden Sie ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES), um sie beim Laden der Arbeitsmappe zu entfernen. Bitte beachten Sie, dass beim Entfernen definierter Namen Formeln in der Arbeitsmappe möglicherweise zerspringen.

## **Definierte Namen filtern beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767873.xlsx), die eine Formel in Zelle C1 enthält, die die definierten Namen d.h. *=SUM(MyName1, MyName2)* enthält. Da wir ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#DEFINED-NAMES) verwenden, um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, bricht die Formel in Zelle C1 in der [ausgegebenen Excel-Datei](61767872.xlsx) ab und Sie sehen *#NAME?* stattdessen. Bitte beachten Sie den folgenden Screenshot, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
