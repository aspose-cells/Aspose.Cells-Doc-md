---
title: Ridimensionare GridWeb nella finestra del browser
type: docs
weight: 40
url: /it/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb, ridimensionare
description: Questo articolo illustra come ridimensionare GridWeb.
---

## **Possibili Scenari di Utilizzo**
A volte è necessario che Aspose.Cells.GridWeb si ridimensioni in base alla finestra del browser. Potresti aver bisogno che GridWeb si adatti sempre alle dimensioni (altezza, larghezza) e sia compatibile con le dimensioni della finestra del browser. Aspose.Cells.GridWeb fornisce la funzione lato client *resize()* a questo scopo. Inoltre, è possibile rendere il controllo GridWeb ridimensionabile nella finestra del browser. Ad esempio, è possibile utilizzare il manico in basso a destra (tramite il mouse) per personalizzare la larghezza/altezza nella finestra. È inoltre necessario includere/specificare i file javascript jquery per farlo funzionare nel codice sorgente della pagina nel tuo progetto.
## **Utilizzo del metodo resize di GridWeb**
Il codice seguente controllerà se è stata presa un'azione di ridimensionamento ogni 100 millisecondi. Quando non ci sono più azioni di ridimensionamento, vuol dire che l'operazione di ridimensionamento è terminata. Utilizziamo un file di modello di esempio che viene importato in GridWeb. Utilizziamo il codice lato client per ridimensionare GridWeb. Lo screenshot mostra che GridWeb si ridimensiona di conseguenza quando si ridimensiona la finestra del browser.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Rendere GridWeb ridimensionabile utilizzando la funzionalità resizable jquery ui**
Il codice seguente renderà il controllo GridWeb ridimensionabile nella finestra del browser. Ad esempio, è possibile utilizzare il manico in basso a destra per personalizzare le dimensioni di GridWeb nella finestra. Utilizziamo lo stesso file di modello che viene importato in GridWeb per primo. Utilizziamo gli script jquery per rendere GridWeb ridimensionabile. Lo screenshot mostra che GridWeb è stato ridimensionato utilizzando il suo manico in basso a destra nella finestra del browser.

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
