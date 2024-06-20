---
title: Anzeige des Zellenbereichs als Datenbeschriftungen
type: docs
weight: 110
url: /de/java/showing-cell-range-as-the-data-labels/
---

## Zeigen Sie den Zellenbereich als Datenbeschriftungen in MS Excel an

In Microsoft Excel 2013 können Sie den Zellenbereich für Datenbeschriftungen anzeigen. Sie können diese Option durch folgende Schritte auswählen

- Wählen Sie die Datenbeschriftungen der Serie aus und klicken Sie mit der rechten Maustaste, um das Kontextmenü zu öffnen.
- Klicken Sie auf **Datenbeschriftungen formatieren...** und es wird **Beschriftungsoptionen** angezeigt.
- Aktivieren oder deaktivieren Sie das Kontrollkästchen **Beschriftung enthält - Wert aus Zellen**.

### **Kontrollkästchen zum Anzeigen des Zellenbereichs als Datenbeschriftungen**

Der folgende Screenshot hebt diese Option zu Ihrer Referenz hervor.

![todo:image_alt_text](showing-cell-range-as-the-data-labels_1.png)

## Zeigen Sie den Zellenbereich als Datenbeschriftungen mit Aspose.Cells

Aspose.Cells bietet die Methode [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange), um das Kontrollkästchen **Beschriftung enthält - Wert aus Zellen** wie im obigen Screenshot gezeigt, zu aktivieren oder zu deaktivieren.

## Java-Code zum Anzeigen von Zellenbereichen als Datenbeschriftungen

Der unten stehende Beispielcode greift auf die Datenbeschriftungen der Diagrammserie zu und setzt dann die Methode [**DataLabels.setShowCellRange()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#ShowCellRange) auf **true**, um die Option **Beschriftung enthält - Wert aus Zellen** zu aktivieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowCellRangeAsTheDataLabels-ShowCellRangeAsTheDataLabels.java" >}}
