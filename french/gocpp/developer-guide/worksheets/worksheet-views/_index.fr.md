---
title: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/go-cpp/worksheet-views/
---

## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page indique les données qui seront ajoutées à chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells, les développeurs peuvent activer les modes vue normale ou aperçu des sauts de page.

### **Contrôle des modes d'affichage**

Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) permettant d’accéder à chaque feuille dans le fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre une large gamme de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'aperçu des sauts de page ou normal, utilisez la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). [IsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/ispagebreakpreview/) retourne une valeur booléenne, ce qui signifie qu'elle ne peut contenir qu'une valeur **vrai** ou **faux**.

#### **Activation de la vue normale**

Configurez une feuille pour la vue normale en définissant la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sur **false**.

#### **Activation de l'aperçu des sauts de page**

Configurez n'importe quelle feuille pour voir les sauts de page en réglant la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) sur **true**. Cela bascule la feuille de la vue normale à l'aperçu des sauts de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la méthode [SetIsPageBreakPreview](https://reference.aspose.com/cells/go-cpp/worksheet/setispagebreakpreview/) pour activer le mode d'aperçu des sauts de page pour la première feuille d'un fichier Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-EnablingPageBreakPreview.go" >}}

## **Facteur de zoom**

### **Utilisation de Microsoft Excel**

Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells & Facteur de zoom**

Aspose.Cells permet également aux développeurs de définir le facteur de zoom de la feuille. Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) qui permet d'accéder à chaque feuille d'un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre une large gamme de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille, utilisez la méthode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la méthode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/).

Un exemple complet est fourni ci-dessous pour démontrer comment utiliser la méthode [SetZoom](https://reference.aspose.com/cells/go-cpp/worksheet/setzoom/) pour définir le facteur de zoom de la première feuille du fichier Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ZoomFactor.go" >}}

## **Figer les volets**

### **Utilisation de Microsoft Excel**

Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Les Volets Figés**

Aspose.Cells permet également aux développeurs d'appliquer le gel des volets aux feuilles à l'exécution. Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) contient une collection [Worksheets](https://reference.aspose.com/cells/go-cpp/worksheetcollection/) qui permet d'accéder à chaque feuille d'un fichier Excel.

Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/) offre une large gamme de méthodes pour gérer les feuilles de calcul. Pour configurer le gel des volets, appelez la méthode [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). La méthode [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) prend les paramètres suivants :

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

Un exemple complet est présenté ci-dessous qui montre comment utiliser la méthode [FreezePanes](https://reference.aspose.com/cells/go-cpp/worksheet/freezepanes_int_int_int_int/) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4ème ligne et la 3ème colonne, où les lignes et les colonnes commencent à l'index 0) de la première feuille du fichier Excel.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FreezePanes.go" >}}

## **Diviser les volets**

Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.

### **Application et Suppression des Volets Divisés**

#### **Division des Volets**

Aspose.Cells fournit une classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) qui représente un fichier Microsoft Excel. La classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) offre une large gamme de méthodes pour gérer un fichier Excel. Pour mettre en œuvre des vues fractionnées, utilisez la méthode [Split](https://reference.aspose.com/cells/go-cpp/worksheet/split/) de la classe [Worksheet](https://reference.aspose.com/cells/go-cpp/worksheet/). Pour supprimer les volets fractionnés, utilisez la méthode [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SplitPanes.go" >}}

#### **Suppression de volets**

Supprimer les volets fractionnés en utilisant la méthode [RemoveSplit](https://reference.aspose.com/cells/go-cpp/worksheet/removesplit/).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemovingPanes.go" >}}
