---
title: Zeilen für zusammengeführte Zellen automatisch anpassen
type: docs
weight: 120
url: /de/net/autofit-rows-for-merged-cells/
---

{{% alert color="primary" %}}

Microsoft Excel bietet eine Funktion, die es Ihnen ermöglicht, die Höhe einer Zelle automatisch an den Inhalt anzupassen. Die Funktion wird als automatische Anpassung von Zeilen bezeichnet. Microsoft Excel führt die Autofit-Operation nicht nativ bei zusammengeführten Zellen durch. Manchmal wird die Funktion für einen Benutzer, der wirklich eine automatische Anpassung von Zeilen in zusammengeführten Zellen benötigt, unerlässlich.

{{% /alert %}}

## **Wie man AutoFitMergedCellsType zum Anpassen von Zeilen verwendet**
Aspose.Cells unterstützt diese Funktion über die [**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/) API. Mit dieser API ist es möglich, Zeilen in einem Arbeitsblatt einschließlich zusammengeführter Zellen automatisch anzupassen. Hier ist eine Liste aller möglichen Arten des automatischen Anpassens von zusammengeführten Zellen:

- Keine
- ErsteZeile
- LetzteZeile
- JedeZeile

## **AutoFit für zusammengeführte Zellen**

Bitte sehen Sie sich den folgenden Code an. Es erstellt ein Arbeitsmappenobjekt und fügt mehrere Arbeitsblätter hinzu. Verwenden Sie verschiedene Methoden für Autofit-Operationen in jedem Arbeitsblatt. Der Screenshot zeigt die Ergebnisse nach der Ausführung des Beispielscodes.

<br>
<img src="result.png" width=80% />

## **C# Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
