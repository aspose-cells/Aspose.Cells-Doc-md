---
title: Filtra gli oggetti durante il caricamento della cartella di lavoro in GridDesktop
type: docs
weight: 1060
url: /it/net/aspose-cells-griddesktop/loading-filter
description: Questo articolo descrive come utilizzare il filtro di caricamento per la libreria Aspose.Cells.GridDesktop.
---
## **Possibili scenari di utilizzo**
 Si prega di utilizzare[GridDesktop.LoadDataFilter](https://reference.aspose.com/cells/net/aspose.cells.griddesktop/griddesktop/properties/loaddatafilter)property durante il filtraggio dei dati dalla cartella di lavoro.

 Il[GridLoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells.griddesktop.data/gridloaddatafilteroptions)enumerazione ha i seguenti valori.
- Tutto
- Impostazioni libro
- CellBlank
- CellBool
- CellData
- CellError
- CellNumeric
- CellString
- CellValue
- Grafico
- Formattazione condizionale
- Convalida dei dati
- Nomi definiti
- Proprietà documento
- Formula
- Collegamenti ipertestuali
- Area unita
- Tabella pivot
- Impostazioni
- Forma
- FoglioDati
- Impostazioni foglio
- Struttura
- Stile
- Tavolo
- VBA
- XmlMap
## **Filtra i dati durante il caricamento della cartella di lavoro**
 Il codice di esempio seguente illustra come filtrare il disegno dalla cartella di lavoro. Si prega di controllare[file excel di esempio](5472489.xlsx) . Come puoi vedere, tutti i grafici/forme/immagini sono stati filtrati dalla cartella di lavoro.
![cartella di lavoro senza immagine](nodrawing.png)
### **Codice di esempio**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingFilter.cs" >}}
 