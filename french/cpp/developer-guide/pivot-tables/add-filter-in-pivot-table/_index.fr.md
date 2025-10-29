---
title: Filtre de tableau croisé dynamique avec C++
linktitle: Filtre de tableau croisé dynamique
type: docs
weight: 130
url: /fr/cpp/add-or-clear-pivot-filter/
description: Apprenez comment ajouter un filtre dans un tableau croisé dynamique avec Aspose.Cells en utilisant C++.
keywords: Ajout d un filtre dans un tableau croisé dynamique sans Office 2013, Office 2016, Office 2019 et Office 365.
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique avec des données connues et souhaitez filtrer le tableau, vous devez apprendre et utiliser le filtre. Cela peut vous aider à filtrer efficacement les données souhaitées. En utilisant l'API Aspose.Cells, vous pouvez ajouter et effacer un filtre sur les valeurs de champ dans les tableaux croisés dynamiques. 

## **Ajouter un filtre dans un tableau croisé dynamique dans Excel**
Ajoutez un filtre dans un tableau croisé dynamique dans Excel, en suivant ces étapes :

1. Sélectionnez le tableau croisé dynamique que vous souhaitez effacer. 
2. Cliquez sur la flèche déroulante pour le filtre que vous souhaitez ajouter dans le tableau croisé dynamique.
3. Sélectionnez « Top 10 » dans le menu déroulant.
<br>
<img src="3.png" width=80% />
4. Définissez le mode d'affichage et le nombre de filtres.
<br>
<img src="4.png" width=80% />

## **Ajouter un filtre dans un tableau croisé dynamique**
Veuillez consulter le code d'exemple suivant. Il défini les données et crée un tableau croisé dynamique basé sur celles-ci. Ajoute ensuite un filtre sur le champ de ligne du tableau croisé dynamique. Enfin, enregistre le classeur au format [XLSX de sortie](filterout.xlsx). Après avoir exécuté le code d'exemple, un tableau croisé dynamique avec filtre top10 est ajouté à la feuille de calcul.

### **Code d'exemple**
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

## **Effacer un filtre dans un tableau croisé dynamique dans Excel**
Effacer le filtre dans le tableau croisé dynamique dans Excel, suivez ces étapes :

1. Sélectionnez le tableau croisé dynamique que vous souhaitez effacer. 
2. Cliquez sur la flèche déroulante pour le filtre que vous souhaitez effacer dans le tableau croisé dynamique.
3. Sélectionnez "Effacer le filtre" dans le menu déroulant.
<br>
<img src="1.png" width=80% />
4. Si vous souhaitez effacer tous les filtres du tableau croisé dynamique, vous pouvez également cliquer sur le bouton "Effacer les filtres" dans l'onglet Analyser le tableau croisé dynamique dans le ruban d'Excel.
<br>
<img src="2.png" width=80% />

## **Effacer le filtre dans un tableau croisé dynamique**
Effacer le filtre dans un tableau croisé dynamique en utilisant Aspose.Cells. Veuillez voir le code d'exemple suivant. 
1. Définir les données et créer un tableau croisé dynamique basé sur celles-ci. 
2. Ajouter un filtre sur le champ de ligne du tableau croisé dynamique. 
3. Enregistrer le classeur au format [XLSX de sortie](out_add.xlsx). Après l'exécution du code d'exemple, un tableau croisé dynamique avec un filtre top10 est ajouté à la feuille de calcul. 
4. Effacer le filtre sur un champ pivotant spécifique. Après l'exécution du code pour effacer le filtre, le filtre sur le champ pivotant spécifique sera effacé. Veuillez vérifier le [XLSX de sortie](out_delete.xlsx).

### **Code d'exemple**
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
{{< app/cells/assistant language="cpp" >}}
