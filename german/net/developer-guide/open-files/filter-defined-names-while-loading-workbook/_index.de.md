---
title: Definierte Namen filtern beim Laden einer Arbeitsmappe
type: docs
weight: 50
url: /de/net/filter-defined-names-while-loading-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es Ihnen, definierte Namen in der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwenden Sie [**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) zum Laden der definierten Namen und verwenden Sie ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions), um sie beim Laden der Arbeitsmappe zu entfernen. Bitte beachten Sie, dass beim Entfernen definierter Namen Formeln in der Arbeitsmappe möglicherweise zerspringen.

## **Definierte Namen filtern beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767860.xlsx), die eine Formel in der Zelle **C1** enthält, die die definierten Namen enthält, d.h. *=SUM(MyName1, MyName2)*. Da wir ~[**LoadDataFilterOptions.DefinedNames**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) verwenden, um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, bricht die Formel in Zelle C1 in der [Ausgabe-Excel-Datei](61767861.xlsx) ab und Sie sehen stattdessen *#NAME?*. Bitte beachten Sie den folgenden Screenshot, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Workbook-FilterDefinedNamesWhileLoadingWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
