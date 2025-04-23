---
title: Gestion des contrôles
type: docs
weight: 120
url: /fr/java/managing-controls/
---

## **Introduction**

Les développeurs peuvent ajouter différents objets graphiques tels que des zones de texte, des cases à cocher, des boutons radio, des listes déroulantes, des étiquettes, des boutons, des lignes, des rectangles, des arcs, des ovales, des curseurs, des barres de défilement, des cadres, etc. Aspose.Cells fournit l'espace de noms Aspose.Cells.Drawing qui contient tous les objets graphiques. Cependant, il existe quelques objets graphiques ou formes qui ne sont pas encore pris en charge. Créez ces objets graphiques dans une feuille de calcul de concepteur à l'aide de Microsoft Excel, puis importez la feuille de calcul de concepteur dans Aspose.Cells. Aspose.Cells vous permet de charger ces objets graphiques à partir d'une feuille de calcul de concepteur et de les écrire dans un fichier généré.

## **Ajout de contrôle de zone de texte à la feuille de calcul**

Une façon de mettre en évidence les informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, ajoutez du texte pour mettre en évidence le nom de l'entreprise ou pour indiquer la région géographique avec les ventes les plus élevées, etc. Aspose.Cells fournit la classe TextBoxes, utilisée pour ajouter une nouvelle zone de texte à la collection. Il y a une autre classe, [**TextBox**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox), qui représente une zone de texte utilisée pour définir tous types de paramètres. Elle a quelques membres importants :

- La méthode [**getTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#TextFrame) renvoie un objet [**MsoTextFrame**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoTextFrame) utilisé pour ajuster le contenu de la zone de texte.
- La méthode [**setPlacement**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Placement) spécifie le type de placement.
- La méthode [**setFont**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Font) spécifie les attributs de police.
- La méthode [**addHyperlink**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#addHyperlink-java.lang.String-) ajoute un lien hypertexte pour la zone de texte.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#FillFormat) renvoie un objet [**MsoFillFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoFillFormat) utilisé pour définir le format de remplissage de la zone de texte.
- La propriété [**LineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#LineFormat) renvoie un objet [**MsoLineFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/MsoLineFormat) généralement utilisé pour le style et le poids de la ligne de la zone de texte.
- La méthode [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/textbox#Text) spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien aménagée avec différents paramètres de format. La seconde est plus simple.

La sortie suivante est générée en exécutant le code :

**Deux zones de texte sont créées dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingTextBoxControl-1.java" >}}

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul du concepteur**

Aspose.Cells vous permet également d'accéder aux zones de texte dans les feuilles de calcul du concepteur et de les manipuler. Utilisez la propriété [**Worksheet.getTextBoxes**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#TextBoxes) pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Microsoft Excel - tsttextboxes.xls - que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et change le texte de la deuxième zone de texte pour enregistrer le fichier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-ManipulatingTextBoxControls-1.java" >}}

## **Ajout du contrôle de case à cocher dans la feuille de calcul**

Les cases à cocher sont pratiques si vous souhaitez fournir un moyen à l'utilisateur de choisir entre deux options, telles que vrai ou faux; oui ou non. Aspose.Cells vous permet d'utiliser des cases à cocher dans les feuilles de calcul. Par exemple, vous pouvez avoir développé une feuille de calcul de projection financière dans laquelle vous pouvez soit tenir compte d'une acquisition particulière, soit non. Dans ce cas, vous voudrez peut-être placer une case à cocher en haut de la feuille de calcul. Vous pouvez ensuite lier l'état de cette case à cocher à une autre cellule, de sorte que si la case à cocher est sélectionnée, la valeur de la cellule est Vrai; si elle n'est pas sélectionnée, la valeur de la cellule est Faux.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de case à cocher dans votre feuille de calcul, suivez ces étapes:

1. Assurez-vous que la barre d'outils Formulaires est affichée.
1. Cliquez sur l'outil **Case à cocher** dans la barre d'outils Formulaires.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra la case à cocher et l'étiquette à côté de la case à cocher.
1. Une fois la case à cocher placée, déplacez le curseur de la souris dans la zone de l'étiquette et modifiez l'étiquette.
1. Dans le champ **Lien de la cellule**, spécifiez l'adresse de la cellule à laquelle cette case à cocher doit être liée.
1. Cliquez sur **OK**.

### **Utilisation d'Aspose.Cells**

Aspose.Cells fournit la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/checkboxcollection), qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il existe une autre classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/java/com.aspose.cells/CheckBox), qui représente une case à cocher. Elle a quelques membres importants:

- La méthode [**setLinkedCell**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#LinkedCell) spécifie une cellule liée à la case à cocher.
- La méthode [**setText**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Text) spécifie la chaîne de texte associée à la case à cocher. C'est l'étiquette de la case à cocher.
- La méthode [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/checkbox#Value) spécifie si la case à cocher est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul. La sortie ci-dessous est générée après l'exécution du code.

**Une case à cocher est ajoutée dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingCheckBoxControl-1.java" >}}

## **Ajout du contrôle de bouton radio à la feuille de calcul**

Un bouton radio, ou un bouton d'option, est un contrôle constitué d'une case ronde. L'utilisateur prend sa décision en sélectionnant la case ronde. Un bouton radio est généralement, sinon toujours, accompagné d'autres boutons. Ces boutons radio semblent et se comportent comme un groupe. L'utilisateur décide quel bouton est valide en ne sélectionnant qu'un seul d'entre eux. Lorsque l'utilisateur clique sur un bouton, il est rempli. Lorsqu'un bouton du groupe est sélectionné, les boutons du même groupe sont vides.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de bouton radio dans votre feuille de calcul, suivez ces étapes:

1. Assurez-vous que la barre d'outils **Formulaires** est affichée.
1. Cliquez sur l'outil **Bouton d'option**.
1. Dans la feuille de calcul, cliquez et faites glisser pour définir le rectangle qui va contenir le bouton d'option et l'étiquette à côté du bouton d'option.
1. Une fois le bouton radio placé dans la feuille de calcul, déplacez le curseur de la souris dans la zone d'étiquette et modifiez l'étiquette.
1. Dans le champ **Lien de la cellule**, spécifiez l'adresse de la cellule à laquelle ce bouton radio doit être lié.
1. Cliquez sur **OK**.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape qui peut être utilisée pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode peut renvoyer un objet RadioButton. La classe RadioButton représente un bouton d’option. Elle possède certains membres importants :

- La méthode setLinkedCell spécifie une cellule liée au bouton radio.
- La méthode setText spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
- La propriété Checked spécifie si le bouton radio est coché ou non.
- La méthode setFillFormat spécifie le format de remplissage du bouton radio.
- La méthode setLineFormat spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des groupes d'âge. La sortie suivante serait générée après l'exécution du code.

**Certains boutons radio sont ajoutés dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRadioButtonControl-1.java" >}}

## **Ajout de contrôle de liste déroulante à une feuille de calcul**

Pour faciliter la saisie de données, ou pour limiter les entrées à certains éléments que vous définissez, vous pouvez créer une liste déroulante, ou une liste déroulante des entrées valides qui sont compilées à partir de cellules ailleurs dans la feuille de calcul. Lorsque vous créez une liste déroulante pour une cellule, une flèche s'affiche à côté de cette cellule. Pour entrer des informations dans cette cellule, cliquez sur la flèche, puis cliquez sur l'entrée que vous souhaitez.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de liste déroulante dans votre feuille de calcul, suivez ces étapes :

1. Assurez-vous que la barre d'outils **Formulaires** est affichée.
1. Cliquez sur l'outil **Liste déroulante**.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui va contenir la liste déroulante.
1. Une fois la liste déroulante placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle pour cliquer sur **Format du contrôle** et spécifiez la plage d'entrée.
1. Dans le champ **Lien de la cellule**, spécifiez l'adresse de la cellule à laquelle cette liste déroulante doit être liée.
1. Cliquez sur **OK**.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape, qui peut être utilisée pour ajouter un contrôle de liste déroulante à la feuille de calcul. La méthode peut renvoyer l'objet ComboBox. La classe ComboBox représente une liste déroulante. Elle possède certains membres importants :

- La méthode setLinkedCell spécifie une cellule liée à la liste déroulante.
- La méthode setInputRange spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La méthode setDropDownLines spécifie le nombre de lignes de liste affichées dans la partie déroulante d'une liste déroulante.
- La méthode setShadow indique si la liste déroulante a un ombrage 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Une liste déroulante est ajoutée dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingComboBoxControl-1.java" >}}

## **Ajout de contrôle de libellé à une feuille de calcul**

Les libellés sont un moyen de fournir aux utilisateurs des informations sur le contenu d'une feuille de calcul. Aspose.Cells permet d'ajouter et de manipuler des libellés dans une feuille de calcul. La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape, utilisée pour ajouter un contrôle de libellé à la feuille de calcul. La méthode renvoie un objet Label. La classe Label représente un libellé dans la feuille de calcul. Elle possède certains membres importants :

- La méthode setText spécifie une chaîne de légende d'un libellé.
- La méthode setPlacement spécifie le type de placement, la manière dont le libellé est attaché aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter un libellé à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Un libellé est ajouté dans la feuille de calcul**

![todo:image_alt_text](managing-controls_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLabelControl-1.java" >}}

## **Ajout de contrôle de liste à une feuille de calcul**

Un contrôle de liste crée un contrôle de liste qui permet de sélectionner un ou plusieurs éléments.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de liste dans une feuille de calcul :

1. Assurez-vous que la barre d'outils **Formulaires** est affichée.
1. Cliquez sur l'outil **Liste déroulante**.
1. Dans la zone de votre feuille de calcul, cliquez et faites glisser pour définir le rectangle qui va contenir la liste déroulante.
1. Une fois la liste déroulante placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle pour cliquer sur **Format du contrôle** et spécifier la plage de saisie.
1. Dans le champ **Lien de cellule**, spécifiez l'adresse de la cellule à laquelle cette liste déroulante doit être liée et définissez l'attribut de type de sélection (Simple, Multiple, Étendue).
1. Cliquez sur **OK**.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape, qui est utilisée pour ajouter un contrôle de liste à une feuille de calcul. La méthode renvoie un objet ListBox. La classe ListBox représente une liste. Elle possède certains membres importants :

- La méthode setLinkedCell spécifie une cellule liée à la liste.
- La méthode setInputRange spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste.
- La méthode setSelectionType spécifie le mode de sélection de la liste déroulante.
- La méthode setShadow indique si la liste déroulante a un ombrage en 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Une liste déroulante est ajoutée à la feuille de calcul** 

![todo:image_alt_text](managing-controls_6.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingListBoxControl-1.java" >}}

## **Ajout d'un contrôle de bouton à une feuille de calcul**

Les boutons sont utiles pour effectuer des actions. Parfois, il est utile d'attribuer une macro VBA au bouton ou d'assigner un lien hypertexte pour ouvrir une page web.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de bouton dans votre feuille de calcul :

1. Assurez-vous que la barre d'outils **Formulaires** est affichée.
1. Cliquez sur l'outil **Bouton**.
1. Dans la zone de votre feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le bouton.
1. Une fois la liste déroulante placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle et sélectionnez **Format de contrôle**, puis spécifiez une macro VBA et des attributs liés à la police, à l'alignement, à la taille, à la marge, etc.
1. Cliquez sur **OK**.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape, utilisée pour ajouter un contrôle de bouton à la feuille de calcul. La méthode peut renvoyer un objet Button. La classe Button représente un bouton. Elle possède quelques membres importants :

- La méthode setText spécifie la légende du bouton.
- La méthode setPlacement spécifie le PlacementType, la manière dont le bouton est attaché aux cellules de la feuille de calcul.
- La méthode addHyperlink ajoute un lien hypertexte pour le contrôle de bouton. En cliquant sur le bouton, vous serez redirigé vers l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Un bouton est ajouté à la feuille de calcul**

![todo:image_alt_text](managing-controls_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingButtonControl-1.java" >}}

## **Ajout de contrôle de ligne à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes automatiques dans vos feuilles de calcul. Vous pouvez créer une ligne facilement. Vous pouvez également formater la ligne. Par exemple, vous pouvez changer la couleur de la ligne, spécifier l'épaisseur et le style de la ligne selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Formes automatiques**, pointez sur **Lignes**, et sélectionnez le style de ligne désiré.
1. Faites glisser pour dessiner la ligne.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre la ligne à être dessinée selon un angle de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée pendant le glissement.
   1. Pour allonger la ligne dans des directions opposées depuis le premier point d'extrémité, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode nommée addShape, utilisée pour ajouter une forme de ligne à la feuille de calcul. La méthode peut renvoyer un objet LineShape. La classe LineShape représente une ligne. Elle possède quelques membres importants :

- La méthode setDashStyle spécifie le format d'une ligne.
- La méthode setPlacement spécifie le PlacementType, la manière dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec différents styles. La sortie suivante est générée après l'exécution du code.

**Quelques lignes sont ajoutées à la feuille de calcul** 

![todo:image_alt_text](managing-controls_8.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingLineControl-1.java" >}}

### **Ajout d'une pointe de flèche à une ligne**

Aspose.Cells vous permet également de dessiner des lignes fléchées. Il est possible d'ajouter une tête de flèche à une ligne et de formater la ligne. Par exemple, vous pouvez changer la couleur de la ligne ou spécifier l'épaisseur et le style de la ligne.

L'exemple suivant montre comment ajouter une pointe de flèche à une ligne. La sortie suivante est générée lors de l'exécution du code.

**Une ligne avec une pointe de flèche est ajoutée à la feuille de calcul** 

![todo:image_alt_text](managing-controls_9.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganArrowHead.java" >}}

## **Ajout d'un contrôle de rectangle dans une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes de rectangle dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous avez également la possibilité de formater la couleur de remplissage et la couleur de la ligne de contrôle. Par exemple, vous pouvez changer la couleur du rectangle, définir la couleur de l'ombrage, spécifier le poids et le style du rectangle selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre le rectangle à dessiner un carré depuis son point de départ, maintenez la touche SHIFT enfoncée pendant le glissement.
   1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode appelée addShape, qui est utilisée pour ajouter une forme de rectangle à une feuille de calcul. La méthode peut renvoyer un objet RectangleShape. La classe RectangleShape représente un rectangle. Elle possède certains membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'un rectangle.
- La méthode setPlacement spécifie le PlacementType, la manière dont le rectangle est attaché aux cellules dans la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul. La sortie suivante est générée lors de l'exécution du code.

**Un rectangle est ajouté dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_10.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingRectangleControl-1.java" >}}

## **Ajout du Contrôle Arc à la Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et pleins. Vous pouvez formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'arc, définir la couleur de dégradé, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Arc** dans les **Formes Automatiques**.
1. Faites glisser pour dessiner l'arc.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode appelée addShape, qui est utilisée pour ajouter une forme d'arc à la feuille de calcul. La méthode peut renvoyer un objet ArcShape. La classe ArcShape représente un arc. Elle possède certains membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'une forme d'arc.
- La méthode setPlacement spécifie le PlacementType, la manière dont l'arc est attaché aux cellules dans la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage de la forme.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : une remplie et l'autre simple. La sortie suivante est générée lors de l'exécution du code

**Deux formes d'arc sont ajoutées à la feuille de calcul** 

![todo:image_alt_text](managing-controls_11.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddingArcControl-1.java" >}}

## **Ajout du Contrôle Ovale à une Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes ovales dans les feuilles de calcul. Créez des formes ovales simples et pleines et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'ovale, définir la couleur de dégradé, spécifier le poids et le style de la forme.

### **Utilisation de Microsoft Excel**

1. Dans la barre d'outils **Dessin**, cliquez sur **Ovale**.
1. Faites glisser pour dessiner l'ovale.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre l'ovale à dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée pendant le glissement.
   1. Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection) fournit une méthode appelée addShape, qui est utilisée pour ajouter une forme d'ovale à une feuille de calcul. La méthode peut renvoyer un objet Ovale. La classe Ovale représente une forme ovale. Elle possède certains membres importants :

- La méthode setLineFormat spécifie les attributs de format de ligne d'une forme d'ovale.
- La méthode setPlacement spécifie le PlacementType, la manière dont l'ovale est attaché aux cellules dans la feuille de calcul.
- La propriété FillFormat spécifie les styles de format de remplissage de la forme.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : l'une est une forme ovale remplie, l'autre est un simple cercle. La sortie suivante est générée lors de l'exécution du code.

**Deux formes ovales sont ajoutées dans la feuille de calcul** 

![todo:image_alt_text](managing-controls_12.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-controls-AddinganOvalControl-1.java" >}}

## **Sujets avancés**
- [Ajouter des contrôles ActiveX à l'aide de Aspose.Cells](/cells/fr/java/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/java/remove-activex-control/)
{{< app/cells/assistant language="java" >}}
