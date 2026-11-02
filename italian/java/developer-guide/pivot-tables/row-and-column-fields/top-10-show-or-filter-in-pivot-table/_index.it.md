---
title: Visualizzazione o filtro dei primi 10 in una tabella pivot
linktitle: Visualizzazione o filtro dei primi 10 in una tabella pivot
description: Scopri come mostrare solo gli elementi che occupano le posizioni più alte o più basse nella classifica di un campo pivot in Aspose.Cells for Java. Questo articolo descrive il metodo Top10AutoShow di Excel 97-2003, la lettura delle opzioni con Top10AutoShowSettings e il filtro dei primi 10 di Excel 2007-365 tramite FilterTop10.
keywords: Aspose.Cells, Java, tabella pivot, primi 10, visualizzazione automatica, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /it/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca ogni elemento di un campo di riga può essere difficile da leggere quando il campo contiene dozzine di elementi. Un report dei primi 10 conserva soltanto gli elementi in cima o in fondo alla classifica, ossia esattamente ciò di cui hanno bisogno i report di classificazione, come «i 5 prodotti principali per ricavi» o «le 3 regioni in fondo alla classifica per numero di vendite». Aspose.Cells supporta due meccanismi a questo scopo, che corrispondono a due generazioni di Microsoft Excel.
- **Visualizzazione automatica di Excel 97-2003** — il metodo `PivotField.top10AutoShow()`. È l'impostazione classica «Mostra i primi/ultimi N elementi», memorizzata direttamente sul campo pivot. Funziona in tutte le versioni di Excel, vecchie e nuove, perché fa parte del formato originale delle tabelle pivot.
- **Filtro dei primi 10 di Excel 2007-365** — il metodo `PivotField.filterTop10()`. È il filtro di valori moderno Top 10, disponibile nel menu del campo, in Filtri valore. Viene memorizzato come oggetto `PivotFilter` associato al campo e supporta classificazioni basate sul numero di elementi o sulla percentuale.

## **Visualizzazione dei primi 10 in Excel 97-2003 (top10AutoShow)**
La visualizzazione automatica classica viene configurata con una singola chiamata a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione `AutoShow` sul campo.
- `isTop` — `true` mantiene gli elementi in cima alla classifica (Primi), mentre `false` mantiene quelli in fondo alla classifica (Ultimi).
- `count` — il numero di elementi da mantenere, ad esempio 10 per un report classico dei primi 10.
- `rankBy` — l'indice in base zero del **campo di dati** i cui valori determinano la classificazione degli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classificazione può essere determinata da un campo di valore o dal campo stesso. Esistono due varianti tipiche, illustrate di seguito.

### **Classificazione in base a un campo di valore**
Classifica gli elementi del campo di riga in base a un campo di valore standard, come Somma di Vendite. L'esempio seguente costruisce una tabella pivot con un campo di riga (`Sport`) e un campo di dati (`Sales`), quindi mostra i primi 2 sport in base alle vendite. `rankBy` è 0 perché «Somma di Vendite» è il campo di dati con indice 0.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Mostra i primi 2 elementi classificati in base a "Sum of Sales" (indice del campo dati 0)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Classificazione in base al campo stesso**
Un campo può anche essere utilizzato per classificare i propri elementi: passare -1 come `rankBy`. Per questa variante non è necessario alcun campo di dati aggiuntivo; il campo deve trovarsi soltanto nell'area delle righe (o delle colonne). L'esempio seguente mostra gli ultimi 3 sport della classifica basata sul campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dall'XML della tabella pivot perché -1 è il valore predefinito del formato e `Top10AutoShowSettings.getRankBy()` restituisce -1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Mostra le 3 voci inferiori classificate in base al campo stesso (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Lettura delle opzioni correnti (Top10AutoShowSettings)**
Il metodo `PivotField.getTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni `AutoShow` attualmente memorizzate sul campo. Utilizzarlo per controllare come verranno presentati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata, anche nel caso di cartelle di lavoro caricate da file.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Le quattro proprietà corrispondono agli attributi classici di `AutoShow` scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), quindi i valori restituiti corrispondono a quelli che verranno applicati da ogni versione di Excel.

## **Nota**

{{% alert color="primary" %}}
- Le proprietà dirette di `PivotField` esposte da `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` e `getAutoShowField()` sono deprecate. Utilizzare invece l'oggetto `Top10AutoShowSettings`: `Top10AutoShowSettings.isAutoShow()` sostituisce `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` sostituisce `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` sostituisce `PivotField.getAutoShowCount()` e `Top10AutoShowSettings.getRankBy()` sostituisce `PivotField.getAutoShowField()`. Il metodo `PivotField.top10AutoShow()` è il metodo supportato per modificare le impostazioni.
- `top10AutoShow` funziona con i campi di riga e di colonna. Un campo presente soltanto nell'area della pagina (filtro) non può essere classificato in questo modo perché i suoi elementi non sono disposti nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro dei primi 10 (filterTop10)**
Le versioni moderne di Excel presentano l'opzione Top 10 come filtro di valori nel menu del campo (Filtri valore, Primi 10...). Aspose.Cells rappresenta questa funzionalità con il metodo `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, che restituisce l'oggetto `PivotFilter` creato:
- `valueFieldIndex` — l'indice in base zero del campo di dati i cui valori aggregati determinano la classificazione degli elementi.
- `type` — determina il significato di `itemCount`. `PivotFilterType.COUNT` mantiene un numero fisso di elementi (l'opzione Elementi della finestra di dialogo). `PivotFilterType.PERCENT` mantiene una percentuale degli elementi, quindi `itemCount` è essa stessa la percentuale: 30 mantiene i primi 30 per cento. `PivotFilterType.SUM` classifica gli elementi in base alla copertura cumulativa dei valori.
- `isTop` — `true` per Primi, `false` per Ultimi.
- `itemCount` — il valore N in «Primi N»; l'unità dipende da `type`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Filtro Top 10 - mantieni i 2 elementi superiori in base a "Sum of Sales" (indice del campo dati 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Per un filtro basato sulla percentuale, mantieni invece il 30% superiore degli elementi:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` e `filterTop10` sono due funzionalità distinte. `AutoShow` scrive sul campo pivot l'insieme degli attributi classici, tra cui `autoShow`, ed è supportato da tutte le versioni di Excel, a partire da Excel 97. `filterTop10` scrive una voce moderna di tipo `PivotFilter`, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, una tabella pivot che utilizza il filtro moderno ricade sulla visualizzazione di tutti gli elementi. Per i documenti che devono essere salvati e riaperti tramite strumenti di versioni precedenti, preferire `top10AutoShow`; per le cartelle di lavoro moderne, preferire `filterTop10` perché può essere utilizzato insieme agli altri filtri di valore.
{{% /alert %}}

## **Articoli correlati**
- [Filtro delle tabelle pivot per etichetta o valore](/cells/it/java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere campi di riga e colonna alla tabella pivot](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Raggruppare i campi pivot nella tabella pivot](/cells/it/java/group-pivot-fields-in-the-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/java/refresh-pivot-table/)
- [Aggiungere un campo di pagina alla tabella pivot](/cells/it/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}