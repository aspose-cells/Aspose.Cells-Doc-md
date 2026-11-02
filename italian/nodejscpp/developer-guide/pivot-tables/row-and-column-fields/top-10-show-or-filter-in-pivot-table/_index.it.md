---
title: Visualizzazione o filtro Top 10 nella tabella pivot
linktitle: Visualizzazione o filtro Top 10 nella tabella pivot
description: Scopri come mostrare solo gli elementi più in alto o più in basso nella classifica di un campo pivot in Aspose.Cells for Node.js via C++. Questo articolo illustra il metodo Top10AutoShow di Excel 97-2003, la lettura delle opzioni tramite Top10AutoShowSettings e il filtro Top 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, Node.js via C++, tabella pivot, top 10, visualizzazione automatica, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, Node.js
type: docs
weight: 20
url: /it/nodejs-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca ogni elemento di un campo di riga può essere difficile da leggere quando il campo contiene decine di elementi. Un report Top 10 mantiene soltanto gli elementi con la classificazione più alta o più bassa, ossia esattamente ciò che serve ai report di classifica: «i 5 prodotti con i ricavi più elevati» o «le 3 regioni con il numero di vendite più basso». Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **AutoShow di Excel 97-2003** — il metodo `pivotField.top10AutoShow()`. Questa è l'impostazione classica «Mostra gli elementi superiori/inferiori N», memorizzata direttamente sul campo pivot. Funziona con tutte le versioni di Excel, antiche e recenti, perché fa parte del formato originale della tabella pivot.
- **Filtro Top 10 di Excel 2007-365** — il metodo `pivotField.filterTop10()`. È il filtro moderno Top 10 basato sui valori, disponibile nel menu del campo, in Filtri valore. Viene memorizzato come oggetto `PivotFilter` associato al campo e offre classificazioni basate sul numero di elementi o sulla percentuale.

## **Visualizzazione Top 10 in Excel 97-2003 (top10AutoShow)**
L'impostazione AutoShow classica viene configurata tramite una singola chiamata a `pivotField.top10AutoShow(isAutoShow, isTop, count, rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `true` mantiene gli elementi con la classificazione più alta (In alto), `false` mantiene quelli con la classificazione più bassa (In basso).
- `count` — numero di elementi da mantenere, ad esempio 10 per un report Top 10 classico.
- `rankBy` — indice a base zero del **campo dati** i cui valori determinano la classificazione degli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classificazione può essere determinata da un campo valore o dal campo stesso. Di seguito sono illustrate due varianti.

### **Classificazione in base a un campo valore**
Classifica gli elementi del campo di riga in base a un campo valore ordinario, ad esempio `Sum of Sales`. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i due sport con le vendite più alte. `rankBy` è 0 perché `Sum of Sales` è il campo dati all'indice 0.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");```

```

### **Classificazione in base al campo stesso**
Un campo può anche essere classificato in base a sé stesso, specificando -1 come `rankBy`. Per questa variante non è necessario alcun campo dati aggiuntivo; è sufficiente che il campo si trovi nell'area delle righe (o delle colonne). L'esempio seguente mostra i 3 sport con la classificazione più bassa in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dal XML della tabella pivot perché -1 è il valore predefinito del formato e `top10AutoShowSettings.getRankBy()` restituisce -1.

```javascript
const AsposeCells = require("aspose.cells.node");
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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Show the bottom 3 items ranked by the field itself (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");```
```

## **Lettura delle opzioni correnti (Top10AutoShowSettings)**
Il getter `pivotField.getTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzarlo per ispezionare come verranno presentati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata. Questo vale anche per le cartelle di lavoro caricate da file.

```javascript
const AsposeCells = require("aspose.cells.node");
const workbook = new AsposeCells.Workbook("output-top10-by-value-field.xlsx");
const pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
const sportField = pivotTable.getRowFields().get(0);
const settings = sportField.getTop10AutoShowSettings();
console.log("AutoShow enabled: " + settings.isAutoShow);
console.log("Direction: " + (settings.isTop ? "Top" : "Bottom"));
console.log("Item count: " + settings.getAutoShowCount());
console.log("Ranking data field index: " + settings.getRankBy());
```

Le quattro proprietà corrispondono agli attributi classici di AutoShow scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`); i valori letti sono quindi quelli che verranno applicati da ogni versione di Excel.

## **Nota**

{{% alert color="primary" %}}
- I getter diretti di `PivotField`, `isAutoShow`, `getIsAscendShow()`, `getAutoShowCount()` e `getAutoShowField()` sono obsoleti. Utilizzare invece l'oggetto `Top10AutoShowSettings`: `pivotField.isAutoShow` diventa `top10AutoShowSettings.isAutoShow`, `pivotField.getIsAscendShow()` diventa `top10AutoShowSettings.isTop`, `pivotField.getAutoShowCount()` diventa `top10AutoShowSettings.getAutoShowCount()` e `pivotField.getAutoShowField()` diventa `top10AutoShowSettings.getRankBy()`. Il metodo `pivotField.top10AutoShow()` è il metodo supportato per modificare le impostazioni.
- `top10AutoShow()` funziona con campi di riga e colonna. Un campo collocato soltanto nell'area della pagina (filtro) non può essere classificato in questo modo, poiché i suoi elementi non sono disposti nel corpo della tabella pivot.
{{% /alert %}}

## **Filtro Top 10 in Excel 2007-365 (filterTop10)**
Nelle versioni moderne di Excel, Top 10 è disponibile come filtro valore nel menu del campo (Filtri valore, Top 10...). Aspose.Cells implementa questo filtro con il metodo `pivotField.filterTop10(valueFieldIndex, type, isTop, itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — indice a base zero del campo dati i cui valori aggregati determinano la classificazione degli elementi.
- `type` — specifica ciò che `itemCount` rappresenta. `PivotFilterType.Count` mantiene un numero fisso di elementi (opzione Elementi della finestra di dialogo). `PivotFilterType.Percent` mantiene una percentuale degli elementi, quindi `itemCount` è la percentuale stessa: 30 mantiene il 30% degli elementi più in alto. `PivotFilterType.SUM` classifica in base alla copertura cumulativa dei valori.
- `isTop` — `true` per In alto, `false` per In basso.
- `itemCount` — il valore N nell'opzione Top N; l'unità di misura dipende da `type`.

```javascript
const AsposeCells = require("aspose.cells.node");

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
pivotTable.calculateData();
const sportField = pivotTable.getRowFields().get(0);
// Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
const filter = sportField.filterTop10(0, AsposeCells.PivotFilterType.Count, true, 2);
// For a percentage-based filter instead, keep the top 30 percent of the items:
// sportField.filterTop10(0, AsposeCells.PivotFilterType.Percent, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");```

```

{{% alert color="primary" %}}
`top10AutoShow` e `filterTop10` sono due funzionalità distinte. AutoShow scrive l'attributo classico `autoShow` sul campo pivot e viene supportato da tutte le versioni di Excel a partire da Excel 97. `filterTop10` scrive una voce `PivotFilter` del formato moderno, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta con una versione precedente di Excel, una tabella pivot che utilizza il filtro moderno ricade sulla visualizzazione di tutti gli elementi. Per i documenti che devono essere salvati e riaperti con strumenti legacy, preferire `top10AutoShow`; per le cartelle di lavoro moderne, preferire `filterTop10` perché si integra con gli altri filtri valore.
{{% /alert %}}

## **Articoli correlati**
- [Filtro delle tabelle pivot per etichetta o valore](/cells/it/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Aggiunta di campi di riga e colonna alla tabella pivot](/cells/it/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Raggruppamento dei campi pivot nella tabella pivot](/cells/it/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Aggiornamento della tabella pivot](/cells/it/nodejs-cpp/refresh-pivot-table/)
- [Aggiunta di un campo pagina alla tabella pivot](/cells/it/nodejs-cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}