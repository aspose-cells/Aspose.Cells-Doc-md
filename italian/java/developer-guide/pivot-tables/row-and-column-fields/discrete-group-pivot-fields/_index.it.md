---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati con nomi specifici, come frutta e verdura, utilizzando DiscreteGroupItem e PivotFieldGroupOptions.DiscreteGroupItems in Aspose.Cells for Java.
keywords: Aspose.Cells for Java, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.group, Java, tabella pivot di Excel
type: docs
weight: 90
url: /it/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico raggruppa gli elementi in base al tipo di dati, ad esempio le date per mese e trimestre o i numeri per intervallo. Il raggruppamento discreto risolve il problema opposto, riunendo elementi specifici e non correlati in gruppi personalizzati con nomi specifici, ad esempio raggruppando i prodotti in categorie come frutta e verdura, i negozi per regione o i conti per zona. Aspose.Cells fornisce il raggruppamento discreto tramite la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che vi appartengono. Gli elementi possono essere identificati in due modi: tramite i loro nomi (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) oppure tramite le rispettive posizioni, a partire da zero, nei dati di origine (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Entrambe le forme producono lo stesso risultato.
- Per applicare il raggruppamento discreto a un campo nell'area delle righe o delle colonne della tabella pivot, passare le opzioni a `PivotField.group(PivotFieldGroupOptions)`.

## **Raggruppamento degli elementi di un campo pivot in base ai nomi degli elementi**
L'esempio seguente costruisce un piccolo elenco di vendite (prodotto, data e importo), crea una tabella pivot da tale elenco con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: `fruit` (`grape`, `cherry`) e `vegetables` (`carrot`, `potato`). Il risultato mostra una disposizione delle righe a due livelli, con il nome del gruppo nel livello esterno e gli elementi originali annidati al di sotto. Ciò consente di analizzare le tendenze per ciascun gruppo personalizzato e per ciascun elemento.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

Dopo `calculateData()`, l'area delle righe della tabella pivot mostra `fruit` (`grape` 50, `cherry` 80) e `vegetable` (`carrot` 60, `potato` 70), con un totale complessivo di 260, mentre le etichette delle colonne mantengono le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppamento degli elementi di un campo pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` li identifica tramite il rispettivo indice. Gli indici corrispondono alle posizioni, a partire da zero, degli elementi nell'ordine in cui compaiono nei dati di origine, non in ordine alfabetico. Nei dati di esempio riportati sopra, `grape` è l'elemento 0, `carrot` è l'elemento 1, `potato` è l'elemento 2 e `cherry` è l'elemento 3; pertanto, `fruit` è `{ 0, 3 }` e `vegetable` è `{ 1, 2 }`. Il risultato è identico a quello dell'esempio basato sui nomi.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a un gruppo personalizzato non vengono persi. Rimangono nella tabella pivot allo stesso livello dei gruppi personalizzati, ciascuno come voce autonoma contenente un solo elemento. Nell'esempio precedente, la definizione del solo gruppo `fruit` lascia `carrot` e `potato` nell'area delle righe come voci autonome accanto al gruppo `fruit`.
- La proprietà `PivotFieldGroupOptions.getNewPivotField()` controlla la disposizione del raggruppamento discreto. Per impostazione predefinita restituisce `true`, valore che aggiunge il campo raggruppato come nuovo campo esterno accanto al campo originale, producendo la disposizione a due livelli mostrata sopra (il numero di campi restituito da `getRowFields()` aumenta a 2). Impostarla su `false` mediante `setNewPivotField(false)` sostituisce il campo originale. L'area delle righe mostra quindi un unico livello contenente solo i nomi dei gruppi e i relativi valori aggregati: `fruit` 130 (50 + 80) e `vegetable` 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere abbinati all'interno dello stesso array `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/java/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi riga e colonna alla tabella pivot](/cells/it/java/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot per etichetta o valore](/cells/it/java/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/java/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}