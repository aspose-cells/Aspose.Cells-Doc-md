---
title: Verwenden der GlobalizationSettings-Klasse für benutzerdefinierte Zwischensummenbeschriftungen und andere Beschriftungen von Kreisdiagrammen
type: docs
weight: 50
url: /de/java/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---
## **Mögliche Nutzungsszenarien**
 Aspose.Cells APIs haben die ausgesetzt[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse, um mit den Szenarien fertig zu werden, in denen der Benutzer benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle verwenden möchte. Außerdem die[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)Klasse kann auch verwendet werden, um die zu ändern**Sonstiges** Bezeichnung für das Kreisdiagramm beim Rendern des Arbeitsblatts oder Diagramms.
## **Einführung in die GlobalizationSettings-Klasse**
 Das[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Die Klasse bietet derzeit die folgenden 3 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um gewünschte Beschriftungen für die Zwischensummen zu erhalten oder benutzerdefinierten Text für die zu rendern**Sonstiges** Beschriftung eines Tortendiagramms.

1. [GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)): Ruft den Gesamtnamen der Funktion ab.
1. [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)): Ruft den Gesamtsummennamen der Funktion ab.
1. [GlobalizationSettings.getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\)): Ruft den Namen von „Anderen“ Beschriftungen für Kreisdiagramme ab.
### **Benutzerdefinierte Beschriftungen für Zwischensummen**
 Das[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) -Klasse kann zum Anpassen der Zwischensummenbeschriftungen verwendet werden, indem die Klasse überschrieben wird[GlobalizationSettings.getTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getTotalName\(int\)) & [GlobalizationSettings.getGrandTotalName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getGrandTotalName\(int\)) Methoden wie oben gezeigt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Um benutzerdefinierte Labels einzufügen, ist es erforderlich, die zuzuweisen[WorkbookSettings.GlobalizationSettings](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#GlobalizationSettings) Eigenschaft zu einer Instanz der*Benutzerdefinierte Einstellungen*oben definierte Klasse, bevor Sie die Zwischensummen zum Arbeitsblatt hinzufügen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomLabelsforSubtotals-CustomLabelsforSubtotals.java" >}}

{{% alert color="primary" %}} 

 Das[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings)Klasse funktioniert nur zum Hinzufügen neuer Zwischensummen. Wenn eine Tabelle bereits Zwischensummen enthält, können ihre Beschriftungen nicht geändert werden.

{{% /alert %}} 
### **Benutzerdefinierter Text für andere Beschriftungen des Kreisdiagramms**
 Das[Globalisierungseinstellungen](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings) Klasse bietet die[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\) )-Methode, die nützlich ist, um der Bezeichnung „Andere“ von Kreisdiagrammen einen benutzerdefinierten Wert zuzuweisen. Der folgende Codeausschnitt definiert eine benutzerdefinierte Klasse und überschreibt die[getOtherName](https://reference.aspose.com/cells/java/com.aspose.cells/globalizationsettings#getOtherName\(\))-Methode, um eine benutzerdefinierte Bezeichnung basierend auf der für JVM festgelegten Standardsprache abzurufen.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomSettings-CustomSettings.java" >}}


 Das folgende Snippet lädt eine vorhandene Tabelle, die ein Kreisdiagramm enthält, und rendert das Diagramm in ein Bild, während es verwendet wird*Benutzerdefinierte Einstellungen*oben erstellte Klasse.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomTextforOtherLabelofPieChart-CustomTextforOtherLabelofPieChart.java" >}}


 Nachfolgend sehen Sie das resultierende Bild, wenn das Gebietsschema des Computers auf Frankreich eingestellt ist. Wie Sie sehen können, wurde das Label „Other“ in „Autre“ übersetzt, wie in definiert*Benutzerdefinierte Einstellungen*Klasse.

![todo: Bild_alt_Text](using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart_1.png)
