---
title: Deaktivieren Sie den Textumbruch für Datenbeschriftungen des Diagramms
type: docs
weight: 60
url: /de/java/disable-text-wrapping-for-data-labels-of-the-chart/
---
{{% alert color="primary" %}}

Microsoft Excel 2013 ermöglicht es Benutzern, Text innerhalb der Datenbeschriftungen eines Diagramms umzubrechen oder aufzulösen. Standardmäßig wird der Text der Datenbeschriftung umbrochen.

{{% /alert %}}

Aspose.Cells bietet die[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped) Methode. Einstellen**WAHR** oder**FALSCH** zum Aktivieren bzw. Deaktivieren des Textumbruchs auf Datenbeschriftungen.

 Verwenden Sie in ähnlicher Weise die[**DataLabels.isTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)Methode, um herauszufinden, ob eine Datenbeschriftung bereits umschlossen ist.

Dieser Screenshot zeigt eine Excel-Beispieldatei Microsoft mit einem Diagramm, in dem der Text der Datenbeschriftungen umbrochen ist. Wie Sie sehen, können Sie das überprüfen oder löschen**Text in Form umbrechen** Option im Abschnitt AUSRICHTUNG des Bereichs Datenbeschriftungen formatieren in Microsoft Excel 2013.

**Umhüllen von Datenetiketten**

![todo: Bild_alt_Text](disable-text-wrapping-for-data-labels-of-the-chart_1.png)

 Der folgende Beispielcode lädt die Excel-Beispieldatei Microsoft mithilfe von Aspose.Cells und deaktiviert den Textumbruch von Datenbeschriftungen mithilfe von[**DataLabels.setTextWrapped()**](https://reference.aspose.com/cells/java/com.aspose.cells/datalabels#IsTextWrapped)Methode. Wenn der Code ausgeführt wird, sieht das Diagramm so aus. Der zuvor umbrochene Text wird nun ausgepackt.

**Datenbeschriftungen nur in einer Zeile anzeigen**

![todo: Bild_alt_Text](disable-text-wrapping-for-data-labels-of-the-chart_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableTextWrapping-DisableTextWrapping.java" >}}
