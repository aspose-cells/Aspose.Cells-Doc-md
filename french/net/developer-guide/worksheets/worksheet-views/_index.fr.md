---
title: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/net/worksheet-views/
description: Cet article expliquera comment utiliser C# et l API .NET pour interagir avec l aperçu des sauts de page d un classeur Excel et des feuilles de calcul. Travaillez avec les fenêtres fractionnées, les fenêtres gelées et le facteur de zoom. 
---

## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

L'affichage normal est l'affichage par défaut d'une feuille de calcul. L'aperçu de saut de page est un affichage d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu de saut de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. En utilisant Aspose.Cells, les développeurs peuvent activer les modes d'affichage normal ou d'aperçu de saut de page.

### **Contrôle des modes d'affichage**

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'affichage normal ou d'aperçu de saut de page, utilisez la propriété [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Activation de la vue normale**

Définissez une feuille de calcul en affichage normal en définissant la propriété [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **false**.

#### **Activation de l'aperçu des sauts de page**

Définissez n'importe quelle feuille de calcul en aperçu de saut de page en définissant la propriété [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **true**. Ce faisant, la feuille de calcul passe de l'affichage normal à l'aperçu de saut de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) pour activer le mode d'aperçu de saut de page pour la première feuille de calcul d'un fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). La vue est basculée en aperçu de saut de page pour la première feuille de calcul en définissant la propriété [**IsPageBreakPreview**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/ispagebreakpreview) sur **true**. Le fichier modifié est enregistré sous le nom output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-PageBreakPreview-1.cs" >}}

## **Facteur de zoom**

### **Utilisation de Microsoft Excel**

Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells & Facteur de zoom**

Aspose.Cells permet aux développeurs de définir le facteur de zoom de la feuille de calcul.
Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la propriété [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**Zoom**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/zoom) pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Le facteur de zoom de la première feuille de calcul est défini à 75 et le fichier modifié est enregistré sous le nom de output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ZoomFactor-1.cs" >}}

## **Figer les volets**

### **Utilisation de Microsoft Excel**

Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Les Volets Figés**

Aspose.Cells permet aux développeurs d'appliquer des volets figés sur des feuilles de calcul à l'exécution.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer des volets figés, appelez la méthode [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) de la classe FeuilleDeCalcul. La méthode [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) prend les paramètres suivants :

- **Ligne**, l'index de la ligne de la cellule à partir de laquelle le gel commencera.
- **Colonne**, l'index de la colonne de la cellule à partir de laquelle le gel commencera.
- **Lignes gelées**, le nombre de lignes visibles dans le volet supérieur.
- **Colonnes gelées**, le nombre de colonnes visibles dans le volet de gauche.

Le fichier book1.xls est ouvert en appelant le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) lors de son instanciation et quelques lignes et colonnes sont figées dans la première feuille de calcul. Le fichier modifié est enregistré sous le nom de output.xls.

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [**FreezePanes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-FreezePanes-1.cs" >}}

## **Diviser les volets**

Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.

### **Application et Suppression des Volets Divisés**

#### **Division des Volets**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour implémenter des vues divisées, utilisez la méthode [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) de la classe [**Split**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/split). Pour supprimer les volets divisés, utilisez la méthode [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-SplitPanes-1.cs" >}}

Après l'exécution du code ci-dessus, le fichier généré aura une vue fractionnée.

#### **Suppression de volets**

Supprimer les volets fractionnés en utilisant la méthode [**RemoveSplit**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/removesplit).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-RemovePanes-1.cs" >}}

## **Sujets avancés**
- [Masquer l'affichage des valeurs nulles dans la feuille de calcul](/cells/fr/net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur d'onglet de feuille de calcul](/cells/fr/net/set-worksheet-tab-color/)
- [Afficher et masquer les quadrillages, les en-têtes de lignes et de colonnes](/cells/fr/net/show-and-hide-gridlines-and-row-column-headers/)
- [Afficher et masquer les lignes, les colonnes et les barres de défilement](/cells/fr/net/show-and-hide-rows-columns-and-scroll-bars/)
- [Afficher et masquer les feuilles de calcul et les onglets](/cells/fr/net/show-and-hide-worksheets-and-tabs/)
- [Afficher les formules au lieu des valeurs dans une feuille de calcul](/cells/fr/net/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/net/use-error-checking-options/)

