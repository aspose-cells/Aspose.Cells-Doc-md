---
title: Filtro pivot con C++
linktitle: Filtro pivot
type: docs
weight: 130
url: /it/cpp/add-or-clear-pivot-filter/
description: Scopri come aggiungere un filtro in pivot table con Aspose.Cells usando C++.
keywords: Aggiunta di un filtro nella tabella pivot senza office 2013, office 2016, office 2019 e office 365.
---

## **Possibili Scenari di Utilizzo**
Quando crei una tabella pivot con dati noti e desideri filtrarla, devi imparare e usare i filtri. Può aiutarti a filtrare efficacemente i dati desiderati. Usando l'API Aspose.Cells, puoi aggiungere e cancellare filtri sui valori dei campi nelle tabelle pivot. 

## **Aggiungi filtro in Pivot Table in Excel**
Per aggiungere un filtro in Pivot Table in Excel, segui questi passaggi:

1. Seleziona la tabella pivot da cui desideri eliminare il filtro. 
2. Clicca sulla freccia a discesa per il filtro che desideri aggiungere in pivot table.
3. Seleziona "Top 10" dal menu a discesa.
<br>
<img src="3.png" width=80% />
4. Imposta la modalità di visualizzazione e il numero di filtri.
<br>
<img src="4.png" width=80% />

## **Aggiungi filtro in Pivot Table**
Si prega di consultare il codice di esempio seguente. Imposta i dati e crea una tabella pivot basata su di essi. Quindi aggiungi un filtro sul campo di riga della tabella pivot. Infine, salvare il libro di lavoro nel formato [output XLSX](filterout.xlsx). Dopo aver eseguito il codice di esempio, viene aggiunta una tabella pivot con filtro top10 al foglio di lavoro.

### **Codice di Esempio**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Save the workbook
    workbook.Save(u"filterout.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Cancella filtro in Pivot Table in Excel**
Elimina filtro nella tabella pivot in Excel, segui questi passaggi:

1. Seleziona la tabella pivot da cui desideri eliminare il filtro. 
2. Fai clic sulla freccia a discesa per il filtro che desideri eliminare nella tabella pivot.
3. Seleziona "Elimina filtro" dal menu a discesa.
<br>
<img src="1.png" width=80% />
4. Se desideri eliminare tutti i filtri dalla tabella pivot, puoi anche fare clic sul pulsante "Elimina filtri" nella scheda Analizza tabella pivot nel nastro di Excel.
<br>
<img src="2.png" width=80% />

## **Cancella filtro in Pivot Table**
Cancella il filtro nella tabella pivot utilizzando Aspose.Cells. Si prega di vedere il seguente codice di esempio. 
1. Impostare i dati e creare una tabella pivot basata su di essi. 
2. Aggiungere un filtro sul campo di riga della tabella pivot. 
3. Salvare il workbook nel formato [output XLSX](out_add.xlsx). Dopo aver eseguito il codice di esempio, una tabella pivot con filtro top10 viene aggiunta al foglio di lavoro. 
4. Cancella il filtro su un campo pivot specifico. Dopo aver eseguito il codice per cancellare il filtro, il filtro sul campo pivot specifico verrà cancellato. Si prega di controllare il [output XLSX](out_delete.xlsx).

### **Codice di Esempio**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");
    cell = cells.Get(u"A6");
    cell.PutValue(u"Guava");
    cell = cells.Get(u"A7");
    cell.PutValue(u"Carambola");
    cell = cells.Get(u"A8");
    cell.PutValue(u"Banana");
    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);
    cell = cells.Get(u"B6");
    cell.PutValue(5);
    cell = cells.Get(u"B7");
    cell.PutValue(2);
    cell = cells.Get(u"B8");
    cell.PutValue(20);

    // Add a PivotTable to the worksheet
    int i = ws.GetPivotTables().Add(u"=A1:B8", u"D10", u"PivotTable1");

    // Access the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Count");
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    PivotField field = pivotTable.GetRowFields().Get(0);
    field.SetIsAutoSort(true);
    field.SetIsAscendSort(false);
    field.SetAutoSortField(0);

    // Add top10 filter
    PivotField filterField = pivotTable.GetRowFields().Get(0);
    filterField.FilterTop10(0, PivotFilterType::Count, false, 5);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_add.xlsx");

    // Clear PivotFilter from the specific PivotField
    pivotTable.GetPivotFilters().ClearFilter(field.GetBaseIndex());
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out_delete.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
