---
title: Filtre de tableau croisé dynamique
type: docs
weight: 130
url: /fr/java/add-or-clear-pivot-filter/
description: Apprenez comment ajouter un filtre dans un tableau croisé dynamique avec la bibliothèque Aspose.Cells Java.
keywords: Ajout d un filtre dans un tableau croisé dynamique sans Office 2013, Office 2016, Office 2019 et Office 365.
---

## **Scénarios d'utilisation possibles**
Lorsque vous créez un tableau croisé dynamique avec des données connues et que vous souhaitez filtrer le tableau croisé dynamique, vous devez apprendre et utiliser un filtre. Cela peut vous aider à filtrer efficacement les données que vous souhaitez. En utilisant l'API Aspose.Cells Java, vous pouvez ajouter un filtre sur les valeurs de champ dans les tableaux croisés dynamiques. 

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
Veuillez consulter le code d'exemple suivant. Il définit les données et crée un tableau croisé dynamique basé sur celles-ci. Ensuite, ajoutez un filtre sur le champ de ligne du tableau croisé dynamique. Enfin, enregistre le classeur au format [XLSX de sortie](out.xlsx). Après avoir exécuté le code d'exemple, un tableau croisé dynamique avec un filtre top10 est ajouté à la feuille de calcul.

### **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Add-filter-in-PivotTable.java" >}}


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
Veuillez consulter le code d'exemple suivant. Il définit les données et crée un tableau croisé dynamique basé sur celles-ci. Ensuite, ajoutez un filtre sur le champ de ligne du tableau croisé dynamique. Enfin, enregistre le classeur au format [XLSX de sortie](out_add.xlsx). Après avoir exécuté le code d'exemple, un tableau croisé dynamique avec un filtre top10 est ajouté à la feuille de calcul. Après avoir ajouté un filtre, lorsque nous avons besoin de données non filtrées, nous pouvons effacer le filtre sur un champ de tableau croisé dynamique spécifique. Après avoir exécuté le code pour effacer le filtre, le filtre sur le champ de tableau croisé dynamique spécifique sera effacé. Veuillez vérifier le [XLSX de sortie](out_delete.xlsx).

### **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}
{{< app/cells/assistant language="java" >}}
