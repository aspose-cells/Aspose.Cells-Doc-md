---
title: Applicare stili alle tabelle pivot in Aspose.Cells for Python via .NET
linktitle: Applicare stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Python via .NET, coprendo le formattazioni automatiche legacy di XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Python via .NET stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/python-net/apply-style-to-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'applicazione sia delle formattazioni automatiche legacy per tabelle pivot (pensate per i file `.xls`) sia degli stili denominati moderni o personalizzati per tabelle pivot (pensati per i file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato del file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.
{{% /alert %}}

## **Introduzione**
Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse dipende dal formato del file in cui si salva la cartella di lavoro, non dal formato da cui la si legge. Una cartella di lavoro caricata da un file `.xls` può essere salvata di nuovo come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.
- `PivotTable.pivot_table_style_type` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, compresi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.pivot_table_style_name` seleziona uno stile personalizzato che definisci tu stesso tramite `workbook.worksheets.table_styles.add_pivot_table_style(...)`. Gli stili personalizzati sono necessari ogni volta che desideri modificare colori, bordi o caratteri oltre quanto offerto dai preset.
Inoltre, `PivotTable.format_all(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione definita tramite le due API basate sul nome dello stile sopra menzionate. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare una formattazione automatica preset legacy di XLS**
`PivotTable.auto_format_type` accetta un valore dall'enumerazione `aspose.cells.pivot.PivotTableAutoFormatType`. I valori disponibili sono `REPORT_1` fino a `REPORT_10`, `CLASSIC` e `TABLE_1` fino a `TABLE_10`.
L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Fruit/Year/Amount, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.REPORT_5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}
**Perché nessun campo colonna?** Le formattazioni automatiche della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) sono state progettate in Excel classico per **tabelle pivot a dimensione singola** con solo campi riga e valori — non dispongono di uno stile predefinito per le intestazioni dei campi colonna. Se la tua tabella pivot necessita di campi colonna, utilizza invece i preset moderni di `PivotTableStyleType` illustrati nello [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), che sono progettati per il layout bidimensionale usato da Excel moderno.
{{% /alert %}}

```python
import aspose.cells as ac
# Scenario 1: Applica un formato automatico preimpostato XLS legacy
# API in uso: PivotTable.AutoFormatType
# Formato file di destinazione: .xls (legacy)
# Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Crea una nuova cartella di lavoro
workbook = ac.Workbook()
# Ottieni il primo foglio di lavoro
sheet = workbook.worksheets[0]
# Popola i dati di origine con la riga di intestazione (Frutto, Anno, Importo)
# e 9 righe di dati che coprono uva, mirtillo, kiwi, ciliegia tra il 2020 e il 2021
sheet.cells[0, 0].put_value("Fruit")
sheet.cells[0, 1].put_value("Year")
sheet.cells[0, 2].put_value("Amount")
sheet.cells[1, 0].put_value("grape")
sheet.cells[1, 1].put_value(2020)
sheet.cells[1, 2].put_value(50)
sheet.cells[2, 0].put_value("blueberry")
sheet.cells[2, 1].put_value(2020)
sheet.cells[2, 2].put_value(30)
sheet.cells[3, 0].put_value("kiwi")
sheet.cells[3, 1].put_value(2020)
sheet.cells[3, 2].put_value(25)
sheet.cells[4, 0].put_value("cherry")
sheet.cells[4, 1].put_value(2020)
sheet.cells[4, 2].put_value(40)
sheet.cells[5, 0].put_value("grape")
sheet.cells[5, 1].put_value(2021)
sheet.cells[5, 2].put_value(60)
sheet.cells[6, 0].put_value("blueberry")
sheet.cells[6, 1].put_value(2021)
sheet.cells[6, 2].put_value(35)
sheet.cells[7, 0].put_value("kiwi")
sheet.cells[7, 1].put_value(2021)
sheet.cells[7, 2].put_value(28)
sheet.cells[8, 0].put_value("cherry")
sheet.cells[8, 1].put_value(2021)
sheet.cells[8, 2].put_value(45)
sheet.cells[9, 0].put_value("grape")
sheet.cells[9, 1].put_value(2020)
sheet.cells[9, 2].put_value(45)
# Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", utilizzando l'intervallo di origine A1:C10
pivot_index = sheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = sheet.pivot_tables[pivot_index]
# Assegna i campi: Frutto -> Righe, Importo -> Dati
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Applica il formato automatico preimpostato XLS legacy "Report5"
# Nota: questa proprietà è significativa solo quando si salva come .xls.
# Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# e usa qualsiasi cosa specificata da PivotTableStyleType / PivotTableStyleName.
pivot_table.auto_format_type = ac.PivotTableAutoFormatType.REPORT5
# Salva la cartella di lavoro nel formato .xls legacy
workbook.save("output.xls")
```

## **Applicare uno stile preset denominato moderno di tabella pivot**

## **Definire e applicare uno stile personalizzato di tabella pivot**
I preset predefiniti non possono essere modificati. Ogni volta che hai bisogno di sovrascrivere colori, bordi o caratteri, devi definire uno stile personalizzato per la tabella pivot. Il flusso di lavoro si compone di tre passaggi:
1. Aggiungi uno stile personalizzato alla collezione `table_styles` della cartella di lavoro tramite `workbook.worksheets.table_styles.add_pivot_table_style(name)`. Questo restituisce l'indice dello stile appena creato.
2. Configura lo stile aggiungendo elementi (come `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) tramite `table_style.table_style_elements.add(TableStyleElementType)`, quindi assegna uno `Style` a ciascun elemento tramite `table_style_element.set_element_style(Style)`.
3. Applica lo stile personalizzato alla tabella pivot impostando `PivotTable.pivot_table_style_name` sul nome dello stile. Non utilizzare qui `pivot_table_style_type`, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}
`pivot_table_style_name` e `pivot_table_style_type` non sono intercambiabili. Usa `pivot_table_style_type` per i preset predefiniti e `pivot_table_style_name` per gli stili personalizzati che hai definito tramite `add_pivot_table_style`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente alla sorgente prevista.
{{% /alert %}}

I valori disponibili di `TableStyleElementType` includono `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` e `PAGE_FIELD_VALUES`.
L'esempio seguente definisce uno stile personalizzato per la tabella pivot con un bordo nero sottile su `WHOLE_TABLE` e un carattere rosso in grassetto su `GRAND_TOTAL_ROW`, quindi lo applica tramite `pivot_table_style_name` e salva come `.xlsx`.

```python
import aspose.cells as ac
import System.Drawing
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Popola i dati sorgente: riga intestazione + 9 righe di dati (A1:C10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(100)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(200)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(300)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(400)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(500)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(600)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(700)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(800)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(900)
# Aggiungi tabella pivot con origine da A1:C10, ancorata a E3, denominata "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
pivot_table.add_field_to_area(ac.PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(ac.PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(ac.PivotFieldType.DATA, "Amount")
# Passo 1: registra un nuovo stile personalizzato di tabella pivot e acquisisci il suo indice
style_index = workbook.worksheets.table_styles.add_pivot_table_style("CustomPivotStyle")
table_style = workbook.worksheets.table_styles[style_index]
# Passo 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
whole_table_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.WHOLE_TABLE)
whole_table_element = table_style.table_style_elements[whole_table_element_index]
whole_table_style = workbook.create_style()
whole_table_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.TOP_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.BOTTOM_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.LEFT_BORDER].color = System.Drawing.Color.Black
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN
whole_table_style.borders[ac.BorderType.RIGHT_BORDER].color = System.Drawing.Color.Black
whole_table_element.set_element_style(whole_table_style)
# Passo 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
grand_total_element_index = table_style.table_style_elements.add(ac.TableStyleElementType.GRAND_TOTAL_ROW)
grand_total_element = table_style.table_style_elements[grand_total_element_index]
grand_total_style = workbook.create_style()
grand_total_style.font.is_bold = True
grand_total_style.font.color = System.Drawing.Color.Red
grand_total_element.set_element_style(grand_total_style)
# Passo 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per preset predefiniti)
pivot_table.pivot_table_style_name = "CustomPivotStyle"
workbook.save("output.xlsx")
```

## **Applicare un unico stile a ogni cella della tabella pivot con FormatAll**
`PivotTable.format_all(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, comprese l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione definita in precedenza tramite `pivot_table_style_type` o `pivot_table_style_name` viene sovrascritta.

{{% alert color="primary" %}}
`format_all` sovrascrive sia `pivot_table_style_type` sia `pivot_table_style_name`. Usalo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.
{{% /alert %}}

L'esempio seguente crea uno `Style` con un riempimento giallo pieno, un carattere blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `format_all` e salva come `.xlsx`.

```python
from System.Drawing import Color
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells import BackgroundType, CellBorderType, BorderType
# Scenario 4: applicare un singolo stile a ogni cella della tabella pivot usando FormatAll
# API utilizzata: PivotTable.FormatAll(Style)
# Formato di destinazione: .xlsx
# Riferimento GitHub: vedere il repository Aspose.Cells-for-.NET — esempi di stile delle tabelle pivot
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
# Popolare i dati di origine: riga di intestazione (riga 1) + 9 righe di dati (righe 2-10)
worksheet.cells["A1"].put_value("Fruit")
worksheet.cells["B1"].put_value("Year")
worksheet.cells["C1"].put_value("Amount")
worksheet.cells["A2"].put_value("Grape")
worksheet.cells["B2"].put_value(2020)
worksheet.cells["C2"].put_value(5000)
worksheet.cells["A3"].put_value("Blueberry")
worksheet.cells["B3"].put_value(2020)
worksheet.cells["C3"].put_value(3000)
worksheet.cells["A4"].put_value("Kiwi")
worksheet.cells["B4"].put_value(2020)
worksheet.cells["C4"].put_value(4000)
worksheet.cells["A5"].put_value("Cherry")
worksheet.cells["B5"].put_value(2020)
worksheet.cells["C5"].put_value(2000)
worksheet.cells["A6"].put_value("Grape")
worksheet.cells["B6"].put_value(2021)
worksheet.cells["C6"].put_value(6000)
worksheet.cells["A7"].put_value("Blueberry")
worksheet.cells["B7"].put_value(2021)
worksheet.cells["C7"].put_value(3500)
worksheet.cells["A8"].put_value("Kiwi")
worksheet.cells["B8"].put_value(2021)
worksheet.cells["C8"].put_value(4500)
worksheet.cells["A9"].put_value("Cherry")
worksheet.cells["B9"].put_value(2021)
worksheet.cells["C9"].put_value(2500)
worksheet.cells["A10"].put_value("Grape")
worksheet.cells["B10"].put_value(2021)
worksheet.cells["C10"].put_value(5500)
# Aggiungere la tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
pivot_index = worksheet.pivot_tables.add("A1:C10", "E3", "Pivot1")
pivot_table = worksheet.pivot_tables[pivot_index]
# Assegnare i campi pivot: Fruit -> area Riga, Year -> area Colonna, Amount -> area Dati
pivot_table.add_field_to_area(PivotFieldType.ROW, "Fruit")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Year")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Amount")
# Creare uno stile che verrà applicato forzatamente a ogni cella della tabella pivot
style = workbook.create_style()
style.foreground_color = Color.Yellow
style.pattern = BackgroundType.SOLID
style.font.is_bold = True
style.font.color = Color.DarkBlue
style.borders[BorderType.TOP_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.TOP_BORDER].color = Color.Black
style.borders[BorderType.BOTTOM_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.BOTTOM_BORDER].color = Color.Black
style.borders[BorderType.LEFT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.LEFT_BORDER].color = Color.Black
style.borders[BorderType.RIGHT_BORDER].line_style = CellBorderType.THIN
style.borders[BorderType.RIGHT_BORDER].color = Color.Black
# Applicare FormatAll: forza questo singolo stile su ogni cella della tabella pivot,
# sovrascrivendo eventuali PivotTableStyleType / PivotTableStyleName impostati in precedenza
pivot_table.format_all(style)
# Salvare la cartella di lavoro nel formato moderno .xlsx
workbook.save("output.xlsx")
```

## **Quale API di stile devo usare?**
La scelta dell'API di stile dipende dal formato del file in cui stai salvando. Usa la tabella seguente come riferimento rapido.
| Formato del file di destinazione | API da usare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.auto_format_type` | Valori da `aspose.cells.pivot.PivotTableAutoFormatType` (ad es. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignorato quando si salva nei formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.pivot_table_style_type` | Valori da `aspose.cells.PivotTableStyleType` (temi chiari/scuri, comprese le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.pivot_table_style_name` + `worksheets.table_styles.add_pivot_table_style(...)` | Da usare quando i preset predefiniti non sono sufficienti. Configura tramite `table_style_element.set_element_style(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.format_all(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile in tutta la tabella pivot. |
In caso di dubbio, salva come `.xlsx` e usa `pivot_table_style_type` per i temi predefiniti, oppure `pivot_table_style_name` per i temi personalizzati.

{{< app/cells/assistant language="python-net" >}}