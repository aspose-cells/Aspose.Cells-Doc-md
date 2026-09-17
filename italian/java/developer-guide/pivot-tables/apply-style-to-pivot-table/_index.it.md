---
title: Applica stili alle tabelle pivot in Aspose.Cells for Java
linktitle: Applica stili alle tabelle pivot
description: Impara come applicare stili predefiniti e personalizzati alle tabelle pivot in Aspose.Cells for Java, coprendo gli autoformati legacy XLS, gli stili denominati moderni di Excel 2007+, gli stili personalizzati delle tabelle pivot e la scorciatoia FormatAll.
keywords: Aspose.Cells Java stile tabella pivot, PivotTableStyleType, AutoFormatType, FormatAll, stile personalizzato, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /it/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells supporta l'applicazione sia degli autoformati legacy delle tabelle pivot (destinati ai file `.xls`) sia degli stili denominati o personalizzati moderni delle tabelle pivot (destinati ai file `.xlsx`, `.xlsm` e `.xlsb`). L'API da chiamare dipende dal formato di file in cui la cartella di lavoro viene salvata, non dal formato da cui è stata caricata.
{{% /alert %}}

## **Introduzione**
Aspose.Cells espone due API di stile parallele per le tabelle pivot. La scelta tra esse è determinata dal formato di file in cui si salva la cartella di lavoro, non dal formato da cui viene letta. Una cartella di lavoro caricata da un file `.xls` può essere salvata nuovamente come `.xlsx` e, in tal caso, si applica l'API di stile moderna anziché quella legacy.
- `PivotTable.PivotTableStyleType` seleziona uno degli stili denominati predefiniti (temi chiari e scuri, compresi gli stili aggiunti in Excel 2017). Questi preset sono di sola lettura.
- `PivotTable.PivotTableStyleName` seleziona uno stile personalizzato che definisci tramite `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)`. Gli stili personalizzati sono necessari ogni volta che si desidera modificare colori, bordi o caratteri oltre ciò che offrono i preset.
Inoltre, `PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, sovrascrivendo qualsiasi impostazione effettuata tramite una delle API di nome stile sopra indicate. Ciò è utile quando è richiesto un aspetto uniforme indipendentemente dal tema sottostante.

## **Applica un autoformato preset XLS legacy**
`PivotTable.AutoFormatType` accetta un valore dall'enumerazione `com.aspose.cells.PivotTableAutoFormatType`. I valori disponibili sono `REPORT_1` fino a `REPORT_10`, `CLASSIC` e `TABLE_1` fino a `TABLE_10`.
L'esempio seguente carica una nuova cartella di lavoro, popola i dati di esempio Fruit/Year/Amount, aggiunge una tabella pivot, applica `PivotTableAutoFormatType.REPORT_5` e salva il risultato come `.xls`.

{{% alert color="primary" %}}
**Perché nessun campo colonna?** Gli autoformati della serie Report (`Report1` fino a `Report10`, `Table1` fino a `Table10`) sono stati progettati in Excel classico per **tabelle pivot monodimensionali** con solo campi riga e valori — non hanno una formattazione predefinita per le intestazioni dei campi colonna. Se la tua tabella pivot necessita di campi colonna, utilizza invece i preset moderni di `PivotTableStyleType` dallo [Scenario 2](#apply-a-modern-named-preset-pivot-table-style), che sono progettati per il layout bidimensionale utilizzato da Excel moderno.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Scenario 1: Applica un formato automatico preimpostato XLS legacy
// API in uso: PivotTable.AutoFormatType
// Formato file di destinazione: .xls (legacy)
// Per esempi completi e file di dati, visitare https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Crea una nuova cartella di lavoro
Workbook workbook = new Workbook();
// Ottieni il primo foglio di lavoro
Worksheet sheet = workbook.getWorksheets().get(0);
// Popola i dati sorgente con la riga di intestazione (Fruit, Year, Amount)
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
// Aggiungi una tabella pivot nella cella di destinazione E3, denominata "Pivot1", utilizzando l'intervallo sorgente A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Assegna i campi: Fruit -> Righe, Amount -> Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Applica il formato automatico preimpostato XLS legacy "Report5"
// Nota: Questa proprietà è significativa solo durante il salvataggio come .xls.
// Quando viene salvato come .xlsx/.xlsm/.xlsb, Excel ignora AutoFormatType
// e utilizza qualsiasi cosa specifichi PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Salva la cartella di lavoro nel formato .xls legacy
workbook.save("output.xls");
```

## **Applica uno stile preset denominato moderno di tabella pivot**

## **Definisci e applica uno stile personalizzato di tabella pivot**
I preset predefiniti non possono essere modificati. Ogni volta che è necessario sovrascrivere colori, bordi o caratteri, è necessario definire uno stile pivot personalizzato. Il flusso di lavoro prevede tre passaggi:
1. Aggiungi uno stile personalizzato alla raccolta `TableStyles` della cartella di lavoro tramite `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)`. Questo restituisce l'indice dello stile appena creato.
2. Configura lo stile aggiungendo elementi (come `WholeTable` o `GrandTotalRow`) tramite `TableStyle.getTableStyleElements().add(TableStyleElementType)`, quindi assegna uno `Style` a ciascun elemento tramite `TableStyleElement.setElementStyle(Style)`.
3. Applica lo stile personalizzato alla tabella pivot impostando `PivotTable.PivotTableStyleName` sul nome dello stile. Non utilizzare `PivotTableStyleType` qui, poiché tale proprietà seleziona i preset predefiniti.

{{% alert color="primary" %}}
`PivotTableStyleName` e `PivotTableStyleType` non sono intercambiabili. Usa `PivotTableStyleType` per i preset predefiniti e `PivotTableStyleName` per gli stili personalizzati che hai definito tramite `addPivotTableStyle`. Impostare entrambi è innocuo, ma viene reso solo quello corrispondente alla fonte prevista.
{{% /alert %}}

I valori disponibili di `TableStyleElementType` includono `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` e `PAGE_FIELD_VALUES`.
L'esempio seguente definisce uno stile pivot personalizzato con un bordo sottile nero su `WholeTable` e un carattere rosso in grassetto su `GrandTotalRow`, quindi lo applica tramite `PivotTableStyleName` e lo salva come `.xlsx`.

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
// Aggiungi tabella pivot con origine da A1:C10, ancorata a E3, denominata "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Passo 1: registra un nuovo stile personalizzato di tabella pivot e memorizza il suo indice
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Passo 2: aggiungi un elemento WholeTable e applica bordi neri sottili su tutti e quattro i lati
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
// Passo 3: aggiungi un elemento GrandTotalRow e applica un font rosso in grassetto
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Passo 4: applica lo stile personalizzato per nome (NON tramite PivotTableStyleType, che è per stili predefiniti integrati)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Applica uno stile a ogni cella della tabella pivot con FormatAll**
`PivotTable.formatAll(Style)` è una scorciatoia che applica un singolo oggetto `Style` a ogni cella della tabella pivot, inclusi l'area dati, le intestazioni di riga e colonna e i totali. Qualsiasi impostazione effettuata in precedenza tramite `PivotTableStyleType` o `PivotTableStyleName` viene sovrascritta.

{{% alert color="primary" %}}
`FormatAll` sovrascrive sia `PivotTableStyleType` che `PivotTableStyleName`. Usalo solo quando è necessario un aspetto uniforme e indipendente dal tema nell'intera tabella pivot.
{{% /alert %}}

L'esempio seguente crea uno `Style` con riempimento giallo a tinta unita, un carattere blu scuro in grassetto e bordi neri sottili su tutti i lati, quindi lo applica con `formatAll` e lo salva come `.xlsx`.

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
// Crea uno Style che verrà applicato forzatamente a ogni cella della tabella pivot
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
// Applica FormatAll: applica forzatamente questo singolo stile a ogni cella della tabella pivot,
// sovrascrivendo qualsiasi PivotTableStyleType / PivotTableStyleName precedentemente impostato
pivotTable.formatAll(style);
// Salva la cartella di lavoro nel formato .xlsx moderno
workbook.save("output.xlsx");
```

## **Quale API di stile dovrei usare?**
La scelta dell'API di stile dipende dal formato di file in cui stai salvando. Usa la tabella seguente come riferimento rapido.
| Formato del file di destinazione | API da utilizzare | Note |
|---|---|---|
| `.xls` (legacy) | `PivotTable.AutoFormatType` | Valori da `com.aspose.cells.PivotTableAutoFormatType` (ad es. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Ignorato quando si salva nei formati moderni. |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile predefinito) | `PivotTable.PivotTableStyleType` | Valori da `com.aspose.cells.PivotTableStyleType` (temi chiari/scuri, comprese le aggiunte di Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (moderno, stile personalizzato) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Da utilizzare quando i preset predefiniti non sono sufficienti. Configura tramite `TableStyleElement.setElementStyle(...)`. |
| Qualsiasi formato (override uniforme) | `PivotTable.formatAll(Style)` | Scorciatoia che sovrascrive qualsiasi altra impostazione di stile nell'intera tabella pivot. |
In caso di dubbio, salva come `.xlsx` e usa `PivotTableStyleType` per i temi predefiniti, oppure `PivotTableStyleName` per i temi personalizzati.

{{< app/cells/assistant language="java" >}}