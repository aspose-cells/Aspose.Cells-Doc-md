---
title: Raggruppamento discreto degli elementi del campo pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi di un campo pivot in gruppi personalizzati denominati, ad esempio frutta e verdura, utilizzando DiscreteGroupItem e pivot_field_group_options.discrete_group_items in Aspose.Cells for Python via .NET.
keywords: Aspose.Cells for Python via .NET, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.group, Python, tabella pivot di Excel
type: docs
weight: 90
url: /it/python-net/discrete-group-pivot-fields/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico raggruppa gli elementi in base al tipo di dati, ad esempio trasformando le date in mesi e trimestri o i numeri in intervalli. Il raggruppamento discreto risolve il problema opposto, consentendo di raggruppare elementi specifici e non correlati in gruppi personalizzati denominati, ad esempio associando prodotti a gruppi come frutta e verdura, punti vendita ad aree geografiche o conti a zone. Aspose.Cells offre il raggruppamento discreto tramite la classe `DiscreteGroupItem` e la proprietà `pivot_field_group_options.discrete_group_items`.
- Un `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che ne fanno parte. Gli elementi possono essere identificati in due modi: tramite i loro nomi (`DiscreteGroupItem("fruit", ["grape", "cherry"])`) oppure tramite le loro posizioni, indicizzate da zero, nei dati di origine (`DiscreteGroupItem("fruit", [0, 3])`). Entrambe le modalità producono lo stesso risultato.
- Il raggruppamento discreto viene applicato a un campo nell'area delle righe o delle colonne della tabella pivot passando le opzioni a `pivot_field.group(PivotFieldGroupOptions)`.

## **Raggruppa gli elementi del campo pivot in base ai nomi degli elementi**
L'esempio seguente costruisce un piccolo elenco di vendite (prodotto, data e importo), crea una tabella pivot con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: frutta (uva, ciliegia) e verdura (carota, patata). Il risultato mostra una struttura a due livelli nell'area delle righe, con il nome del gruppo come livello esterno e gli elementi originali annidati al di sotto, in modo da consentire la lettura degli andamenti per gruppo personalizzato e per elemento.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# Group specific items into custom groups using 0-based source-appearance indexes
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotField.xlsx")
```

Dopo `calculate_data()`, l'area delle righe della tabella pivot mostra frutta (uva 50, ciliegia 80) e verdura (carota 60, patata 70), con un totale generale di 260, mentre le etichette delle colonne riportano le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppa gli elementi del campo pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` identifica gli elementi tramite l'indice. Gli indici corrispondono alle posizioni, indicizzate da zero, degli elementi nell'ordine in cui compaiono nei dati di origine, non in ordine alfabetico. Nei dati di esempio riportati sopra, uva è l'elemento 0, carota è l'elemento 1, patata è l'elemento 2 e ciliegia è l'elemento 3; pertanto frutta è `{ 0, 3 }` e verdura è `{ 1, 2 }`. Il risultato è identico a quello dell'esempio basato sui nomi.

```python
import aspose.cells as ac
from aspose.cells.pivot import DiscreteGroupItem, PivotFieldGroupOptions, PivotFieldType, PivotTableStyleType
from datetime import datetime
wb = ac.Workbook()
sheet = wb.worksheets[0]
cells = sheet.cells
cells.get(0, 0).value = "product"
cells.get(1, 0).value = "grape"
cells.get(2, 0).value = "carrot"
cells.get(3, 0).value = "potato"
cells.get(4, 0).value = "cherry"
date_style = wb.create_style()
date_style.custom = "m/d/yyyy"
cells.get(0, 1).value = "date"
cells.get(1, 1).value = datetime(2021, 2, 5)
cells.get(2, 1).value = datetime(2022, 3, 8)
cells.get(3, 1).value = datetime(2023, 4, 10)
cells.get(4, 1).value = datetime(2024, 5, 16)
for r in range(1, 5):
    cells.get(r, 1).set_style(date_style)
cells.get(0, 2).value = "amount"
cells.get(1, 2).value = 50
cells.get(2, 2).value = 60
cells.get(3, 2).value = 70
cells.get(4, 2).value = 80
# Add a pivot table with the destination cell A12 (row 11, column 0)
pivot_table = sheet.pivot_tables.add("=Sheet1!A1:C5", 11, 0)
pivot_table.add_field_to_area(PivotFieldType.ROW, "product")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "date")
pivot_table.add_field_to_area(PivotFieldType.DATA, "amount")
pivot_table.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM10
# grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
# (zero-based positions in the order the items appear in the source data)
fruit = DiscreteGroupItem("fruit", [0, 3])
vegetable = DiscreteGroupItem("vegetable", [1, 2])
group_options = PivotFieldGroupOptions()
group_options.discrete_group_items = [fruit, vegetable]
pivot_table.row_fields[0].group(group_options)
pivot_table.calculate_data()
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx")
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati a alcun gruppo personalizzato non vengono persi: rimangono nella tabella pivot allo stesso livello dei gruppi personalizzati, ciascuno come voce autonoma contenente un solo elemento. Nell'esempio precedente, se si definisce solo il gruppo della frutta, carota e patata rimangono nell'area delle righe come voci autonome accanto al gruppo della frutta.
- La proprietà `pivot_field_group_options.new_pivot_field` controlla la struttura del raggruppamento discreto. Il valore predefinito è `True`: in questo caso, il campo raggruppato viene aggiunto come nuovo campo esterno accanto al campo originale, creando la disposizione a due livelli mostrata sopra (`row_fields` passa a 2). Se il valore è impostato su `False`, il campo originale viene sostituito. L'area delle righe mostra quindi un unico livello contenente solo i nomi dei gruppi e i relativi valori aggregati: frutta 130 (50 + 80) e verdura 130 (60 + 70).
- È possibile utilizzare contemporaneamente i costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici all'interno dello stesso elenco `discrete_group_items`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/python-net/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi di riga e di colonna alla tabella pivot](/cells/it/python-net/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot per etichetta o valore](/cells/it/python-net/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/python-net/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}