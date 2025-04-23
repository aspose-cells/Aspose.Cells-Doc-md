---
title: Ajouter un champ calculé dans le tableau croisé dynamique avec C++
linktitle: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/cpp/add-calculated-field-in-pivot-table/
description: Comment ajouter un champ calculé dans un tableau croisé dynamique avec Aspose.Cells for C++.
keywords: Ajout d un champ calculé dans un tableau croisé dynamique.
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique basé sur des données connues, vous constatez que les données qui s'y trouvent ne correspondent pas à ce que vous souhaitez. Les données que vous souhaitez sont la combinaison de ces données d'origine. Par exemple, vous devez ajouter, soustraire, multiplier et diviser les données d'origine avant de les vouloir. À ce moment-là, vous devez construire un champ calculé et définir la formule correspondante pour le calcul. Ensuite, effectuez des statistiques et d'autres opérations sur le champ calculé. 

## **Ajouter un champ calculé dans un tableau croisé dynamique dans Excel**
Insérer un champ calculé dans un tableau croisé dynamique dans Excel, suivez ces étapes :

1. Sélectionnez le tableau croisé dynamique auquel vous souhaitez ajouter un champ calculé. 
2. Accédez à l'onglet Analyse du tableau croisé dynamique dans le ruban.
3. Cliquez sur "Champs, éléments et ensembles" puis sélectionnez "Champ calculé" dans le menu déroulant.
4. Dans le champ "Nom", entrez un nom pour le champ calculé.
5. Dans le champ "Formule", entrez la formule du calcul que vous souhaitez effectuer en utilisant les noms de champ appropriés du tableau croisé dynamique et les opérateurs mathématiques. 
<br>
<img src="1.png" width=80% />
6. Cliquez sur "OK" pour créer le champ calculé.
7. Le nouveau champ calculé apparaîtra dans la liste des champs du tableau croisé dynamique sous la section "Valeurs".
8. Faites glisser le champ calculé dans la section Valeurs du tableau croisé dynamique pour afficher les valeurs calculées.
<br>
<img src="2.png" width=80% />

## **Ajouter un champ calculé dans le tableau croisé dynamique en utilisant C++**
Ajouter un champ calculé au fichier Excel en utilisant Aspose.Cells. Veuillez voir le code d'exemple suivant. Après avoir exécuté le code d'exemple, un tableau croisé dynamique avec un champ calculé est ajouté à la feuille de calcul.
1. Définissez les données d'origine et créez un tableau croisé dynamique. 
2. Créez le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique.
3. Ajoutez le champ calculé à la zone de données. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

## **Code d'exemple**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a Workbook object
    Workbook workbook;

    // Obtaining the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the values to the cells
    Cell cell = cells.Get("A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get("B1");
    cell.PutValue(u"Count");

    cell = cells.Get("C1");
    cell.PutValue(u"Price");

    cell = cells.Get("A2");
    cell.PutValue(u"Apple");

    cell = cells.Get("A3");
    cell.PutValue(u"Mango");

    cell = cells.Get("A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get("A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get("B2");
    cell.PutValue(5);

    cell = cells.Get("B3");
    cell.PutValue(3);

    cell = cells.Get("B4");
    cell.PutValue(6);

    cell = cells.Get("B5");
    cell.PutValue(4);

    cell = cells.Get("C2");
    cell.PutValue(5);

    cell = cells.Get("C3");
    cell.PutValue(20);

    cell = cells.Get("C4");
    cell.PutValue(30);

    cell = cells.Get("C5");
    cell.PutValue(60);

    // Adding a PivotTable to the worksheet
    int32_t i = ws.GetPivotTables().Add(u"=A1:C5", u"D10", u"PivotTable1");

    // Accessing the instance of the newly added PivotTable
    PivotTable pivotTable = ws.GetPivotTables().Get(i);
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);

    // Adding a calculated field to PivotTable and dragging it to data area
    pivotTable.AddCalculatedField(u"total", u"=Count*Price", true);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
