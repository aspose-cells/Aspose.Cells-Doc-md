---
title: Copia degli intervalli di Excel
linktitle: Copiare gli intervalli
type: docs
weight: 30
url: /it/java/copy-ranges-of-Excel/
---

## **Introduzione**

In Excel, è possibile selezionare un intervallo, copiare l'intervallo, quindi incollarlo con opzioni specifiche nello stesso foglio di lavoro, in altri fogli di lavoro o in altri file.

## **Copiare intervalli utilizzando Aspose.Cells**

Aspose.Cells fornisce alcuni metodi di sovraccarico [Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range) per copiare l'intervallo.
## **Copia Intervallo**

Creazione di due intervalli: l'intervallo di origine, l'intervallo di destinazione, quindi copiare l'intervallo di origine nell'intervallo di destinazione con il metodo Range.Copy.

Vedere il codice seguente:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Incolla l'intervallo con opzioni**

Aspose.Cells supporta l'incollaggio del intervallo con un tipo specifico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Copia solo i dati dell'intervallo.**
Puoi anche copiare i dati con il metodo Range.CopyData come nei seguenti codici:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


