---
title: Verwenden von Bild Markern beim Gruppieren von Daten in Smart Markern
type: docs
weight: 30
url: /de/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Verwenden von Bildmarkern beim Gruppieren von Daten in Smart Markern**
Das folgende Beispiel erstellt eine Arbeitsmappe und fügt dann folgende Smart-Marker-Tags in die Zellen D2, E2 und F2 ein.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Dann füllt es die Datenquelle mit Daten und ruft die [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) Methode auf, um die Smart-Marker-Tags zu verarbeiten. Der Code verwendet diese Bilder, d.h. [moon.png](5115492.png) und [moon2.png](5115491.png), aber Sie können jedes Bild verwenden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
{{< app/cells/assistant language="csharp" >}}
