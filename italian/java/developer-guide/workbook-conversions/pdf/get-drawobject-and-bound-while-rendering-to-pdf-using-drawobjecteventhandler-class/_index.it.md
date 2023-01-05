---
title: Ottieni DrawObject e Bound durante il rendering su PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 60
url: /it/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Possibili scenari di utilizzo**

Aspose.Cells fornisce una classe astratta[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) che ha un[**disegnare()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metodo. L'utente può implementare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)e utilizzare il[**disegnare()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metodo per ottenere il[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)e**Limite**durante il rendering di Excel in PDF o Image. Ecco una breve descrizione dei parametri del[**disegnare()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw(com.aspose.cells.DrawObject,%20float,%20float,%20float,%20float)) metodo.

-  drawObject:[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)sarà inizializzato e restituito durante il rendering

- x: A sinistra di[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: dall'alto[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- larghezza: Larghezza di[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- altezza: Altezza di[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Se stai eseguendo il rendering del file Excel su PDF, puoi utilizzare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)classe con[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Allo stesso modo, se stai eseguendo il rendering del file Excel in Immagine, puoi utilizzare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler)classe con[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Ottieni DrawObject e Bound durante il rendering in Pdf utilizzando la classe DrawObjectEventHandler**

Vedere il seguente codice di esempio. Carica il[esempio di file Excel](64716843.xlsx)e lo salva come[uscita PDF](64716842.pdf). Durante il rendering su PDF, utilizza[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler)proprietà e cattura il[**DisegnaOggetto**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) e**Limite**di celle e oggetti esistenti, ad esempio immagini, ecc. Se il tipo drawObject è Cell, stampa i suoi Bound e StringValue. E se il tipo drawObject è Image, stampa il suo Bound e Shape Name. Si prega di consultare l'output della console del codice di esempio fornito di seguito per ulteriore assistenza.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Uscita console**

{{< highlight "java" >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
