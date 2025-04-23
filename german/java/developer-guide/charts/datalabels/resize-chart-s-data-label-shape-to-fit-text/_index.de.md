---
title: Größe der Beschriftungsform des Diagramms anpassen, um den Text anzupassen
type: docs
weight: 190
url: /de/java/resize-chart-s-data-label-shape-to-fit-text/
---

{{% alert color="primary" %}}

Die Excel-Anwendung bietet die Option **Form an Text anpassen** für Datenbeschriftungen von Diagrammen, um die Größe der Form zu erhöhen, damit der Text hineinpasst. Diese Option kann in der Excel-Benutzeroberfläche ausgewählt werden, indem eine der Datenbeschriftungen im Diagramm ausgewählt wird. Klicken Sie mit der rechten Maustaste und wählen Sie das Menü **Datenbeschriftungen formatieren** aus. Auf der Registerkarte **Größe & Eigenschaften** wird **Ausrichtung** erweitert, um die zugehörigen Eigenschaften, einschließlich der Option **Form an Text anpassen**, anzuzeigen.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_1.png)

{{% /alert %}}

## **Ändern der Größe der Datenbeschriftungsform des Diagramms, um den Text anzupassen**

Um das Feature von Excel zu imitieren, die Formen der Datenbeschriftung an den Text anzupassen, haben die Aspose.Cells APIs die Eigenschaft vom Typ Boolean [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText) freigelegt. Der folgende Code zeigt das einfache Anwendungsszenario der Eigenschaft [**DataLabels.ResizeShapeToFitText**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsResizeShapeToFitText).

Das Diagramm sieht vor der Ausführung des Codes wie folgt aus.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ResizeChartDataLabelShapeToFitText-ResizeChartDataLabelShapeToFitText.java" >}}

Das Diagramm sieht nach der Ausführung des Codes wie folgt aus.

![todo:image_alt_text](resize-chart-s-data-label-shape-to-fit-text_3.png)
{{< app/cells/assistant language="java" >}}
