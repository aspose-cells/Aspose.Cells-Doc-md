---
title: Copia gli intervalli di Excel
linktitle: Copia intervalli
type: docs
weight: 105
url: /it/net/copy-ranges-of-Excel/
---
## **introduzione**

In Excel, puoi selezionare un intervallo, copiare l'intervallo, quindi incollarlo con opzioni specifiche nello stesso foglio di lavoro, in altri fogli di lavoro o in altri file.

## **Copia gli intervalli utilizzando Aspose.Cells**

 Aspose.Cells fornisce un certo sovraccarico[Intervallo.Copia](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) metodi per copiare l'intervallo.
 E[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) solo lo stile di copia della gamma;[Intervallo.CopiaDati](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) solo il valore di copia dell'intervallo

## **Intervallo di copia**

Creazione di due intervalli: l'intervallo di origine, l'intervallo di destinazione, quindi la copia dell'intervallo di origine nell'intervallo di destinazione con il metodo Range.Copy.

Vedere il seguente codice:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Incolla intervallo con opzioni**

Aspose.Cells supporta l'incollaggio dell'intervallo con un tipo specifico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Copia solo i dati dell'intervallo.**
Inoltre puoi copiare i dati con il metodo Range.CopyData come i seguenti codici:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Argomenti avanzati**
- [Copia le altezze delle righe dell'intervallo di origine nell'intervallo di destinazione](/cells/it/net/copy-row-heights-of-source-range-to-destination-range/)


