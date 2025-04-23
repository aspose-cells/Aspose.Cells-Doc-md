---
title: Gestione delle immagini
type: docs
weight: 10
url: /it/java/managing-pictures/
---

Aspose.Cells consente ai programmatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, la posizione di queste immagini può essere controllata in fase di esecuzione, come discusso più in dettaglio nelle sezioni successive.

Questo articolo spiega come aggiungere immagini e come inserire un'immagine che mostra il contenuto di determinate celle.

## **Aggiunta di immagini**

Aggiungere immagini a un foglio di calcolo è molto semplice. Bastano poche righe di codice.

Chiamare semplicemente il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) della collezione [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (incapsulata nell'oggetto [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Il metodo [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice della colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome del file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Posizionamento delle immagini**

Le immagini possono essere posizionate utilizzando Aspose.Cells come segue:

- [Posizionamento Assoluto](/cells/it/java/managing-pictures/#absolute-positioning).

### **Posizionamento Assoluto**

I programmatori possono posizionare le immagini in modo assoluto utilizzando i metodi [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) e [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) dell'oggetto [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Argomenti avanzati**
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/java/insert-a-linked-picture-from-web-address/)
- [Inserire un'immagine basata sul riferimento di cella](/cells/it/java/insert-a-picture-based-on-cell-reference/)
- [Inserire un'immagine web da un URL in un foglio di calcolo Excel](/cells/it/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="java" >}}
