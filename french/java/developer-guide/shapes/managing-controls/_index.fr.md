---
title: Gestion des contrôles
type: docs
weight: 120
url: /fr/java/managing-controls/
---
## **Introduction**

Les développeurs peuvent ajouter différents objets de dessin tels que des zones de texte, des cases à cocher, des boutons radio, des zones de liste déroulante, des étiquettes, des boutons, des lignes, des rectangles, des arcs, des ovales, des compteurs, des barres de défilement, des zones de groupe, etc. Aspose.Cells fournit l'espace de noms Aspose.Cells.Drawing qui contient tous les objets de dessin. Cependant, certains objets ou formes de dessin ne sont pas encore pris en charge. Créez ces objets de dessin dans une feuille de calcul de concepteur à l'aide de Microsoft Excel, puis importez la feuille de calcul de concepteur dans Aspose.Cells. Aspose.Cells vous permet de charger ces objets de dessin à partir d'une feuille de calcul de concepteur et de les écrire dans un fichier généré.

## **Ajout du contrôle TextBox à la feuille de calcul**

 Une façon de souligner les informations importantes dans un rapport consiste à utiliser une zone de texte. Par exemple, ajoutez du texte pour mettre en surbrillance le nom de l'entreprise ou pour indiquer la région géographique avec les ventes les plus élevées, etc. Aspose.Cells fournit la classe TextBoxes, utilisée pour ajouter une nouvelle zone de texte à la collection. Il y a une autre classe,[**Zone de texte**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox)qui représente une zone de texte utilisée pour définir tous les types de paramètres. Il compte quelques membres importants :

-  Le[**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) méthode renvoie un[**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) objet utilisé pour ajuster le contenu de la zone de texte.
-  Le[**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) La méthode spécifie le type de placement.
-  Le[**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) La méthode spécifie les attributs de la police.
-  Le[**ajouterHyperlien**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink(java.lang.String)) ajoute un lien hypertexte pour la zone de texte.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) retours de propriété[**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) objet utilisé pour définir le format de remplissage de la zone de texte.
-  Le[**Format de ligne**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) la propriété renvoie le[**MsoLineFormatMsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) objet généralement utilisé pour le style et l'épaisseur de la ligne de la zone de texte.
-  Le[**Définir le texte**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) La méthode spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien fournie avec différents paramètres de format. La seconde est simple.

La sortie suivante est générée en exécutant le code :

**Deux zones de texte sont créées dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul Designer**

 Aspose.Cells vous permet également d'accéder aux zones de texte dans les feuilles de travail du concepteur et de les manipuler. Utilisez le[**Feuille de calcul.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) propriété pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Excel Microsoft - tsttextboxes.xls - que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et modifie le texte de la deuxième zone de texte pour enregistrer le fichier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Ajout du contrôle CheckBox à la feuille de calcul**

Les cases à cocher sont pratiques si vous souhaitez permettre à un utilisateur de choisir entre deux options, telles que vrai ou faux ; Oui ou non. Aspose.Cells vous permet d'utiliser des cases à cocher dans les feuilles de calcul. Par exemple, vous avez peut-être développé une feuille de calcul de projection financière dans laquelle vous pouvez comptabiliser ou non une acquisition particulière. Dans ce cas, vous pouvez placer une case à cocher en haut de la feuille de calcul. Vous pouvez ensuite lier l'état de cette case à cocher à une autre cellule, de sorte que si la case est cochée, la valeur de la cellule est True ; si elle n'est pas sélectionnée, la valeur de la cellule est Faux.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de case à cocher dans votre feuille de calcul, procédez comme suit :

1. Assurez-vous que la barre d'outils Formulaires est affichée.
1.  Clique le**Case à cocher** outil de la barre d'outils Formulaires.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra la case à cocher et l'étiquette à côté de la case à cocher.
1. Une fois la case à cocher placée, déplacez le curseur de la souris dans la zone d'étiquette et modifiez l'étiquette.
1.  Dans le**Cell Lien** spécifiez l'adresse de la cellule à laquelle cette case à cocher doit être liée.
1.  Cliquer sur**D'ACCORD**.

### **En utilisant Aspose.Cells**

 Aspose.Cells fournit le[**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection) class, qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il y a une autre classe,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), qui représente une case à cocher. Il compte quelques membres importants :

-  Le[**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) La méthode spécifie une cellule qui est liée à la case à cocher.
-  Le[**Définir le texte**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) La méthode spécifie la chaîne de texte associée à la case à cocher. C'est l'étiquette de la case à cocher.
-  Le[**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) La méthode spécifie si la case est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul. La sortie ci-dessous est générée après l'exécution du code.

**Une case à cocher est ajoutée dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Ajout du contrôle RadioButton à la feuille de calcul**

Un bouton radio, ou un bouton d'option, est un contrôle constitué d'une case ronde. L'utilisateur prend sa décision en sélectionnant la case ronde. Un bouton radio est généralement, sinon toujours, accompagné d'autres. Ces boutons radio apparaissent et se comportent comme un groupe. L'utilisateur décide quel bouton est valide en n'en sélectionnant qu'un seul. Lorsque l'utilisateur clique sur un bouton, celui-ci est rempli. Lorsqu'un bouton du groupe est sélectionné, les boutons du même groupe sont vides.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle Bouton radio dans votre feuille de calcul, procédez comme suit :

1.  Assurez-vous que le**Formes** barre d'outils s'affiche.
1.  Clique le**Bouton d'option** outil.
1. Dans la feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le bouton d'option et l'étiquette à côté du bouton d'option.
1. Une fois le bouton radio placé dans la feuille de calcul, déplacez le curseur de la souris dans la zone d'étiquette et modifiez l'étiquette.
1.  Dans le**Cell Lien** champ, indiquez l'adresse de la cellule à laquelle ce bouton radio doit être lié.
1.  Cliquez sur**D'ACCORD**.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)La classe fournit une méthode nommée addShape qui peut être utilisée pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode peut renvoyer un objet RadioButton. La classe RadioButton représente un bouton d'option. Il compte quelques membres importants :

- La méthode setLinkedCell spécifie une cellule qui est liée au bouton radio.
- La méthode setText spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
- La propriété Checked spécifie si le bouton radio est coché ou non.
- La méthode setFillFormat spécifie le format de remplissage du bouton radio.
- La méthode setLineFormat spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des tranches d'âge. La sortie suivante serait générée après l'exécution du code.

**Certains RadioButtons sont ajoutés dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Ajout d'un contrôle Combo Box à une feuille de calcul**

Pour faciliter la saisie de données ou pour limiter les entrées à certains éléments que vous définissez, vous pouvez créer une zone de liste déroulante ou une liste déroulante d'entrées valides compilées à partir de cellules situées ailleurs sur la feuille de calcul. Lorsque vous créez une liste déroulante pour une cellule, elle affiche une flèche à côté de cette cellule. Pour entrer des informations dans cette cellule, cliquez sur la flèche, puis cliquez sur l'entrée souhaitée.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de zone de liste déroulante dans votre feuille de calcul, procédez comme suit :

1.  Assurez-vous que le**Formes** barre d'outils s'affiche.
1.  Clique sur le**Boîte combo** outil.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra la zone de liste déroulante.
1.  Une fois la zone de liste déroulante placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle pour cliquer sur**Contrôle des formats** et spécifiez la plage d'entrée.
1.  Dans le**Cell Lien** champ, indiquez l'adresse de la cellule à laquelle cette combo box doit être liée.
1.  Cliquer sur**D'ACCORD**.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)La classe fournit une méthode nommée addShape, qui peut être utilisée pour ajouter un contrôle de zone de liste déroulante à la feuille de calcul. La méthode peut renvoyer un objet ComboBox. La classe ComboBox représente une zone de liste déroulante. Il compte quelques membres importants :

- La méthode setLinkedCell spécifie une cellule qui est liée à la zone de liste déroulante.
- La méthode setInputRange spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la zone de liste déroulante.
- La méthode setDropDownLines spécifie le nombre de lignes de liste affichées dans la partie déroulante d'une zone de liste déroulante.
- La méthode setShadow indique si la zone de liste déroulante a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de liste déroulante à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Une zone de liste déroulante est ajoutée dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Ajout d'un contrôle d'étiquette à une feuille de calcul**

 Les étiquettes sont un moyen de fournir aux utilisateurs des informations sur le contenu d'une feuille de calcul. Aspose.Cells permet d'ajouter et de manipuler des étiquettes dans une feuille de calcul. Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)La classe fournit une méthode nommée addShape, utilisée pour ajouter un contrôle d'étiquette à la feuille de calcul. La méthode renvoie un objet Label. La classe Label représente une étiquette dans la feuille de calcul. Il compte quelques membres importants :

- La méthode setText spécifie la chaîne de légende d'une étiquette.
- La méthode setPlacement spécifie le PlacementType, la manière dont l'étiquette est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter une étiquette à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Une étiquette est ajoutée dans la feuille de calcul**

![tâche : image_autre_texte](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Ajout d'un contrôle de zone de liste à une feuille de calcul**

Un contrôle de zone de liste crée un contrôle de liste qui permet la sélection d'un ou plusieurs éléments.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de zone de liste dans une feuille de calcul :

1.  Assurez-vous que le**Formes** barre d'outils s'affiche.
1.  Clique sur le**Zone de liste** outil.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra la zone de liste.
1.  Une fois la zone de liste placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle pour cliquer sur**Contrôle des formats** et spécifiez la plage d'entrée.
1.  Dans le**Cell Lien**champ, indiquez l'adresse de la cellule à laquelle cette list box doit être liée et définissez l'attribut type de sélection (Single, Multi, Extend)
1.  Cliquez sur**D'ACCORD**.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) La classe fournit une méthode nommée addShape, qui est utilisée pour ajouter un contrôle de zone de liste à une feuille de calcul. La méthode renvoie un objet ListBox. La classe ListBox représente une zone de liste. Il compte quelques membres importants :

- La méthode setLinkedCell spécifie une cellule qui est liée à la zone de liste.
- La méthode setInputRange spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la zone de liste.
- La méthode setSelectionType spécifie le mode de sélection de la zone de liste.
- La méthode setShadow indique si la zone de liste a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de liste à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Une zone de liste est ajoutée dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Ajout d'un contrôle de bouton à une feuille de calcul**

Les boutons sont utiles pour effectuer certaines actions. Parfois, il est utile d'attribuer une macro VBA au bouton ou d'attribuer un lien hypertexte pour ouvrir une page Web.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de bouton dans votre feuille de calcul :

1.  Assurez-vous que le**Formes** barre d'outils s'affiche.
1.  Clique sur le**Bouton** outil.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le bouton.
1.  Une fois la zone de liste placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle et sélectionnez**Contrôle des formats**, puis spécifiez une macro VBA et les attributs liés à la police, l'alignement, la taille, la marge, etc.
1.  Cliquer sur**D'ACCORD**.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) La classe fournit une méthode nommée addShape, utilisée pour ajouter un contrôle de bouton à la feuille de calcul. La méthode peut renvoyer un objet Button. La classe Button représente un bouton. Il compte quelques membres importants :

- La méthode setText spécifie la légende du bouton.
- La méthode setPlacement spécifie le PlacementType, la façon dont le bouton est attaché aux cellules de la feuille de calcul.
- La méthode addHyperlink ajoute un lien hypertexte pour le contrôle de bouton. Cliquez sur le bouton pour accéder à l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code

**Un bouton est ajouté dans la feuille de calcul**

![tâche : image_autre_texte](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Ajout d'un contrôle de ligne à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes automatiques dans vos feuilles de calcul. Vous pouvez facilement créer une ligne. Vous êtes également autorisé à formater la ligne. Par exemple, vous pouvez modifier la couleur de la ligne, spécifier l'épaisseur et le style de la ligne selon vos besoins.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Formes automatiques** , pointer vers**Lignes**, puis sélectionnez le style de ligne souhaité.
1. Faites glisser pour tracer la ligne.
1. Effectuez l'une des actions suivantes ou les deux :
 1. Pour contraindre la ligne à tracer à des angles de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
 1. Pour allonger la ligne dans des directions opposées à partir du premier point d'extrémité, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection)La classe fournit une méthode nommée addShape, qui est utilisée pour ajouter une forme de ligne à la feuille de calcul. La méthode peut renvoyer un objet LineShape. La classe LineShape représente une ligne. Il compte quelques membres importants :

- La méthode setDashStyle spécifie le format d'une ligne.
- La méthode setPlacement spécifie le PlacementType, la façon dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec des styles différents. La sortie suivante est générée après l'exécution du code

**Quelques lignes sont ajoutées dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Ajouter une pointe de flèche à une ligne**

Aspose.Cells vous permet également de tracer des lignes fléchées. Il est possible d'ajouter une pointe de flèche à une ligne, et de formater la ligne. Par exemple, vous pouvez modifier la couleur de la ligne ou spécifier l'épaisseur et le style de la ligne.

L'exemple suivant montre comment ajouter une pointe de flèche à une ligne. La sortie suivante est générée lors de l'exécution du code.

**Une ligne avec une pointe de flèche est ajoutée dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Ajout d'un contrôle Rectangle à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes rectangulaires dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous êtes également autorisé à formater la couleur de remplissage et la couleur de la bordure du contrôle. Par exemple, vous pouvez modifier la couleur du rectangle, définir la couleur d'ombrage, spécifier l'épaisseur et le style du rectangle selon vos besoins.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Effectuez l'une des actions suivantes ou les deux :
 1. Pour contraindre le rectangle à dessiner un carré à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
 1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) La classe fournit une méthode nommée addShape, qui est utilisée pour ajouter une forme de rectangle à une feuille de calcul. La méthode peut renvoyer un objet RectangleShape. La classe RectangleShape représente un rectangle. Il compte quelques membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'un rectangle.
- La méthode setPlacement spécifie le PlacementType, la façon dont le rectangle est attaché aux cellules de la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Un rectangle est ajouté dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Ajout du contrôle d'arc à la feuille de travail**

Aspose.Cells vous permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et pleins. Vous êtes autorisé à formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / modifier la couleur de l'arc, définir la couleur d'ombrage, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Arc** dans le**Formes automatiques**.
1. Faites glisser pour dessiner l'arc.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) La classe fournit une méthode nommée addShape, qui est utilisée pour ajouter une forme d'arc à la feuille de calcul. La méthode peut renvoyer un objet ArcShape. La classe ArcShape représente un arc. Il compte quelques membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'une forme d'arc.
- La méthode setPlacement spécifie le PlacementType, la manière dont l'arc est attaché aux cellules de la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage de la forme.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : l'une est remplie et l'autre est simple. La sortie suivante est générée lors de l'exécution du code

**Deux formes d'arc sont ajoutées à la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Ajout d'un contrôle ovale à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes ovales dans des feuilles de calcul. Créez des formes ovales simples et remplies et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / modifier la couleur de l'ovale, définir la couleur d'ombrage, spécifier le poids et le style de la forme.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**ovale** .
1. Faites glisser pour dessiner l'ovale.
1. Effectuez l'une des actions suivantes ou les deux :
 1. Pour contraindre l'ovale à dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
1. Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) La classe fournit une méthode nommée addShape, qui est utilisée pour ajouter une forme ovale à une feuille de calcul. La méthode peut renvoyer un objet Oval. La classe Oval représente une forme ovale. Il compte quelques membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'une forme ovale.
-  La méthode setPlacement spécifie le**Type d'emplacement** , la manière dont l'ovale est attaché aux cellules de la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage de la forme.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : l'une est un ovale rempli, l'autre est un simple cercle. La sortie suivante est générée lors de l'exécution du code.

**Deux formes ovales sont ajoutées dans la feuille de calcul** 

![tâche : image_autre_texte](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Sujets avancés**
- [Ajouter des contrôles ActiveX à l'aide de Aspose.Cells](/cells/fr/java/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/java/remove-activex-control/)
