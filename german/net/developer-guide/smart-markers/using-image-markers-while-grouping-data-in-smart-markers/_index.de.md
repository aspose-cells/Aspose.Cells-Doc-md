---
title: Verwenden von Bildmarkierungen beim Gruppieren von Daten in Smart-Markierungen
type: docs
weight: 30
url: /de/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Verwenden von Bildmarkierungen beim Gruppieren von Daten in Smart-Markierungen**
Das folgende Beispiel erstellt eine Arbeitsmappe und fügt dann die folgenden Smart-Marker-Tags in den Zellen D2, E2 bzw. F2 hinzu.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Dann füllt es die Datenquelle mit Daten und ruft die auf[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) Methode zur Verarbeitung von Smart-Marker-Tags. Der Code verwendet diese Bilder dh[Mond.png](5115492.png) und[moon2.png](5115491.png) aber Sie können jedes Bild verwenden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
