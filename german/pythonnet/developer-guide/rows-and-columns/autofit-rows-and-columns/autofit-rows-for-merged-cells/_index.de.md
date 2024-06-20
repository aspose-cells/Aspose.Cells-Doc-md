---
title: Zeilen für zusammengeführte Zellen automatisch anpassen
type: docs
weight: 120
url: /de/python-net/autofit-rows-for-merged-cells/
description: In diesem Artikel wird gezeigt, wie man mit Hilfe der Aspose.Cells für Python via .NET API Zeilen für zusammengeführte Zellen automatisch anpasst.
keywords: Python Excel Bibliothek, Python So verwenden Sie AutoFitMergedCellsType, um Zeilen automatisch anzupassen, Autofit Rows für zusammengeführte Zellen in Python.
---

{{% alert color="primary" %}}

Microsoft Excel bietet eine Funktion, die es Ihnen ermöglicht, die Höhe einer Zelle automatisch an den Inhalt anzupassen. Die Funktion wird als automatische Anpassung von Zeilen bezeichnet. Microsoft Excel führt die Autofit-Operation nicht nativ bei zusammengeführten Zellen durch. Manchmal wird die Funktion für einen Benutzer, der wirklich eine automatische Anpassung von Zeilen in zusammengeführten Zellen benötigt, unerlässlich.

{{% /alert %}}

## **Wie man AutoFitMergedCellsType zum Anpassen von Zeilen verwendet**
Aspose.Cells für Python via .NET unterstützt diese Funktion durch die [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/python-net/aspose.cells/autofitmergedcellstype/) API. Unter Verwendung dieser API ist es möglich, Zeilen in einem Arbeitsblatt einschließlich zusammengeführter Zellen automatisch anzupassen. Hier ist eine Liste aller möglichen Arten des automatischen Anpassens von zusammengeführten Zellen:

- NONE
- ERSTE_ZEILE
- LETZTE_ZEILE
- JEDE_ZEILE

## **AutoFit für zusammengeführte Zellen**

Bitte sehen Sie sich den folgenden Code an. Es erstellt ein Arbeitsmappenobjekt und fügt mehrere Arbeitsblätter hinzu. Verwenden Sie verschiedene Methoden für Autofit-Operationen in jedem Arbeitsblatt. Der Screenshot zeigt die Ergebnisse nach der Ausführung des Beispielscodes.

<br>
<img src="result.png" width=80% />

## **C# Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutoFitRowsMergedCells-1.py" >}}
