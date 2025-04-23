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

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-): Holt den Total-Namen der Funktion.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-): Holt den Gesamttotal-Namen der Funktion.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--): Holt den Namen für "Andere"-Labels bei Kreisdiagrammen.
### **Benutzerdefinierte Beschriftungen für Zwischensummen**
Die Klasse [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) kann verwendet werden, um die Subtotal-Labels durch Überschreiben der Methoden [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName-int-) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName-int-) individuell anzupassen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Um benutzerdefinierte Beschriftungen einzufügen, muss die Eigenschaft [WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) einem Exemplar der oben definierten *CustomSettings*-Klasse vor dem Hinzufügen der Zwischensummen auf dem Arbeitsblatt zugewiesen werden.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

Die [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse funktioniert nur bei Hinzufügen neuer Zwischensummen. Wenn eine Tabellenkalkulation bereits Zwischensummen enthält, können ihre Beschriftungen nicht geändert werden.

{{% /alert %}} 
### **Benutzerdefinierter Text für Andere Beschriftung im Kreisdiagramm**
Die Klasse [GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) bietet die Methode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--) an, die nützlich ist, um dem "Other"-Label in Kreisdiagrammen einen benutzerdefinierten Wert zu geben. Das folgende Codebeispiel definiert eine benutzerdefinierte Klasse und überschreibt die Methode [getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName--), um eine benutzerdefinierte Beschriftung anhand der Standardspracheinstellung für JVM zu erhalten.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


Der folgende Code lädt eine vorhandene Tabellenkalkulation mit einem Kreisdiagramm und rendert das Diagramm zu einem Bild, während die erstellte *CustomSettings*-Klasse verwendet wird.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


Das folgende Bild zeigt das Ergebnis, wenn die Regionaleinstellung des Rechners auf Frankreich gesetzt ist. Wie Sie sehen können, wurde das Label "Other" gemäß der Definition in der Klasse *CustomSettings* in "Autre" übersetzt.

![todo:image_alt_text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
{{< app/cells/assistant language="java" >}}
