---
title: Gestion des contrôles
type: docs
weight: 150
url: /fr/net/managing-controls/
---

## **Introduction**

Les développeurs peuvent ajouter différents objets graphiques tels que des zones de texte, des cases à cocher, des boutons radio, des listes déroulantes, des étiquettes, des boutons, des lignes, des rectangles, des arcs, des ovales, des curseurs, des barres de défilement, des cadres, etc. Aspose.Cells fournit l'espace de noms Aspose.Cells.Drawing qui contient tous les objets graphiques. Cependant, il existe quelques objets graphiques ou formes qui ne sont pas encore pris en charge. Créez ces objets graphiques dans une feuille de calcul de concepteur à l'aide de Microsoft Excel, puis importez la feuille de calcul de concepteur dans Aspose.Cells. Aspose.Cells vous permet de charger ces objets graphiques à partir d'une feuille de calcul de concepteur et de les écrire dans un fichier généré.

## **Ajout d'un contrôle de zone de texte à une feuille de calcul**

Une façon de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, ajoutez du texte pour mettre en évidence le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes, etc. Aspose.Cells fournit la classe [**TextBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textboxcollection), utilisée pour ajouter une nouvelle zone de texte à la collection. Il y a une autre classe, [**TextBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/textbox), qui représente une zone de texte utilisée pour définir tous les types de paramètres. Elle a certains membres importants :

- La propriété [**TextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/textframe) renvoie un objet [**MsoTextFrame**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msotextframe) utilisé pour ajuster le contenu de la zone de texte.
- La propriété [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie le type de placement.
- La propriété [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) spécifie les attributs de police.
- La méthode [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) ajoute un lien hypertexte pour la zone de texte.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) renvoie un objet [**MsoFillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msofillformat) utilisé pour définir le format de remplissage pour la zone de texte.
- La propriété [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) renvoie un objet [**MsoLineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/msolineformat) généralement utilisé pour le style et le poids de la ligne de la zone de texte.
- La propriété [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien aménagée avec différents paramètres de format. La seconde est plus simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingTextBoxControl-1.cs" >}}

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul du concepteur**

Aspose.Cells vous permet également d'accéder aux zones de texte dans les feuilles de calcul du concepteur et de les manipuler. Utilisez la propriété [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/textboxes) pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Microsoft Excel que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et modifie le texte de la deuxième zone de texte pour enregistrer le fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-ManipulatingTextBoxControls-1.cs" >}}

## **Ajout d'un contrôle de case à cocher à une feuille de calcul**

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

Aspose.Cells fournit la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkboxcollection), qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il existe une autre classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox), qui représente une case à cocher. Elle a quelques membres importants:

- La propriété [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée à la case à cocher.
- La propriété [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie la chaîne de texte associée à la case à cocher. Il s'agit de l'étiquette de la case à cocher.
- La propriété [**Value**](https://reference.aspose.com/cells/net/aspose.cells.drawing/checkbox/properties/value) spécifie si la case à cocher est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingCheckBoxControl-1.cs" >}}

## **Ajout d'un contrôle de bouton d'option à la feuille de calcul**

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

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddRadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addradiobutton), qui est utilisée pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton). La classe [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton) représente un bouton d'option. Elle possède quelques membres importants :

- La propriété [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée au bouton radio.
- La propriété [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
- La propriété [**IsChecked**](https://reference.aspose.com/cells/net/aspose.cells.drawing/radiobutton/properties/ischecked) spécifie si le bouton radio est coché ou non.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) spécifie le format de remplissage du bouton radio.
- La propriété [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des groupes d'âge.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRadioButtonControl-1.cs" >}}

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

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcombobox), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox). La classe [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox) représente une liste déroulante. Elle possède des membres importants :

- La propriété [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée à la liste déroulante.
- La propriété [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La propriété [**DropDownLines**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/dropdownlines) spécifie le nombre de lignes de la liste affichées dans la partie déroulante d'une liste déroulante.
- La propriété [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/combobox/properties/shadow) indique si la liste déroulante a un ombrage en 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingComboBoxControl-1.cs" >}}

## **Ajout de contrôle de libellé à une feuille de calcul**

Les libellés permettent de fournir aux utilisateurs des informations sur le contenu d'une feuille de calcul. Aspose.Cells permet d'ajouter et de manipuler des libellés dans une feuille de calcul. La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddLabel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlabel), utilisée pour ajouter un contrôle de libellé à la feuille de calcul. La méthode renvoie un objet [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/net/aspose.cells.drawing/label) représente un libellé dans la feuille de calcul. Elle possède des membres importants :

- La méthode [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie une chaîne de légende pour un libellé.
- La méthode [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie le [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la façon dont le libellé est attaché aux cellules dans la feuille de calcul.

L'exemple suivant montre comment ajouter un libellé à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLabelControl-1.cs" >}}

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlistbox), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox). La classe [**ListBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox) représente une liste déroulante et possède certains membres importants :

- La méthode [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée à la liste déroulante.
- La méthode [**InputRange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/inputrange) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La méthode [**SelectionType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/selectiontype) spécifie le mode de sélection de la liste déroulante.
- La méthode [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/listbox/properties/shadow) indique si la liste déroulante possède un ombrage 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingListBoxControl-1.cs" >}}

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddButton**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addbutton), utilisée pour ajouter un contrôle de bouton à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button). La classe [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/net/aspose.cells.drawing/button) représente un bouton et possède certains membres importants :

- La propriété [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie la légende du bouton.
- La propriété [**Font**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/font) spécifie les attributs de police pour l'étiquette du contrôle de bouton.
- La propriété [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie le [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), le mode d'attache du bouton aux cellules de la feuille de calcul.
- La propriété [**AddHyperlink**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/addhyperlink) ajoute un lien hypertexte pour le contrôle de bouton. En cliquant sur le bouton, vous serez redirigé vers l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingButtonControl-1.cs" >}}

## **Ajout d'un contrôle de ligne dans la feuille de calcul**

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Formes automatiques**, pointez sur **Lignes**, et sélectionnez le style de ligne désiré.
1. Faites glisser pour dessiner la ligne.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre la ligne à être dessinée selon un angle de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée pendant le glissement.
   1. Pour allonger la ligne dans des directions opposées depuis le premier point d'extrémité, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddLine**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addline), utilisée pour ajouter une forme de ligne à la feuille de calcul. La méthode renvoie un objet [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape). La classe [**LineShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/lineshape) représente une ligne. Elle possède quelques membres importants:

- La méthode [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) spécifie le format d'une ligne.
- La méthode [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie la [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la manière dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec différents styles.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingLineControl-1.cs" >}}

### **Ajout d'une tête de flèche à une ligne**

Aspose.Cells vous permet également de dessiner des lignes fléchées. Il est possible d'ajouter une tête de flèche à une ligne et de formater la ligne. Par exemple, vous pouvez changer la couleur de la ligne ou spécifier l'épaisseur et le style de la ligne.

L'exemple suivant montre comment ajouter une tête de flèche à une ligne.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddinganArrowHead-1.cs" >}}

## **Ajout d'un contrôle de rectangle dans une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes de rectangle dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous avez également la possibilité de formater la couleur de remplissage et la couleur de la ligne de contrôle. Par exemple, vous pouvez changer la couleur du rectangle, définir la couleur de l'ombrage, spécifier le poids et le style du rectangle selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre le rectangle à dessiner un carré depuis son point de départ, maintenez la touche SHIFT enfoncée pendant le glissement.
   1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddRectangle**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addrectangle), qui est utilisée pour ajouter une forme de rectangle à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/rectangleshape) représente un rectangle. Elle possède certains membres importants:

- La propriété [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) spécifie les attributs de mise en forme de ligne d'un rectangle.
- La propriété [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie la manière dont le rectangle est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) spécifie les styles de mise en forme de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingRectangleControl-1.cs" >}}

## **Ajout du Contrôle Arc à la Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et pleins. Vous pouvez formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'arc, définir la couleur de dégradé, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Arc** dans les **Formes Automatiques**.
1. Faites glisser pour dessiner l'arc.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddArc**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addarc), qui est utilisée pour ajouter une forme d'arc à une feuuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/arcshape) représente un arc. Elle possède certains membres importants:

- La propriété [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) spécifie les attributs de mise en forme de ligne d'une forme d'arc.
- La propriété [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie la manière dont l'arc est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) spécifie les styles de format de remplissage de la forme.
- La propriété [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : l'une pleine et l'autre simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingArcControl-1.cs" >}}

## **Ajout du Contrôle Ovale à une Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes ovales dans les feuilles de calcul. Créez des formes ovales simples et pleines et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'ovale, définir la couleur de dégradé, spécifier le poids et le style de la forme.

### **Utilisation de Microsoft Excel**

- Sur la barre d'outils *Dessin*, cliquez sur *Ovale*.
- Faites glisser pour dessiner l'ovale.
- Faites l'une ou l'autre des choses suivantes :
- Pour contraindre l'ovale et dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
- Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddOval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addoval), qui permet d'ajouter une forme ovale à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oval) représente une forme ovale. Elle possède des membres importants :

- La propriété [**LineFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lineformat) spécifie les attributs du format de ligne d'une forme ovale.
- La propriété [**Placement**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/placement) spécifie la [**PlacementType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/placementtype), la façon dont l'ovale est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/fillformat) spécifie les styles de format de remplissage de la forme.
- La propriété [**LowerRightRow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightrow) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**LowerRightColumn**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/lowerrightcolumn) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : une est un ovale rempli, l'autre est un simple cercle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingOvalControl-1.cs" >}}

## **Ajout d'un contrôle de type Spinner à la feuille de calcul**

Une zone de saisie est une zone de texte attachée à un bouton (appelé bouton de défilement) composée d'une flèche vers le haut et d'une flèche vers le bas sur lesquelles vous cliquez pour changer de façon incrémentale la valeur dans la zone de texte. En utilisant les zones de saisie, vous pouvez voir comment les modifications apportées à votre modèle financier affectent les sorties du modèle. Vous pouvez attacher un bouton de défilement à une cellule d'entrée spécifique. Lorsque vous cliquez sur la flèche vers le haut ou vers le bas sur le bouton de défilement, la valeur entière dans la cellule d'entrée ciblée augmente ou diminue. *Aspose.Cells* vous permet de créer des défilements dans vos feuilles de calcul.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de type Spinner dans votre feuille de calcul :

- Assurez-vous que la barre d'outils *Formulaires* est affichée.
- Cliquez sur l'outil *Spinner*.
- Dans la zone de votre feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le défilement.
- Une fois le défilement placé dans la feuille de calcul, faites un clic droit sur le contrôle, puis cliquez sur *Format de contrôle* et spécifiez les valeurs maximale, minimale et incrémentale.
- Dans le champ *Lier à la cellule*, spécifiez l'adresse de la cellule à laquelle ce défilement doit être lié.
- Cliquez sur *OK*.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**AddSpinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addspinner), qui permet d'ajouter un contrôle de type Spinner à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner) représente un défilement. Elle possède des membres importants :

- La propriété [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée à la boîte de liste.
- La propriété [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/max) spécifie la valeur maximale de la plage de la boîte de liste.
- La propriété [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/min) spécifie la valeur minimale de la plage de la boîte de liste.
- La propriété [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/incrementalchange) spécifie la valeur pour laquelle un spinner est incrémenté lorsqu'une ligne est défilée.
- La propriété [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/shadow) indique si la boîte de liste a un ombrage en 3D.
- La propriété [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/spinner/properties/currentvalue) spécifie la valeur actuelle de la boîte de liste.

L'exemple suivant montre comment ajouter une boîte de liste à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingSpinnerControl-1.cs" >}}

## **Ajout d'un contrôle de barre de défilement à une feuille de calcul**

Un contrôle de barre de défilement est utilisé pour aider à sélectionner des données sur une feuille de calcul de la même manière qu'un contrôle de boîte de liste. En ajoutant le contrôle à une feuille de calcul et en le liant à une cellule, il est possible de renvoyer une valeur numérique pour la position actuelle du contrôle.

### **Utilisation de Microsoft Excel**

- Pour ajouter une barre de défilement dans Excel 2003 et dans les versions antérieures, cliquez sur le bouton *Barre de défilement* dans la barre d'outils *Formulaires*, puis créez une barre de défilement qui couvre les cellules B2:B6 en hauteur et qui est d'environ un quart de la largeur de la colonne.
- Pour ajouter une barre de défilement dans Excel 2007, cliquez sur l'onglet *Développeur*, cliquez sur *Insérer*, puis cliquez sur *Barre de défilement* dans la section Contrôles de formulaire.
- Cliquez avec le bouton droit sur la barre de défilement, puis cliquez sur *Format de contrôle*.
- Saisissez les informations suivantes et cliquez sur *OK* :
  - Dans la zone *Valeur actuelle*, tapez 1.
  - Dans la zone *Valeur minimale*, tapez 1. Cette valeur restreint le haut de la barre de défilement au premier élément de la liste.
  - Dans la zone *Valeur maximale*, tapez 20. Ce nombre spécifie le nombre maximal d'entrées dans la liste.
  - Dans la zone *Changement incrémentiel*, tapez 1. Cette valeur contrôle le nombre de chiffres par lequel la barre de défilement incrémente la valeur actuelle.
  - Dans la case *Changement de page*, tapez 5. Cette entrée contrôle de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la boîte de défilement.
  - Pour mettre une valeur numérique dans la cellule G1 (selon l'élément sélectionné dans la liste), tapez G1 dans la zone *Lien de la cellule*.
- Cliquez sur n'importe quelle cellule pour désélectionner la barre de défilement.

Lorsque vous cliquez sur la commande haut ou bas de la barre de défilement, la cellule G1 est mise à jour avec un numéro qui indique la valeur actuelle de la barre de défilement plus ou moins le changement incrémentiel de la barre de défilement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addscrollbar), qui est utilisée pour ajouter un contrôle de barre de défilement à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar) représente une barre de défilement. Elle a quelques membres importants:

- La propriété [**LinkedCell**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/linkedcell) spécifie une cellule liée à la barre de défilement.
- La propriété [**Max**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/max) spécifie la valeur maximale pour la plage de la barre de défilement.
- La propriété [**Min**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/min) spécifie la valeur minimale pour la plage de la barre de défilement.
- La propriété [**IncrementalChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/incrementalchange) spécifie la quantité de valeur par laquelle une barre de défilement est incrémentée d'un défilement de ligne.
- La propriété [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/shadow) indique si la barre de défilement a un ombrage en 3D.
- La propriété [**CurrentValue**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/currentvalue) spécifie la valeur actuelle de la barre de défilement.
- La propriété [**PageChange**](https://reference.aspose.com/cells/net/aspose.cells.drawing/scrollbar/properties/pagechange) spécifie de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la boîte de défilement.

L'exemple suivant montre comment ajouter une barre de défilement à la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingScrollBarControl-1.cs" >}}

## **Ajout du contrôle GroupBox aux contrôles de groupe dans une feuille de calcul**

Parfois, vous devez implémenter des boutons radio ou d'autres contrôles qui appartiennent à un certain groupe, vous pouvez le faire en incluant soit un groupe box, soit un contrôle de rectangle. Ces deux objets serviraient de délimiteur du groupe. Après avoir ajouté l'une de ces formes, vous pouvez ensuite ajouter deux boutons radio ou d'autres objets de groupe ou plus.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de groupe box dans votre feuille de calcul et placer des contrôles dedans:

- Pour démarrer un formulaire, dans le menu principal, cliquez sur *Affichage*, suivi de *Barres d'outils* et *Formulaires*.
- Sur la barre d'outils *Formulaires*, cliquez sur *Group Box* et dessinez un rectangle sur la feuille de calcul.
- Tapez une chaîne de légende pour la boîte.
- Sur la barre d'outils *Formulaires*, cliquez sur *Bouton d'option* et cliquez à l'intérieur de la *Zone de groupe* juste sous la chaîne de légende.
- À nouveau sur la barre d'outils *Formulaires*, cliquez sur *Bouton d'option* et cliquez à l'intérieur de la *Zone de groupe* en dessous du premier bouton radio.
- Encore une fois sur la barre d'outils *Formulaires*, cliquez sur *Bouton d'option* et cliquez à l'intérieur de la *Zone de groupe* sous le précédent bouton radio.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**AddGroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addgroupbox), qui est utilisée pour ajouter un contrôle de zone de groupe à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox). De plus, la méthode [**Group**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/group) de la classe [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) regroupe les formes, elle prend un tableau [**Shape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape) en paramètre et renvoie un objet [**GroupShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox) représente une zone de groupe. Elle possède quelques membres importants :

- La propriété [**Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) spécifie la chaîne de légende de la zone de groupe.
- La propriété [**Shadow**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupbox/properties/shadow) indique si la zone de groupe a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de groupe et regrouper les contrôles dans la feuille de calcul.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Controls-AddingGroupBoxControl-1.cs" >}}

## **Sujets avancés**
- [Ajouter des contrôles ActiveX à l'aide de Aspose.Cells](/cells/fr/net/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/net/remove-activex-control/)
- [Mise à jour du contrôle ComboBox ActiveX](/cells/fr/net/update-activex-combobox-control/)
