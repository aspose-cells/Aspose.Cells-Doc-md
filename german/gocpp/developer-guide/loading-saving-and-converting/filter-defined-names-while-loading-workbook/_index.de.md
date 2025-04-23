---
title: Definierte Namen filtern beim Laden einer Arbeitsmappe
type: docs
weight: 50
url: /de/go-cpp/filter-defined-names-while-loading-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells ermöglicht es, definierte Namen in der Arbeitsmappe zu filtern oder zu entfernen. Bitte verwenden Sie [**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/), um definierte Namen beim Laden der Arbeitsmappe zu laden. Beachten Sie, dass das Entfernen definierter Namen Formeln in der Arbeitsmappe beeinträchtigen kann.

## **Definierte Namen filtern beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die [Beispieldatei Excel](61767860.xlsx), die eine Formel in Zelle **C1** enthält, die definierte Namen beinhaltet, z.B. *=SUM(MyName1, MyName2)*. Da wir ~[**LoadDataFilterOptions_DefinedNames**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions/) verwenden, um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, bricht die Formel in Zelle C1 der [Ausgabedatei Excel](61767861.xlsx) und es erscheint *#NAME?*. Unten sehen Sie einen Screenshot, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterDefinedNamesWhileLoadingWorkbook.go" >}}
