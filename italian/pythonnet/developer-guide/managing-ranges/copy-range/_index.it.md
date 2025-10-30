---
title: Copia degli intervalli di Excel
linktitle: Copiare gli intervalli
type: docs
weight: 105
url: /it/python-net/copy-ranges-of-excel/
description: Questo articolo descrive come copiare intervalli di Excel con la libreria Aspose.Cells per Python via .NET.
keywords: Libreria Python per Excel, Come copiare intervalli di Excel in Python, Come copiare solo i dati dell intervallo con la libreria python excel, Come incollare l intervallo con opzioni, Come copiare solo i dati dell intervallo.
---

## **Introduzione**

In Excel, è possibile selezionare un intervallo, copiare l'intervallo, quindi incollarlo con opzioni specifiche nello stesso foglio di lavoro, in altri fogli di lavoro o in altri file.

## **Copia intervalli utilizzando la libreria Aspose.Cells per Python Excel**

Aspose.Cells for Python via .NET fornisce alcuni metodi di sovraccarico [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range) per copiare l'intervallo.
E [**Range.copy_style**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_style/#aspose.cells.Range) solo lo stile di copia dell'intervallo; [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) solo il valore di copia dell'intervallo

## **Copia Intervallo**

Creazione di due intervalli: intervallo di origine, intervallo di destinazione, quindi copia dell'intervallo di origine all'intervallo di destinazione con il metodo [**Range.copy**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy/#aspose.cells.Range).

Vedere il codice seguente:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range.py" >}}

## **Incolla l'intervallo con opzioni**

Aspose.Cells for Python via .NET supporta l'incollaggio dell'intervallo con un tipo specifico.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Paste-Range.py" >}}

## **Copia solo i dati dell'intervallo**
È anche possibile copiare i dati con il metodo [**Range.copy_data**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy_data/#aspose.cells.Range) come nei seguenti codici:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Copy-Range-Data.py" >}}

## **Argomenti avanzati**
- [Copia l'altezza delle righe dell'intervallo di origine nell'intervallo di destinazione](/cells/it/python-net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="python-net" >}}
