---
title: Ottieni DrawObject e Bound durante la resa in PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 60
url: /it/java/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce una classe astratta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) che ha un metodo [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-). L'utente può implementare [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) e utilizzare il metodo [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-) per ottenere [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) e **Bound** durante la resa di Excel in PDF o Immagine. Ecco una breve descrizione dei parametri del metodo [**draw()**](https://reference.aspose.com/cells/java/com.aspose.cells/drawobjecteventhandler#draw-com.aspose.cells.DrawObject-float-float-float-float-).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) sarà inizializzato e restituito durante la resa

- x: Sinistra di [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- y: Alto di [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- larghezza: larghezza di [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

- altezza: altezza di [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject)

Se stai rendendo un file Excel in PDF, allora puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) con [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler). Allo stesso modo, se stai rendendo un file Excel in un'immagine, puoi utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObjectEventHandler) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DrawObjectEventHandler).

## **Ottieni DrawObject e Bound durante il rendering in Pdf usando la classe DrawObjectEventHandler**

Si prega di consultare il seguente codice di esempio. Carica il [file Excel di esempio](64716843.xlsx) e lo salva come [file PDF di output](64716842.pdf). Durante il rendering in PDF, utilizza la proprietà [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#DrawObjectEventHandler) e cattura il [**DrawObject**](https://reference.aspose.com/cells/java/com.aspose.cells/DrawObject) e **Bound** delle celle esistenti e degli oggetti come immagini ecc. Se il tipo di drawObject è Cell, stampa il suo Bound e il suo StringValue. E se il tipo di drawObject è Image, stampa il suo Bound e il Nome della Forma. Si prega di vedere l'output della console del codice di esempio qui sotto per ulteriore assistenza.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.java" >}}

## **Output della console**

{{< highlight java >}}

[X]: 153.60349 [Y]: 82.94118 [Width]: 103.203476 [Height]: 14.470589 [Cell Value]: This is sample text.

\----------------------

[X]: 267.28854 [Y]: 153.12354 [Width]: 161.25542 [Height]: 128.78824 [Shape Name]: Sun

\----------------------

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
