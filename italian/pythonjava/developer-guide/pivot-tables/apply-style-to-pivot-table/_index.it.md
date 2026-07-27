---
title: Applicare stili alle tabelle pivot in Aspose.Cells per .NET
linktitle: Applicare stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Python via Java, coprendo autoformati XLS legacy, stili denominati moderni di Excel 2007+, stili personalizzati per tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Python via Java stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/python-java/apply-style-to-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta l'applicazione sia degli autoformati legacy per tabelle pivot (destinati ai file `.xls`) sia degli stili denominati moderni o personalizzati per tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra di esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui è stata letta. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx`, e in tal caso si applica l'API di stile moderna anziché quella legacy.

Per l'output legacy `.xls`, utilizzare il metodo `pivotTable.setAutoFormatType(int)` insieme all'enumerazione `com.aspose.cells.pivot.PivotTableAutoFormatType`. Questa API corrisponde al selettore di autoformato che la versione classica di Excel offriva per le tabelle pivot.

Per l'output moderno `.xlsx`, `.xlsm` e `.xlsb`, sono disponibili due varianti dell'API di stile:

- `pivotTable.setPivotTableStyleType(int)` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono in sola lettura.
- `pivotTable.setPivotTableStyleName(String)` seleziona uno stile personalizzato definito dall'utente tramite `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o font oltre a quanto offerto dai preset.

Inoltre, `pivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione effettuata tramite una delle API basate sul nome di stile sopra indicate. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicare un autoformato preset XLS legacy**

Il metodo `setAutoFormatType` su una tabella pivot accetta un valore dall'enumerazione `com.aspose.cells.pivot.PivotTableAutoFormatType`. I valori disponibili sono `REPORT_1` fino a `REPORT_10`, `CLASSIC` e `TABLE_1` fino a `TABLE_10`.

{{% alert color="primary" %}}

`setAutoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa impostazione e ricorre alle impostazioni `setPivotTableStyleType` e `setPivotTableStyleName`.

{{% /alert %}}

L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.REPORT_5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}

**Perché nessun campo colonna?** Gli autoformati della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) erano progettati in Excel classico per **tabelle pivot monodimensionali** con soli campi riga e valori — non hanno uno stile integrato per le intestazioni dei campi colonna. Se la tua tabella pivot richiede campi colonna, usa i preset moderni `PivotTableStyleType` dello Scenario 2 qui sotto, progettati per il layout bidimensionale usato da Excel moderno.

{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, PivotFieldType, PivotTableAutoFormatType

# Scenario 1: Applica un formato automatico preimpostato XLS legacy
# API in uso: PivotTable.AutoFormatType
# Formato file di destinazione: .xls (legacy)
# Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Crea una nuova cartella di lavoro
workbook = Workbook()

# Ottieni il primo foglio di lavoro
sheet = workbook.getWorksheets().get(0)

# Popola i dati sorgente con la riga di intestazione (Frutta, Anno, Importo)
# e 9 righe di dati che coprono uva, mirtillo, kiwi, ciliegia tra il 2020 e il 2021
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

# Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", utilizzando l'intervallo sorgente A1:C10
pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = sheet.getPivotTables().get(pivotIndex)

# Assegna i campi: Frutta -> Righe, Anno -> Colonne, Importo -> Dati
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Applica il formato automatico preimpostato XLS legacy "Report5"
# Nota: questa proprietà è significativa solo durante il salvataggio come .xls.
# Se salvato come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
# e utilizza qualsiasi cosa specifichino PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.Report5)

# Salva la cartella di lavoro nel formato .xls legacy
workbook.save("output.xls")

jpype.shutdownJVM()
```

## **Applicare uno stile preset denominato moderno di tabella pivot**

Il metodo `setPivotTableStyleType` su una tabella pivot accetta un valore dall'enumerazione `com.aspose.cells.PivotTableStyleType`. L'enumerazione copre i temi chiari `PIVOT_TABLE_STYLE_LIGHT_1` fino a `PIVOT_TABLE_STYLE_LIGHT_28` e i temi scuri `PIVOT_TABLE_STYLE_DARK_1` fino a `PIVOT_TABLE_STYLE_DARK_28`. Gli stili aggiunti in Excel 2017 (la seconda serie di temi chiari e scuri) sono raggiungibili tramite la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza dell'autoformato legacy, lo stile selezionato qui viene reso fedelmente da Excel e sopravvive ai round-trip attraverso altri strumenti Office.

L'esempio seguente utilizza gli stessi dati Frutto/Anno/Importo, crea una tabella pivot identica, applica `PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1` e salva la cartella di lavoro come `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PivotTableStyleType, PivotFieldType

# Scenario 2: Applica uno stile predefinito moderno di Excel 2007+ utilizzando PivotTableStyleType.
# Formato del file di destinazione: .xlsx. L'enum PivotTableStyleType si trova nel namespace Aspose.Cells
# (non in Aspose.Cells.Pivot) — ecco perché non servono ulteriori using per esso.
# Riferimento GitHub: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit")
worksheet.getCells().get("B1").putValue("Year")
worksheet.getCells().get("C1").putValue("Amount")

# 9 righe di dati di Frutto / Anno / Importo
worksheet.getCells().get("A2").putValue("Grape")
worksheet.getCells().get("B2").putValue(2020)
worksheet.getCells().get("C2").putValue(100)

worksheet.getCells().get("A3").putValue("Blueberry")
worksheet.getCells().get("B3").putValue(2020)
worksheet.getCells().get("C3").putValue(150)

worksheet.getCells().get("A4").putValue("Kiwi")
worksheet.getCells().get("B4").putValue(2020)
worksheet.getCells().get("C4").putValue(200)

worksheet.getCells().get("A5").putValue("Cherry")
worksheet.getCells().get("B5").putValue(2020)
worksheet.getCells().get("C5").putValue(180)

worksheet.getCells().get("A6").putValue("Grape")
worksheet.getCells().get("B6").putValue(2021)
worksheet.getCells().get("C6").putValue(120)

worksheet.getCells().get("A7").putValue("Blueberry")
worksheet.getCells().get("B7").putValue(2021)
worksheet.getCells().get("C7").putValue(170)

worksheet.getCells().get("A8").putValue("Kiwi")
worksheet.getCells().get("B8").putValue(2021)
worksheet.getCells().get("C8").putValue(210)

worksheet.getCells().get("A9").putValue("Cherry")
worksheet.getCells().get("B9").putValue(2021)
worksheet.getCells().get("C9").putValue(190)

worksheet.getCells().get("A10").putValue("Grape")
worksheet.getCells().get("B10").putValue(2021)
worksheet.getCells().get("C10").putValue(130)

# Aggiungi una tabella pivot in E3 con nome "Pivot1", con origine dati da A1:C10
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assegna i campi pivot: Frutto -> area Righe, Anno -> area Colonne, Importo -> area Dati
pivotTable.addFieldToArea(PivotFieldType.Row, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.Column, "Year")
pivotTable.addFieldToArea(PivotFieldType.Data, "Amount")

# Applica uno stile pivot predefinito moderno di Excel 2007+.
# PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
# viene ignorato da Excel per tali formati. PivotTableStyleDark1 appartiene alla famiglia
# dei temi scuri (PivotTableStyleDark1..PivotTableStyleDark28), e lo stesso enum espone anche
# i temi più recenti chiari/scuri di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PivotTableStyleDark1)

# Salva come .xlsx moderno — è il formato per cui PivotTableStyleType è significativo.
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Definire e applicare uno stile personalizzato per tabella pivot**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o font, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro è composto da tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Questo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WHOLE_TABLE` o `GRAND_TOTAL_ROW`) tramite `tableStyle.getTableStyleElements().add(TableStyleElementType)`, quindi assegnare un `Style` a ciascun elemento tramite `tableStyleElement.setElementStyle(Style)`.
3. Applicare lo stile personalizzato alla tabella pivot chiamando `pivotTable.setPivotTableStyleName(String)` con il nome dello stile. Non utilizzare qui `setPivotTableStyleType`, poiché tale metodo seleziona i preset predefiniti.

{{% alert color="primary" %}}

`setPivotTableStyleName` e `setPivotTableStyleType` non sono intercambiabili. Utilizzare `setPivotTableStyleType` per i preset predefiniti e `setPivotTableStyleName` per gli stili personalizzati definiti tramite `addPivotTableStyle`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente alla sorgente prevista.

{{% /alert %}}

I valori disponibili di `TableStyleElementType` includono `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` e `PAGE_FIELD_VALUES`.

L'esempio seguente definisce uno stile pivot personalizzato con un bordo nero sottile su `WHOLE_TABLE` e un font rosso in grassetto su `GRAND_TOTAL_ROW`, quindi lo applica tramite `setPivotTableStyleName` e salva come `.xlsx`.

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

# Popola i dati di origine: riga intestazione + 9 righe di dati (A1:C10)
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

# Aggiungi tabella pivot con origine A1:C10, ancorata in E3, denominata "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Passo 1: registra un nuovo stile di tabella pivot personalizzato e cattura il suo indice
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

# Passo 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per preset integrati)
pivotTable.setPivotTableStyleName("CustomPivotStyle")

workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Applicare un singolo stile a ogni cella della tabella pivot con FormatAll**

`pivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione precedente effettuata tramite `setPivotTableStyleType` o `setPivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`formatAll` sovrascrive sia `setPivotTableStyleType` sia `setPivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema in tutta la tabella pivot.

{{% /alert %}}

L'esempio seguente crea un `Style` con riempimento solido giallo, un font blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `formatAll` e salva come `.xlsx`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style
from asposecells.api import Color
from asposecells.api import PivotTable, PivotFieldType
from asposecells.api import BorderType, CellBorderType, BackgroundType

# Scenario 4: Applica un singolo Stile a ogni cella della tabella pivot utilizzando FormatAll
# API in uso: PivotTable.FormatAll(Style)
# Formato di destinazione: .xlsx
# Riferimento GitHub: vedere il repository Aspose.Cells-for-.NET — esempi di stile delle tabelle pivot

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Popola i dati di origine: riga di intestazione (riga 1) + 9 righe di dati (righe 2-10)
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

# Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1")
pivotTable = worksheet.getPivotTables().get(pivotIndex)

# Assegna i campi pivot: Frutta -> area Riga, Anno -> area Colonna, Importo -> area Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount")

# Costruisci uno Stile che verrà forzato su ogni cella della tabella pivot
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

# Salva la cartella di lavoro nel formato moderno .xlsx
workbook.save("output.xlsx")

jpype.shutdownJVM()
```

## **Quale API di stile devo utilizzare?**

La scelta dell'API di stile dipende dal formato di file in cui si sta salvando. Utilizzare la tabella seguente come riferimento rapido.

| Formato file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `pivotTable.setAutoFormatType(int)` | Valori da `com.aspose.cells.pivot.PivotTableAutoFormatType` (ad es. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignorato quando si salva in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `pivotTable.setPivotTableStyleType(int)` | Valori da `com.aspose.cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `pivotTable.setPivotTableStyleName(String)` + `tableStyles.addPivotTableStyle(String)` | Utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `tableStyleElement.setElementStyle(Style)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `pivotTable.formatAll(Style)` | Scorciatoia che sovrascrive ogni altra impostazione di stile in tutta la tabella pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `setPivotTableStyleType` per i temi predefiniti, oppure `setPivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="python" >}}