---
title: Filtra gli Oggetti durante il caricamento del Workbook o del Foglio di Lavoro
type: docs
weight: 330
url: /it/net/filter-objects-while-loading-workbook-or-worksheet/
---

## **Possibili Scenari di Utilizzo**
Si prega di utilizzare la proprietà [LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) per filtrare i dati dalla cartella di lavoro. Ma se si desidera filtrare i dati dai singoli fogli di lavoro, allora sarà necessario sovrascrivere il metodo [LoadFilter.StartSheet](https://reference.aspose.com/cells/net/aspose.cells/loadfilter/methods/startsheet). Si prega di fornire il valore appropriato dall'enumerazione [LoadDataFilterOptions]()https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) durante la creazione o il lavoro con [LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter).

L'enumerazione [LoadDataFilterOptions](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) ha i seguenti valori possibili.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-FilteringObjects.cs" >}}
## **Filtra oggetti durante il caricamento del foglio di lavoro**
Il codice di esempio seguente carica il [file Excel di origine](5115255.xlsx) e filtra i seguenti dati dai suoi fogli di lavoro utilizzando un filtro personalizzato.

- Filtra i Grafici dalla cartella di lavoro denominata NoCharts.
- Filtra le Forme dalla cartella di lavoro denominata NoShapes.
- Filtra la formattazione condizionale dalla cartella di lavoro denominata NoConditionalFormatting.

Una volta caricato il [file Excel di origine](5115255.xlsx) con un filtro personalizzato, si prendono le immagini di tutti i fogli di lavoro uno per uno. Ecco le immagini di output per il riferimento. Come si può vedere, la prima immagine non contiene grafici, la seconda immagine non ha forme e la terza immagine non ha formattazione condizionale.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-1.cs" >}}


Così si utilizza la classe CustomLoadFilter come per i nomi dei fogli di lavoro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilteringObjectsAtLoadTime-CustomFilteringPerWorksheet-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
