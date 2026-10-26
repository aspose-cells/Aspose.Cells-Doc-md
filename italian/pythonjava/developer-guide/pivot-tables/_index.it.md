---
title: Tabelle pivot
linktitle: Tabelle pivot
description: Crea e formatta le tabelle pivot con Aspose.Cells for Python via Java.
keywords: Creare tabella pivot, Inserire tabella pivot, Formattare tabella pivot.
type: docs
weight: 160
url: /it/python-java/create-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un report riepilogativo interattivo: condensa un grande volume di dati grezzi disposti riga per riga in una matrice compatta senza utilizzare una sola formula. Si decide quali colonne diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregate come valori; la tabella pivot esegue il raggruppamento e i calcoli:
- **Riepilogare** — vendite totali per prodotto, per area geografica o per trimestre, invece di lunghe catene di formule.
- **Confrontare** — le categorie nelle righe e i periodi nelle colonne trasformano un elenco piatto in un report incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Analizzare in dettaglio** — fare doppio clic su un valore riepilogato per esaminare le righe di origine.
- **Aggiornare** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero report.
Scenari tipici sono la creazione di cruscotti di vendita, l'analisi delle spese e l'analisi dell'inventario, per rispondere a domande come «come si suddividono questi numeri per categoria e periodo?». Aspose.Cells for Python via Java consente di creare le stesse tabelle pivot mediante il codice, in modo che le cartelle di lavoro generate dall'applicazione contengano report pronti all'uso anziché soltanto dati grezzi.

### **Modello a oggetti della tabella pivot**
Aspose.Cells offre un insieme di classi utilizzate per creare e gestire le tabelle pivot. Gli elementi costitutivi sono:
- `PivotField` rappresenta un campo in una `PivotTable`.
- `PivotFieldCollection` rappresenta una raccolta di tutti gli oggetti `PivotField` in una `PivotTable`.
- `PivotTable` rappresenta una tabella pivot su un foglio di lavoro.
- `PivotTableCollection` rappresenta una raccolta di tutti gli oggetti `PivotTable` su un foglio di lavoro.

### **Creazione di una semplice tabella pivot con Aspose.Cells**
Creare una tabella pivot richiede tre passaggi operativi, seguiti dal salvataggio: scrivere i dati di origine nelle celle del foglio di lavoro, aggiungere la tabella pivot nella posizione di destinazione e inserire i campi nelle aree delle righe, delle colonne e dei dati.
1. Aggiungere i dati a un foglio di lavoro utilizzando il metodo `putValue` della cella. Questi dati verranno utilizzati come origine dati della tabella pivot.
2. Aggiungere una tabella pivot al foglio di lavoro chiamando il metodo `add` della raccolta `PivotTables`: `add(sourceData, row, column)`. `sourceData` è l'intervallo di origine (ad esempio, "A1:C8"); `row` e `column` sono le coordinate indicizzate da zero della cella di destinazione, situata nell'angolo superiore sinistro della tabella pivot (la cella E3 corrisponde alla riga 2 e alla colonna 4). Il metodo restituisce direttamente il nuovo oggetto `PivotTable`.
3. Aggiungere i campi della tabella pivot tramite il metodo `addFieldToArea` dell'oggetto `PivotTable`: il nome del campo va inserito nell'area delle righe (`PivotFieldType.ROW`), nell'area delle colonne (`PivotFieldType.COLUMN`) o nell'area dei dati (`PivotFieldType.DATA`).
4. Salvare la cartella di lavoro: la tabella pivot viene scritta nel file salvato.
Dopo l'esecuzione del codice di esempio, una tabella pivot viene aggiunta al foglio di lavoro.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

# Crea un nuovo workbook e ottieni il primo foglio di lavoro
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

# Scrivi i dati di origine: vendite per sport e trimestre
cells.get("A1").putValue("Sport")
cells.get("B1").putValue("Quarter")
cells.get("C1").putValue("Sales")
cells.get("A2").putValue("Golf")
cells.get("B2").putValue("Qtr3")
cells.get("C2").putValue(1500)
cells.get("A3").putValue("Golf")
cells.get("B3").putValue("Qtr4")
cells.get("C3").putValue(2000)
cells.get("A4").putValue("Tennis")
cells.get("B4").putValue("Qtr3")
cells.get("C4").putValue(600)
cells.get("A5").putValue("Tennis")
cells.get("B5").putValue("Qtr4")
cells.get("C5").putValue(1500)
cells.get("A6").putValue("Tennis")
cells.get("B6").putValue("Qtr3")
cells.get("C6").putValue(4070)
cells.get("A7").putValue("Tennis")
cells.get("B7").putValue("Qtr4")
cells.get("C7").putValue(5000)
cells.get("A8").putValue("Golf")
cells.get("B8").putValue("Qtr3")
cells.get("C8").putValue(6430)

# Aggiungi una tabella pivot nella cella di destinazione E3, usando A1:C8 come origine
pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4)

# Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport")
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter")
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales")

# Salva il workbook
workbook.save("pivotTable_test_out.xlsx")
```

{{% alert color="primary" %}}
Quando si assegna un intervallo di celle come origine dati, l'intervallo deve andare dall'angolo superiore sinistro all'angolo inferiore destro. Ad esempio, "A1:C3" è valido, ma "C3:A1" non lo è.
{{% /alert %}}

## Articoli correlati
- [Aggiungere campi di filtro a una tabella pivot in Aspose.Cells for Python via Java](/cells/it/python-java/add-page-field-in-pivot-table/)
- [Applicare stili alle tabelle pivot in Aspose.Cells for Python via Java](/cells/it/python-java/apply-style-to-pivot-table/)
- [Modificare il layout dei campi pagina nella tabella pivot](/cells/it/python-java/change-page-field-layout/)
- [Filtrare le tabelle pivot per etichetta o valore](/cells/it/python-java/filter-by-label-or-value-of-pivot-table/)
- [Gestire i campi valore della tabella pivot in Aspose.Cells for Python via Java](/cells/it/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}