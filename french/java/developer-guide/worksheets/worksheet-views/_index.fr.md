---
title: Vues de la feuille de calcul
type: docs
weight: 10
url: /fr/java/worksheet-views/
---

## **Aperçu des sauts de page**
Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page pour que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells, les développeurs peuvent activer les modes de vue normale ou d'aperçu des sauts de page.
### **Contrôle des modes d'affichage**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/java/cells/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/java/cells/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/java/cells/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes normal ou aperçu avant impression, utilisez la méthode [setPageBreakPreview](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#IsPageBreakPreview) de la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet).
#### **Activation de la vue normale**
Définissez n'importe quelle feuille de calcul en vue normale en utilisant la méthode [setPageBreakPreview](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#IsPageBreakPreview) de la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet) et en passant **false** en tant que paramètre.
#### **Activation de l'aperçu des sauts de page**
Définissez n'importe quelle feuille de calcul en aperçu avant impression en utilisant la méthode [setPageBreakPreview](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#IsPageBreakPreview) de la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet) et en passant **true** en tant que paramètre.

Un exemple complet est donné ci-dessous qui démontre l'utilisation de la méthode [setPageBreakPreview](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#IsPageBreakPreview) de la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet) pour activer le mode aperçu avant impression pour la première feuille de calcul du fichier Excel.

Sur la capture d'écran ci-dessous, vous pouvez voir que le fichier Book1.xls est en vue normale.

**Book1.xls: Feuille de calcul avant modification** 

![todo:image_alt_text](worksheet-views_1.png)

Le fichier Book1.xls est ouvert avec la classe [Workbook](https://reference.aspose.com/java/cells/com.aspose.cells/workbook) et le mode est changé en aperçu avant impression pour la première feuille de calcul. Le fichier modifié est enregistré sous le nom de output.xls.

**Ouput.xls : feuille de calcul après modification** 

![todo:image_alt_text](worksheet-views_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-PageBreakPreview-PageBreakPreview.java" >}}
## **Facteur de zoom**
Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

**Définition du facteur de zoom à l'aide de Microsoft Excel** 

![todo:image_alt_text](worksheet-views_3.png)

Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul.
### **Contrôler le facteur de zoom**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/java/cells/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/java/cells/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/java/cells/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la méthode [setZoom](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#Zoom) de la classe [Worksheet](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet).

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [setZoom](https://reference.aspose.com/java/cells/com.aspose.cells/worksheet#Zoom) pour définir le facteur de zoom de la première feuille de calcul dans un fichier Excel.

Sur la capture d'écran ci-dessous, vous pouvez voir le fichier Book1.xls dans la vue par défaut.

**Book1.xls : feuille de calcul avant modification** 

![todo:image_alt_text](worksheet-views_4.png)

Le fichier Book1.xls est ouvert avec la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) et le facteur de zoom de la première feuille de calcul est défini à 75. Le fichier modifié est enregistré sous le nom output.xls.

**Output.xls : feuille de calcul après modification** 

![todo:image_alt_text](worksheet-views_5.png)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ZoomFactor-ZoomFactor.java" >}}
## **Figer les volets**
Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

**Utiliser les volets figés dans Microsoft Excel** 

![todo:image_alt_text](worksheet-views_6.png)

Aspose.Cells permet également aux développeurs d'appliquer des volets figés aux feuilles de calcul pendant l'exécution.

Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) permettant d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer des volets figés, appelez la méthode [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La méthode [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) prend les paramètres suivants :

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

L'exemple complet ci-dessous montre comment utiliser la méthode [freezePanes](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#freezePanes\(int,%20int,%20int,%20int\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir d'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-FreezePanes-FreezePanes.java" >}}


Sur la capture d'écran ci-dessous, vous pouvez voir le fichier Book1.xls sans volets figés.

**Book1.xls: visualisation de la feuille de calcul avant toute modification** 

![todo:image_alt_text](worksheet-views_7.png)

Le fichier Book1.xls est ouvert avec la classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) puis quelques lignes et colonnes sont figées sur la première feuille de calcul. Le fichier modifié est enregistré sous le nom output.xls.

**Outlook.xls: visualisation de la feuille de calcul après modification** 

![todo:image_alt_text](worksheet-views_8.png)
## **Diviser les volets**
Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.
### **Application et Suppression des Volets Divisés**
#### **Division des Volets**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) offre un large éventail de propriétés et de méthodes pour la gestion des fichiers Excel. Pour implémenter des vues fractionnées, utilisez la méthode [split](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#split\(\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). Pour supprimer les volets fractionnés, utilisez la méthode [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) .

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-SplitPanes-SplitPanes.java" >}}



Après l'exécution du code ci-dessus, le fichier généré a une vue fractionnée.

**Volets fractionnés dans le fichier de sortie** 

![todo:image_alt_text](worksheet-views_9.png)
#### **Suppression de volets**
Les développeurs peuvent supprimer les volets fractionnés en utilisant la méthode [removeSplit](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#removeSplit\(\)) de la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovePanes-RemovePanes.java" >}}


## **Sujets avancés**
- [Masquer l'affichage des valeurs nulles dans la feuille de calcul](/cells/fr/java/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur d'onglet de feuille de calcul](/cells/fr/java/set-worksheet-tab-color/)
- [Afficher et masquer les éléments](/cells/fr/java/show-and-hide-elements/)
- [Afficher les formules au lieu des valeurs dans une feuille de calcul](/cells/fr/java/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/java/use-error-checking-options/)
