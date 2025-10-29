---
title: Gestion des contrôles
type: docs
weight: 150
url: /fr/python-net/managing-controls/
---

## **Introduction**

Les développeurs peuvent ajouter différents objets de dessin tels que des zones de texte, des cases à cocher, des boutons radio, des zones de liste déroulante, des étiquettes, des boutons, des lignes, des rectangles, des arcs, des ovales, des spins, des barres de défilement, des groupes, etc. Aspose.Cells pour Python via .NET fournit l'espace de noms Aspose.Cells.Drawing qui contient tous les objets de dessin. Cependant, il existe quelques objets de dessin ou formes qui ne sont pas encore supportés. Créez ces objets de dessin dans une feuille de calcul créative avec Microsoft Excel, puis importez cette feuille dans Aspose.Cells. Aspose.Cells pour Python via .NET vous permet de charger ces objets de dessin depuis une feuille de calcul créée et de les écrire dans un fichier généré.

## **Ajout d'un contrôle de zone de texte à une feuille de calcul**

Une façon de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, ajouter du texte pour souligner le nom de l'entreprise ou indiquer la région géographique avec les ventes les plus élevées, etc. Aspose.Cells pour Python via .NET fournit la classe [**TextBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textboxcollection), utilisée pour ajouter une nouvelle zone de texte à la collection. Il existe une autre classe, [**TextBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/textbox), qui représente une zone de texte utilisée pour définir tous les types de paramètres. Elle possède quelques membres importants :

- La propriété [**text_frame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text_frame) renvoie un objet [**MsoTextFrame**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msotextframe) utilisé pour ajuster le contenu de la zone de texte.
- La propriété [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie le type de placement.
- La propriété [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) spécifie les attributs de police.
- La méthode [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) ajoute un lien hypertexte pour la zone de texte.
- La propriété [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) renvoie un objet [**MsoFillFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msofillformat) utilisé pour définir le format de remplissage pour la zone de texte.
- La propriété [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) renvoie un objet [**MsoLineFormat**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/msolineformat) généralement utilisé pour le style et le poids de la ligne de la zone de texte.
- La propriété [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien aménagée avec différents paramètres de format. La seconde est plus simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingTextBoxControl-1.py" >}}

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul du concepteur**

Aspose.Cells pour Python via .NET permet également d'accéder aux zones de texte dans les feuilles de calcul de conception et de les manipuler. Utilisez la propriété [**Worksheet.TextBoxes**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/text_boxes) pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Microsoft Excel que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et modifie le texte de la deuxième zone de texte pour enregistrer le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-ManipulatingTextBoxControls-1.py" >}}

## **Ajout d'un contrôle de case à cocher à une feuille de calcul**

Les cases à cocher sont pratiques si vous souhaitez offrir à un utilisateur un moyen de choisir entre deux options, telles que vrai ou faux ; oui ou non. Aspose.Cells pour Python via .NET autorise l'utilisation de cases à cocher dans les feuilles de calcul. Par exemple, vous pouvez avoir développé une feuille de projection financière dans laquelle vous pouvez traiter ou non une acquisition particulière. Dans ce cas, vous pouvez placer une case à cocher en haut de la feuille. Vous pouvez alors lier le statut de cette case à une autre cellule, de sorte que si la case est cochée, la valeur de la cellule soit Vrai, sinon elle soit Faux.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de case à cocher dans votre feuille de calcul, suivez ces étapes:

1. Assurez-vous que la barre d'outils Formulaires est affichée.
1. Cliquez sur l'outil **Case à cocher** dans la barre d'outils Formulaires.
1. Dans votre zone de feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra la case à cocher et l'étiquette à côté de la case à cocher.
1. Une fois la case à cocher placée, déplacez le curseur de la souris dans la zone de l'étiquette et modifiez l'étiquette.
1. Dans le champ **Lien de la cellule**, spécifiez l'adresse de la cellule à laquelle cette case à cocher doit être liée.
1. Cliquez sur **OK**.

### **Utiliser Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET fournit la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkboxcollection), qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il existe une autre classe, [**Aspose.Cells.Drawing.CheckBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox), qui représente une case à cocher. Elle possède quelques membres importants :

- La propriété [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée à la case à cocher.
- La propriété [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie la chaîne de texte associée à la case à cocher. Il s'agit de l'étiquette de la case à cocher.
- La propriété [**value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/checkbox/value) spécifie si la case à cocher est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingCheckBoxControl-1.py" >}}

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

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_radio_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_radio_button), qui est utilisée pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton). La classe [**Aspose.Cells.Drawing.RadioButton**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton) représente un bouton d'option. Elle possède quelques membres importants :

- La propriété [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée au bouton radio.
- La propriété [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
- La propriété [**is_checked**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/radiobutton/is_checked) spécifie si le bouton radio est coché ou non.
- La propriété [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) spécifie le format de remplissage du bouton radio.
- La propriété [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des groupes d'âge.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRadioButtonControl-1.py" >}}

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

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**Aspose.Cells.Drawing.ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_combo_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_combo_box), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox). La classe [**Aspose.Cells.Drawing.ComboBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox) représente une liste déroulante. Elle possède des membres importants :

- La propriété [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée à la liste déroulante.
- La propriété [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La propriété [**drop_down_lines**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/drop_down_lines) spécifie le nombre de lignes de la liste affichées dans la partie déroulante d'une liste déroulante.
- La propriété [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/combobox/shadow) indique si la liste déroulante a un ombrage en 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingComboBoxControl-1.py" >}}

## **Ajout de contrôle de libellé à une feuille de calcul**

Les étiquettes sont un moyen de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul. Aspose.Cells pour Python via .NET permet d'ajouter et de manipuler des étiquettes dans une feuille de calcul. La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_label), utilisée pour ajouter un contrôle d'étiquette à la feuille de calcul. La méthode renvoie un objet [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label). La classe [**Label**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/label) représente une étiquette dans la feuille de calcul. Elle possède quelques membres importants :

- La méthode [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie une chaîne de légende pour un libellé.
- La méthode [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie le [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la façon dont le libellé est attaché aux cellules dans la feuille de calcul.

L'exemple suivant montre comment ajouter un libellé à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLabelControl-1.py" >}}

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

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_list_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_list_box), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox). La classe [**ListBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox) représente une liste déroulante et possède certains membres importants :

- La méthode [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée à la liste déroulante.
- La méthode [**input_range**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/input_range) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La méthode [**selection_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/selection_type) spécifie le mode de sélection de la liste déroulante.
- La méthode [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/listbox/shadow) indique si la liste déroulante possède un ombrage 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingListBoxControl-1.py" >}}

## **Ajout d'un contrôle de bouton à une feuille de calcul**

Les boutons sont utiles pour effectuer des actions. Parfois, il est utile d'attribuer une macro VBA au bouton ou d'assigner un lien hypertexte pour ouvrir une page web.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de bouton dans votre feuille de calcul :

1. Assurez-vous que la barre d'outils **Formulaires** est affichée.
1. Cliquez sur l'outil **Bouton**.
1. Dans la zone de votre feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le bouton.
1. Une fois la liste déroulante placée dans la feuille de calcul, cliquez avec le bouton droit sur le contrôle et sélectionnez **Format de contrôle**, puis spécifiez une macro VBA et des attributs liés à la police, à l'alignement, à la taille, à la marge, etc.
1. Cliquez sur **OK**.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_button), utilisée pour ajouter un contrôle de bouton à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button). La classe [**Aspose.Cells.Drawing.Button**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/button) représente un bouton et possède certains membres importants :

- La propriété [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie la légende du bouton.
- La propriété [**font**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/font) spécifie les attributs de police pour l'étiquette du contrôle de bouton.
- La propriété [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie le [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), le mode d'attache du bouton aux cellules de la feuille de calcul.
- La propriété [**add_hyperlink**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/add_hyperlink) ajoute un lien hypertexte pour le contrôle de bouton. En cliquant sur le bouton, vous serez redirigé vers l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingButtonControl-1.py" >}}

## **Ajout d'un contrôle de ligne dans la feuille de calcul**

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Formes automatiques**, pointez sur **Lignes**, et sélectionnez le style de ligne désiré.
1. Faites glisser pour dessiner la ligne.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre la ligne à être dessinée selon un angle de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée pendant le glissement.
   1. Pour allonger la ligne dans des directions opposées depuis le premier point d'extrémité, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_line**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_line), utilisée pour ajouter une forme de ligne à la feuille de calcul. La méthode renvoie un objet [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape). La classe [**LineShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/lineshape) représente une ligne. Elle possède quelques membres importants:

- La méthode [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) spécifie le format d'une ligne.
- La méthode [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie la [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la manière dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec différents styles.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingLineControl-1.py" >}}

### **Ajout d'une tête de flèche à une ligne**

Aspose.Cells pour Python via .NET permet également de tracer des lignes de flèches. Il est possible d'ajouter une tête de flèche à une ligne, et de formater la ligne. Par exemple, vous pouvez changer la couleur de la ligne, ou spécifier le poids et le style de la ligne.

L'exemple suivant montre comment ajouter une tête de flèche à une ligne.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddinganArrowHead-1.py" >}}

## **Ajout d'un contrôle de rectangle dans une feuille de calcul**

Aspose.Cells pour Python via .NET permet de dessiner des formes rectangulaires dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous êtes également autorisé à formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez changer la couleur du rectangle, définir la couleur de l'ombrage, spécifier le poids et le style du rectangle selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre le rectangle à dessiner un carré depuis son point de départ, maintenez la touche SHIFT enfoncée pendant le glissement.
   1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_rectangle**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_rectangle), qui est utilisée pour ajouter une forme de rectangle à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/rectangleshape) représente un rectangle. Elle possède certains membres importants:

- La propriété [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) spécifie les attributs de mise en forme de ligne d'un rectangle.
- La propriété [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie la manière dont le rectangle est attaché aux cellules dans la feuille de calcul.
- La propriété [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) spécifie les styles de mise en forme de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingRectangleControl-1.py" >}}

## **Ajout du Contrôle Arc à la Feuille de Calcul**

Aspose.Cells pour Python via .NET permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et remplis. Vous êtes autorisé à formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'arc, définir la couleur d’ombrage, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Arc** dans les **Formes Automatiques**.
1. Faites glisser pour dessiner l'arc.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_arc**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_arc), qui est utilisée pour ajouter une forme d'arc à une feuuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/arcshape) représente un arc. Elle possède certains membres importants:

- La propriété [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) spécifie les attributs de mise en forme de ligne d'une forme d'arc.
- La propriété [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie la manière dont l'arc est attaché aux cellules dans la feuille de calcul.
- La propriété [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) spécifie les styles de format de remplissage de la forme.
- La propriété [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : l'une pleine et l'autre simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingArcControl-1.py" >}}

## **Ajout du Contrôle Ovale à une Feuille de Calcul**

Aspose.Cells pour Python via .NET permet de dessiner des formes ovales dans les feuilles de calcul. Créez des formes ovales simples et remplies, et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'ovale, définir la couleur d’ombrage, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation de Microsoft Excel**

- Sur la barre d'outils *Dessin*, cliquez sur *Ovale*.
- Faites glisser pour dessiner l'ovale.
- Faites l'une ou l'autre des choses suivantes :
- Pour contraindre l'ovale et dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
- Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_oval), qui permet d'ajouter une forme ovale à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oval) représente une forme ovale. Elle possède des membres importants :

- La propriété [**line_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/line_format) spécifie les attributs du format de ligne d'une forme ovale.
- La propriété [**placement**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/placement) spécifie la [**PlacementType**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/placementtype), la façon dont l'ovale est attaché aux cellules dans la feuille de calcul.
- La propriété [**fill_format**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/fill_format) spécifie les styles de format de remplissage de la forme.
- La propriété [**lower_right_row**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_row) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**lower_right_column**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/lower_right_column) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : une est un ovale rempli, l'autre est un simple cercle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingOvalControl-1.py" >}}

## **Ajout d'un contrôle de type Spinner à la feuille de calcul**

Une boîte de rotation est une zone de texte attachée à un bouton (appelé bouton de rotation) composé d'une flèche vers le haut et d'une flèche vers le bas que vous cliquez pour modifier la valeur de manière incrémentale dans la zone de texte. En utilisant les boîtes de rotation, vous pouvez voir comment les changements d'entrée dans votre modèle financier modifieront les sorties du modèle. Vous pouvez attacher un bouton de rotation à une cellule d'entrée spécifique. Pendant que vous cliquez sur la flèche vers le haut ou vers le bas du bouton de rotation, la valeur entière dans la cellule d'entrée ciblée augmente ou diminue. *Aspose.Cells pour Python via .NET* vous permet de créer des spins dans vos feuilles de calcul.

### **Utilisation de Microsoft Excel**

Pour placer un contrôle de type Spinner dans votre feuille de calcul :

- Assurez-vous que la barre d'outils *Formulaires* est affichée.
- Cliquez sur l'outil *Spinner*.
- Dans la zone de votre feuille de calcul, cliquez et faites glisser pour définir le rectangle qui contiendra le défilement.
- Une fois le défilement placé dans la feuille de calcul, faites un clic droit sur le contrôle, puis cliquez sur *Format de contrôle* et spécifiez les valeurs maximale, minimale et incrémentale.
- Dans le champ *Lier à la cellule*, spécifiez l'adresse de la cellule à laquelle ce défilement doit être lié.
- Cliquez sur *OK*.

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode nommée [**add_spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_spinner), qui permet d'ajouter un contrôle de type Spinner à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner) représente un défilement. Elle possède des membres importants :

- La propriété [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée à la boîte de liste.
- La propriété [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/max) spécifie la valeur maximale de la plage de la boîte de liste.
- La propriété [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/min) spécifie la valeur minimale de la plage de la boîte de liste.
- La propriété [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/incremental_change) spécifie la valeur pour laquelle un spinner est incrémenté lorsqu'une ligne est défilée.
- La propriété [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/shadow) indique si la boîte de liste a un ombrage en 3D.
- La propriété [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/spinner/current_value) spécifie la valeur actuelle de la boîte de liste.

L'exemple suivant montre comment ajouter une boîte de liste à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingSpinnerControl-1.py" >}}

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

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_scroll_bar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_scroll_bar), qui est utilisée pour ajouter un contrôle de barre de défilement à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar) représente une barre de défilement. Elle a quelques membres importants:

- La propriété [**linked_cell**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/linked_cell) spécifie une cellule liée à la barre de défilement.
- La propriété [**max**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/max) spécifie la valeur maximale pour la plage de la barre de défilement.
- La propriété [**min**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/min) spécifie la valeur minimale pour la plage de la barre de défilement.
- La propriété [**incremental_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/incremental_change) spécifie la quantité de valeur par laquelle une barre de défilement est incrémentée d'un défilement de ligne.
- La propriété [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/shadow) indique si la barre de défilement a un ombrage en 3D.
- La propriété [**current_value**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/current_value) spécifie la valeur actuelle de la barre de défilement.
- La propriété [**page_change**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/scrollbar/page_change) spécifie de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la boîte de défilement.

L'exemple suivant montre comment ajouter une barre de défilement à la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingScrollBarControl-1.py" >}}

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

### **Utiliser Aspose.Cells pour Python via .NET**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) fournit une méthode appelée [**add_group_box**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_group_box), qui est utilisée pour ajouter un contrôle de zone de groupe à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox). De plus, la méthode [**group**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/group) de la classe [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) regroupe les formes, elle prend un tableau [**Shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape) en paramètre et renvoie un objet [**GroupShape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox) représente une zone de groupe. Elle possède quelques membres importants :

- La propriété [**text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) spécifie la chaîne de légende de la zone de groupe.
- La propriété [**shadow**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupbox/shadow) indique si la zone de groupe a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de groupe et regrouper les contrôles dans la feuille de calcul.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Controls-AddingGroupBoxControl-1.py" >}}

## **Sujets avancés**
- [Ajouter des contrôles ActiveX](/cells/fr/python-net/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/python-net/remove-activex-control/)
- [Mise à jour du contrôle ComboBox ActiveX](/cells/fr/python-net/update-activex-combobox-control/)
{{< app/cells/assistant language="python-net" >}}
