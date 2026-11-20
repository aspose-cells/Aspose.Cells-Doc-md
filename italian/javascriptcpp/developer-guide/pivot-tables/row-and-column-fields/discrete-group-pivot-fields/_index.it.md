---
title: Raggruppamento discreto degli elementi dei campi pivot
linktitle: Raggruppamento discreto
description: Scopri come raggruppare gli elementi dei campi pivot in gruppi personalizzati con un nome specifico, come frutta e verdura, utilizzando DiscreteGroupItem e PivotFieldGroupOptions.discreteGroupItems in Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells, tabella pivot, raggruppamento discreto, DiscreteGroupItem, PivotFieldGroupOptions, raggruppamento di elementi pivot, gruppi personalizzati, PivotField.group, Aspose.Cells for JavaScript via C++, tabella pivot di Excel
type: docs
weight: 90
url: /it/javascript-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possibili scenari di utilizzo**
- Il raggruppamento automatico raccoglie gli elementi in base al tipo di dati, ad esempio raggruppando le date per mese e trimestre e i numeri per intervalli. Il raggruppamento discreto risolve il problema opposto, raggruppando elementi specifici e non correlati in gruppi personalizzati con un nome specifico, ad esempio prodotti in categorie come frutta e verdura, negozi per regione o account per zona. Aspose.Cells fornisce il raggruppamento discreto mediante la classe `DiscreteGroupItem` e la proprietà `PivotFieldGroupOptions.discreteGroupItems`.
- Un `DiscreteGroupItem` è costituito da un nome di gruppo e dagli elementi che vi appartengono. Gli elementi possono essere identificati in due modi: in base ai loro nomi (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) o alle rispettive posizioni nei dati di origine, indicizzate da zero (`new DiscreteGroupItem("fruit", [0, 3])`). Entrambe le forme producono lo stesso risultato.
- Il raggruppamento discreto si applica a un campo nell'area delle righe o delle colonne della tabella pivot, passando le opzioni a `PivotField.group(PivotFieldGroupOptions)`.

## **Raggruppa gli elementi dei campi pivot in base ai nomi degli elementi**
L'esempio seguente costruisce un piccolo elenco di vendite (prodotto, data e importo), crea da esso una tabella pivot con `product` nell'area delle righe, `date` nell'area delle colonne e `amount` nell'area dei dati, quindi definisce due gruppi personalizzati in base ai nomi degli elementi: `fruit` (`grape`, `cherry`) e `vegetables` (`carrot`, `potato`). Il risultato mostra una struttura a due livelli nell'area delle righe, con il nome del gruppo come livello superiore e gli elementi originali annidati al di sotto, per consentire l'analisi dell'andamento per ciascun gruppo personalizzato e per ciascun elemento.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            const { Workbook, DiscreteGroupItem, PivotFieldGroupOptions } = AsposeCells;
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType =
                    AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // Group specific items into custom groups by item names
                const fruit = new DiscreteGroupItem("fruit", ["grape", "cherry"]);
                const vegetable = new DiscreteGroupItem("vegetable", ["carrot", "potato"]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotField.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Dopo `calculateData()`, l'area delle righe della tabella pivot mostra `fruit` (`grape` 50, `cherry` 80) e `vegetable` (`carrot` 60, `potato` 70), con il totale complessivo di 260, mentre le etichette delle colonne mantengono le quattro date (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024).

## **Raggruppa gli elementi dei campi pivot in base agli indici degli elementi**
Quando i nomi degli elementi sono lunghi o localizzati, il secondo costruttore di `DiscreteGroupItem` identifica gli elementi tramite l'indice. Gli indici indicano le posizioni degli elementi nei dati di origine, numerate da zero e secondo l'ordine di comparsa, non in ordine alfabetico. Nei dati di esempio precedenti, `grape` è l'elemento 0, `carrot` è l'elemento 1, `potato` è l'elemento 2 e `cherry` è l'elemento 3, pertanto `fruit` è `{ 0, 3 }` e `vegetable` è `{ 1, 2 }`. Il risultato è identico all'esempio basato sui nomi.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            const {
                Workbook,
                SaveFormat,
                DiscreteGroupItem,
                PivotFieldGroupOptions
            } = AsposeCells;
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').addEventListener('click', async () => {
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                cells.get(0, 0).value = "product";
                cells.get(1, 0).value = "grape";
                cells.get(2, 0).value = "carrot";
                cells.get(3, 0).value = "potato";
                cells.get(4, 0).value = "cherry";
                const dateStyle = workbook.createStyle();
                dateStyle.custom = "m/d/yyyy";
                cells.get(0, 1).value = "date";
                cells.get(1, 1).value = new Date(2021, 1, 5);
                cells.get(2, 1).value = new Date(2022, 2, 8);
                cells.get(3, 1).value = new Date(2023, 3, 10);
                cells.get(4, 1).value = new Date(2024, 4, 16);
                for (let r = 1; r <= 4; r++) {
                    cells.get(r, 1).style = dateStyle;
                }
                cells.get(0, 2).value = "amount";
                cells.get(1, 2).value = 50;
                cells.get(2, 2).value = 60;
                cells.get(3, 2).value = 70;
                cells.get(4, 2).value = 80;
                // Add a pivot table with the destination cell A12 (row 11, column 0)
                const pivotTable = sheet.pivotTables.add("=Sheet1!A1:C5", 11, 0);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
                pivotTable.pivotTableStyleType = AsposeCells.PivotTableStyleType.PivotTableStyleMedium10;
                // grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
                // (zero-based positions in the order the items appear in the source data)
                const fruit = new DiscreteGroupItem("fruit", [0, 3]);
                const vegetable = new DiscreteGroupItem("vegetable", [1, 2]);
                const groupOptions = new PivotFieldGroupOptions();
                groupOptions.discreteGroupItems = [fruit, vegetable];
                pivotTable.rowFields.get(0).group(groupOptions);
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "outputDiscreteGroupPivotFieldByIndex.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

## **Nota**

{{% alert color="primary" %}}
- Gli elementi non assegnati ad alcun gruppo personalizzato non vengono persi. Rimangono nella tabella pivot, allo stesso livello dei gruppi personalizzati, ciascuno come voce autonoma con un solo elemento. Nell'esempio precedente, definendo solo il gruppo `fruit`, `carrot` e `potato` rimangono nell'area delle righe come voci autonome accanto al gruppo `fruit`.
- La proprietà `PivotFieldGroupOptions.newPivotField` controlla la disposizione del raggruppamento discreto. Per impostazione predefinita è `true`; in questo modo, il campo raggruppato viene aggiunto come nuovo campo esterno accanto a quello originale, producendo la struttura a due livelli mostrata sopra (`rowFields` passa a contenere 2 elementi). Impostandola su `false`, il campo originale viene sostituito e l'area delle righe mostra un unico livello contenente solo i nomi dei gruppi con i rispettivi valori aggregati, `fruit` 130 (50 + 80) e `vegetable` 130 (60 + 70).
- I costruttori di `DiscreteGroupItem` basati sui nomi e sugli indici possono essere combinati all'interno dello stesso array `discreteGroupItems`.
{{% /alert %}}

## **Articoli correlati**
- [Raggruppa i campi pivot nella tabella pivot](/cells/it/javascript-cpp/group-pivot-fields-in-the-pivot-table/)
- [Aggiungi campi di riga e colonna alla tabella pivot](/cells/it/javascript-cpp/pivot-table-add-row-and-column-fields/)
- [Filtra le tabelle pivot in base all'etichetta o al valore](/cells/it/javascript-cpp/filter-by-label-or-value-of-pivot-table/)
- [Applica uno stile alla tabella pivot](/cells/it/javascript-cpp/apply-style-to-pivot-table/)
- [Aggiorna la tabella pivot](/cells/it/javascript-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}