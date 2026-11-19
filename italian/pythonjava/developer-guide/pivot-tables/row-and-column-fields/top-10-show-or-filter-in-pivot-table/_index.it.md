---
title: Mostra o Filtra i Top 10 in Tabella Pivot
linktitle: Mostra o Filtra i Top 10 in Tabella Pivot
description: Scopri come mostrare solo gli elementi classificati al primo o all'ultimo posto di un campo pivot in Aspose.Cells for Python via Java, questo articolo copre il metodo top10AutoShow di Excel 97‑2003, la lettura delle opzioni con Top10AutoShowSettings e il filtro Top 10 di Excel 2007‑365 via filterTop10.
keywords: Aspose.Cells for Python via Java, tabella pivot, top 10, visualizzazione automatica, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /it/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari d'uso**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può essere difficile da leggere quando il campo ha decine di membri. Un report Top 10 mantiene solo gli elementi più alti o più bassi in classifica, che è esattamente ciò di cui hanno bisogno i report di ranking — “top 5 prodotti per fatturato” o “bottom 3 regioni per numero di vendite”. Aspose.Cells supporta due meccanismi per questo, corrispondenti a due generazioni di Microsoft Excel.
- **Excel 97-2003 AutoShow** — il metodo `PivotField.top10AutoShow()`. Questa è l'impostazione classica “Mostra i primi/ultimi N elementi” memorizzata direttamente sul campo pivot. Funziona in ogni versione di Excel, vecchia e nuova, perché fa parte del formato originale della tabella pivot.
- **Excel 2007-365 Top 10 Filter** — il metodo `PivotField.filterTop10()`. Questo è il filtro valore Top 10 moderno che si trova nel menu del campo sotto Filtri valore. Viene memorizzato come oggetto `PivotFilter` collegato al campo e offre classificazione basata sul conteggio degli elementi e sulla percentuale.

## **Visualizzazione Top 10 in Excel 97-2003 (top10AutoShow)**
L'AutoShow classico si configura con una singola chiamata a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — abilita o disabilita l'impostazione AutoShow sul campo.
- `isTop` — `True` mantiene gli elementi più alti in classifica (Top), `False` mantiene i più bassi (Bottom).
- `count` — numero di elementi da conservare, ad esempio 10 per un report Top 10 classico.
- `rankBy` — l'indice (basato su zero) del **campo dati** i cui valori classificano gli elementi. Passare -1 per classificare gli elementi in base al campo stesso.

La classifica può essere basata su un campo valore o sul campo stesso. Esistono due varianti naturali, illustrate di seguito.

### **Classifica per un Campo Valore**
Classifica gli elementi del campo di riga in base a un normale campo valore, ad esempio Somma delle Vendite. L'esempio seguente crea una tabella pivot con un campo riga (`Sport`) e un campo dati (`Sales`), quindi mostra i primi 2 sport per vendite. `rankBy` è 0 perché “Sum of Sales” è il campo dati all'indice 0.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
sport_field.top10AutoShow(True, True, 2, 0)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Classifica per il Campo Stesso**
Un campo può anche essere classificato da sé stesso — passare -1 come `rankBy`. Non è necessario un campo dati aggiuntivo per questa variante; il campo deve semplicemente trovarsi nell'area riga (o colonna). L'esempio seguente mostra le ultime 3 sport classificati in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dal XML della tabella pivot perché -1 è il valore predefinito del formato, e `Top10AutoShowSettings.getRankBy()` restituisce -1.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sport")
worksheet.getCells().get("B1").putValue("Quarter")
worksheet.getCells().get("C1").putValue("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.getCells().get(row, 0).putValue(sport)
        worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
        row += 1
pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
pivot_table.calculateData()
sport_field = pivot_table.getRowFields().get(0)
# Show the bottom 3 items ranked by the field itself (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Lettura delle Opzioni Correnti (Top10AutoShowSettings)**
Il metodo `PivotField.getTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzalo per ispezionare come una cartella di lavoro esistente, o una tabella pivot appena configurata, presenterà i suoi elementi — inclusi i file delle cartelle di lavoro caricati.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
workbook = Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.getWorksheets().get(0).getPivotTables().get(0)
sport_field = pivot_table.getRowFields()[0]
settings = sport_field.getTop10AutoShowSettings()
print("AutoShow enabled: " + str(settings.isAutoShow()))
print("Direction: " + ("Top" if settings.isTop() else "Bottom"))
print("Item count: " + str(settings.getAutoShowCount()))
print("Ranking data field index: " + str(settings.getRankBy()))
jpype.shutdownJVM()
```

Le quattro proprietà corrispondono agli attributi AutoShow classici scritti nel XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), così i valori letti indietro sono quelli che ogni versione di Excel rispetterà.

## **Nota**

{{% alert color="primary" %}}
- Gli accessor diretti di `PivotField` `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` e `getAutoShowField()` sono contrassegnati come obsoleti. Utilizzare l'oggetto `Top10AutoShowSettings`: `PivotField.isAutoShow()` diventa `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` diventa `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` diventa `Top10AutoShowSettings.getAutoShowCount()`, e `PivotField.getAutoShowField()` diventa `Top10AutoShowSettings.getRankBy()`. Il metodo `top10AutoShow()` stesso è il modo supportato per modificare le impostazioni.
- `top10AutoShow` funziona con i campi riga e colonna. Un campo presente solo nell'area pagina (filtro) non può essere classificato in questo modo perché i suoi elementi non sono visualizzati nel corpo della pivot.
{{% /alert %}}

## **Excel 2007-365: Filtro Top 10 (filterTop10)**
Le versioni moderne di Excel espongono Top 10 come filtro valore nel menu del campo (Filtri valore, Top 10...). Aspose.Cells lo modella con il metodo `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, che restituisce il `PivotFilter` creato:
- `valueFieldIndex` — l'indice (basato su zero) del campo dati i cui valori aggregati classificano gli elementi.
- `type` — significato di `itemCount`. `PivotFilterType.COUNT` conserva un numero fisso di elementi (opzione Elementi della finestra). `PivotFilterType.PERCENT` conserva una percentuale degli elementi, quindi `itemCount` è la percentuale stessa — 30 mantiene il top 30 percento. `PivotFilterType.SUM` classifica in base alla copertura di valore cumulativa.
- `isTop` — `True` per Top, `False` per Bottom.
- `itemCount` — il N in Top N; la sua unità dipende da `type`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotFieldType, PivotFilterType
try:
    workbook = Workbook()
    worksheet = workbook.getWorksheets().get(0)
    worksheet.getCells().get("A1").putValue("Sport")
    worksheet.getCells().get("B1").putValue("Quarter")
    worksheet.getCells().get("C1").putValue("Sales")
    sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
    row = 2
    for sport in sports:
        for quarter in range(1, 4):
            worksheet.getCells().get(row, 0).putValue(sport)
            worksheet.getCells().get(row, 1).putValue("Qtr" + str(quarter))
            worksheet.getCells().get(row, 2).putValue(1000 + 777 * row)
            row += 1
    pivot_table = worksheet.getPivotTables().add("A1:C16", 2, 5)
    pivot_table.addFieldToArea(PivotFieldType.ROW, "Sport")
    pivot_table.addFieldToArea(PivotFieldType.DATA, "Sales")
    pivot_table.calculateData()
    sport_field = pivot_table.getRowFields().get(0)
    # Top 10 Filter — keep the top 2 items by "Sum of Sales" (data field index 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # For a percentage-based filter instead, keep the top 30 percent of the items:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` e `filterTop10` sono due funzionalità separate. AutoShow scrive l'attributo classico `autoShow` impostato sul campo pivot ed è rispettato da tutte le versioni di Excel a partire da Excel 97. `filterTop10` scrive una voce moderna `PivotFilter`, che richiede Excel 2007 o successivo. Quando una cartella di lavoro è aperta in una versione di Excel più vecchia, una tabella pivot che utilizza il filtro moderno torna a mostrare tutti gli elementi. Per i documenti che devono passare attraverso strumenti legacy, preferire `top10AutoShow`; per le cartelle di lavoro moderne, preferire `filterTop10` perché si combina con gli altri filtri valore.
{{% /alert %}}

## **Articoli correlati**
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere campi riga e colonna alla tabella pivot](/cells/it/python-java/pivot-table-add-row-and-column-fields/)
- [Raggruppare i campi pivot nella tabella pivot](/cells/it/python-java/group-pivot-fields-in-the-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/python-java/refresh-pivot-table/)
- [Aggiungere campo pagina nella tabella pivot](/cells/it/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}