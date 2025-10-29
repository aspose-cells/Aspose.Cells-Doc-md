---
title: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/cpp/worksheet-views/
---

## **Aperçu des sauts de page**
Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page indique les données qui seront ajoutées à chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells, les développeurs peuvent activer les modes vue normale ou aperçu des sauts de page.
### **Contrôle des modes d'affichage**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) offre une large gamme de méthodes pour gérer les feuilles de calcul. Pour activer les modes vue normale ou aperçu des sauts de page, utilisez la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/ispagebreakpreview/) renvoie une valeur booléenne, ce qui signifie qu'elle peut uniquement stocker une valeur **true** ou **false**.
#### **Activation de la vue normale**
Définir une feuille de calcul en vue normale en définissant la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) à **false**.
#### **Activation de l'aperçu des sauts de page**
Définir n'importe quelle feuille de calcul en aperçu des sauts de page en définissant la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) à **true**. Ce faisant, la feuille de calcul passe de la vue normale à l'aperçu des sauts de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setispagebreakpreview/) pour activer le mode aperçu des sauts de page pour la première feuille de calcul d'un fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-EnablingPageBreakPreview-new.cpp" >}}
## **Facteur de zoom**
### **Utilisation de Microsoft Excel**
Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.
### **Aspose.Cells & Facteur de zoom**
Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille de calcul. Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) permettant d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) propose une large gamme de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la méthode [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la méthode [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la méthode [SetZoom](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setzoom/) pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-ZoomFactor-new.cpp" >}}
## **Figer les volets**
### **Utilisation de Microsoft Excel**
Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.
### **Aspose.Cells & Les Volets Figés**
Aspose.Cells permet également aux développeurs d'appliquer des volets figés aux feuilles de calcul à l'exécution. Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) contient une collection de [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) propose une large gamme de méthodes pour gérer les feuilles de calcul. Pour configurer les volets figés, appelez la méthode [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). La méthode [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) prend les paramètres suivants:

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [FreezePanes](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4ème rangée et la 3ème colonne, où les rangées et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-FreezePanes-new.cpp" >}}
## **Diviser les volets**
Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.
### **Application et Suppression des Volets Divisés**
#### **Division des Volets**
Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) propose une large gamme de méthodes pour gérer un fichier Excel. Pour appliquer des vues divisées, utilisez la méthode [Split](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) de la classe [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). Pour supprimer les volets divisés, utilisez la méthode [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-SplitPanes-new.cpp" >}}
#### **Suppression de volets**
Supprimez les volets divisés à l'aide de la méthode [RemoveSplit](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-WorksheetViews-RemovingPanes-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
