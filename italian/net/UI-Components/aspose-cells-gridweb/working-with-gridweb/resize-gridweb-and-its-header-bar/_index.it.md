---
title: Ridimensiona GridWeb e la sua barra dell'intestazione
type: docs
weight: 30
url: /it/net/resize-gridweb-and-its-header-bar/
---
{{% alert color="primary" %}} 

[Aggiungere GridWeb al modulo Web](/cells/it/net/add-gridweb-to-web-form/), ha illustrato il ridimensionamento del controllo Aspose.Cells.GridWeb tramite WYSIWYG. Questo articolo spiega come eseguire la stessa operazione ma in fase di esecuzione usando l'API Aspose.Cells.GridWeb. Spiega inoltre come ridimensionare le barre di intestazione del controllo Aspose.Cells.GridWeb per semplificarne la lettura dei dati.

{{% /alert %}} 
## **Modifica della larghezza e dell'altezza di Aspose.Cells.GridWeb**
Modificare la larghezza e l'altezza del controllo Aspose.Cells.GridWeb è una caratteristica semplice ma importante. Il controllo Aspose.Cells.GridWeb è rappresentato dalla classe GridWeb nell'API. Per ridimensionare la larghezza e l'altezza del controllo GridWeb, usa semplicemente le sue proprietà di larghezza e altezza.

{{% alert color="primary" %}} 

La larghezza e l'altezza del controllo possono essere definite in pixel o punti.

{{% /alert %}} 

L'output del frammento di codice che segue è mostrato di seguito.

**Larghezza e altezza modificate del controllo GridWeb** 

![cose da fare:immagine_alt_testo](resize-gridweb-and-its-header-bar_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeGridWeb.aspx-ResizeGridWeb.cs" >}}
### **Modifica della larghezza e dell'altezza della barra dell'intestazione**
Aspose.Cells. Il controllo GridWeb contiene due barre di intestazione come segue:

- Barra dell'intestazione superiore, questa barra dell'intestazione rappresenta le colonne come A , B , C , D ecc.
- Barra di intestazione sinistra, questa barra di intestazione rappresenta le righe come 1 , 2 , 3 , 4 ecc.

Entrambe queste barre di intestazione sono mostrate di seguito.

**Barre di intestazione** 

![cose da fare:immagine_alt_testo](resize-gridweb-and-its-header-bar_2.png)

Modificare l'altezza della barra dell'intestazione superiore e la larghezza della barra dell'intestazione sinistra utilizzando rispettivamente le proprietà HeaderBarHeight e HeaderBarWidth del controllo GridWeb. La figura seguente mostra l'output dell'esempio di codice che segue.

**Larghezza e altezza della barra dell'intestazione modificate** 

![cose da fare:immagine_alt_testo](resize-gridweb-and-its-header-bar_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ResizeHeaderBar.aspx-ResizeHeaderBar.cs" >}}
