---
title: Utilizzare i marker di immagine durante il raggruppamento dei dati nei Smart Marker
type: docs
weight: 30
url: /it/net/using-image-markers-while-grouping-data-in-smart-markers/
---

## **Utilizzo di marcatori immagine durante la raggruppamento dei dati in Smart Markers**
Il codice di esempio seguente crea un foglio di lavoro e poi aggiunge i seguenti tag del marker intelligente nelle celle D2, E2 e F2 rispettivamente

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Successivamente riempie l'origine dati con dati e chiama il metodo [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) per processare i tag del marker intelligente. Il codice utilizza queste immagini ossia [moon.png](5115492.png) e [moon2.png](5115491.png) ma è possibile utilizzare qualsiasi immagine



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
{{< app/cells/assistant language="csharp" >}}
