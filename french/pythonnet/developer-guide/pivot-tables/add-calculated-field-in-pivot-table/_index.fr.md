---
title: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/python-net/add-calculated-field-in-pivot-table/
description: Comment ajouter un champ calculé dans un tableau croisé dynamique avec Aspose.Cells for Python via .NET.
keywords: Adding a calculated field in pivot table.
---
##  **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique basé sur des données connues, vous constatez que les données qu'il contient ne correspondent pas à celles que vous souhaitez. Les données souhaitées sont la combinaison de ces données originales. Par exemple, vous devez ajouter, soustraire, multiplier et diviser les données originales avant de vouloir les données. À ce stade, vous devez créer un champ calculé et définir la formule de calcul correspondante. Effectuez ensuite quelques statistiques et autres opérations sur le champ calculé.

##  **Ajouter un champ calculé dans le tableau croisé dynamique dans Excel**
Insérez un champ calculé dans un tableau croisé dynamique dans Excel, suivez ces étapes :

1.  Sélectionnez le tableau croisé dynamique auquel vous souhaitez ajouter un champ calculé.
2. Accédez à l'onglet Analyse de tableau croisé dynamique sur le ruban.
3. Cliquez sur « Champs, éléments et ensembles », puis sélectionnez « Champ calculé » dans le menu déroulant.
4. Dans le champ "Nom", saisissez un nom pour le champ calculé.
5. Dans le champ "Formule", saisissez la formule du calcul que vous souhaitez effectuer en utilisant les noms de champs de tableau croisé dynamique et les opérateurs mathématiques appropriés.
<br>
<img src="1.png" width=80% />
6. Cliquez sur "ok" pour créer le champ calculé.
7. Le nouveau champ calculé apparaîtra dans la liste des champs du tableau croisé dynamique sous la section Valeurs.
8. Faites glisser le champ calculé vers la section Valeurs du tableau croisé dynamique pour afficher les valeurs calculées.
<br>
<img src="2.png" width=80% />

##  **Ajouter un champ calculé dans le tableau croisé dynamique à l'aide de C#**
Ajoutez le champ calculé au fichier Excel en utilisant Aspose.Cells for Python via .NET. Veuillez consulter l'exemple de code suivant. Après avoir exécuté l'exemple de code, un tableau croisé dynamique avec un champ calculé est ajouté à la feuille de calcul.
1.  Définissez les données d'origine et créez un tableau croisé dynamique.
2. Créez le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique.
 3. Ajoutez le champ calculé à la zone de données.
 4. Enfin, il enregistre le classeur dans[sortie XLSX](out.xlsx) format.

##  **Exemple de code**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-Add-calculated-field-in-PivotTable.py" >}}
