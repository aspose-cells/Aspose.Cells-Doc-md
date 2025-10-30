---
title: Filtra gli Oggetti durante il caricamento del Workbook o del Foglio di Lavoro
type: docs
weight: 330
url: /it/python-net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Possibili Scenari di Utilizzo**
Usa la proprietà [LoadOptions.load_filter](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) durante la filtrazione dei dati dal workbook. Se invece vuoi filtrare i dati da fogli di lavoro individuali, dovrai sovrascrivere il metodo [LoadFilter.start_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter/start_sheet). Fornisci un valore appropriato dall’enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) durante la creazione o l’utilizzo di [LoadFilter](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter).

L’enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) ha i seguenti valori possibili.

- Tutti
- Impostazioni del libro
- Cellavuota
- Cella booleana
- Dati cella
- Errore cella
- Numerico cella
- Stringa cella
- Valore cella
- Chart
- Formattazione condizionale
- Convalida dati
- Nomi definiti
- Proprietà documento
- Formula
- Collegamenti ipertestuali
- Area unita
- Tabella pivot
- Impostazioni
- Forma
- Dati del Foglio
- Impostazioni del Foglio
- Struttura
- Stile
- Tabella
- VBA
- XmlMap
## **Filtra oggetti durante il caricamento della cartella di lavoro**
Il codice di esempio seguente illustra come filtrare i grafici dalla cartella di lavoro. Si prega di controllare il [file excel di esempio](5115258.xlsx) utilizzato in questo codice e il [PDF di output](5115257.pdf) generato da esso. Come si può vedere nel PDF di output, tutti i grafici sono stati filtrati fuori dalla cartella di lavoro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilteringObjectsAtLoadTime-FilteringObjects.py" >}}

{{< app/cells/assistant language="python-net" >}}
