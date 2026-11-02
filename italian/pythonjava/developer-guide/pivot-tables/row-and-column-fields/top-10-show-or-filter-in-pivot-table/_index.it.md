---
title: Visualizzazione o filtro dei primi 10 in una tabella pivot
linktitle: Visualizzazione o filtro dei primi 10 in una tabella pivot
description: Scopri come mostrare in Aspose.Cells for Python via Java solo gli elementi posizionati più in alto o più in basso nella classifica di un campo pivot. Questo articolo illustra il metodo top10AutoShow di Excel 97-2003, la lettura delle opzioni con Top10AutoShowSettings e il filtro dei primi 10 di Excel 2007-365 tramite filterTop10.
keywords: Aspose.Cells for Python via Java, tabella pivot, primi 10, visualizzazione automatica, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /it/python-java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può risultare difficile da leggere quando il campo contiene decine di elementi. Un report dei primi 10 mantiene soltanto gli elementi posizionati più in alto o più in basso nella classifica, offrendo esattamente i risultati necessari per report di classificazione come «i 5 prodotti principali in base al fatturato» o «le 3 regioni con meno vendite». Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **AutoShow di Excel 97-2003** — il metodo `PivotField.top10AutoShow()`. Questa è l'impostazione classica «Mostra i primi/ultimi N elementi», memorizzata direttamente nel campo pivot. Funziona in tutte le versioni di Excel, sia vecchie sia recenti, perché fa parte del formato originale della tabella pivot.
- **Filtro dei primi 10 di Excel 2007-365** — il metodo `PivotField.filterTop10()`. È il filtro moderno sui valori «Primi 10», disponibile nel menu del campo sotto «Filtri valori». Viene memorizzato come oggetto `PivotFilter` associato al campo e consente una classificazione basata sul numero di elementi o sulla percentuale.

## **Visualizzazione dei primi 10 in Excel 97-2003 (top10AutoShow)**
L'impostazione AutoShow classica viene configurata con una singola chiamata a `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)`:
- `isAutoShow` — attiva o disattiva l'impostazione AutoShow nel campo.
- `isTop` — `True` mantiene gli elementi con la classificazione più alta (Primi), mentre `False` mantiene quelli con la classificazione più bassa (Ultimi).
- `count` — indica quanti elementi mantenere, ad esempio 10 per un report classico dei primi 10.
- `rankBy` — l'indice, a partire da zero, del **campo dati** i cui valori vengono utilizzati per classificare gli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classificazione può essere basata su un campo valore o sul campo stesso. Di seguito sono illustrate due varianti.

### **Classificazione in base a un campo valore**
Classificare gli elementi del campo di riga in base a un campo valore, ad esempio Somma delle vendite. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i 2 sport con le vendite più alte. `rankBy` è 0 perché «Somma delle vendite» è il campo dati all'indice 0.

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
sport_field.setAutoShow(True)
sport_field.setAutoShowCount(2)
sport_field.setAutoShowField(2)
pivot_table.calculateData()
workbook.save("output-top10-by-value-field.xlsx")
jpype.shutdownJVM()
```

### **Classificazione in base al campo stesso**
Un campo può essere classificato in base a sé stesso, passando -1 come `rankBy`. Per questa variante non è necessario alcun campo dati aggiuntivo; è sufficiente che il campo si trovi nell'area delle righe (o delle colonne). L'esempio seguente mostra i 3 sport in fondo alla classifica, ordinati in base al campo stesso. Quando questa impostazione viene salvata, l'attributo `rankBy` viene omesso dall'XML della tabella pivot perché -1 è il valore predefinito del formato e `Top10AutoShowSettings.getRankBy()` restituisce nuovamente il valore -1.

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
# Mostra i 3 elementi inferiori classificati in base al campo stesso (rankBy = -1)
sport_field.top10AutoShow(True, False, 3, -1)
pivot_table.calculateData()
workbook.save("output-top10-by-field-itself.xlsx")
jpype.shutdownJVM()
```

## **Lettura delle opzioni correnti (Top10AutoShowSettings)**
Il metodo `PivotField.getTop10AutoShowSettings()` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate nel campo. Utilizzarlo per controllare come vengono presentati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata, indipendentemente dal fatto che la cartella di lavoro sia stata caricata da file.

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

Le quattro proprietà corrispondono agli attributi AutoShow classici scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`); pertanto, i valori letti corrispondono a quelli applicati da ogni versione di Excel.

## **Nota**

{{% alert color="primary" %}}
- Le API di accesso diretto di `PivotField`, ossia `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` e `getAutoShowField()`, sono obsolete. Utilizzare invece l'oggetto `Top10AutoShowSettings`: `PivotField.isAutoShow()` diventa `Top10AutoShowSettings.isAutoShow()`, `PivotField.isAscendShow()` diventa `Top10AutoShowSettings.isTop()`, `PivotField.getAutoShowCount()` diventa `Top10AutoShowSettings.getAutoShowCount()` e `PivotField.getAutoShowField()` diventa `Top10AutoShowSettings.getRankBy()`. Il metodo `top10AutoShow()` è il metodo supportato per modificare le impostazioni.
- `top10AutoShow` funziona con i campi di riga e di colonna. Un campo collocato esclusivamente nell'area della pagina (filtro) non può essere classificato in questo modo, poiché i suoi elementi non sono disposti nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro dei primi 10 (filterTop10)**
Le versioni moderne di Excel offrono «Primi 10» come filtro sui valori nel menu del campo (Filtri valori, Primi 10...). Aspose.Cells modella questa funzionalità tramite il metodo `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)`, che restituisce il `PivotFilter` creato:
- `valueFieldIndex` — l'indice, a partire da zero, del campo dati i cui valori aggregati vengono utilizzati per classificare gli elementi.
- `type` — determina il significato di `itemCount`. `PivotFilterType.COUNT` mantiene un numero fisso di elementi (opzione Elementi della finestra di dialogo). `PivotFilterType.PERCENT` mantiene una percentuale di elementi; pertanto, `itemCount` rappresenta la percentuale stessa e il valore 30 mantiene i primi 30 per cento. `PivotFilterType.SUM` classifica gli elementi in base alla copertura cumulativa dei valori.
- `isTop` — `True` per Primi, `False` per Ultimi.
- `itemCount` — il valore N in «Primi N»; l'unità di misura dipende da `type`.

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
    # Filtro Top 10 — mantieni i 2 elementi in base a "Sum of Sales" (indice del campo dati 0)
    filter = sport_field.filterTop10(0, PivotFilterType.COUNT, True, 2)
    # Per un filtro basato su percentuale, mantieni i primi 30 percento degli elementi:
    # sport_field.filterTop10(0, PivotFilterType.PERCENT, True, 30)
    pivot_table.getPivotCache().refresh()
    pivot_table.calculateData()
    workbook.save("output-top10-filter.xlsx")
finally:
    jpype.shutdownJVM()
```

{{% alert color="primary" %}}
`top10AutoShow` e `filterTop10` sono due funzionalità distinte. AutoShow scrive il gruppo di attributi classici `autoShow` sul campo pivot e la relativa impostazione viene rispettata da tutte le versioni di Excel, a partire da Excel 97. `filterTop10` scrive una voce `PivotFilter` moderna, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, una tabella pivot che usa il filtro moderno torna a mostrare tutti gli elementi. Per i documenti che devono essere rielaborati senza perdita di dati tramite strumenti legacy, è preferibile `top10AutoShow`; per le cartelle di lavoro moderne, è preferibile `filterTop10` perché si combina con gli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Filtraggio delle tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Aggiunta di campi di riga e colonna alla tabella pivot](/cells/it/python-java/pivot-table-add-row-and-column-fields/)
- [Raggruppamento dei campi pivot nella tabella pivot](/cells/it/python-java/group-pivot-fields-in-the-pivot-table/)
- [Aggiornamento della tabella pivot](/cells/it/python-java/refresh-pivot-table/)
- [Aggiunta di un campo pagina alla tabella pivot](/cells/it/python-java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python" >}}