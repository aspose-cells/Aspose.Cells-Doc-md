---
title: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/java/add-calculated-field-in-pivot-table/
description: Comment ajouter un champ calculé dans un tableau croisé dynamique avec Aspose.Cells.
keywords: Adding a calculated field in pivot table.
---
##  **Scénarios d'utilisation possibles**
 Lorsque vous créez un tableau croisé dynamique basé sur des données connues, vous constatez que les données qu'il contient ne correspondent pas à ce que vous souhaitez. Les données que vous voulez sont la combinaison de ces données d'origine. Par exemple, vous devez ajouter, soustraire, multiplier et diviser les données d'origine avant de vouloir les données. À ce stade, vous devez créer un champ calculé et définir la formule correspondante pour le calcul. Effectuez ensuite des statistiques et d'autres opérations sur le champ calculé.

##  **Ajouter un champ calculé dans le tableau croisé dynamique dans Excel**
Insérez un champ calculé dans un tableau croisé dynamique dans Excel, procédez comme suit :

1.  Sélectionnez le tableau croisé dynamique auquel vous souhaitez ajouter un champ calculé.
2. Accédez à l'onglet PivotTable Analyze du ruban.
3. Cliquez sur « Champs, éléments et ensembles », puis sélectionnez « Champ calculé » dans le menu déroulant.
4. Dans le champ "Nom", entrez un nom pour le champ calculé.
 5. Dans le champ "Formule", entrez la formule que vous souhaitez exécuter en utilisant les noms de champ de tableau croisé dynamique et les opérateurs mathématiques appropriés.
<br>
<img src="1.png" width=80% />
6. Cliquez sur "ok" pour créer le champ calculé.
7. Le nouveau champ calculé apparaîtra dans la liste des champs de tableau croisé dynamique sous la section Valeurs.
8. Faites glisser le champ calculé vers la section Valeurs du tableau croisé dynamique pour afficher les valeurs calculées.
<br>
<img src="2.png" width=80% />

##  **Ajouter un champ calculé dans le tableau croisé dynamique**
Veuillez consulter l'exemple de code suivant. Le code définit d'abord les données d'origine et crée un tableau croisé dynamique. Créez ensuite le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique et ajoutez le champ calculé à la zone de données. Enfin, il enregistre le classeur dans[sortie XLSX](out.xlsx) format. Après avoir exécuté l'exemple de code, un tableau croisé dynamique avec un champ calculé est ajouté à la feuille de calcul.

##  **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
