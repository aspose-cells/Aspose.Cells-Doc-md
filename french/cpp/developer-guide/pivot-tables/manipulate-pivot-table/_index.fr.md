---
title: Manipuler le tableau croisé dynamique
type: docs
weight: 20
url: /fr/cpp/manipulate-pivot-table/
---
##  **Scénarios d'utilisation possibles**
En plus de créer de nouveaux tableaux croisés dynamiques, vous pouvez manipuler les tableaux croisés dynamiques nouveaux et existants. Vous pouvez modifier les données dans la plage source du tableau croisé dynamique, puis les actualiser, les calculer et atteindre les nouvelles valeurs des cellules du tableau croisé dynamique. Veuillez utiliser[Tableau croisé dynamique.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) et[PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/)méthodes après avoir modifié les valeurs dans la plage source du tableau croisé dynamique pour actualiser le tableau croisé dynamique.
##  **Manipuler le tableau croisé dynamique**
 L'exemple de code suivant charge le[exemple de fichier Excel](23167013.xlsx) et accède au tableau croisé dynamique existant dans sa première feuille de calcul. Il modifie la valeur de la cellule B3 qui se trouve à l'intérieur de la plage source du tableau croisé dynamique, puis actualise le tableau croisé dynamique. Avant d'actualiser le tableau croisé dynamique, il accède à la valeur de la cellule H8 du tableau croisé dynamique qui est 15 et après avoir actualisé le tableau croisé dynamique, sa valeur passe à 6. Veuillez consulter le[sortie du fichier Excel](23167014.xlsx)généré avec ce code et la capture d'écran montrant l'effet de l'exemple de code sur l'exemple de fichier Excel. Veuillez également consulter la sortie de la console ci-dessous qui montre la valeur de la cellule H8 du tableau croisé dynamique avant et après l'actualisation du tableau croisé dynamique.

![tâche : image_alt_text](manipulate-pivot-table_1.png)
##  **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
##  **Sortie console**
 Vous trouverez ci-dessous la sortie console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier Excel](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
