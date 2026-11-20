---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati con nome, come frutta e verdura, utilizzando DiscreteGroupItem e PivotFieldGroupOptions.getDiscreteGroupItems in Aspose.Cells for Python via Java.
keywords: Aspose.Cells, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento degli elementi pivot, gruppi personalizzati, PivotField.group, Python via Java, tabella pivot di Excel
type: docs
weight: 90
url: /it/python-java/discrete-group-pivot-fields/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico raccoglie gli elementi in base al tipo di dati, ad esempio raggruppando le date in mesi e trimestri o i numeri in intervalli. Il raggruppamento discreto risolve il problema opposto, raggruppando elementi specifici e non correlati in gruppi personalizzati con nome, ad esempio i prodotti in gruppi come frutta e verdura, i negozi in regioni o i conti in zone. Aspose.Cells for Python via Java consente il raggruppamento discreto tramite la classe `DiscreteGroupItem` e il metodo `PivotFieldGroupOptions.getDiscreteGroupItems()`.
- Un `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che vi appartengono. Gli elementi possono essere identificati in due modi: tramite i rispettivi nomi (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) oppure tramite le rispettive posizioni, indicizzate da zero, nei dati di origine (`DiscreteGroupItem("fruit", [0, 3])`). Entrambe le forme producono lo stesso risultato.
- Il raggruppamento discreto viene applicato a un campo nell'area delle righe o delle colonne della tabella pivot passando le opzioni a `PivotField.group(PivotFieldGroupOptions)`.

## **Raggruppa gli elementi dei campi pivot in base ai nomi**
L'esempio seguente crea un piccolo elenco di vendite (prodotto, data e importo), genera una tabella pivot con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: frutta (uva, ciliegia) e verdura (carota, patata). Il risultato mostra una disposizione a due livelli, con il nome del gruppo come livello esterno e gli elementi originali annidati al di sotto, in modo da consentire l'analisi dell'andamento per gruppo personalizzato e per elemento.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    Worksheet,
    Cells,
    Range,
    SaveFormat,
    DiscreteGroupItem,
    PivotFieldGroupOptions,
    PivotFieldType,
    PivotTableStyleType,
)
GregorianCalendar = jpype.JPackage("java.util").GregorianCalendar
def create_date(year, month, day):
    calendar = GregorianCalendar(year, month - 1, day)
    return calendar.getTime()
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(create_date(2021, 2, 5))
cells.get(2, 1).putValue(create_date(2022, 3, 8))
cells.get(3, 1).putValue(create_date(2023, 4, 10))
cells.get(4, 1).putValue(create_date(2024, 5, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
# Group specific items into custom groups by item names
fruit = DiscreteGroupItem("fruit", ["grape", "cherry"])
vegetable = DiscreteGroupItem("vegetable", ["carrot", "potato"])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.calculateData()
pivot_table.getRowFields().get(0).group(group_options)
wb.save("outputDiscreteGroupPivotField.xlsx")
jpype.shutdownJVM()
```

Dopo `calculateData()`, l'area delle righe della tabella pivot mostra frutta (uva 50, ciliegia 80) e verdura (carota 60, patata 70), con un totale complessivo di 260, mentre le etichette delle colonne mantengono le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppa gli elementi dei campi pivot in base agli indici**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` identifica gli elementi tramite l'indice. Gli indici corrispondono alle posizioni, indicizzate da zero, degli elementi nell'ordine in cui compaiono nei dati di origine, non in ordine alfabetico. Nei dati di esempio riportati sopra, uva è l'elemento 0, carota l'elemento 1, patata l'elemento 2 e ciliegia l'elemento 3; pertanto, frutta è `{ 0, 3 }` e verdura è `{ 1, 2 }`. Il risultato è identico a quello dell'esempio basato sui nomi.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import (
    Workbook,
    PivotFieldType,
    PivotTableStyleType,
)
Date = jpype.JClass("java.util.Date")
DiscreteGroupItem = jpype.JClass("com.aspose.cells.DiscreteGroupItem")
PivotFieldGroupOptions = jpype.JClass("com.aspose.cells.PivotFieldGroupOptions")
wb = Workbook()
sheet = wb.getWorksheets().get(0)
cells = sheet.getCells()
cells.get(0, 0).putValue("product")
cells.get(1, 0).putValue("grape")
cells.get(2, 0).putValue("carrot")
cells.get(3, 0).putValue("potato")
cells.get(4, 0).putValue("cherry")
date_style = wb.createStyle()
date_style.setCustom("m/d/yyyy")
cells.get(0, 1).putValue("date")
cells.get(1, 1).putValue(Date(2021 - 1900, 2 - 1, 5))
cells.get(2, 1).putValue(Date(2022 - 1900, 3 - 1, 8))
cells.get(3, 1).putValue(Date(2023 - 1900, 4 - 1, 10))
cells.get(4, 1).putValue(Date(2024 - 1900, 5 - 1, 16))
for r in range(1, 5):
    cells.get(r, 1).setStyle(date_style)
cells.get(0, 2).putValue("amount")
cells.get(1, 2).putValue(50.0)
cells.get(2, 2).putValue(60.0)
cells.get(3, 2).putValue(70.0)
cells.get(4, 2).putValue(80.0)
pivot_table = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0)
pivot_table.addFieldToArea(PivotFieldType.ROW, "product")
pivot_table.addFieldToArea(PivotFieldType.COLUMN, "date")
pivot_table.addFieldToArea(PivotFieldType.DATA, "amount")
pivot_table.setPivotTableStyleType(
    PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
)
pivot_table.calculateData()
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.setDiscreteGroupItems([fruit, vegetable])
pivot_table.getRowFields().get(0).group(group_options)
pivot_table.calculateData()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
jpype.shutdownJVM()
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a alcun gruppo personalizzato non vengono persi. Rimangono nella tabella pivot allo stesso livello dei gruppi personalizzati, ciascuno come voce separata composta da un solo elemento. Nell'esempio basato sui nomi, definendo solo il gruppo frutta, carota e patata rimangono nell'area delle righe come voci autonome accanto al gruppo frutta.
- I metodi `PivotFieldGroupOptions.getNewPivotField()` e `setNewPivotField()` controllano la disposizione del raggruppamento discreto. Per impostazione predefinita, `getNewPivotField()` restituisce true, il che aggiunge il campo raggruppato come nuovo campo più esterno accanto a quello originale e produce la disposizione a due livelli mostrata sopra (`getRowFields()` aumenta a 2). Usare `setNewPivotField(false)` per sostituire invece il campo originale; l'area delle righe mostra quindi un unico livello contenente solo i nomi dei gruppi con i relativi valori aggregati: frutta 130 (50 + 80) e verdura 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere misti all'interno della stessa raccolta `getDiscreteGroupItems()`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/python-java/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi di riga e colonna alla tabella pivot](/cells/it/python-java/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/python-java/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}