---
title: Gestione degli intervalli
linktitle: Intervalli
type: docs
weight: 105
url: /it/python-net/managing-ranges/
description: Questo articolo mostra come gestire intervalli con Aspose.Cells per Python via .NET API.
keywords: Libreria Excel Python, gestione intervalli Python, Creare intervallo in Python, Inserire valore nelle celle dell intervallo in Python, Impostare stile delle celle dell intervallo in Python, Ottenere Regione Corrente dell Intervallo in Python.
---

## **Introduzione**

In Excel, è possibile selezionare più celle con una selezione del riquadro del mouse, l'insieme di celle selezionate è chiamato "Intervallo".

Ad esempio, è possibile fare clic col pulsante sinistro del mouse sulla cella "A1" di Excel e quindi trascinare fino alla cella "C4". L'area rettangolare selezionata può essere facilmente creata come un oggetto utilizzando Aspose.Cells per Python via .NET.

Ecco come creare un intervallo, inserire un valore, impostare uno stile e fare altre operazioni sull'oggetto "Intervallo".

## **Gestione Intervalli Utilizzando la Libreria Excel Python di Aspose.Cells**

Aspose.Cells for Python via .NET fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) che rappresenta un file Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una raccolta di [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) che consente di accedere a ciascun foglio di lavoro in un file Excel. Un foglio di lavoro è rappresentato dalla classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fornisce una raccolta di [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

## **Come Creare un Intervallo**

Quando si desidera creare un'area rettangolare che si estende da A1 a C4, è possibile utilizzare il seguente codice:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Create.py" >}}

## **Come Inserire Valore nelle Celle dell'Intervallo**

Supponiamo di avere un intervallo di celle che si estende su A1:C4. La matrice crea 4 * 3 = 12 celle. Le singole celle dell'intervallo sono disposte in sequenza.

Nell'esempio seguente viene mostrato come inserire alcuni valori nelle celle dell'Intervallo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-PutValue.py" >}}

## **Come Impostare lo Stile delle Celle dell'Intervallo**

Nell'esempio seguente viene mostrato come impostare lo stile delle celle dell'Intervallo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-SetStyle.py" >}}

## **Come Ottenere la Regione Corrente dell'Intervallo**

CurrentRegion è una proprietà che restituisce un oggetto Range che rappresenta la regione corrente. 

La regione corrente è una gamma delimitata da qualsiasi combinazione di righe o colonne vuote. Solo lettura.

In Excel, puoi ottenere l'area CurrentRegion tramite:
1. Seleziona un'area (range1) con il mouse.
2. Clicca su "Home - Modifica - Trova e seleziona - Vai a speciale - Regione corrente", oppure usa "Ctrl+Shift+*", vedrai che Excel ti aiuterà automaticamente a selezionare un'area (range2), ora l'hai fatta, range2 è la CurrentRegion di range1.

Utilizzando Aspose.Cells per Python via .NET, è possibile utilizzare la proprietà "Range.current_region" per eseguire la stessa funzione.

Si prega di scaricare il file di test seguente, aprirlo in Excel, utilizzare il mouse per selezionare un'area "A1:D7", quindi fare clic su "Ctrl+Shift+*", vedrai che l'area "A1:C3" è selezionata.

[current_region.xlsx](current_region.xlsx)

Ora si prega di eseguire l'esempio seguente, vedere come funziona in Aspose.Cells per Python via .NET:

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-CurrentRegion.py" >}}

## **Argomenti avanzati**
- [Riempimento automatico dell'area del file Excel](/cells/it/python-net/autofill-ranges/)
- [Copia dei range di Excel](/cells/it/python-net/copy-ranges-of-excel/)
- [Copia solo i dati dell'intervallo.](/cells/it/python-net/copy-range-data-only/)
- [Copia intervallo dati con stile.](/cells/it/python-net/copy-range-data-with-style/)
- [Copia solo lo stile dell'intervallo](/cells/it/python-net/copy-range-style-only/)
- [Crea un intervallo di unione](/cells/it/python-net/create-union-range/)
- [Taglia e incolla il range](/cells/it/python-net/cut-and-paste-cells/)
- [Elimina ranges](/cells/it/python-net/delete-ranges-from-excel/)
- [Ottieni l'indirizzo, il conteggio delle celle, lo spostamento, l'intera colonna e la riga intera del range](/cells/it/python-net/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Inserisci ranges](/cells/it/python-net/insert-ranges-to-excel/)
- [Unisci o Separa Intervallo di Celle](/cells/it/python-net/merge-or-unmerge-range-of-cells/)
- [Sposta Intervallo di Celle in un Foglio di Lavoro](/cells/it/python-net/move-range-of-cells-in-a-worksheet/)
- [Crea Riferimenti con Nome a Livello di Cartella e Foglio di Lavoro](/cells/it/python-net/create-workbook-and-worksheet-scoped-named-ranges/)
- [Cerca e Sostituisci Dati in un Intervallo](/cells/it/python-net/search-and-replace-data-in-a-range/)

{{< app/cells/assistant language="python-net" >}}
