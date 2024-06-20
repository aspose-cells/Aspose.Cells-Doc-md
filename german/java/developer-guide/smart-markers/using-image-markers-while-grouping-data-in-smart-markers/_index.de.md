---
title: Verwenden von Bild Markern beim Gruppieren von Daten in Smart Markern
type: docs
weight: 630
url: /de/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Dieser Artikel zeigt ein Beispiel, das die Verwendung von Bildmarkern beim Gruppieren von Daten in Smart Markern veranschaulicht.

{{% /alert %}} 
## **Verwenden von Bildmarkern beim Gruppieren von Daten in Smart Markern**
Der folgende Beispielscode erstellt eine Arbeitsmappe und fügt anschließend die folgenden Smart-Marker-Tags in die Zellen D2, E2 und F2 ein.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Dann füllt es die Datenquelle mit Daten und ruft die [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\))Methode auf, um die Smart-Marker-Tags zu verarbeiten. Der Code verwendet diese Bilder d.h [moon.png](5472549.png) und [moon2.png](5472548.png) aber Sie können jedes Bild verwenden. Der folgende Screenshot zeigt die Ausgabe dieses Beispiels. Wie Sie sehen können, sind die Daten in Spalte E und F in Bezug auf die Daten in Spalte D gruppiert.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
