---
title: Manipuler le tableau croisé dynamique
type: docs
weight: 20
url: /fr/cpp/manipulate-pivot-table/
---
## **Scénarios d'utilisation possibles**
Outre la création de nouveaux tableaux croisés dynamiques, vous pouvez manipuler les tableaux croisés dynamiques nouveaux et existants. Vous pouvez modifier les données dans la plage source du tableau croisé dynamique, puis les actualiser et les calculer et atteindre les nouvelles valeurs des cellules du tableau croisé dynamique. Veuillez utiliser[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6) et[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)méthodes après avoir modifié les valeurs dans la plage source du tableau croisé dynamique pour actualiser le tableau croisé dynamique.
## **Manipuler le tableau croisé dynamique**
 L'exemple de code suivant charge le[exemple de fichier excel](23167013.xlsx) et accède au tableau croisé dynamique existant à l'intérieur de sa première feuille de calcul. Il modifie la valeur de la cellule B3 qui se trouve dans la plage source du tableau croisé dynamique, puis actualise le tableau croisé dynamique. Avant d'actualiser le tableau croisé dynamique, il accède à la valeur de la cellule du tableau croisé dynamique H8 qui est 15 et après avoir actualisé le tableau croisé dynamique, sa valeur passe à 6. Veuillez consulter le[fichier excel de sortie](23167014.xlsx)généré avec ce code et la capture d'écran montrant l'effet de l'exemple de code sur l'exemple de fichier Excel. Veuillez également consulter la sortie de la console ci-dessous qui indique la valeur de la cellule du tableau croisé dynamique H8 avant et après l'actualisation du tableau croisé dynamique.

![tâche : image_autre_texte](manipulate-pivot-table_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **Sortie console**
 Vous trouverez ci-dessous la sortie de la console de l'exemple de code ci-dessus lorsqu'il est exécuté avec le[exemple de fichier excel](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
