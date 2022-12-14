---
title: Filtra gli oggetti durante il caricamento della cartella di lavoro o del foglio di lavoro
type: docs
weight: 330
url: /it/net/filter-objects-while-loading-workbook-or-worksheet/
---
## **Possibili scenari di utilizzo**
Si prega di utilizzare[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)property durante il filtraggio dei dati dalla cartella di lavoro. Ma se vuoi filtrare i dati da singoli fogli di lavoro, dovrai sovrascrivere il file[LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet)metodo. Si prega di fornire un valore appropriato da[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)enumerazione durante la creazione o l'utilizzo[Carica filtro](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

 Il[LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)enumerazione ha i seguenti possibili valori.

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
## **Filtra gli oggetti durante il caricamento della cartella di lavoro**
 Il codice di esempio seguente illustra come filtrare i grafici dalla cartella di lavoro. Si prega di controllare[file excel di esempio](5115258.xlsx) utilizzato in questo codice e il[uscita PDF](5115257.pdf)generato da esso. Come puoi vedere nel PDF di output, tutti i grafici sono stati filtrati dalla cartella di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtra gli oggetti durante il caricamento del foglio di lavoro**
 Il codice di esempio seguente carica il file[file excel di origine](5115255.xlsx) e filtra i seguenti dati dai fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i grafici dal foglio di lavoro denominato NoCharts.
- Filtra le forme dal foglio di lavoro denominato NoShapes.
- Filtra la formattazione condizionale dal foglio di lavoro denominato NoConditionalFormatting.

 Una volta, carica il file[file excel di origine](5115255.xlsx) con un filtro personalizzato, prende le immagini di tutti i fogli di lavoro uno per uno. Ecco le immagini di output per riferimento. Come puoi vedere, la prima immagine non ha grafici, la seconda immagine non ha forme e la terza immagine non ha formattazione condizionale.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Ecco come utilizzare la classe CustomLoadFilter secondo i nomi dei fogli di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
