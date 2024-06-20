---
title: Ottieni DrawObject e Bound durante la resa in PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 70
url: /it/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells fornisce una classe astratta [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) che ha un metodo [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw). L'utente può implementare [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) e utilizzare il metodo [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) per ottenere il [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) e Bound mentre si renderizza Excel in PDF o immagine. Ecco una breve descrizione dei parametri del metodo [**Draw()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw).

- drawObject: [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) verrà inizializzato e restituito durante la resa

- x: Sinistra di [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: Alto di [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- larghezza: larghezza di [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- altezza: altezza di [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Se si sta rendendo il file Excel in PDF, è possibile utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) con [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler). Allo stesso modo, se si sta rendendo il file Excel in immagine, è possibile utilizzare la classe [**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) con [**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Ottieni DrawObject e Bound durante il rendering in Pdf usando la classe DrawObjectEventHandler**

Si prega di vedere il seguente codice di esempio. Carica il [file Excel di esempio](64716821.xlsx) e lo salva come [PDF di output](64716822.pdf). Durante la conversione in PDF, utilizza la proprietà [**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) e cattura la [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) e il Bound delle celle esistenti e degli oggetti come le immagini, ecc. Se il tipo [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) è Cell, stampa il suo Bound e StringValue. E se il tipo [**DrawObject**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) è Immagine, stampa il suo Bound e il nome della forma. Si prega di vedere l'output della console del codice di esempio qui sotto per ulteriori informazioni.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Output della console**

{{< highlight java >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
