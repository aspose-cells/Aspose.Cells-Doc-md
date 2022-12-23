---
title: Gestione delle immagini
type: docs
weight: 10
url: /it/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells consente agli sviluppatori di aggiungere immagini ai fogli di calcolo in fase di esecuzione. Inoltre, il posizionamento di queste immagini può essere controllato in fase di esecuzione, come discusso più dettagliatamente nelle prossime sezioni.

Aspose.Cells for Java supporta solo i formati immagine: BMP, JPEG, PNG, GIF.

Gli indici utilizzati negli esempi iniziano da 0.

{{% /alert %}}

## **Aggiunta di immagini**

L'aggiunta di immagini a un foglio di calcolo è molto semplice. Bastano poche righe di codice.

 Basta chiamare il[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) metodo del[**Immagini**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) raccolta (incapsulata nel file[**Foglio di lavoro**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) oggetto). Il[**Inserisci**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String)) accetta i seguenti parametri:

- **Indice della riga in alto a sinistra**, l'indice della riga in alto a sinistra.
- **Indice colonna in alto a sinistra**, l'indice della colonna in alto a sinistra.
- **Nome file immagine**, il nome del file immagine, completo di percorso.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Posizionamento delle immagini**

Le immagini possono essere posizionate utilizzando Aspose.Cells come segue:

- [Posizionamento assoluto](/cells/it/java/managing-pictures/#absolute-positioning).

### **Posizionamento assoluto**

 Gli sviluppatori possono posizionare le immagini in modo assoluto utilizzando il file[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) e[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) metodi del[**Immagine**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)oggetto.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Argomenti avanzati**
- [Inserisci un'immagine collegata dall'indirizzo web](/cells/it/java/insert-a-linked-picture-from-web-address/)
- [Inserisci un'immagine basata sul riferimento Cell](/cells/it/java/insert-a-picture-based-on-cell-reference/)
- [Inserisci l'immagine Web da un URL in un foglio di lavoro Excel](/cells/it/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
