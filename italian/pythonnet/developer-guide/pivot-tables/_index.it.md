---
title: Inserisci una tabella pivot
linktitle: Inserisci una tabella pivot
description: Crea e formatta tabelle pivot con Aspose.Cells for Python via .NET.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot.
type: docs
weight: 160
url: /it/python-net/create-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un rapporto riepilogativo interattivo: consente di condensare un ampio blocco di dati grezzi, disposti riga per riga, in una matrice compatta senza ricorrere a una sola formula. Si decide quali colonne diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregate come valori: la tabella pivot esegue sia il raggruppamento sia i calcoli:
- **Sintetizzare** — vendite totali per prodotto, per regione o per trimestre, anziché lunghe catene di formule.
- **Confrontare** — categorie nelle righe e periodi nelle colonne trasformano un elenco piatto in un rapporto incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Analizzare in dettaglio** — fare doppio clic su un valore riepilogativo per esaminare le righe di origine.
- **Aggiornare** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero rapporto.
Tra gli scenari tipici vi sono i cruscotti di vendita, l'analisi delle spese e l'analisi dell'inventario, per rispondere a domande del tipo «come si suddividono questi numeri per categoria e per periodo?». Aspose.Cells for Python via .NET consente di creare a livello di codice le stesse tabelle pivot, in modo che le cartelle di lavoro generate dall'applicazione possano contenere rapporti pronti all'uso anziché soltanto i dati grezzi.

### **Modello a oggetti della tabella pivot**
Aspose.Cells for Python via .NET fornisce un insieme dedicato di classi nel namespace [**aspose.cells.pivot**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/), utilizzate per creare e controllare le tabelle pivot. Tali classi consentono di creare e impostare gli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/), i componenti fondamentali di una tabella pivot. Gli oggetti sono:
- [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) rappresenta un campo in un oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable/).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfieldcollection) rappresenta una raccolta di tutti gli oggetti [**PivotField**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivotfield/) in un oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) rappresenta un oggetto PivotTable in un foglio di lavoro.
- [**PivotTableCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection) rappresenta una raccolta di tutti gli oggetti [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable) in un foglio di lavoro.

### **Creazione di una tabella pivot semplice con Aspose.Cells**
La creazione di una tabella pivot richiede tre passaggi, seguiti dal salvataggio: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e collocare i campi nelle aree delle righe, delle colonne e dei dati.
1. Aggiungere i dati a un foglio di lavoro utilizzando il metodo [**put_value**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/put_value/#str) dell'oggetto [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Questi dati costituiranno l'origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection/add/#str-str-str) della raccolta [**PivotTables**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottablecollection): `add(source_data, row, column)`. `source_data` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono, rispettivamente, gli indici di riga e di colonna della cella di destinazione, situata nell'angolo superiore sinistro della tabella pivot; gli indici sono base zero (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable).
3. Collocare i campi con il metodo `add_field_to_area` dell'oggetto [**PivotTable**](https://reference.aspose.com/cells/python-net/aspose.cells.pivot/pivottable): il nome di un campo viene inserito nell'area delle righe (`PivotFieldType.ROW`), nell'area delle colonne (`PivotFieldType.COLUMN`) o nell'area dei dati (`PivotFieldType.DATA`).
4. Salvare la cartella di lavoro: la tabella pivot viene scritta nel file salvato.
Dopo l'esecuzione del codice di esempio, la tabella pivot viene aggiunta al foglio di lavoro.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType

# Crea una nuova cartella di lavoro e ottieni il primo foglio di lavoro
workbook = ac.Workbook()
sheet = workbook.worksheets[0]

# Scrivi i dati di origine: vendite per sport e trimestre
sheet.cells.get("A1").put_value("Sport")
sheet.cells.get("B1").put_value("Quarter")
sheet.cells.get("C1").put_value("Sales")
sheet.cells.get("A2").put_value("Golf")
sheet.cells.get("B2").put_value("Qtr3")
sheet.cells.get("C2").put_value(1500)
sheet.cells.get("A3").put_value("Golf")
sheet.cells.get("B3").put_value("Qtr4")
sheet.cells.get("C3").put_value(2000)
sheet.cells.get("A4").put_value("Tennis")
sheet.cells.get("B4").put_value("Qtr3")
sheet.cells.get("C4").put_value(600)
sheet.cells.get("A5").put_value("Tennis")
sheet.cells.get("B5").put_value("Qtr4")
sheet.cells.get("C5").put_value(1500)
sheet.cells.get("A6").put_value("Tennis")
sheet.cells.get("B6").put_value("Qtr3")
sheet.cells.get("C6").put_value(4070)
sheet.cells.get("A7").put_value("Tennis")
sheet.cells.get("B7").put_value("Qtr4")
sheet.cells.get("C7").put_value(5000)
sheet.cells.get("A8").put_value("Golf")
sheet.cells.get("B8").put_value("Qtr3")
sheet.cells.get("C8").put_value(6430)

# Aggiungi una tabella pivot alla cella di destinazione E3, usando A1:C8 come origine
pivot_table = sheet.pivot_tables.add("A1:C8", 2, 4)

# Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivot_table.add_field_to_area(PivotFieldType.ROW, "Sport")
pivot_table.add_field_to_area(PivotFieldType.COLUMN, "Quarter")
pivot_table.add_field_to_area(PivotFieldType.DATA, "Sales")

# Salva la cartella di lavoro
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Quando un intervallo di celle viene assegnato come origine dati, l'intervallo deve andare dall'angolo superiore sinistro all'angolo inferiore destro. Ad esempio, "A1:C3" è valido, ma "C3:A1" non lo è.
{{% /alert %}}

## Articoli correlati
- [Aggiungere campi filtro a una tabella pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/apply-style-to-pivot-table/)
- [Modificare il layout dei campi pagina nella tabella pivot](/cells/it/python-net/change-page-field-layout/)
- [Filtrare le tabelle pivot in base a etichetta o valore](/cells/it/python-net/filter-by-label-or-value-of-pivot-table/)
- [Gestire i campi valore delle tabelle pivot in Aspose.Cells for Python via .NET](/cells/it/python-net/manage-value-fields/)

{{< app/cells/assistant language="python-net" >}}