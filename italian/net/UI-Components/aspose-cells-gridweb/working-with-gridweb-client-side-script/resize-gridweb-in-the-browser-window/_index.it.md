---
title: Ridimensiona GridWeb nella finestra del browser
type: docs
weight: 40
url: /it/net/resize-gridweb-in-the-browser-window/
---
## **Possibili scenari di utilizzo**
 volte vuoi Aspose.Cells.GridWeb dovrebbe ridimensionarsi in base alla finestra del browser. Potrebbe essere necessario che GridWeb regoli sempre le sue dimensioni (altezza, larghezza) e sia compatibile con le dimensioni della finestra del browser. Aspose.Cells.GridWeb fornisce lato client*ridimensiona()* funzione allo scopo. Inoltre, puoi persino rendere il controllo GridWeb ridimensionabile nella finestra del browser. Ad esempio, puoi utilizzare la maniglia in basso a destra (tramite il mouse) per personalizzarne la larghezza/altezza nella finestra. Devi anche includere/specificare i file Javascript jquery per farlo funzionare nell'origine della pagina nel tuo progetto.
## **Utilizzando il metodo di ridimensionamento di GridWeb**
Il codice seguente verificherà se viene eseguita un'azione di ridimensionamento ogni 100 millisecondi. Quando non ci sono più azioni di ridimensionamento, pensa che l'operazione di ridimensionamento sia terminata. Utilizziamo un file modello di esempio che viene importato in GridWeb. Usiamo il codice lato client per ridimensionare il GridWeb. Lo screenshot mostra che GridWeb si ridimensiona di conseguenza durante il ridimensionamento della finestra del browser.

![cose da fare:immagine_alt_testo](resize-gridweb-in-the-browser-window_1.png)
### **Codice di esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **Rendere GridWeb ridimensionabile utilizzando la funzione ridimensionabile dell'interfaccia utente jquery**
Il codice seguente renderà il controllo GridWeb ridimensionabile nella finestra del browser. Ad esempio, puoi utilizzare l'handle in basso a destra per personalizzare la sua dimensione di GridWeb nella finestra. Utilizziamo lo stesso file modello importato prima in GridWeb. Utilizziamo script jquery per rendere ridimensionabile GridWeb. Lo screenshot mostra che GridWeb è stato ridimensionato utilizzando la sua maniglia in basso a destra nella finestra del browser.

![cose da fare:immagine_alt_testo](resize-gridweb-in-the-browser-window_2.png)
### **Codice di esempio**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
