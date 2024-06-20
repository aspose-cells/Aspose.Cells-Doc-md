---
title: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/net/add-calculated-field-in-pivot-table/
description: Comment ajouter un champ calculé dans un tableau croisé dynamique avec Aspose.Cells.
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

## **Ajouter un champ calculé dans un tableau croisé dynamique en utilisant C#**
Ajouter un champ calculé au fichier Excel en utilisant Aspose.Cells. Veuillez voir le code d'exemple suivant. Après avoir exécuté le code d'exemple, un tableau croisé dynamique avec un champ calculé est ajouté à la feuille de calcul.
1. Définissez les données d'origine et créez un tableau croisé dynamique. 
2. Créez le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique.
3. Ajoutez le champ calculé à la zone de données. 
4. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). 

## **Code d'exemple**
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-calculated-field-in-PivotTable.cs" >}}
