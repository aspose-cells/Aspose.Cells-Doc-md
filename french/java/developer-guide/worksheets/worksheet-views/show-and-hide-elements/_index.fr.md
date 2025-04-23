---
title: Afficher et masquer des éléments
type: docs
weight: 60
url: /fr/java/show-and-hide-elements/
---

{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris les feuilles de calcul, les lignes, les colonnes, les onglets, les barres de défilement, les lignes de quadrillage,

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

Un fichier Excel peut avoir une ou plusieurs feuilles de calcul. Lorsque nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Donc, **Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

**Contrôler la visibilité des feuilles de calcul :**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) offre une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Cependant, pour contrôler la visibilité d'une feuille de calcul, les développeurs peuvent utiliser la méthode [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Rendre une feuille de calcul visible**

Les développeurs peuvent rendre une feuille de calcul visible en passant **true** en tant que paramètre à la méthode [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Masquer une feuille de calcul**

Les développeurs peuvent masquer une feuille de calcul en passant **false** en tant que paramètre à la méthode [**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

**Exemple :**

Un exemple complet est donné ci-dessous qui montre comment utiliser la méthode [**setVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) pour masquer la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Feuille de calcul - Avant modification :**

Sur la capture d'écran ci-dessous, vous pouvez voir que le fichier **Book1.xls** contient trois feuilles de calcul : **Feuil1**, **Feuil2** et **Feuil3**.

![todo:image_alt_text](show-and-hide-elements_1.png)

**Figure:** Vue de la feuille de calcul avant toute modification

**Feuille de calcul - Après l'exécution du code d'exemple:**

Le fichier **Book1.xls** est ouvert en utilisant la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), puis la première feuille de calcul du fichier **Book1.xls** est rendue masquée. Le fichier modifié est enregistré sous le nom de **output.xls**, dont la vue picturale est montrée ci-dessous :

![todo:image_alt_text](show-and-hide-elements_2.png)

**Figure:** Vue de la feuille de calcul après modification

**Réglage du type de visibilité**

Vous pouvez également masquer les feuilles de calcul d'une manière spéciale. Cette fonctionnalité peut masquer la feuille de calcul de telle sorte que la seule façon de la rendre à nouveau visible est en donnant [**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY-HIDDEN) en tant que valeur de paramètre pour la méthode [**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) dans le code (il est à noter ici que les utilisateurs ne peuvent pas rendre l'objet visible dans MS Excel directement en utilisant ses options de menu). Les utilisateurs peuvent également utiliser la méthode [**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) pour vérifier si une feuille de calcul est marquée comme Très masqué ou non.

## **Afficher ou Masquer les onglets**

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:

- Onglets de feuille.
- Boutons de défilement d'onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.

**Onglets de feuille & boutons de défilement des onglets**

![todo:image_alt_text](show-and-hide-elements_3.png)

En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement dans les fichiers Excel.

**Contrôler la visibilité des onglets :**
Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fournit une vaste gamme de propriétés et de méthodes pour gérer un fichier Excel.

### **Masquage des onglets**

Masquer les onglets dans un fichier Excel en définissant la méthode [**getSettings().setShowTabs(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Rendre les onglets visibles**

Rendre les onglets visibles avec la méthode [**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Exemple de code complet :**

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls.

Vous pouvez voir que le fichier Book1.xls contient des onglets dans la figure ci-dessous. Après l'exécution du code d'exemple, les onglets sont cachés, comme vous pouvez le voir sur la capture d'écran du fichier output.xls ci-dessous.

**book1.xls : Fichier Excel avant toute modification**

![todo:image_alt_text](show-and-hide-elements_4.png)

**output.xls : Fichier Excel après modification**

![todo:image_alt_text](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Afficher et masquer les lignes et les colonnes**

Toutes les feuilles de calcul dans un fichier Excel sont composées de cellules qui sont disposées en lignes et colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier, ainsi que pour identifier les cellules individuelles. Par exemple, les lignes sont numérotées - 1, 2, 3, 4, etc. - et les colonnes sont ordonnées alphabétiquement - A, B, C, D, etc. Les valeurs de ligne et de colonne sont affichées dans les en-têtes. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces en-têtes de ligne et de colonne.

**Contrôler la visibilité des feuilles de calcul :**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe Worksheet fournit un large éventail de propriétés et de méthodes pour la gestion des feuilles de calcul. Pour contrôler la visibilité des en-têtes de ligne et de colonne, utilisez la méthode [**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la classe Worksheet.

### **Masquer les entêtes de ligne/colonne**

Masquez les en-têtes de ligne et de colonne en utilisant la méthode [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

### **Rendre les entêtes de ligne/colonne visibles**

Rendez les en-têtes de ligne et de colonne visibles en utilisant la méthode [**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

Un exemple complet est donné ci-dessous qui démontre comment utiliser la méthode [**setRowColumnHeadersVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) pour masquer les en-têtes de ligne et de colonne de la première feuille de calcul d'un fichier Excel.

La capture d'écran ci-dessous montre que le fichier Book1.xls contient trois feuilles de calcul : Feuil1, Feuil2 et Feuil3. Chaque feuille de calcul affiche les en-têtes de ligne et de colonne.

**Book1.xls : feuille de calcul avant modification**

![todo:image_alt_text](show-and-hide-elements_6.png)

Le fichier Book1.xls est ouvert en utilisant la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) et les en-têtes de ligne et de colonne sur la première feuille de calcul sont masqués. Le fichier modifié est enregistré sous le nom de output.xls.

**Vue de la feuille de calcul après la modification**

![todo:image_alt_text](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont très utilisées pour naviguer dans le contenu de n'importe quel fichier. En général, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel propose également des barres de défilement horizontales et verticales permettant aux utilisateurs de naviguer dans le contenu de la feuille de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

**Contrôler la visibilité des barres de défilement :**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fournit une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Cependant, pour contrôler la visibilité des barres de défilement dans le fichier Excel, les développeurs peuvent utiliser les méthodes [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) et [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

### **Masquer les barres de défilement**

Masquez les barres de défilement en définissant les méthodes [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) ou [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) sur **false**.

### **Rendre les barres de défilement visibles**

Rendez les barres de défilement visibles en définissant les méthodes [**setVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) ou [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) de la classe Workbook sur **true**.

**Exemple de code complet :**

Ci-dessous se trouve un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous le nom de output.xls.

La capture d'écran ci-dessous montre le fichier Book1.xls contenant les deux barres de défilement. Le fichier modifié est enregistré sous le nom de fichier output.xls, également montré ci-dessous.

**Book1.xls : Fichier Excel avant toute modification**

![todo:image_alt_text](show-and-hide-elements_8.png)

**output.xls : Fichier Excel après modification**

![todo:image_alt_text](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Afficher et masquer les quadrillages**

Toutes les feuilles de calcul de Microsoft Excel sont dotées par défaut de lignes de grille. Elles aident à délimiter les cellules, de sorte qu'il est facile d'entrer des données dans des cellules particulières. Les lignes de grille nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

Aspose.Cells vous permet également de contrôler la visibilité des lignes de grille.

### **Contrôler la visibilité des lignes de la grille**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient un [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité des lignes de grille, utilisez la méthode [**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Rendre les quadrillages visibles**

Pour rendre les lignes de la grille visibles, utilisez la méthode [**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

#### **Masquer les quadrillages**

Masquez les lignes de la grille en utilisant la méthode [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet).

{{% alert color="primary" %}}

Les lignes de la grille sont appliquées à l'ensemble de la feuille. Pour 'masquer' les lignes de la grille sur une partie d'une feuille de calcul, utilisez la [formatage des bordures](/cells/fr/java/create-table-by-using-border-lines-for-a-range/) pour définir les bordures à une couleur qui se fond dans le schéma de couleurs de la feuille.

{{% /alert %}}

**Exemple : Masquer les lignes de la grille sur une feuille de calcul particulière**

L'exemple ci-dessous démontre l'utilisation de la méthode [**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) pour masquer les lignes de la grille de la première feuille de calcul d'un fichier Excel.

La capture d'écran ci-dessous montre que le fichier Book1.xls contient trois feuilles de calcul : Feuil1, Feuil2 et Feuil3. Toutes ces feuilles de calcul ont des lignes de grille.

**Vue de la feuille de calcul avant la modification**

![todo:image_alt_text](show-and-hide-elements_10.png)

Le fichier Book1.xls est ouvert en utilisant la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) et ensuite les lignes de la grille de la première feuille de calcul sont masquées. Le fichier modifié est enregistré sous le nom de fichier output.xls.

**Vue de la feuille de calcul après la modification**

![todo:image_alt_text](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Articles connexes**

{{% alert color="primary" %}}

- [Fonctionnalités de mise en page](/cells/fr/java/page-setup-features/)
- [Ajouter des bordures aux cellules pour créer un tableau](/cells/fr/java/create-table-by-using-border-lines-for-a-range/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
