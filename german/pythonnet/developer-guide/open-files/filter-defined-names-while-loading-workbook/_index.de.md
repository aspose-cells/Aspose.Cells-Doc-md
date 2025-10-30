---
title: Definierte Namen filtern beim Laden einer Arbeitsmappe
type: docs
weight: 50
url: /de/python-net/filter-defined-names-while-loading-workbook/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells for Python via .NET ermöglicht es Ihnen, definierte Namen im Arbeitsbuch zu filtern oder zu entfernen. Verwenden Sie [**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/), um definierte Namen zu laden, und ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/), um sie beim Laden des Arbeitsbuchs zu entfernen. Bitte beachten Sie, dass das Entfernen definierter Namen dazu führen kann, dass Formeln im Arbeitsbuch nicht mehr korrekt funktionieren.

## **Definierte Namen filtern beim Laden der Arbeitsmappe**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767860.xlsx), die eine Formel in der Zelle **C1** enthält, die die definierten Namen enthält, d.h. *=SUM(MyName1, MyName2)*. Da wir ~[**LoadDataFilterOptions.DEFINED_NAMES**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/) verwenden, um die definierten Namen beim Laden der Arbeitsmappe zu entfernen, bricht die Formel in Zelle C1 in der [Ausgabe-Excel-Datei](61767861.xlsx) ab und Sie sehen stattdessen *#NAME?*. Bitte beachten Sie den folgenden Screenshot, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](filter-defined-names-while-loading-workbook_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDefinedNamesWhileLoadingWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
