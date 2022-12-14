---
title: Afficher et masquer les éléments
type: docs
weight: 60
url: /fr/java/show-and-hide-elements/
---
{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur d'afficher et de masquer les éléments d'un classeur, notamment les feuilles de calcul, les lignes, les colonnes, les onglets, les barres de défilement, le quadrillage,

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

 Un fichier Excel peut contenir une ou plusieurs feuilles de calcul. Chaque fois que nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Alors,**Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

**Contrôle de la visibilité des feuilles de travail :**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel.[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Mais, pour contrôler la visibilité d'une feuille de calcul, les développeurs peuvent utiliser[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) méthode de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.

### **Rendre une feuille de calcul visible**

 Les développeurs peuvent rendre une feuille de calcul visible en passant**vrai** comme paramètre de la[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) méthode de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.

### **Masquer une feuille de calcul**

 Les développeurs peuvent masquer une feuille de calcul en passant**faux** comme paramètre de la[**setVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) méthode de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer.

**Exemple:**

 Un exemple complet est donné ci-dessous qui démontre l'utilisation de[**setVisible(faux)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsVisible) méthode de[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) class pour masquer la première feuille de calcul du fichier Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-HideUnhideWorksheet-1.java" >}}

**Feuille de travail - Avant modification :**

 Dans la capture d'écran ci-dessous, vous pouvez voir que**Livre1.xls** le fichier contient trois feuilles de calcul :**Feuille1** , **Feuille2** et**Feuille3** .

![tâche : image_autre_texte](show-and-hide-elements_1.png)

**Chiffre:** Vue feuille de calcul avant toute modification

**Feuille de travail - Après l'exécution de l'exemple de code :**

**Livre1.xls** le fichier est ouvert à l'aide de[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe, puis la première feuille de travail de la**Livre1.xls** le fichier est masqué. Le fichier modifié est enregistré sous**sortie.xls**fichier dont la vue picturale est présentée ci-dessous :

![tâche : image_autre_texte](show-and-hide-elements_2.png)

**Chiffre:** Affichage de la feuille de calcul après modification

**Définition du type de visibilité**

 Vous pouvez également masquer les feuilles de calcul d'une manière spéciale. Cette fonctionnalité peut masquer la feuille de calcul de sorte que la seule façon pour vous de la rendre à nouveau visible est de donner[**VisibilityType.VERY_HIDDEN**](https://reference.aspose.com/cells/java/com.aspose.cells/visibilitytype#VERY_HIDDEN) comme valeur de paramètre pour le[**setVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) méthode dans le code (il est à noter ici que l'utilisateur ne peut pas rendre l'objet visible directement dans MS Excel en utilisant ses options de menu). Les utilisateurs peuvent également utiliser[**getVisibilityType**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VisibilityType) méthode pour vérifier si une feuille de calcul est marquée comme VeryHidden ou non.

## **Afficher ou masquer les onglets**

Si vous regardez attentivement le bas d'un fichier Excel Microsoft, vous verrez un certain nombre de contrôles. Ceux-ci inclus:

- Onglets de feuille.
- Boutons de défilement des onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur n'importe quel onglet pour passer à cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel contient un bon nombre de feuilles de calcul, vous avez besoin de boutons pour les parcourir. Ainsi, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de la feuille.

**Onglets de feuille et boutons de défilement d'onglet**

![tâche : image_autre_texte](show-and-hide-elements_3.png)

À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement des onglets dans les fichiers Excel.

**Contrôle de la visibilité des onglets :**
 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel.

### **Masquer les onglets**

 Masquer les onglets dans un fichier Excel en définissant le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classer'[**getSettings().setShowTabs(faux)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

### **Rendre les onglets visibles**

 Rendre les onglets visibles avec le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classer'[**getSettings().setShowTabs(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#ShowTabs) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayTab-1.java" >}}

**Exemple de code complet :**

Vous trouverez ci-dessous un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous output.xls.

Vous pouvez voir que le fichier Book1.xls contient des onglets dans la figure ci-dessous. Une fois l'exemple de code exécuté, les onglets sont masqués, comme vous pouvez le voir sur la capture d'écran du fichier output.xls ci-dessous.

**book1.xls : fichier Excel avant toute modification**

![tâche : image_autre_texte](show-and-hide-elements_4.png)

**output.xls : fichier Excel après modification**

![tâche : image_autre_texte](show-and-hide-elements_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideTabs-1.java" >}}

## **Afficher et masquer les lignes et les colonnes**

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier des cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont classées par ordre alphabétique – A, B, C, D, etc. Les valeurs des lignes et des colonnes sont affichées dans les en-têtes. À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces en-têtes de ligne et de colonne.

**Contrôle de la visibilité des feuilles de travail :**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Excel Microsoft. La classe Workbook contient une WorksheetCollection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classer. La classe Worksheet fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité des en-têtes de ligne et de colonne, utilisez la classe Worksheet'[**setRowColumnHeadersVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) méthode.

### **Masquer les en-têtes de ligne/colonne**

 Masquez les en-têtes de ligne et de colonne à l'aide de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setRowColumnHeadersVisible(faux)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) méthode.

### **Rendre les en-têtes de ligne/colonne visibles**

 Rendre visibles les en-têtes de ligne et de colonne à l'aide de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setRowColumnHeadersVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) méthode.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setRowColumnHeadersVisible(faux)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsRowColumnHeadersVisible) méthode pour masquer les en-têtes de ligne et de colonne de la première feuille de calcul d'un fichier Excel.

La capture d'écran ci-dessous montre que Book1.xls contient trois feuilles de calcul : Sheet1, Sheet2 et Sheet3. Chaque feuille de calcul affiche des en-têtes de ligne et de colonne.

**Book1.xls : feuille de calcul avant modification**

![tâche : image_autre_texte](show-and-hide-elements_6.png)

 Book1.xls est ouvert en utilisant le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class' et les en-têtes de ligne et de colonne de la première feuille de calcul sont masqués. Le fichier modifié est enregistré sous output.xls.

**Affichage de la feuille de calcul après modification**

![tâche : image_autre_texte](show-and-hide-elements_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-HideUnhideWorksheet-1.java" >}}

## **Afficher et masquer les barres de défilement**

Les barres de défilement sont très utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel fournit également des barres de défilement horizontales et verticales permettant aux utilisateurs de faire défiler le contenu des feuilles de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

**Contrôle de la visibilité des barres de défilement :**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel.[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Mais, pour contrôler la visibilité des barres de défilement dans le fichier Excel, les développeurs peuvent utiliser[**setVScrollBarVisiblesetVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) & [**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) méthodes de la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classer.

### **Masquer les barres de défilement**

 Masquez les barres de défilement en définissant le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classer'[**setVScrollBarVisiblesetVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) ou[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) méthodes pour**faux**.

### **Rendre les barres de défilement visibles**

 Rendre les barres de défilement visibles en définissant la classe Workbook'[**setVScrollBarVisiblesetVScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsVScrollBarVisible) ou[**setHScrollBarVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#IsHScrollBarVisible) méthodes pour**vrai**.

**Exemple de code complet :**

Vous trouverez ci-dessous un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous output.xls.

La capture d'écran ci-dessous montre le fichier Book1.xls contenant les deux barres de défilement. Le fichier modifié est enregistré en tant que fichier output.xls, également affiché ci-dessous.

**Book1.xls : fichier Excel avant toute modification**

![tâche : image_autre_texte](show-and-hide-elements_8.png)

**output.xls : fichier Excel après modification**

![tâche : image_autre_texte](show-and-hide-elements_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-display-DisplayHideScrollBars-1.java" >}}

## **Afficher et masquer le quadrillage**

Toutes les feuilles de calcul Excel Microsoft ont un quadrillage par défaut. Ils aident à délimiter les cellules, de sorte qu'il est facile d'entrer des données dans des cellules particulières. Le quadrillage nous permet de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

Aspose.Cells vous permet également de contrôler la visibilité du quadrillage.

### **Contrôle de la visibilité des quadrillages**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) qui permet d'accéder à chaque feuille de calcul du fichier.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité des lignes de grille, utilisez le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setGridlinesVisible**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) méthode.

#### **Rendre le quadrillage visible**

 Pour rendre le quadrillage visible, utilisez le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setGridlinesVisible(true)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) méthode.

#### **Masquer le quadrillage**

 Masquer le quadrillage à l'aide de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) méthode.

{{% alert color="primary" %}}

Le quadrillage s'applique à l'ensemble de la feuille. Pour "masquer" le quadrillage d'une section d'une feuille de calcul, utilisez[formatage des bordures](/cells/fr/java/create-table-by-using-border-lines-for-a-range/) pour définir les bordures sur une couleur qui se fond dans le jeu de couleurs de la feuille.

{{% /alert %}}

**Exemple : Masquer le quadrillage d'une feuille de calcul particulière**

 L'exemple ci-dessous illustre l'utilisation de[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer'[**setGridlinesVisible(false)**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#IsGridlinesVisible) méthode pour masquer le quadrillage de la première feuille de calcul d'un fichier Excel.

La capture d'écran ci-dessous montre que le fichier Book1.xls contient trois feuilles de calcul : Sheet1, Sheet2 et Sheet3. Toutes ces feuilles de travail ont un quadrillage.

**Vue feuille de calcul avant modification**

![tâche : image_autre_texte](show-and-hide-elements_10.png)

 Le fichier Book1.xls est ouvert à l'aide de la[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) class, puis le quadrillage de la première feuille de calcul sont masqués. Le fichier modifié est enregistré en tant que fichier output.xls.

**Affichage de la feuille de calcul après modification**

![tâche : image_autre_texte](show-and-hide-elements_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-DisplayHideGridlines-DisplayHideGridlines.java" >}}

### **Articles Liés**

{{% alert color="primary" %}}

- [Fonctionnalités de mise en page](/cells/fr/java/page-setup-features/).
- [Ajouter des bordures aux cellules pour créer un tableau](/cells/fr/java/create-table-by-using-border-lines-for-a-range/).

{{% /alert %}}
