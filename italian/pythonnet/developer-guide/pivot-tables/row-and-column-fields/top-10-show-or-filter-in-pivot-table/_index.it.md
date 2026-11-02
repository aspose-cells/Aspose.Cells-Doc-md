---
title: Mostrare o filtrare i primi 10 in una tabella pivot
linktitle: Mostrare o filtrare i primi 10 in una tabella pivot
description: Scoprire come usare Aspose.Cells for Python via .NET per mostrare solo gli elementi che occupano le prime o le ultime posizioni in classifica all'interno di un campo pivot. Questo articolo descrive il metodo top_10_auto_show di Excel 97-2003, la lettura delle opzioni tramite top_10_auto_show_settings e il filtro Primi 10 di Excel 2007-365 tramite filter_top10.
keywords: Aspose.Cells, Python via .NET, tabella pivot, primi 10, mostra automatica, top_10_auto_show, top_10_auto_show_settings, PivotFieldTop10AutoShowSettings, filter_top10, PivotFilterType, PivotField, Python
type: docs
weight: 20
url: /it/python-net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
Una tabella pivot che elenca tutti gli elementi di un campo di riga può essere difficile da leggere quando il campo contiene decine di membri. Un report sui primi 10 conserva soltanto gli elementi che occupano le prime o le ultime posizioni in classifica, come richiesto dai report basati sulla classifica, ad esempio "i 5 prodotti con il reddito più alto" o "le 3 regioni con il minor numero di vendite". Aspose.Cells supporta due meccanismi a questo scopo, corrispondenti a due generazioni di Microsoft Excel.
- **Excel 97-2003 AutoShow** — il metodo `PivotField.top_10_auto_show()`. È l'impostazione classica "Mostra i primi/ultimi N elementi", memorizzata direttamente sul campo pivot. Funziona in tutte le versioni di Excel, indipendentemente dalla loro età, perché fa parte del formato originale della tabella pivot.
- **Excel 2007-365: filtro Primi 10** — il metodo `PivotField.filter_top10()`. È il moderno filtro dei valori Primi 10, disponibile nei Filtri valore del menu del campo. Viene memorizzato come oggetto `PivotFilter` associato al campo e supporta classifiche basate sul numero di elementi o sulla percentuale.

## **Mostra dei primi 10 in Excel 97-2003 (top_10_auto_show)**
L'AutoShow classico viene configurato mediante una singola chiamata al metodo `PivotField.top_10_auto_show(bool is_auto_show, bool is_top, int count, int rank_by)`:
- `is_auto_show` — abilita o disabilita l'impostazione AutoShow sul campo.
- `is_top` — `True` mantiene gli elementi classificati più in alto (Primi), mentre `False` mantiene quelli classificati più in basso (Ultimi).
- `count` — il numero di elementi da mantenere, ad esempio 10 per un report classico sui primi 10.
- `rank_by` — l'indice in base zero del **campo dati** i cui valori determinano la classifica degli elementi. Passare -1 per classificare gli elementi in base al campo stesso.
La classifica può essere determinata da un campo valore o dal campo stesso. Di seguito sono illustrate due varianti.

### **Classifica in base a un campo valore**
Classifica gli elementi del campo di riga in base a un campo valore standard, ad esempio Somma di vendite. L'esempio seguente crea una tabella pivot con un campo di riga (`Sport`) e un campo dati (`Sales`), quindi mostra i primi 2 sport in base alle vendite. `rank_by` è 0 perché "Somma di vendite" è il campo dati all'indice 0.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Mostra i 2 elementi principali classificati in base a "Sum of Sales" (indice del campo dati 0)
sport_field.top_10_auto_show(True, True, 2, 0)
pivot_table.calculate_data()
workbook.save("output-top10-by-value-field.xlsx")
```

### **Classifica in base al campo stesso**
Un campo può essere classificato in base ai propri valori: passare -1 come `rank_by`. Per questa variante non è necessario alcun campo dati aggiuntivo; è sufficiente che il campo sia posizionato nell'area delle righe (o delle colonne). L'esempio seguente mostra gli ultimi 3 sport in base ai valori del campo stesso. Quando questa impostazione viene salvata, l'attributo `rank_by` viene omesso dal XML della tabella pivot perché -1 è il valore predefinito del formato e `top_10_auto_show_settings.rank_by` restituisce di nuovo il valore -1.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
sport_field.top_10_auto_show(True, False, 3, -1)
pivot_table.calculate_data()
workbook.save("output-top10-by-field-itself.xlsx")
```

## **Lettura delle opzioni correnti (top_10_auto_show_settings)**
La proprietà `PivotField.top_10_auto_show_settings` restituisce un oggetto `PivotFieldTop10AutoShowSettings` che espone le opzioni AutoShow attualmente memorizzate sul campo. Utilizzarla per controllare come verranno presentati gli elementi in una cartella di lavoro esistente o in una tabella pivot appena configurata, anche quando la cartella di lavoro è stata caricata da file.

```python
import aspose.cells as ac
workbook = ac.Workbook("output-top10-by-value-field.xlsx")
pivot_table = workbook.worksheets[0].pivot_tables[0]
sport_field = pivot_table.row_fields[0]
settings = sport_field.top_10_auto_show_settings
print("AutoShow enabled: " + str(settings.is_auto_show))
print("Direction: " + ("Top" if settings.is_top else "Bottom"))
print("Item count: " + str(settings.auto_show_count))
print("Ranking data field index: " + str(settings.rank_by))
```

Le quattro proprietà corrispondono agli attributi classici di AutoShow scritti nell'XML della tabella pivot (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), quindi i valori letti sono quelli riconosciuti da tutte le versioni di Excel.

## **Nota**

{{% alert color="primary" %}}
- Le proprietà dirette `is_auto_show`, `is_ascend_show`, `auto_show_count` e `auto_show_field` di `PivotField` sono obsolete. Utilizzare invece l'oggetto `top_10_auto_show_settings`: `is_auto_show` corrisponde a `top_10_auto_show_settings.is_auto_show`, `is_ascend_show` a `top_10_auto_show_settings.is_top`, `auto_show_count` a `top_10_auto_show_settings.auto_show_count` e `auto_show_field` a `top_10_auto_show_settings.rank_by`. Per modificare le impostazioni, utilizzare il metodo `top_10_auto_show()`.
- `top_10_auto_show` funziona con i campi di riga e di colonna. Un campo collocato soltanto nell'area dei campi filtro (area pagina) non può essere classificato in questo modo, perché i suoi elementi non sono organizzati nel corpo della tabella pivot.
{{% /alert %}}

## **Excel 2007-365: filtro Primi 10 (filter_top10)**
Le versioni moderne di Excel offrono Primi 10 come filtro sui valori nel menu del campo (Filtri valore, Primi 10...). Aspose.Cells implementa questa funzionalità mediante il metodo `PivotField.filter_top10(int value_field_index, PivotFilterType type, bool is_top, int item_count)`, che restituisce l'oggetto `PivotFilter` creato:
- `value_field_index` — l'indice in base zero del campo dati i cui valori aggregati determinano la classifica degli elementi.
- `type` — il significato di `item_count`. `PivotFilterType.COUNT` mantiene un numero fisso di elementi (opzione Elementi della finestra di dialogo). `PivotFilterType.PERCENT` mantiene una percentuale degli elementi; pertanto `item_count` corrisponde direttamente alla percentuale: 30 mantiene il 30% degli elementi con i valori più alti. `PivotFilterType.SUM` classifica in base alla copertura cumulativa del valore.
- `is_top` — `True` per selezionare i valori più alti (Primi), `False` per selezionare quelli più bassi (Ultimi).
- `item_count` — il valore N nella selezione dei primi N; l'unità dipende da `type`.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType, PivotFilterType
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
worksheet.cells.get("A1").put_value("Sport")
worksheet.cells.get("B1").put_value("Quarter")
worksheet.cells.get("C1").put_value("Sales")
sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"]
row = 2
for sport in sports:
    for quarter in range(1, 4):
        worksheet.cells.get(row, 0).put_value(sport)
        worksheet.cells.get(row, 1).put_value("Qtr" + str(quarter))
        worksheet.cells.get(row, 2).put_value(1000 + 777 * row)
        row += 1
pivot_table = worksheet.pivot_tables.add("A1:C16", 2, 5)
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")
pivot_table.calculate_data()
sport_field = pivot_table.row_fields[0]
# Filtro Top 10 — mantieni i 2 migliori elementi in base a "Somma delle vendite" (indice del campo dati 0)
filter = sport_field.filter_top10(0, PivotFilterType.COUNT, True, 2)
# Per un filtro basato sulla percentuale, mantieni invece il 30% degli elementi con i valori più alti:
# sport_field.filter_top10(0, PivotFilterType.PERCENT, True, 30)
pivot_table.pivot_cache.refresh()
pivot_table.calculate_data()
workbook.save("output-top10-filter.xlsx")
```

{{% alert color="primary" %}}
`top_10_auto_show` e `filter_top10` sono due funzionalità distinte. AutoShow scrive sul campo pivot gli attributi classici associati a `autoShow` e viene applicato da tutte le versioni di Excel a partire da Excel 97. `filter_top10` scrive una voce `PivotFilter` moderna, che richiede Excel 2007 o versioni successive. Quando una cartella di lavoro viene aperta in una versione precedente di Excel, la tabella pivot che usa il filtro moderno viene visualizzata con tutti gli elementi. Per i documenti che devono superare un ciclo di salvataggio e riapertura con strumenti di versioni precedenti, preferire `top_10_auto_show`; per le cartelle di lavoro moderne, preferire `filter_top10`, perché si integra con gli altri filtri sui valori.
{{% /alert %}}

## **Articoli correlati**
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-net/filter-by-label-or-value-of-pivot-table/)
- [Aggiungere campi di riga e di colonna alla tabella pivot](/cells/it/python-net/pivot-table-add-row-and-column-fields/)
- [Raggruppare i campi pivot nella tabella pivot](/cells/it/python-net/group-pivot-fields-in-the-pivot-table/)
- [Aggiornare la tabella pivot](/cells/it/python-net/refresh-pivot-table/)
- [Aggiungere un campo pagina alla tabella pivot](/cells/it/python-net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="python-net" >}}