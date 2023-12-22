---
title: Zeilen automatisch anpassen für zusammengeführte Zeilen Cells
type: docs
weight: 120
url: /de/net/autofit-rows-for-merged-cells/
---
{{% alert color="primary" %}}

Microsoft Excel bietet eine Funktion, mit der Sie die Höhe einer Zelle automatisch entsprechend ihrem Inhalt anpassen können. Die Funktion wird als automatische Zeilenanpassung bezeichnet. Microsoft Excel legt den automatischen Anpassungsvorgang für zusammengeführte Zellen nicht nativ fest. Manchmal ist die Funktion für einen Benutzer von entscheidender Bedeutung, der die automatische Zeilenanpassung auch für verbundene Zellen implementieren muss.

{{% /alert %}}

##  **So verwenden Sie AutoFitMergedCellsType für die automatische Anpassung von Zeilen**
 Aspose.Cells unterstützt diese Funktion durch[**AutoFitterOptions.AutoFitMergedCellsType**](https://reference.aspose.com/cells/net/aspose.cells/autofitmergedcellstype/)API. Mit dieser API ist es möglich, Zeilen in einem Arbeitsblatt einschließlich zusammengeführter Zellen automatisch anzupassen. Hier ist eine Liste aller möglichen Arten der automatischen Anpassung zusammengeführter Zellen:

- Keiner
- Erste Linie
- Letzte Linie
- Jede Zeile

##  **Zeilen für zusammengeführte Zeilen automatisch anpassen Cells**

Bitte sehen Sie sich den folgenden Code an. Er erstellt ein Arbeitsmappenobjekt und fügt mehrere Arbeitsblätter hinzu. Verwenden Sie in jedem Arbeitsblatt unterschiedliche Methoden für Autofit-Vorgänge. Der Screenshot zeigt die Ergebnisse nach der Ausführung des Beispielcodes.

<br>
<img src="result.png" width=80% />

##  **C# Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AutoFitRowsMergedCells-1.cs" >}}
