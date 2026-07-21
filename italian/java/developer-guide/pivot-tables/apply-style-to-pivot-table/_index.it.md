---
title: Applicazione di stili alle tabelle pivot
linktitle: Applicazione di stili alle tabelle pivot
description: Scopri come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Java, incluse le formattazioni automatiche legacy XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati per tabelle pivot e il collegamento FormatAll.
keywords: Aspose.Cells Java stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells supporta l'applicazione sia delle formattazioni automatiche legacy per pivot (pensate per i file `.xls`) sia degli stili moderni denominati o personalizzati per tabelle pivot (pensati per i file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.

{{% /alert %}}

## **Introduzione**

Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui viene letta. Una cartella di lavoro caricata da un file `.xls` può essere risalvata come `.xlsx` e, in tal caso, si applica l'API di stile moderna anziché quella legacy.

Per l'output `.xls` legacy, utilizzare la proprietà `PivotTable.AutoFormatType` insieme all'enumerazione `com.aspose.cells.PivotTableAutoFormatType`. Questa API corrisponde al selettore di formattazione automatica che la versione classica di Excel offriva per le tabelle pivot.

Per l'output moderno `.xlsx`, `.xlsm` e `.xlsb`, sono disponibili due varianti di API di stile:

- `PivotTable.PivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, inclusi gli stili aggiunti in Excel 2017). Questi preset sono in sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato definito dall'utente tramite `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o font oltre quanto offerto dai preset.

Inoltre, `PivotTable.formatAll(Style)` è un collegamento che applica un singolo oggetto `Style` a ogni cella della pivot, sovrascrivendo qualsiasi impostazione effettuata tramite una delle due API basate sul nome dello stile sopra descritte. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applicazione di una formattazione automatica preset legacy XLS**

`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `com.aspose.cells.PivotTableAutoFormatType`. I valori disponibili sono `REPORT_1` fino a `REPORT_10`, `CLASSIC` e `TABLE_1` fino a `TABLE_10`.

{{% alert color="primary" %}}

`AutoFormatType` viene rispettato solo quando la cartella di lavoro viene salvata come `.xls`. Quando la stessa cartella di lavoro viene salvata come `.xlsx`, `.xlsm` o `.xlsb`, Excel ignora questa proprietà e ricade sulle impostazioni `PivotTableStyleType` e `PivotTableStyleName`.

{{% /alert %}}

L'esempio seguente carica una cartella di lavoro nuova, popola i dati di esempio Frutto/Anno/Importo, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.REPORT_5` e salva il risultato come `.xls`.

```java
import com.aspose.cells.*;

// Scenario 1: Applica un formato automatico preimpostato XLS legacy
// API in uso: PivotTable.AutoFormatType
// Formato del file di destinazione: .xls (legacy)
// Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-Java

// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();

// Ottieni il primo foglio di lavoro
Worksheet sheet = workbook.getWorksheets().get(0);

// Popola i dati di origine con la riga di intestazione (Fruit, Year, Amount)
// e 9 righe di dati che coprono grape, blueberry, kiwi, cherry negli anni 2020 e 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");

sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);

sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);

sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);

sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);

sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);

sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);

sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);

sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);

sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);

// Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", usando l'intervallo di origine A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);

// Assegna i campi: Fruit -> Righe, Year -> Colonne, Amount -> Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Applica il formato automatico preimpostato XLS legacy "Report5"
// Nota: questa proprietà è significativa solo quando si salva come .xls.
// Quando si salva come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// e utilizza qualsiasi PivotTableStyleType / PivotTableStyleName specificato.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);

// Salva la cartella di lavoro nel formato legacy .xls
workbook.save("output.xls");
```

## **Applicazione di uno stile preset denominato moderno per tabelle pivot**

`PivotTable.PivotTableStyleType` accetta un valore dall'enumerazione `com.aspose.cells.PivotTableStyleType`. L'enumerazione copre i temi chiari `PIVOT_TABLE_STYLE_LIGHT_1` fino a `PIVOT_TABLE_STYLE_LIGHT_28` e i temi scuri `PIVOT_TABLE_STYLE_DARK_1` fino a `PIVOT_TABLE_STYLE_DARK_28`. Gli stili aggiunti in Excel 2017 (la seconda ondata di temi chiari e scuri) sono raggiungibili attraverso la stessa enumerazione.

Questa è l'API consigliata per qualsiasi formato di file moderno. A differenza della formattazione automatica legacy, lo stile qui selezionato viene reso fedelmente da Excel e sopravvive ai cicli di andata e ritorno attraverso altri strumenti Office.

L'esempio seguente utilizza gli stessi dati Frutto/Anno/Importo, crea una tabella pivot identica, applica `PIVOT_TABLE_STYLE_DARK_1` e salva la cartella di lavoro come `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Riga di intestazione: Frutto / Anno / Importo
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 righe di dati di Frutto / Anno / Importo
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// Aggiungi una tabella pivot in E3 con nome "Pivot1", con origine da A1:C10
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Frutto -> area Riga, Anno -> area Colonna, Importo -> area Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Applica uno stile pivot preimpostato denominato moderno di Excel 2007+.
// PivotTableStyleType è l'API corretta per i file .xlsx / .xlsm / .xlsb; AutoFormatType
// viene ignorato da Excel per quei formati. PivotTableStyleDark1 appartiene alla famiglia del tema scuro
// (PivotTableStyleDark1..PivotTableStyleDark28), e lo stesso enum espone anche i
// temi chiari/scuri più recenti di Excel 2017 (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Salva come .xlsx moderno - questo è il formato per il quale PivotTableStyleType è significativo.
workbook.save("output.xlsx");
```

## **Definire e applicare uno stile personalizzato per tabelle pivot**

I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o font, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro prevede tre passaggi:

1. Aggiungere uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Questo restituisce l'indice dello stile appena creato.
2. Configurare lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.getTableStyleElements().add(TableStyleElementType)`, quindi assegnare uno `Style` a ciascun elemento tramite `TableStyleElement.setElementStyle(Style)`.
3. Applicare lo stile personalizzato alla pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare qui `PivotTableStyleType`, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}

`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Utilizzare `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati definiti tramite `addPivotTableStyle`. Impostarli entrambi è innocuo, ma solo quello corrispondente alla fonte prevista viene reso.

{{% /alert %}}

I valori di `TableStyleElementType` disponibili includono `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` e `PAGE_FIELD_VALUES`.

L'esempio seguente definisce uno stile pivot personalizzato con un bordo sottile nero su `WholeTable` e un font rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e salva come `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Popola i dati di origine: riga di intestazione + 9 righe di dati (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

// Aggiungi una tabella pivot con origine da A1:C10, ancorata in E3, denominata "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Passaggio 1: registra un nuovo stile personalizzato di tabella pivot e acquisisci il suo indice
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Passaggio 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);

// Passaggio 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);

// Passaggio 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per preset predefiniti)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Applicazione di un unico stile a ogni cella della pivot con FormatAll**

`PivotTable.formatAll(Style)` è un collegamento che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione precedente effettuata tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}

`FormatAll` sovrascrive sia `PivotTableStyleType` che `PivotTableStyleName`. Utilizzarlo solo quando è richiesto un aspetto uniforme e indipendente dal tema nell'intera tabella pivot.

{{% /alert %}}

L'esempio seguente crea uno `Style` con un riempimento giallo uniforme, un font blu scuro in grassetto e bordi sottili neri su tutti i lati, quindi lo applica con `formatAll` e salva come `.xlsx`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);

// Popola i dati di origine: riga di intestazione (riga 1) + 9 righe di dati (righe 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);

// Aggiungi tabella pivot: intervallo di origine A1:C10, cella di destinazione E3, nome "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Assegna i campi pivot: Fruit -> area Riga, Year -> area Colonna, Amount -> area Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

// Crea uno Style che verrà applicato forzatamente su ogni cella della tabella pivot
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());

style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());

style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());

// Applica FormatAll: forza questo singolo stile su ogni cella della tabella pivot,
// sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName impostato in precedenza
pivotTable.formatAll(style);

// Salva la cartella di lavoro nel formato moderno .xlsx
workbook.save("output.xlsx");
```

## **Quale API di stile devo usare?**

La scelta dell'API di stile dipende dal formato di file in cui si sta salvando. Utilizzare la tabella seguente come riferimento rapido.

| Formato del file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `com.aspose.cells.PivotTableAutoFormatType` (ad es. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignorato durante il salvataggio in formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `com.aspose.cells.PivotTableStyleType` (temi chiari/scuri, incluse le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Da utilizzare quando i preset predefiniti non sono sufficienti. Configurare tramite `TableStyleElement.setElementStyle(...)`. |
| Qualsiasi formato (sovrascrittura uniforme) | `PivotTable.formatAll(Style)` | Collegamento che sovrascrive ogni altra impostazione di stile nell'intera tabella pivot. |

In caso di dubbio, salvare come `.xlsx` e utilizzare `PivotTableStyleType` per i temi predefiniti, oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="java" >}}