---
title: Copia gli intervalli di Excel
linktitle: Copia intervalli
type: docs
weight: 30
url: /it/java/copy-ranges-of-Excel/
---
## **introduzione**

In Excel, puoi selezionare un intervallo, copiare l'intervallo, quindi incollarlo con opzioni specifiche nello stesso foglio di lavoro, in altri fogli di lavoro o in altri file.

## **Copia gli intervalli utilizzando Aspose.Cells**

 Aspose.Cells fornisce un certo sovraccarico[Intervallo.Copia](https://reference.aspose.com/cells/java/com.aspose.cells/range) metodi per copiare l'intervallo.
## **Intervallo di copia**

Creazione di due intervalli: l'intervallo di origine, l'intervallo di destinazione, quindi la copia dell'intervallo di origine nell'intervallo di destinazione con il metodo Range.Copy.

Vedere il seguente codice:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **Incolla intervallo con opzioni**

Aspose.Cells supporta l'incollaggio dell'intervallo con un tipo specifico.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **Copia solo i dati dell'intervallo.**
Inoltre puoi copiare i dati con il metodo Range.CopyData come i seguenti codici:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


