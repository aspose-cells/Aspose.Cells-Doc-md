---
title: Textumbruch für Datenbeschriftungen des Diagramms deaktivieren
type: docs
weight: 60
url: /de/java/disable-text-wrapping-for-data-labels-of-the-chart/
---

{{% alert color="primary" %}}

Microsoft Excel 2013 ermöglicht es Benutzern, Text in den Datenbeschriftungen eines Diagramms umzubrechen oder nicht umzubrechen. Standardmäßig ist der Datenbeschriftungstext umgebrochen.

{{% /alert %}}

Aspose.Cells bietet die Methode [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Legen Sie **True** oder **False** fest, um das Umbringen von Text in Datenbeschriftungen zu aktivieren oder zu deaktivieren.

Verwenden Sie ähnlich die Methode [**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped), um festzustellen, ob eine Datenbeschriftung bereits umgebrochen ist.

Dieser Screenshot zeigt eine Beispieldatei von Microsoft Excel, die ein Diagramm mit umgebrochenem Datenbeschriftungstext enthält. Wie Sie sehen können, können Sie die Option **Text in Form umbrechen** im Bereich AUSRICHTUNG des Panels DATENBESCHRIFTUNGEN formatieren in Microsoft Excel 2013 aktivieren oder deaktivieren.

**Einwickeln von Datenbeschriftungen**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

Der folgende Beispielcode lädt die Beispieldatei von Microsoft Excel mit Aspose.Cells und deaktiviert das Einwickeln des Texts in den Datenbeschriftungen mithilfe der Methode [**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped). Wenn der Code ausgeführt wird, sieht das Diagramm so aus. Der zuvor eingerollte Text ist jetzt entrollt.

**Nur Datenbeschriftungen in einer Zeile anzeigen**

![todo:image_alt_text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
