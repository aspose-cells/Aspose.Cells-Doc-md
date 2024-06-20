---
title: Mettre à jour les références dans d autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul
type: docs
weight: 700
url: /fr/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/
---

{{% alert color="primary" %}} 

Lorsque vous supprimez des colonnes et des lignes vides dans une feuille de calcul, alors ses références dans d'autres feuilles de calcul deviennent invalides. Si vous souhaitez éviter ce comportement et que ces références soient également mises à jour, veuillez utiliser le [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) et le définir sur **true**.

{{% /alert %}} 
## **Mettre à jour les références dans d'autres feuilles de calcul tout en supprimant les colonnes et les rangées vides dans une feuille de calcul**
Veuillez consulter le code d'exemple suivant et sa sortie console. La cellule E3 dans la deuxième feuille de calcul a une formule =Sheet1!C3 qui fait référence à la cellule C3 de la première feuille de calcul. Si vous définissez la propriété [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) comme **true**, cette formule sera mise à jour et deviendra =Sheet1!A1 en supprimant les colonnes et les lignes vides dans la première feuille de calcul. Cependant, si vous définissez la propriété [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) comme **false**, la formule dans la cellule E3 de la deuxième feuille de calcul restera =Sheet1!C3 et deviendra invalide.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-Updatereferencesinotherworksheetswhiledeletingblankcolumnsandrowsinworksheet-1.java" >}}
## **Sortie console**
Ceci est la sortie console du code d'exemple ci-dessus lorsque la propriété [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) a été définie sur **true**.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!A1

Cell Value: 4

{{< /highlight >}}

Ceci est la sortie console du code d'exemple ci-dessus lorsque la propriété [DeleteOptions.UpdateReference](https://reference.aspose.com/cells/java/com.aspose.cells/deleteoptions#UpdateReference) a été définie sur **false**. Comme vous pouvez le voir, la formule dans la cellule E3 de la deuxième feuille de calcul n'est pas mise à jour et sa valeur de cellule est maintenant de 0 au lieu de 4, ce qui est invalide.

{{< highlight java >}}

 Cell E3 before deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 4


Cell E3 after deleting blank columns and rows in Sheet1.

\--------------------------------------------------------

Cell Formula: =Sheet1!C1

Cell Value: 0

{{< /highlight >}}
