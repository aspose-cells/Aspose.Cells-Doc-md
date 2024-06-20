---
title: Filtra gli oggetti durante il caricamento del foglio di lavoro in GridDesktop
type: docs
weight: 1060
url: /it/net/aspose-cells-griddesktop/loading-filter
description: Questo articolo descrive come utilizzare il filtro di caricamento in GridDesktop.
keywords: GridDesktop,loading,loading filter,filter
---

## **Possibili Scenari di Utilizzo**
Si prega di utilizzare la proprietà [GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter) durante il filtraggio dei dati dal foglio di lavoro.

L'enumerazione [GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions) ha i seguenti valori.
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
## **Filtrare i dati durante il caricamento del Workbook**
Il seguente codice di esempio illustra come filtrare i disegni dal workbook. Si prega di controllare il [file di excel di esempio](5472489.xlsx). Come potete vedere, tutti i grafici/forme/immagini sono stati filtrati dal workbook.
![workbook senza immagine](nodrawing.png)
### **Codice di Esempio**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}

