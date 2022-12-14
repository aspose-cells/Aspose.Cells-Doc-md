---
title: Anzeige des Bereichs Cell als Datenbeschriftung
type: docs
weight: 110
url: /de/java/showing-cell-range-as-the-data-labels/
---
## Zellbereich als Datenbeschriftungen in MS Excel anzeigen

In Microsoft Excel 2013 können Sie den Cell-Bereich für Datenbeschriftungen anzeigen. Sie können diese Option auswählen, indem Sie diesen Schritten folgen

- Wählen Sie Datenetiketten der Serie und klicken Sie mit der rechten Maustaste, um das Popup-Menü zu öffnen.
-  Drücke den**Datenbeschriftungen formatieren...** und es wird sich zeigen**Beschriftungsoptionen**.
-  Aktivieren oder deaktivieren Sie das Kontrollkästchen**Etikett enthält - Wert von Cells**.

### **Kontrollkästchen zum Anzeigen des Bereichs Cell als Datenetiketten**

Der folgende Screenshot hebt diese Option als Referenz hervor.

![todo: Bild_alt_Text](showing-cell-range-as-the-data-labels_1.png)

## Zellbereich als Datenbeschriftungen mit Aspose.Cells anzeigen

 Aspose.Cells bietet die[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) Methode zum Aktivieren oder Deaktivieren des Kontrollkästchens**Etikett enthält - Wert von Cells** wie im Screenshot oben gezeigt.

## Java-Code zum Anzeigen des Zellbereichs als Datenbeschriftungen

 Der folgende Beispielcode greift auf die Datenbeschriftungen der Diagrammreihe zu und legt sie dann fest[**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) Methode auf true zu überprüfen**Etikett enthält - Wert von Cells** Möglichkeit.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
