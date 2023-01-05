---
title: Ottieni DrawObject e Bound durante il rendering su PDF utilizzando la classe DrawObjectEventHandler
type: docs
weight: 70
url: /it/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells fornisce una classe astratta[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) che ha un[**Disegnare()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)metodo. L'utente può implementare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler) e utilizzare il[**Disegnare()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw) metodo per ottenere il[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)e Associato durante il rendering di Excel a PDF o Immagine. Ecco una breve descrizione dei parametri del[**Disegnare()**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler/methods/draw)metodo.

-  drawObject:[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) sarà inizializzato e restituito durante il rendering

- x: A sinistra di[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- y: dall'alto[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- larghezza: Larghezza di[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

- altezza: Altezza di[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)

Se stai eseguendo il rendering del file Excel su PDF, puoi utilizzare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)classe con[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler) . Allo stesso modo, se stai eseguendo il rendering del file Excel in Immagine, puoi utilizzare[**DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobjecteventhandler)classe con[**ImageOrPrintOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/drawobjecteventhandler).

## **Ottieni DrawObject e Bound durante il rendering in Pdf utilizzando la classe DrawObjectEventHandler**

 Vedere il seguente codice di esempio. Carica il[esempio di file Excel](64716821.xlsx) e lo salva come[uscita PDF](64716822.pdf). Durante il rendering su PDF, utilizza[**PdfSaveOptions.DrawObjectEventHandler**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/drawobjecteventhandler)proprietà e cattura il[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) e Bound di celle e oggetti esistenti, ad esempio immagini, ecc. Se the[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject) type è Cell, ne stampa Bound e StringValue. E se il[**DisegnaOggetto**](https://reference.aspose.com/cells/net/aspose.cells.rendering/drawobject)type è Image, stampa il suo Bound and Shape Name. Si prega di consultare l'output della console del codice di esempio fornito di seguito per ulteriore assistenza.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-GetDrawObjectAndBoundUsingDrawObjectEventHandler.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

 [X]: 153.6035 [Y]: 82.94118 [Width]: 103.2035 [Height]: 14.47059 [Cell Value]: This is sample text.

----------------------

[X]: 267.6917 [Y]: 153.4853 [Width]: 160.4491 [Height]: 128.0647 [Shape Name]: Sun

----------------------

{{< /highlight >}}
