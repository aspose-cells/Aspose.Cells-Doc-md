---
title: Verwenden von Bildmarkierungen beim Gruppieren von Daten in Smart-Markierungen
type: docs
weight: 630
url: /de/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Dieser Artikel enthält ein Beispiel, das die Verwendung von Bildmarkierungen beim Gruppieren von Daten in intelligenten Markierungen veranschaulicht.

{{% /alert %}} 
## **Verwenden von Bildmarkierungen beim Gruppieren von Daten in Smart-Markierungen**
Der folgende Beispielcode erstellt eine Arbeitsmappe und fügt dann die folgenden intelligenten Markierungstags in den Zellen D2, E2 bzw. F2 hinzu.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Dann füllt es die Datenquelle mit Daten und ruft die auf[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) )-Methode zum Verarbeiten von Smart-Marker-Tags. Der Code verwendet diese Bilder dh[Mond.png](5472549.png) und[moon2.png](5472548.png) aber Sie können jedes Bild verwenden. Der folgende Screenshot zeigt die Ausgabe dieses Beispielcodes. Wie Sie sehen können, sind die Daten in Spalte E und F in Bezug auf die Daten in Spalte D gruppiert.

![todo: Bild_alt_Text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
