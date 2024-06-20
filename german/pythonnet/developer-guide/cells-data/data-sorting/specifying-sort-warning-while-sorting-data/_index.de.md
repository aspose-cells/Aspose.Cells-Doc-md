---
title: Angabe von Sortierwarnungen beim Sortieren von Daten.
type: docs
weight: 140
url: /de/python-net/specifying-sort-warning-while-sorting-data/
description: Erfahren Sie, wie Sie Warnhinweise beim Sortieren von Daten mithilfe der Aspose.Cells für Python via .NET API festlegen.
keywords: Python Excel Bibliothek, Warnmeldung hinzufügen beim Sortieren von Daten, Warnung einstellen beim Sortieren von Daten in Python, Warnmeldung auswählen beim Sortieren von Daten
---

## **Mögliche Verwendungsszenarien**

Betrachten Sie bitte diese Textdaten, d.h. {11, 111, 22}. Diese Textdaten werden sortiert, da 111 vor 22 kommt. Wenn Sie jedoch möchten, dass diese Daten nicht als Text, sondern als Zahlen sortiert werden, werden sie zu {11, 22, 111}, weil numerisch 111 nach 22 kommt. Aspose.Cells für Python via .NET bietet die Eigenschaft {0}, um dieses Problem zu behandeln. Bitte setzen Sie diese Eigenschaft auf **true** und Ihre Textdaten werden als numerische Daten sortiert. Der folgende Screenshot zeigt den Sortierhinweis, den Microsoft Excel anzeigt, wenn Textdaten, die wie numerische Daten aussehen, sortiert werden.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Beispielcode**

Der folgende Beispielscode veranschaulicht die Verwendung der [**DataSorter.sort_as_number**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_as_number/)-Eigenschaft wie zuvor erläutert. Bitte überprüfen Sie die [Beispieldatei Excel](43352075.xlsx) und die [Ausgabedatei Excel](43352076.xlsx) für mehr Hilfe.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SpecifyingSortWarningWhileSortingData.py" >}}
