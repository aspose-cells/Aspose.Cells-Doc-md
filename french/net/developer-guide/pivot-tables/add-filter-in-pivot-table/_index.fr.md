---
title: Filtre de tableau croisé dynamique
type: docs
weight: 130
url: /fr/net/add-or-clear-pivot-filter/
description: Apprenez comment ajouter un filtre dans un tableau croisé dynamique avec Aspose.Cells.
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
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Add-filter-in-PivotTable.cs" >}}

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
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "PivotTables-Clear-filter-in-PivotTable.cs" >}}
{{< app/cells/assistant language="csharp" >}}
