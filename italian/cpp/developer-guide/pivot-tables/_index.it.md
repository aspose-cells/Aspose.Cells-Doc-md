---
title: Crea una tabella pivot
linktitle: Crea una tabella pivot
description: Crea e formatta tabelle pivot con Aspose.Cells for C++.
keywords: Crea tabella pivot, Inserisci tabella pivot, Formatta tabella pivot.
type: docs
weight: 160
url: /it/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Che cos'è una tabella pivot?**
Una tabella pivot è un report di riepilogo interattivo: condensa un grande blocco di dati grezzi, disposti riga per riga, in una matrice compatta senza ricorrere a formule. Si decide quali colonne diventano etichette di riga, quali diventano etichette di colonna e quali vengono aggregate come valori; la tabella pivot esegue il raggruppamento e i calcoli:
- **Riepiloga** — vendite totali per prodotto, per area geografica o per trimestre, anziché lunghe catene di formule.
- **Confronta** — le categorie nelle righe e i periodi nelle colonne trasformano un elenco lineare in un report incrociato in cui le tendenze sono visibili a colpo d'occhio.
- **Analisi dettagliata** — fare doppio clic su un valore riepilogativo per esaminare le righe di origine.
- **Aggiorna** — quando i dati di origine cambiano, un singolo aggiornamento ricalcola l'intero report.
Gli scenari tipici includono dashboard delle vendite, suddivisioni delle spese e analisi dell'inventario: qualsiasi domanda del tipo «come si distribuiscono questi numeri per categoria e nel tempo?». In Aspose.Cells for C++, una tabella pivot viene creata tramite il metodo [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) di un foglio di lavoro. Una volta creata, è possibile gestirla mediante la classe [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/).

## **Crea una tabella pivot**
Il seguente codice di esempio mostra come creare una tabella pivot e gestirla. Consultare il [file Excel di output](23167010.xlsx) generato con questo codice e la schermata seguente, che mostra il file Excel di output in Microsoft Excel.
![todo:image_alt_text](create-pivot-table_1.png)

## **Codice di esempio**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Crea un nuovo workbook e ottieni il primo foglio di lavoro
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Scrivi i dati di origine: vendite per sport e trimestre
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Aggiungi una tabella pivot alla cella di destinazione E3, usando A1:C8 come origine
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Assegna i campi pivot: Sport a Righe, Quarter a Colonne, Sales a Dati
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Salva il workbook
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}