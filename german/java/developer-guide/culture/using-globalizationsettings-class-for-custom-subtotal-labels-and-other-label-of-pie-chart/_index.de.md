---
title: Verwendung der GlobalizationSettings Klasse für benutzerdefinierte Teilergebnisbezeichnungen und andere Beschriftungen des Kuchendiagramms
type: docs
weight: 50
url: /de/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells APIs haben die Klasse [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) freigelegt, um mit Szenarien umzugehen, in denen der Benutzer benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabellenkalkulation verwenden möchte. Außerdem kann die Klasse [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) auch verwendet werden, um die **Andere**-Beschriftung für das Kreisdiagramm zu ändern, während das Arbeitsblatt oder das Diagramm gerendert wird.
## **Einführung in die GlobalizationSettings-Klasse**
Die [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse bietet derzeit die folgenden 3 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um gewünschte Beschriftungen für die Zwischensummen zu erhalten oder benutzerdefinierten Text für die **Andere**-Beschriftung eines Kreisdiagramms zu rendern.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Ruft den Gesamtnamen der Funktion ab.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Ruft den Gesamtsummen-Namen der Funktion ab.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Ruft den Namen der "Andere"-Beschriftungen für Kreisdiagramme ab.
### **Benutzerdefinierte Beschriftungen für Zwischensummen**
Die [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse kann verwendet werden, um die Zwischensummen-Beschriftungen anzupassen, indem die Methoden [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) überschrieben werden, wie im Folgenden dargestellt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Um benutzerdefinierte Beschriftungen einzufügen, muss die Eigenschaft [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) einem Exemplar der oben definierten *CustomSettings*-Klasse vor dem Hinzufügen der Zwischensummen auf dem Arbeitsblatt zugewiesen werden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

Die [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse funktioniert nur bei Hinzufügen neuer Zwischensummen. Wenn eine Tabellenkalkulation bereits Zwischensummen enthält, können ihre Beschriftungen nicht geändert werden.

{{% /alert %}} 
### **Benutzerdefinierter Text für Andere Beschriftung im Kreisdiagramm**
Die [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse bietet die Methode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)), die nützlich ist, um der "Andere"-Beschriftung von Kreisdiagrammen einen benutzerdefinierten Wert zu geben. Der folgende Code definiert eine benutzerdefinierte Klasse und überschreibt die Methode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)), um basierend auf der für JVM festgelegten Standardsprache eine benutzerdefinierte Beschriftung zu erhalten.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Der folgende Code lädt eine vorhandene Tabellenkalkulation mit einem Kreisdiagramm und rendert das Diagramm zu einem Bild, während die erstellte *CustomSettings*-Klasse verwendet wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Das folgende Bild zeigt das Ergebnis, wenn die Regionaleinstellung des Rechners auf Frankreich gesetzt ist. Wie Sie sehen können, wurde das Label "Other" gemäß der Definition in der Klasse *CustomSettings* in "Autre" übersetzt.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
