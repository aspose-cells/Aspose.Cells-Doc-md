---
title: Utilizzo di marcatori immagine durante il raggruppamento di dati in marcatori intelligenti
type: docs
weight: 30
url: /it/net/using-image-markers-while-grouping-data-in-smart-markers/
---
## **Utilizzo di marcatori immagine durante il raggruppamento di dati in marcatori intelligenti**
L'esempio seguente crea una cartella di lavoro e quindi aggiunge i seguenti tag smart marker rispettivamente nelle celle D2, E2 e F2.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Quindi riempie l'origine dati con i dati e chiama il file[WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) metodo per elaborare i tag dei marcatori intelligenti. Il codice utilizza queste immagini, ad es[luna.png](5115492.png) e[luna2.png](5115491.png) ma puoi usare qualsiasi immagine.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingImageMarkersWhileGroupingDataInSmartMarkers-UsingImageMarkersWhileGroupingDataInSmartMarkers.cs" >}}
