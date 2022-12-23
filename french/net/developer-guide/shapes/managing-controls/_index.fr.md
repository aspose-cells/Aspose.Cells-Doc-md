---
title: Gestion des contrôles
type: docs
weight: 150
url: /fr/net/managing-controls/
---
## **Introduction**

Les développeurs peuvent ajouter différents objets de dessin tels que des zones de texte, des cases à cocher, des boutons radio, des zones de liste déroulante, des étiquettes, des boutons, des lignes, des rectangles, des arcs, des ovales, des compteurs, des barres de défilement, des zones de groupe, etc. Aspose.Cells fournit l'espace de noms Aspose.Cells.Drawing qui contient tous les objets de dessin. Cependant, certains objets ou formes de dessin ne sont pas encore pris en charge. Créez ces objets de dessin dans une feuille de calcul de concepteur à l'aide de Microsoft Excel, puis importez la feuille de calcul de concepteur dans Aspose.Cells. Aspose.Cells vous permet de charger ces objets de dessin à partir d'une feuille de calcul de concepteur et de les écrire dans un fichier généré.

## **Ajout d'un contrôle de zone de texte à une feuille de calcul**

 Une façon de souligner les informations importantes dans un rapport consiste à utiliser une zone de texte. Par exemple, ajoutez du texte pour mettre en surbrillance le nom de l'entreprise ou pour indiquer la région géographique avec les ventes les plus élevées, etc. Aspose.Cells fournit le[**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection) classe, utilisée pour ajouter une nouvelle zone de texte à la collection. Il y a une autre classe,[**Zone de texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox)qui représente une zone de texte utilisée pour définir tous les types de paramètres. Il compte quelques membres importants :

-  Le[**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) la propriété renvoie un[**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) objet utilisé pour ajuster le contenu de la zone de texte.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) La propriété spécifie le type de placement.
-  Le[**Police de caractère**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) La propriété spécifie les attributs de la police.
-  Le[**Ajouter un lien hypertexte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) La méthode ajoute un lien hypertexte pour la zone de texte.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) la propriété renvoie un[**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) objet utilisé pour définir le format de remplissage de la zone de texte.
-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) la propriété renvoie le[**MsoLineFormatMsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) objet généralement utilisé pour le style et l'épaisseur de la ligne de la zone de texte.
-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) propriété spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien fournie avec différents paramètres de format. La seconde est simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul Designer**

 Aspose.Cells vous permet également d'accéder aux zones de texte dans les feuilles de travail du concepteur et de les manipuler. Utilisez le[**Feuille de calcul.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) propriété pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Excel Microsoft que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et modifie le texte de la deuxième zone de texte pour enregistrer le fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Ajout d'un contrôle de case à cocher à une feuille de calcul**

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

 Aspose.Cells fournit le[**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection) class, qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il y a une autre classe,[**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), qui représente une case à cocher. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propriété spécifie une cellule qui est liée à la case à cocher.
-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propriété spécifie la chaîne de texte associée à la case à cocher. C'est l'étiquette de la case à cocher.
-  Le[**Évaluer**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) La propriété spécifie si la case est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Ajout d'un contrôle de bouton radio à la feuille de calcul**

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

[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**Ajouter un bouton radio**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton) , qui est utilisé pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) objet. La classe[**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) représente un bouton d'option. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) propriété spécifie une cellule qui est liée au bouton radio.
-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)La propriété spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
-  Le[**Est vérifié**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) La propriété spécifie si le bouton radio est coché ou non.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La propriété spécifie le format de remplissage du bouton radio.
-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propriété spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des tranches d'âge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

 Le[**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox) , qui est utilisé pour ajouter un contrôle de zone de liste déroulante à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) objet. La classe[**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) représente une zone de liste déroulante. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propriété spécifie une cellule qui est liée à la zone de liste déroulante.
-  Le[**Plage d'entrée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) La propriété spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la zone de liste déroulante.
-  Le[**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) La propriété spécifie le nombre de lignes de liste affichées dans la partie déroulante d'une zone de liste déroulante.
-  Le[**Ombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) La propriété indique si la zone de liste déroulante a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de liste déroulante à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Ajout d'un contrôle d'étiquette à une feuille de calcul**

 Les étiquettes sont un moyen de fournir aux utilisateurs des informations sur le contenu d'une feuille de calcul. Aspose.Cells permet d'ajouter et de manipuler des étiquettes dans une feuille de calcul. Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel) , utilisé pour ajouter un contrôle d'étiquette à la feuille de calcul. La méthode retourne un[**Étiquette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) objet. La classe[**Étiquette**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) représente une étiquette dans la feuille de calcul. Il compte quelques membres importants :

-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La méthode spécifie la chaîne de légende d'une étiquette.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) méthode spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la façon dont l'étiquette est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter une étiquette à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterListeBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox) , qui est utilisé pour ajouter un contrôle de zone de liste à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) objet. La classe[**Zone de liste**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) représente une zone de liste. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La méthode spécifie une cellule qui est liée à la zone de liste.
-  Le[**Plage d'entrée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) La méthode spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la zone de liste.
-  Le[**Type de sélection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype)La méthode spécifie le mode de sélection de la zone de liste.
-  Le[**Ombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) La méthode indique si la zone de liste a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de liste à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

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

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterBouton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton) , utilisé pour ajouter un contrôle de bouton à la feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) objet. La classe[**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) représente un bouton. Il compte quelques membres importants :

-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propriété spécifie la légende du bouton.
-  Le[**Police de caractère**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) La propriété spécifie les attributs de police pour l'étiquette du contrôle de bouton.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propriété spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la manière dont le bouton est attaché aux cellules de la feuille de calcul.
-  Le[**Ajouter un lien hypertexte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) La propriété ajoute un lien hypertexte pour le contrôle de bouton. Cliquez sur le bouton pour accéder à l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Ajout d'un contrôle de ligne à la feuille de calcul**

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Formes automatiques** , pointer vers**Lignes**, puis sélectionnez le style de ligne souhaité.
1. Faites glisser pour tracer la ligne.
1. Effectuez l'une des actions suivantes ou les deux :
 1. Pour contraindre la ligne à tracer à des angles de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
 1. Pour allonger la ligne dans des directions opposées à partir du premier point d'extrémité, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterLigne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline) , qui est utilisé pour ajouter une forme de ligne à la feuille de calcul. La méthode retourne un[**Forme de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) objet. La classe[**Forme de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) représente une ligne. Il compte quelques membres importants :

-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La méthode spécifie le format d'une ligne.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) méthode spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype)la manière dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec des styles différents.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Ajouter une pointe de flèche à une ligne**

Aspose.Cells vous permet également de tracer des lignes fléchées. Il est possible d'ajouter une pointe de flèche à une ligne, et de formater la ligne. Par exemple, vous pouvez modifier la couleur de la ligne ou spécifier l'épaisseur et le style de la ligne.

L'exemple suivant montre comment ajouter une pointe de flèche à une ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Ajout d'un contrôle Rectangle à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes rectangulaires dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous êtes également autorisé à formater la couleur de remplissage et la couleur de la bordure du contrôle. Par exemple, vous pouvez modifier la couleur du rectangle, définir la couleur d'ombrage, spécifier l'épaisseur et le style du rectangle selon vos besoins.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Effectuez l'une des actions suivantes ou les deux :
 1. Pour contraindre le rectangle à dessiner un carré à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
 1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle) , qui est utilisé pour ajouter une forme de rectangle à une feuille de calcul. La méthode retourne[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) objet. La classe[**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) représente un rectangle. Il compte quelques membres importants :

-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propriété spécifie les attributs de format de ligne d'un rectangle.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propriété spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la manière dont le rectangle est attaché aux cellules de la feuille de calcul.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) La propriété spécifie les styles de format de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Ajout du contrôle d'arc à la feuille de travail**

Aspose.Cells vous permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et pleins. Vous êtes autorisé à formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / modifier la couleur de l'arc, définir la couleur d'ombrage, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation d'Excel Microsoft**

1.  Sur le**Dessin** barre d'outils, cliquez sur**Arc** dans le**Formes automatiques**.
1. Faites glisser pour dessiner l'arc.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc) , qui est utilisé pour ajouter une forme d'arc à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) objet. La classe[**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) représente un arc. Il compte quelques membres importants :

-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propriété spécifie les attributs de format de ligne d'une forme d'arc.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propriété spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la façon dont l'arc est attaché aux cellules de la feuille de calcul.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)La propriété spécifie les styles de format de remplissage de la forme.
-  Le[**ligne inférieure droite**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La propriété spécifie l'index de ligne du coin inférieur droit.
-  Le[**Colonne inférieure droite**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La propriété spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : l'une est remplie et l'autre est simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Ajout d'un contrôle ovale à une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes ovales dans des feuilles de calcul. Créez des formes ovales simples et remplies et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / modifier la couleur de l'ovale, définir la couleur d'ombrage, spécifier le poids et le style de la forme.

### **Utilisation d'Excel Microsoft**

-  Sur le*Dessin* barre d'outils, cliquez sur*ovale*.
- Faites glisser pour dessiner l'ovale.
- Effectuez l'une des actions suivantes ou les deux :
- Pour contraindre l'ovale à dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
- Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterOvale**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval) , qui est utilisé pour ajouter une forme ovale à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) objet. La classe[**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) représente une forme ovale. Il compte quelques membres importants :

-  Le[**Format de ligne**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) La propriété spécifie les attributs de format de ligne d'une forme ovale.
-  Le[**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) propriété spécifie la[**Type d'emplacement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la manière dont l'ovale est attaché aux cellules de la feuille de calcul.
-  Le[**RemplirFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat)La propriété spécifie les styles de format de remplissage de la forme.
-  Le[**ligne inférieure droite**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) La propriété spécifie l'index de ligne du coin inférieur droit.
-  Le[**Colonne inférieure droite**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) La propriété spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : l'une est un ovale rempli, l'autre est un simple cercle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Ajout du contrôle Spinner à la feuille de calcul**

 Une zone de sélection numérique est une zone de texte attachée à un bouton (appelé bouton de sélection numérique) composée d'une flèche vers le haut et d'une flèche vers le bas sur lesquelles vous cliquez pour modifier progressivement la valeur dans la zone de texte. En utilisant des compteurs numériques, vous pouvez voir comment les changements d'entrée de votre modèle financier modifieront les sorties du modèle. Vous pouvez attacher un bouton rotatif à une cellule d'entrée spécifique. Lorsque vous cliquez sur la flèche vers le haut ou vers le bas sur le bouton de rotation, la valeur entière dans la cellule d'entrée ciblée augmente ou diminue.*Aspose.Cells* vous permet de créer des spinners dans vos feuilles de calcul.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de zone de sélection numérique dans votre feuille de calcul :

-  Assurez-vous que le*Formes* barre d'outils s'affiche.
-  Clique le*Fileur* outil.
- Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le spinner.
-  Une fois le spinner placé dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle et cliquez sur*Contrôle des formats* et spécifiez les valeurs maximales, minimales et incrémentielles.
-  Dans le*Cell Lien* champ, indiquez l'adresse de la cellule à laquelle cette boîte numérique doit être liée.
-  Cliquer sur*D'ACCORD*.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner) qui est utilisé pour ajouter un contrôle de zone de sélection numérique à une feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) objet. La classe[**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) représente une spinbox. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) La propriété spécifie une cellule qui est liée à la zone de sélection numérique.
-  Le[**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) La propriété spécifie la valeur maximale de la plage de la zone de sélection numérique.
-  Le[**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) La propriété spécifie la valeur minimale de la plage de la zone de sélection numérique.
-  Le[**ChangementIncrémental**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) La propriété spécifie la quantité de valeur pour laquelle un spinner est incrémenté d'un défilement de ligne.
-  Le[**Ombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) La propriété indique si la zone de sélection numérique a un ombrage 3D.
-  Le[**Valeur actuelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) La propriété spécifie la valeur actuelle de la zone de sélection numérique.

L'exemple suivant montre comment ajouter une zone de sélection numérique à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Ajout d'un contrôle de barre de défilement à une feuille de calcul**

Un contrôle de barre de défilement est utilisé pour aider à sélectionner des données sur une feuille de calcul de la même manière qu'un contrôle de zone de sélection numérique. En ajoutant le contrôle à une feuille de calcul et en le liant à une cellule, il est possible de renvoyer une valeur numérique pour la position actuelle du contrôle.

### **Utilisation d'Excel Microsoft**

- Pour ajouter une barre de défilement dans Excel 2003 et dans les versions antérieures, cliquez sur le*Barre de défilement* bouton sur le*Formes* barre d'outils, puis créez une barre de défilement qui couvre les cellules B2:B6 en hauteur et représente environ un quart de la largeur de la colonne.
-  Pour ajouter une barre de défilement dans Excel 2007, cliquez sur le*Développeur* onglet, cliquez*Insérer* , puis cliquez sur*Barre de défilement* dans la section Contrôles de formulaire.
-  Cliquez avec le bouton droit sur la barre de défilement, puis cliquez sur*Contrôle des formats*.
-  Saisissez les informations suivantes, puis cliquez sur*D'ACCORD*:
 - Dans le*Valeur actuelle* boîte, type 1.
 - Dans le*Valeur minimum* zone, tapez 1. Cette valeur limite le haut de la barre de défilement au premier élément de la liste.
 - Dans le*Valeur maximum* zone, tapez 20. Ce nombre spécifie le nombre maximum d'entrées dans la liste.
 - Dans le*Changement progressif* zone, tapez 1. Cette valeur contrôle de combien de nombres le contrôle de la barre de défilement incrémente la valeur actuelle.
 - Dans le*Changement de page* zone, tapez 5. Cette entrée contrôle de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la zone de défilement.
 Pour mettre une valeur numérique dans la cellule G1 (en fonction de l'élément sélectionné dans la liste), tapez G1 dans la*Cell lien* boîte.
- Cliquez sur n'importe quelle cellule pour que la barre de défilement ne soit pas sélectionnée.

Lorsque vous cliquez sur la commande haut ou bas de la barre de défilement, la cellule G1 est mise à jour avec un nombre qui indique la valeur actuelle de la barre de défilement plus ou moins le changement incrémentiel de la barre de défilement.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**Ajouter une barre de défilement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar) , qui est utilisé pour ajouter un contrôle de barre de défilement à la feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) objet. La classe[**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) représente une barre de défilement. Il compte quelques membres importants :

-  Le[**Cellule Liée**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) propriété spécifie une cellule qui est liée à la barre de défilement.
-  Le[**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) La propriété spécifie la valeur maximale de la plage de la barre de défilement.
-  Le[**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) La propriété spécifie la valeur minimale de la plage de la barre de défilement.
-  Le[**ChangementIncrémental**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) La propriété spécifie la valeur pour laquelle une barre de défilement est incrémentée d'un défilement de ligne.
-  Le[**Ombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) La propriété indique si la barre de défilement a un ombrage 3D.
-  Le[**Valeur actuelle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) La propriété spécifie la valeur actuelle de la barre de défilement.
-  Le[**Changement de page**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange)La propriété spécifie de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la boîte de défilement.

L'exemple suivant montre comment ajouter une barre de défilement à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Ajout d'un contrôle GroupBox à des contrôles de groupe dans une feuille de calcul**

Parfois, vous devez implémenter des boutons radio ou d'autres contrôles appartenant à un certain groupe, vous pouvez les implémenter en incluant soit une zone de groupe, soit un contrôle rectangle. N'importe lequel de ces deux objets servirait de délimiteur du groupe. Après avoir ajouté l'une de ces formes, vous pouvez ensuite ajouter deux boutons radio ou plus ou d'autres objets de groupe.

### **Utilisation d'Excel Microsoft**

Pour placer un contrôle de zone de groupe dans votre feuille de calcul et y placer des contrôles :

-  Pour démarrer un formulaire, dans le menu principal, cliquez sur*Vue* , suivie par*Barres d'outils* et*Formes*.
-  Sur le*Formes* barre d'outils, cliquez sur le*Zone de groupe* et dessinez un rectangle sur la feuille de calcul.
- Saisissez une chaîne de légende pour la zone.
-  Sur le*Formes* barre d'outils, cliquez sur*Bouton d'option* et cliquez à l'intérieur du*Zone de groupe* juste sous la chaîne de légende.
-  Du*Formes* barre d'outils à nouveau, cliquez sur*Bouton d'option* et cliquez à l'intérieur du*Zone de groupe*sous le premier bouton radio.
-  Encore une fois sur le*Formes* barre d'outils, cliquez sur*Bouton d'option* et cliquez à l'intérieur du*Zone de groupe* sous le bouton radio précédent.

### **En utilisant Aspose.Cells**

 Le[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe fournit une méthode nommée[**AjouterGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox) , qui est utilisé pour ajouter un contrôle de zone de groupe à la feuille de calcul. La méthode retourne un[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) objet. De plus, le[**Groupe**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) méthode de la[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) classe regroupe les formes, il faut un[**Façonner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) tableau en paramètre et renvoie un[**Forme de groupe**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape) objet. La classe[**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) représente une zone de groupe. Il compte quelques membres importants :

-  Le[**Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) La propriété spécifie la chaîne de légende de la zone de groupe.
-  Le[**Ombre**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) La propriété indique si la zone de groupe a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de groupe et regrouper les contrôles dans la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Sujets avancés**
- [Ajouter des contrôles ActiveX à l'aide de Aspose.Cells](/cells/fr/net/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/net/remove-activex-control/)
- [Mettre à jour le contrôle ComboBox ActiveX](/cells/fr/net/update-activex-combobox-control/)
