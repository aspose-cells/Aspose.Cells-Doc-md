---
title: Utilizzare i marker di immagine durante il raggruppamento dei dati nei Smart Marker
type: docs
weight: 630
url: /it/java/using-image-markers-while-grouping-data-in-smart-markers/
---

{{% alert color="primary" %}} 

Questo articolo presenta un esempio che illustra l'utilizzo dei marker di immagine durante il raggruppamento dei dati nei Smart Marker.

{{% /alert %}} 
## **Utilizzo di marcatori immagine durante la raggruppamento dei dati in Smart Markers**
Il seguente codice di esempio crea un foglio di lavoro e quindi aggiunge le seguenti etichette di smart marker nei rispettivi celle D2, E2 e F2.

{{< highlight java >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

Poi riempie la fonte dati con i dati e chiama il metodo [WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process--) per elaborare i tag degli smart marker. Il codice utilizza queste immagini, ovvero [moon.png](5472549.png) e [moon2.png](5472548.png), ma è possibile utilizzare qualsiasi immagine. La seguente schermata mostra il risultato di questo esempio di codice. Come si può vedere, i dati nelle colonne E e F sono raggruppati rispetto ai dati nella colonna D.

![todo:image_alt_text](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
{{< app/cells/assistant language="java" >}}
