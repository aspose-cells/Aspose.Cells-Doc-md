---
title: Manipuler le tableau croisé dynamique
type: docs
weight: 20
url: /fr/cpp/manipulate-pivot-table/
---

## **Scénarios d'utilisation possibles**
En plus de créer de nouveaux tableaux croisés dynamiques, vous pouvez manipuler les tableaux croisés dynamiques neufs et existants. Vous pouvez modifier les données dans la plage source du tableau croisé dynamique, puis rafraîchir, calculer et obtenir les nouvelles valeurs des cellules du tableau croisé dynamique. Veuillez utiliser les méthodes [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) et [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) après avoir modifié les valeurs dans la plage source du tableau croisé dynamique pour rafraîchir le tableau croisé dynamique.
## **Manipuler le tableau croisé dynamique**
Le code d'exemple suivant charge le [fichier Excel exemple](23167013.xlsx) et accède au tableau croisé dynamique existant dans sa première feuille de calcul. Il modifie la valeur de la cellule B3 qui se trouve à l'intérieur de la plage source du tableau croisé dynamique, puis rafraîchit le tableau croisé dynamique. Avant de rafraîchir le tableau croisé dynamique, il accède à la valeur de la cellule du tableau croisé dynamique H8 qui est de 15 et après le rafraîchissement du tableau croisé dynamique, sa valeur change à 6. Veuillez consulter le [fichier Excel de sortie](23167014.xlsx) généré avec ce code et la capture d'écran montrant l'effet du code d'exemple sur le fichier Excel exemple. Veuillez également consulter la sortie de la console ci-dessous qui montre la valeur de la cellule du tableau croisé dynamique H8 avant et après le rafraîchissement du tableau croisé dynamique.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Sortie console**
Voici la sortie de la console du code d'exemple ci-dessus lorsqu'il est exécuté avec le [fichier Excel exemple](23167013.xlsx) fourni.

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
