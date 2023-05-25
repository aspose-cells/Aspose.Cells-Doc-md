---
title: Effacer le filtre dans le tableau croisé dynamique
type: docs
weight: 130
url: /fr/java/clear-filter-in-pivot-table/
description: Comment effacer PivotFilter du PivotField spécifique dans le tableau croisé dynamique avec Aspose.Cells.
keywords: Clear PivotFilter in pivot table.
---
##  **Scénarios d'utilisation possibles**
 Lorsque vous créez un tableau croisé dynamique avec des données connues et que vous souhaitez filtrer le tableau croisé dynamique, vous devez apprendre et utiliser le filtre. Cela peut vous aider à filtrer efficacement les données que vous souhaitez. En utilisant le Aspose.Cells API, vous pouvez filtrer les valeurs de champ dans les tableaux croisés dynamiques.

##  **Effacer le filtre dans le tableau croisé dynamique dans Excel**
Effacer le filtre dans le tableau croisé dynamique dans Excel, suivez ces étapes :

1.  Sélectionnez le tableau croisé dynamique pour lequel vous souhaitez effacer le filtre.
2. Cliquez sur la flèche déroulante du filtre que vous souhaitez effacer dans le tableau croisé dynamique.
3. Sélectionnez "Effacer le filtre" dans le menu déroulant.
<img src="1.png" width=80% />
4. Si vous souhaitez effacer tous les filtres du tableau croisé dynamique, vous pouvez également cliquer sur le bouton "Effacer les filtres" dans l'onglet Analyser le tableau croisé dynamique du ruban dans Excel.
<img src="2.png" width=80% />

##  **Effacer le filtre dans le tableau croisé dynamique**
 Veuillez consulter l'exemple de code suivant. Il définit les données et crée un tableau croisé dynamique basé sur celles-ci. Ajoutez ensuite un filtre sur le champ de ligne du tableau croisé dynamique. Enfin, il enregistre le classeur dans[sortie XLSX](out_add.xlsx) format. Après avoir exécuté l'exemple de code, un tableau croisé dynamique avec le filtre top10 est ajouté à la feuille de calcul. Après avoir ajouté un filtre, lorsque nous avons besoin de données non filtrées, nous pouvons effacer le filtre sur un champ pivot spécifique. Après avoir exécuté le code pour effacer le filtre, le filtre sur le champ pivot spécifique sera effacé. S'il vous plaît, vérifiez le[sortie XLSX](out_delete.xlsx).

##  **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "PivotTables-Clear-filter-in-PivotTable.java" >}}