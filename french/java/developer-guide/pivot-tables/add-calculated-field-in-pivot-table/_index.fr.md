---
title: Ajouter un champ calculé dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/java/add-calculated-field-in-pivot-table/
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
5. Dans le champ "Formule", entrez la formule que vous souhaitez effectuer en utilisant les noms de champ de tableau croisé dynamique appropriés et les opérateurs mathématiques. 
<br>
<img src="1.png" width=80% />
6. Cliquez sur "OK" pour créer le champ calculé.
7. Le nouveau champ calculé apparaîtra dans la liste des champs du tableau croisé dynamique sous la section "Valeurs".
8. Faites glisser le champ calculé dans la section Valeurs du tableau croisé dynamique pour afficher les valeurs calculées.
<br>
<img src="2.png" width=80% />

## **Ajouter un champ calculé dans un tableau croisé dynamique**
Veuillez consulter le code d'exemple suivant. Le code définit d'abord les données d'origine et crée un tableau croisé dynamique. Ensuite, créez le champ calculé en fonction du PivotField existant dans le tableau croisé dynamique et ajoutez le champ calculé à la zone de données. Enfin, enregistrez le classeur au format [XLSX de sortie](out.xlsx). Après l'exécution du code d'exemple, un tableau croisé dynamique avec champ calculé est ajouté à la feuille de calcul.

## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-calculated-field-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
