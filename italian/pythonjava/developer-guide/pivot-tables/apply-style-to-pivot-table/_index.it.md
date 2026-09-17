---
title: Applica stili alle tabelle pivot in Aspose.Cells for Python via Java
linktitle: Applica stili alle tabelle pivot
description: Impara come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Python via Java, trattando i formati automatici legacy XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati di tabella pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Python via Java stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'applicazione sia dei formati automatici legacy per le tabelle pivot (pensati per i file `.xls`) sia degli stili moderni denominati o personalizzati per le tabelle pivot (pensati per i file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file con cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.
{{% /alert %}}

## **Introduzione**
Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse è determinata dal formato di file con cui salvi la cartella di lavoro, non dal formato da cui la leggi. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx` e, in tal caso, si applica l'API di stile moderna anziché quella legacy.
- `pivotTable.setPivotTableStyleType(int)` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `pivotTable.setPivotTableStyleName(String)` seleziona uno stile personalizzato che definisci tu stesso tramite `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Gli stili personalizzati sono necessari ogni volta che vuoi modificare colori, bordi o font oltre quanto offerto dai preset.
Inoltre, `pivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi cosa impostata tramite le due API basate sul nome di stile sopra. È utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applica un formato automatico predefinito legacy XLS**
Il metodo `setAutoFormatType` su una tabella pivot accetta un valore dall'enumerazione `com.aspose.cells.pivot.PivotTableAutoFormatType`. I valori disponibili sono `REPORT_1` fino a `REPORT_10`, `CLASSIC` e `TABLE_1` fino a `TABLE_10`.
L'esempio seguente carica una cartella di lavoro vuota, popola i dati di esempio Fruit/Year/Amount, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.REPORT_5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}
**Perché nessun campo di colonna?** I formati automatici della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) sono stati progettati nel classico Excel per **tabelle pivot a dimensione singola** con solo campi di riga e valori — non hanno alcuna formattazione predefinita per le intestazioni dei campi di colonna. Se la tua tabella pivot richiede campi di colonna, utilizza invece i preset moderni di `PivotTableStyleType` dallo [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), che sono progettati per il layout bidimensionale utilizzato da Excel moderno.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType
# Scenario 1: Applica un formato automatico preimpostato XLS legacy
# API in uso: PivotTable.AutoFormatType
# Formato del file di destinazione: .xls (legacy)
# Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Crea una nuova cartella di lavoro
workbook = Workbook()
# Ottieni il primo foglio di lavoro
sheet = workbook.getWorksheets().get(0)
# Popola i dati di origine con la riga di intestazione (Fruit, Year, Amount)
# e 9 righe di dati che coprono grape, blueberry, kiwi, cherry negli anni 2020 e 2021
sheet.getCells().get(0, 0).putValue("Fruit")
sheet.getCells().get(0, 1).putValue("Year")
sheet.getCells().get(0, 2).putValue("Amount")
sheet.getCells().get(1, 0).putValue("grape")
sheet.getCells().get(1, 1).putValue(2020)
sheet.getCells().get(1, 2).putValue(50)
sheet.getCells().get(2, 0).putValue("blueberry")
sheet.getCells().get(2, 1).putValue(2020)
sheet.getCells().get(2, 2).putValue(30)
sheet.getCells().get(3, 0).putValue("kiwi")
sheet.getCells().get(3, 1).putValue(2020)
sheet.getCells().get(3, 2).putValue(25)
sheet.getCells().get(4, 0).putValue("cherry")
sheet.getCells().get(4, 1).putValue(2020)
sheet.getCells().get(4, 2).putValue(40)
sheet.getCells().get(5, 0).putValue("grape")
sheet.getCells().get(5, 1).putValue(2021)
sheet.getCells().get(5, 2).putValue(60)
sheet.getCells().get(6, 0).putValue("blueberry")
sheet.getCells().get(6, 1).putValue(2021)
sheet.getCells().get(6, 2).putValue(35)
sheet.getCells().get(7, 0).putValue("kiwi")
sheet.getCells().get(7, 1).putValue(2021)
sheet.getCells().get(7, 2).putValue(28)
sheet.getCells().get(8, 0).putValue("cherry")
sheet.getCells().get(8, 1).putValue(2021)
sheet.getCells().get(8, 2).putValue(45)
sheet.getCells().get(9, 0).putValue("grape")
sheet.getCells().get(9, 1).putValue(2020)
sheet.getCells().get(9, 2).putValue(45)
# Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", usando l'intervallo di origine A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)
# Assegna i campi: Fruit -> Righe, Amount -> Dati
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")
# Applica il formato automatico preimpostato XLS legacy "Report5"
# Nota: questa proprietà ha significato solo quando si salva come .xls.
# Quando viene salvato come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# e utilizza qualsiasi PivotTableStyleType / PivotTableStyleName specificato.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)
# Salva la cartella di lavoro nel formato legacy .xls
workbook.save("output.xls")
jpype.shutdownJVM()
```

## **Applica uno stile di tabella pivot predefinito denominato moderno**

## **Definisci e applica uno stile personalizzato di tabella pivot**
I preset predefiniti non possono essere modificati. Ogni volta che hai bisogno di sovrascrivere colori, bordi o font, devi definire uno stile personalizzato per la tabella pivot. Il flusso di lavoro prevede tre passaggi:
1. Aggiungi uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Questo restituisce l'indice dello stile appena creato.
2. Configura lo stile aggiungendo elementi (come `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) tramite `tableStyle.getTableStyleElements().add(TableStyleElementType)`, quindi assegna uno `Style` a ciascun elemento tramite `tableStyleElement.setElementStyle(Style)`.
3. Applica lo stile personalizzato alla tabella pivot chiamando `pivotTable.setPivotTableStyleName(String)` con il nome dello stile. Non utilizzare qui `setPivotTableStyleType`, poiché quel metodo seleziona i preset predefiniti.

{{% alert color="primary" %}}
`setPivotTableStyleName` e `setPivotTableStyleType` non sono intercambiabili. Usa `setPivotTableStyleType` per i preset predefiniti e `setPivotTableStyleName` per gli stili personalizzati che hai definito tramite `addPivotTableStyle`. Impostarli entrambi è innocuo, ma viene reso solo quello corrispondente alla sorgente prevista.
{{% /alert %}}

I valori disponibili di `TableStyleElementType` includono `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` e `PAGE_FIELD_VALUES`.
L'esempio seguente definisce uno stile personalizzato di tabella pivot con un bordo sottile nero su `WHOLE_TABLE` e un font rosso in grassetto su `GRAND_TOTAL_ROW`, quindi lo applica tramite `setPivotTableStyleName` e salva come `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from asposecells.api import PivotFieldType, TableStyleElementType, BorderType, CellBorderType
from java.awt import Color
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Popola i dati sorgente: riga di intestazione + 9 righe di dati (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(200)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(300)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(400)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(500)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(600)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(700)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(800)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(900)
# Aggiungi una tabella pivot con origine A1:C10, ancorata in E3, denominata "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Passo 1: registra un nuovo stile di tabella pivot personalizzato e memorizza il suo indice
styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle")
tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex)
# Passo 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE)
wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex)
wholeTableStyle = workbook.createStyle()
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
wholeTableStyle.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
wholeTableElement.setElementStyle(wholeTableStyle)
# Passo 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW)
grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex)
grandTotalStyle = workbook.createStyle()
grandTotalStyle.getFont().setBold(True)
grandTotalStyle.getFont().setColor(Color.RED)
grandTotalElement.setElementStyle(grandTotalStyle)
# Passo 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è riservato ai preset predefiniti)
pivotTable.setPivotTableStyleName("CustomPivotStyle")
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Applica uno stile a ogni cella della tabella pivot con FormatAll**
`pivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dei dati, le intestazioni di riga e colonna e i totali. Qualsiasi cosa precedentemente impostata tramite `setPivotTableStyleType` o `setPivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}
`formatAll` sovrascrive sia `setPivotTableStyleType` sia `setPivotTableStyleName`. Usalo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.
{{% /alert %}}

L'esempio seguente crea uno `Style` con un riempimento giallo pieno, un font blu scuro in grassetto e bordi sottili neri su tutti i lati, quindi lo applica con `formatAll` e salva come `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType
# Scenario 4: Applica un singolo stile a ogni cella della tabella pivot usando FormatAll
# API in uso: PivotTable.FormatAll(Style)
# Formato di destinazione: .xlsx
# Riferimento GitHub: vedi il repository Aspose.Cells-for-.NET — esempi di stile delle tabelle pivot
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
# Popola i dati sorgente: riga intestazione (riga 1) + 9 righe di dati (righe 2-10)
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(5000)
worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(3000)
worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(4000)
worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(2000)
worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(6000)
worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(3500)
worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(4500)
worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(2500)
worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(5500)
# Aggiungi tabella pivot: intervallo sorgente A1:C10, cella di destinazione E3, nome "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)
# Assegna campi pivot: Frutta -> area Riga, Anno -> area Colonna, Importo -> area Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")
# Crea uno stile che verrà forzato su ogni cella della tabella pivot
style = workbook.createStyle()
style.setForegroundColor(Color.YELLOW)
style.setPattern(BackgroundType.SOLID)
style.getFont().setIsBold(True)
style.getFont().setColor(Color.DARK_BLUE)
style.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.TOP_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.BOTTOM_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.LEFT_BORDER).setColor(Color.BLACK)
style.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)
style.getBorders().get(BorderType.RIGHT_BORDER).setColor(Color.BLACK)
# Applica FormatAll: forza questo singolo stile su ogni cella della tabella pivot,
# sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName precedentemente impostato
pivotTable.formatAll(style)
# Salva la cartella di lavoro nel formato .xlsx moderno
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Quale API di stile devo usare?**
La scelta dell'API di stile dipende dal formato di file con cui stai salvando. Usa la tabella seguente come riferimento rapido.
| Formato del file di destinazione | API da usare | Note |
|---|---|---|
| `.xls` (legacy) | `pivotTable.setAutoFormatType(int)` | Valori da `com.aspose.cells.pivot.PivotTableAutoFormatType` (ad es. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignorato quando si salva nei formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `pivotTable.setPivotTableStyleType(int)` | Valori da `com.aspose.cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Da usare quando i preset predefiniti non sono sufficienti. Configura tramite `tableStyleElement.setElementStyle(Style)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `pivotTable.formatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |
In caso di dubbio, salva come `.xlsx` e usa `setPivotTableStyleType` per i temi predefiniti oppure `setPivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="python" >}}