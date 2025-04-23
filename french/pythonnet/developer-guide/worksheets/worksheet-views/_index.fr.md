---
title: Vues de la feuille de calcul
type: docs
weight: 40
url: /fr/python-net/worksheet-views/
description: Cet article décrira comment utiliser l API Aspose.Cells pour Python via .NET pour interagir avec l aperçu des sauts de page d un classeur Excel et de ses feuilles de calcul. Travaillez avec les volets fractionnés, les volets gelés et le facteur de zoom. 
keywords: Bibliothèque Excel pour Python, comment définir l aperçu des sauts de page, comment activer la vue normale, comment régler le facteur de zoom, comment geler les volets, comment fractionner les volets, comment supprimer les volets.
---

## **Aperçu des sauts de page**

Toutes les feuilles de calcul peuvent être visualisées sous deux modes :

-Vue normale.
-Aperçu des sauts de page.

La vue normale est la vue par défaut d'une feuille de calcul. L'aperçu des sauts de page est une vue d'édition qui affiche une feuille de calcul telle qu'elle sera imprimée. L'aperçu des sauts de page montre quelles données iront sur chaque page afin que vous puissiez ajuster la zone d'impression et les sauts de page. Avec Aspose.Cells pour Python via .NET, les développeurs peuvent activer la vue normale ou l'aperçu des sauts de page.

### **Contrôle des modes d'affichage**

Aspose.Cells pour Python via .NET fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour activer les modes d'affichage normal ou d'aperçu de saut de page, utilisez la propriété [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

#### **Activation de la vue normale**

Définissez une feuille de calcul en affichage normal en définissant la propriété [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **false**.

#### **Activation de l'aperçu des sauts de page**

Définissez n'importe quelle feuille de calcul en aperçu de saut de page en définissant la propriété [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **true**. Ce faisant, la feuille de calcul passe de l'affichage normal à l'aperçu de saut de page.

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) pour activer le mode d'aperçu de saut de page pour la première feuille de calcul d'un fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). La vue est basculée en aperçu de saut de page pour la première feuille de calcul en définissant la propriété [**is_page_break_preview**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_page_break_preview) sur **true**. Le fichier modifié est enregistré sous le nom output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-PageBreakPreview-1.py" >}}

## **Facteur de zoom**

### **Utilisation de Microsoft Excel**

Microsoft Excel offre une fonctionnalité permettant aux utilisateurs de définir le zoom ou le facteur d'échelle d'une feuille de calcul. Cette fonctionnalité aide les utilisateurs à voir le contenu de la feuille de calcul dans des vues plus petites ou plus grandes. Les utilisateurs peuvent définir le facteur de zoom sur n'importe quelle valeur.

### **Aspose.Cells & Facteur de zoom**

Aspose.Cells permet aux développeurs de définir le facteur de zoom de la feuille de calcul.
Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une vaste gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour définir le facteur de zoom d'une feuille de calcul, utilisez la propriété [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). Le facteur de zoom est défini en attribuant une valeur numérique (entier) à la propriété [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la propriété [**zoom**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/zoom) pour définir le facteur de zoom de la première feuille de calcul du fichier Excel.

Le fichier book1.xls est ouvert en créant une instance de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Le facteur de zoom de la première feuille de calcul est défini à 75 et le fichier modifié est enregistré sous le nom de output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ZoomFactor-1.py" >}}

## **Figer les volets**

### **Utilisation de Microsoft Excel**

Les volets figés sont une fonctionnalité fournie par Microsoft Excel. Le fait de figer les volets vous permet de sélectionner des données à rester visibles lors du défilement dans une feuille de calcul.

### **Aspose.Cells & Les Volets Figés**

Aspose.Cells permet aux développeurs d'appliquer des volets figés sur des feuilles de calcul à l'exécution.

Aspose.Cells fournit une classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour configurer des volets figés, appelez la méthode [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) de la classe FeuilleDeCalcul. La méthode [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#int-int-int-int) prend les paramètres suivants :

- **ligne**, l'index de la ligne à partir de laquelle le gel commencera.
- **colonne**, l'index de la colonne à partir de laquelle le gel commencera.
- **lignes_gelées**, le nombre de lignes visibles dans le volet supérieur.
- **colonnes_gelées**, le nombre de colonnes visibles dans le volet de gauche.

Le fichier book1.xls est ouvert en appelant le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) lors de son instanciation et quelques lignes et colonnes sont figées dans la première feuille de calcul. Le fichier modifié est enregistré sous le nom de output.xls.

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [**freeze_panes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/freeze_panes/#str-int-int) pour figer des lignes et des colonnes (à partir de C4, représenté par la 4e ligne et la 3e colonne, où les lignes et les colonnes commencent à partir de l'index 0) de la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-FreezePanes-1.py" >}}

## **Diviser les volets**

Si vous avez besoin de diviser l'écran pour obtenir deux vues différentes dans la même feuille de calcul, utilisez la fonction de division des volets. Microsoft Excel propose une fonctionnalité très pratique qui vous permet de voir plus d'une copie de votre feuille de calcul, et de pouvoir faire défiler indépendamment chaque volet de votre feuille de calcul : diviser les volets.

Les volets fonctionnent simultanément. Si vous apportez une modification dans l'un, la modification apparaît simultanément dans l'autre. Aspose.Cells fournit la fonctionnalité de diviser les volets aux utilisateurs.

### **Application et Suppression des Volets Divisés**

#### **Division des Volets**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour implémenter des vues divisées, utilisez la méthode [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) de la classe [**split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/split). Pour supprimer les volets divisés, utilisez la méthode [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

Dans l'exemple, nous utilisons un fichier de modèle simple qui est chargé, puis la fonctionnalité de volets divisés est appliquée sur une cellule dans la première feuille de calcul. Le fichier mis à jour est enregistré.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-SplitPanes-1.py" >}}

Après l'exécution du code ci-dessus, le fichier généré aura une vue fractionnée.

#### **Suppression de volets**

Supprimer les volets fractionnés en utilisant la méthode [**remove_split**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/remove_split).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-RemovePanes-1.py" >}}

## **Sujets avancés**
- [Masquer l'affichage des valeurs nulles dans la feuille de calcul](/cells/fr/python-net/hiding-the-display-of-zero-values-in-the-worksheet/)
- [Définir la couleur d'onglet de feuille de calcul](/cells/fr/python-net/set-worksheet-tab-color/)
- [Afficher et masquer les quadrillages, les en-têtes de lignes et de colonnes](/cells/fr/python-net/show-and-hide-gridlines-and-row-column-headers/)
- [Afficher et masquer les lignes, les colonnes et les barres de défilement](/cells/fr/python-net/show-and-hide-rows-columns-and-scroll-bars/)
- [Afficher et masquer les feuilles de calcul et les onglets](/cells/fr/python-net/show-and-hide-worksheets-and-tabs/)
- [Afficher les formules au lieu des valeurs dans une feuille de calcul](/cells/fr/python-net/show-formulas-instead-of-values-in-a-worksheet/)
- [Utiliser les options de vérification des erreurs](/cells/fr/python-net/use-error-checking-options/)

