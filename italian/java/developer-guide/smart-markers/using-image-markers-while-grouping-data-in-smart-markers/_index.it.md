---
title: Utilizzo di marcatori immagine durante il raggruppamento di dati in marcatori intelligenti
type: docs
weight: 630
url: /it/java/using-image-markers-while-grouping-data-in-smart-markers/
---
{{% alert color="primary" %}} 

Questo articolo presenta un esempio che illustra l'utilizzo dei marcatori immagine durante il raggruppamento dei dati in marcatori intelligenti.

{{% /alert %}} 
## **Utilizzo di marcatori immagine durante il raggruppamento di dati in marcatori intelligenti**
Il seguente codice di esempio crea una cartella di lavoro e quindi aggiunge i seguenti tag marcatore intelligente rispettivamente nelle celle D2, E2 e F2.

{{< highlight "java" >}}

 &=Person.Name(group:normal,skip:1)

&=Person.City

&=Person.Photo(Picture:FitToCell)

{{< /highlight >}}

 Quindi riempie l'origine dati con i dati e chiama il file[WorkbookDesigner.Process()](https://reference.aspose.com/cells/java/com.aspose.cells/workbookdesigner#process\(\) ) metodo per elaborare i tag dei marcatori intelligenti. Il codice utilizza queste immagini, ad es[luna.png](5472549.png) e[luna2.png](5472548.png) ma puoi usare qualsiasi immagine. Lo screenshot seguente mostra l'output di questo codice di esempio. Come puoi vedere, i dati nella colonna E e F sono raggruppati rispetto ai dati nella colonna D.

![cose da fare:immagine_alt_testo](using-image-markers-while-grouping-data-in-smart-markers_1.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Technical-Articles-SmartMarkerGroupingImage.java" >}}
