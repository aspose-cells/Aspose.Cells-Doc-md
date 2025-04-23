---
title: Copia degli intervalli di Excel
linktitle: Copiare gli intervalli
type: docs
weight: 105
url: /it/net/copy-ranges-of-Excel/
---

## **Introduzione**

In Excel, è possibile selezionare un intervallo, copiare l'intervallo, quindi incollarlo con opzioni specifiche nello stesso foglio di lavoro, in altri fogli di lavoro o in altri file.

## **Copiare intervalli utilizzando Aspose.Cells**

Aspose.Cells fornisce alcuni metodi [Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy) per copiare il range.
E [Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/) copia solo lo stile del range; [Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/) copia solo il valore del range.

## **Copia Intervallo**

Creazione di due intervalli: l'intervallo di origine, l'intervallo di destinazione, quindi copiare l'intervallo di origine nell'intervallo di destinazione con il metodo Range.Copy.

Vedere il codice seguente:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **Incolla l'intervallo con opzioni**

Aspose.Cells supporta l'incollaggio del intervallo con un tipo specifico.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **Copia solo i dati dell'intervallo**
Puoi anche copiare i dati con il metodo Range.CopyData come nei seguenti codici:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **Argomenti avanzati**
- [Copia l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione](/cells/it/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
