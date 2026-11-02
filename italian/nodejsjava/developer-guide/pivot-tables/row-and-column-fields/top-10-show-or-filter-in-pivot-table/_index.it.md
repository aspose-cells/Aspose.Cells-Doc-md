---
title: Mostrare o filtrare i primi 10 elementi in una tabella pivot
linktitle: Mostrare o filtrare i primi 10 elementi in una tabella pivot
description: Scopri come mostrare solo gli elementi di un campo pivot posizionati più in alto o più in basso nella classifica in Aspose.Cells for Node.js tramite Java. Questo articolo illustra il metodo Top10AutoShow di Excel 97-2003, la lettura delle opzioni con Top10AutoShowSettings e il filtro dei primi 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, Node.js tramite Java, tabella pivot, primi 10, visualizzazione automatica, top10AutoShow, getTop10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /it/nodejs-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può essere difficile da leggere quando il campo contiene decine di elementi. Un report dei primi 10 conserva soltanto gli elementi posizionati più in alto o più in basso nella classifica, esattamente ciò di cui necessitano i report basati sulla classifica — "i 5 prodotti con i ricavi più alti" o "le 3 aree con il minor numero di vendite". Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **AutoShow di Excel 97-2003** — il metodo `PivotField.top10AutoShow()`. Questa è l'impostazione classica "Mostra i primi/ultimi N elementi", memorizzata direttamente sul campo pivot. Funziona in tutte le versioni di Excel, sia recenti che meno recenti, perché fa parte del formato originale delle tabelle pivot.
- **Filtro dei primi 10 di Excel 2007-365** — il metodo `PivotField.filterTop10()`. Questo è il filtro moderno dei valori denominato "Primi 10", disponibile nel menu del campo sotto "Filtri sui valori". Viene memorizzato come oggetto `PivotFilter` associato al campo e supporta classifiche in base al numero di elementi o alla percentuale.

## **Mostrare i primi 10 in Excel 97-2003 (Top10AutoShow)**
L'impostazione classica AutoShow viene configurata mediante una singola chiamata a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `true` mantiene gli elementi più in alto nella classifica (Primi), mentre `false` mantiene quelli più in basso (Ultimi).
- `count` — il numero di elementi da mantenere, ad esempio 10 per un classico report dei primi 10.
- `rankBy` — l'indice a base zero del **campo dati** i cui valori vengono utilizzati per classificare gli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classifica può essere determinata in base a un campo di valore o al campo stesso. Sono disponibili due varianti comuni, illustrate di seguito.

### **Classificare in base a un campo di valore**
Classificare gli elementi del campo di riga in base a un normale campo di valore, ad esempio Somma di Sales. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i 2 sport con le vendite più alte. `rankBy` è 0 perché "Somma di Sales" è il campo dati all'indice 0.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Classificare in base al campo stesso**
Un campo può anche essere classificato in base a sé stesso: passare -1 come `rankBy`. Per questa variante non è necessario alcun campo dati aggiuntivo; il campo deve essere collocato nell'area delle righe o delle colonne. L'esempio seguente mostra i 3 sport classificati più in basso in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dall'XML della tabella pivot perché -1 è il valore predefinito del formato e `getTop10AutoShowSettings().getRankBy()` restituisce -1.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Lettura delle opzioni correnti (Top10AutoShowSettings)**
Il metodo `PivotField.getTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzarlo per controllare come verranno visualizzati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata. È possibile esaminare allo stesso modo le cartelle di lavoro caricate da un file.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow());
console.log("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

I getter `isAutoShow()`, `isTop()`, `getAutoShowCount()` e `getRankBy()` corrispondono agli attributi classici AutoShow scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), pertanto i valori letti sono quelli che verranno applicati da tutte le versioni di Excel.

## **Nota**

{{% alert color="primary" %}}
- I getter diretti `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` e `getAutoShowField()` di `PivotField` sono deprecati. Utilizzare invece l'oggetto restituito da `getTop10AutoShowSettings()`: `isAutoShow()` diventa `getTop10AutoShowSettings().isAutoShow()`, `isAscendShow()` diventa `getTop10AutoShowSettings().isTop()`, `getAutoShowCount()` diventa `getTop10AutoShowSettings().getAutoShowCount()` e `getAutoShowField()` diventa `getTop10AutoShowSettings().getRankBy()`. Il metodo `top10AutoShow()` è il metodo previsto per modificare le impostazioni.
- `top10AutoShow()` funziona con i campi di riga e di colonna. Un campo presente soltanto nell'area della pagina (filtro) non può essere classificato in questo modo, perché i suoi elementi non sono disposti nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro Primi 10 (FilterTop10)**
Le versioni moderne di Excel offrono il filtro Primi 10 tra i filtri sui valori del menu del campo (Filtri sui valori, Primi 10...). Aspose.Cells lo rappresenta tramite il metodo `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — l'indice a base zero del campo dati i cui valori aggregati vengono utilizzati per classificare gli elementi.
- `type` — indica il significato di `itemCount`. `PivotFilterType.COUNT` mantiene un numero fisso di elementi (l'opzione Elementi della finestra di dialogo). `PivotFilterType.PERCENT` mantiene una percentuale degli elementi, quindi `itemCount` è la percentuale stessa: 30 mantiene il 30% degli elementi classificati più in alto. `PivotFilterType.SUM` classifica gli elementi in base alla copertura cumulativa dei valori.
- `isTop` — `true` per Primi, `false` per Ultimi.
- `itemCount` — il valore N in "Primi N"; l'unità dipende da `type`.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get(0, 0).putValue("Sport");
worksheet.getCells().get(0, 1).putValue("Quarter");
worksheet.getCells().get(0, 2).putValue("Sales");
const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
let row = 2;
for (const sport of sports) {
    for (let quarter = 1; quarter <= 3; quarter++) {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
const pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.COUNT, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow()` e `filterTop10()` sono due funzionalità distinte. AutoShow scrive sul campo pivot il set di attributi classici relativo a `autoShow` e viene riconosciuto da tutte le versioni di Excel, da Excel 97 in poi. `filterTop10()` scrive una voce `PivotFilter` moderna, che richiede Excel 2007 o versione successiva. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, una tabella pivot che usa il filtro moderno visualizza tutti gli elementi. Per i documenti che devono completare un ciclo di elaborazione tramite strumenti di versioni precedenti, preferire `top10AutoShow()`; per le cartelle di lavoro moderne, preferire `filterTop10()` perché può essere utilizzato insieme agli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere campi di riga e colonna alla tabella pivot](/cells/it/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Raggruppare i campi pivot nella tabella pivot](/cells/it/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/nodejs-java/refresh-pivot-table/)
- [Aggiungere un campo di pagina alla tabella pivot](/cells/it/nodejs-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}