---
title: Gestion des contrôles avec C++
linktitle: Gestion des contrôles
type: docs
weight: 150
url: /fr/cpp/managing-controls/
description: Apprenez comment ajouter et gérer divers contrôles comme lignes, rectangles, arcs, ovales, spinner, barres de défilement et boîtes de groupe dans les feuilles de calcul en utilisant Aspose.Cells avec C++.
---

## **Introduction**

Les développeurs peuvent ajouter différents objets de dessin tels que zones de texte, cases à cocher, boutons radio, combobox, étiquettes, boutons, lignes, rectangles, arcs, ovales, spinners, barres de défilement, boîtes de groupe, etc. Aspose.Cells offre l'espace de noms `Aspose::Cells::Drawing` qui contient tous les objets de dessin. Cependant, il y a quelques objets de dessin ou formes qui ne sont pas encore supportés. Créez ces objets de dessin dans une feuille de calcul de conception en utilisant Microsoft Excel, puis importez la feuille de calcul de conception dans Aspose.Cells. Aspose.Cells vous permet de charger ces objets de dessin à partir d'une feuille de calcul de conception et de les écrire dans un fichier généré.

## **Ajout d'un contrôle de zone de texte à une feuille de calcul**

Une façon de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, ajoutez du texte pour mettre en évidence le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes, etc. Aspose.Cells fournit la classe [**TextBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textboxcollection/), utilisée pour ajouter une nouvelle zone de texte à la collection. Il y a une autre classe, [**TextBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/textbox/), qui représente une zone de texte utilisée pour définir tous les types de paramètres. Elle a certains membres importants :

- La propriété [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie le type de placement.
- La propriété [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) spécifie les attributs de police.
- La méthode [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) ajoute un lien hypertexte pour la zone de texte.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) renvoie un objet [**MsoFillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msofillformat/) utilisé pour définir le format de remplissage pour la zone de texte.
- La propriété [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) renvoie un objet [**MsoLineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/msolineformat/) généralement utilisé pour le style et le poids de la ligne de la zone de texte.
- La propriété [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie le texte d'entrée pour la zone de texte.

L'exemple suivant crée deux zones de texte dans la première feuille de calcul du classeur. La première zone de texte est bien aménagée avec différents paramètres de format. La seconde est plus simple.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // The path to the documents directory.
    U16String dataDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get the first worksheet in the book.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new textbox to the collection.
    int32_t textboxIndex = worksheet.GetTextBoxes().Add(2, 1, 160, 200);

    // Get the textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Fill the text.
    textbox0.SetText(u"ASPOSE______The .NET & JAVA Component Publisher!");

    // Set the placement.
    textbox0.SetPlacement(PlacementType::FreeFloating);

    // Set the font color.
    textbox0.GetFont().SetColor(Color::Blue());

    // Set the font to bold.
    textbox0.GetFont().SetIsBold(true);

    // Set the font size.
    textbox0.GetFont().SetSize(14);

    // Set font attribute to italic.
    textbox0.GetFont().SetIsItalic(true);

    // Add a hyperlink to the textbox.
    textbox0.AddHyperlink(u"http://www.aspose.com/");

    // Get the fill format of the textbox.
    FillFormat fillFormat = textbox0.GetFill();

    // Get the line format type of the textbox.
    LineFormat lineFormat = textbox0.GetLine();

    // Set the line weight.
    lineFormat.SetWeight(6.0);

    // Set the dash style to squaredot.
    lineFormat.SetDashStyle(MsoLineDashStyle::SquareDot);

    // Add another textbox.
    textboxIndex = worksheet.GetTextBoxes().Add(15, 4, 85, 120);

    // Get the second textbox.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(textboxIndex);

    // Input some text to it.
    textbox1.SetText(u"This is another simple text box");

    // Set the placement type as the textbox will move and resize with cells.
    textbox1.SetPlacement(PlacementType::MoveAndSize);

    // Save the excel file.
    workbook.Save(dataDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

## **Manipulation des contrôles de zone de texte dans les feuilles de calcul du concepteur**

Aspose.Cells vous permet également d'accéder aux zones de texte dans les feuilles de calcul du concepteur et de les manipuler. Utilisez la propriété [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettextboxes/) pour obtenir la collection de zones de texte dans la feuille.

L'exemple suivant utilise le fichier Microsoft Excel que nous avons créé dans l'exemple ci-dessus. Il obtient les chaînes de texte des deux zones de texte et modifie le texte de la deuxième zone de texte pour enregistrer le fichier.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // The path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file.
    Workbook workbook(srcDir + u"book1.xls");

    // Get the first worksheet in the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first textbox object.
    TextBox textbox0 = worksheet.GetTextBoxes().Get(0);

    // Obtain the text in the first textbox.
    U16String text0 = textbox0.GetText();

    // Get the second textbox object.
    TextBox textbox1 = worksheet.GetTextBoxes().Get(1);

    // Obtain the text in the second textbox.
    U16String text1 = textbox1.GetText();

    // Change the text of the second textbox.
    textbox1.SetText(u"This is an alternative text");

    // Save the excel file.
    workbook.Save(srcDir + u"output.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

Aspose.Cells fournit la classe [**CheckBoxCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkboxcollection/), qui est utilisée pour ajouter une nouvelle case à cocher à la collection. Il existe une autre classe, [**Aspose::Cells::Drawing::CheckBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/), qui représente une case à cocher. Elle a quelques membres importants:

- La propriété [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée à la case à cocher.
- La propriété [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie la chaîne de texte associée à la case à cocher. Il s'agit de l'étiquette de la case à cocher.
- La propriété [**GetValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/checkbox/getvalue/) spécifie si la case à cocher est cochée ou non.

L'exemple suivant montre comment ajouter une case à cocher à la feuille de calcul.

```c++
#include <iostream>
#include <Aspose.Cells.h>
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Creating a new Workbook instance
    Workbook excelbook = Workbook();

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add a checkbox to the first worksheet in the workbook
    int32_t index = worksheet.GetCheckBoxes().Add(5, 5, 100, 120);

    // Get the checkbox object
    Drawing::CheckBox checkbox = worksheet.GetCheckBoxes().Get(index);

    // Set its text string
    checkbox.SetText(u"Click it!");

    // Get cells collection and set B1 cell value
    Cells cells = worksheet.GetCells();
    Cell cellB1 = cells.Get(u"B1");
    cellB1.PutValue(u"LnkCell");

    // Set B1 cell as a linked cell for the checkbox
    checkbox.SetLinkedCell(u"B1");

    // Check the checkbox by default
    checkbox.SetValue(true);

    // Save the excel file
    excelbook.Save(u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

[**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) classe fournit une méthode nommée [**AddRadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addradiobutton/), qui est utilisée pour ajouter un contrôle de bouton radio à une feuille de calcul. La méthode retourne un objet [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/). La classe [**Aspose::Cells::Drawing::RadioButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/) représente un bouton d'option. Elle possède des membres importants :

- La propriété [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée au bouton radio.
- La propriété [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie la chaîne de texte associée au bouton radio. C'est l'étiquette du bouton radio.
- La propriété [**IsChecked**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/radiobutton/ischecked/) spécifie si le bouton radio est coché ou non.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) spécifie le format de remplissage du bouton radio.
- La propriété [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) spécifie les styles de format de ligne du bouton d'option.

L'exemple suivant montre comment ajouter des boutons radio à une feuille de calcul. L'exemple ajoute trois boutons radio représentant des groupes d'âge.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a new Workbook.
    Workbook excelbook;

    // Get the first worksheet
    Worksheet sheet = excelbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = sheet.GetCells();

    // Insert a value in C2
    Cell cellC2 = cells.Get(u"C2");
    cellC2.PutValue(u"Age Groups");

    // Set the font text bold.
    Style style = cellC2.GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);

    // Apply the style back
    cellC2.SetStyle(style);

    // Add radio buttons to the first sheet.
    ShapeCollection shapes = sheet.GetShapes();

    // Create first radio button
    RadioButton radio1= shapes.AddRadioButton(3, 0, 2, 0, 30, 110);


    // Set its text string.
    radio1.SetText(u"20-29");
    // Set A1 cell as a linked cell for the radio button.
    radio1.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio1.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line1 = radio1.GetLine();
    line1.SetWeight(4);
    // Set the dash style of the radio button.
    line1.SetDashStyle(MsoLineDashStyle::Solid);

    // Create second radio button
    RadioButton radio2 = shapes.AddRadioButton(6, 0, 2, 0, 30, 110);
    // Set its text string.
    radio2.SetText(u"30-39");
    // Set A1 cell as a linked cell for the radio button.
    radio2.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio2.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line2 = radio2.GetLine();
    line2.SetWeight(4);
    // Set the dash style of the radio button.
    line2.SetDashStyle(MsoLineDashStyle::Solid);

    // Create third radio button
    RadioButton radio3=shapes.AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string.
    radio3.SetText(u"40-49");
    // Set A1 cell as a linked cell for the radio button.
    radio3.SetLinkedCell(u"A1");
    // Make the radio button 3-D.
    radio3.SetShadow(true);
    // Set the weight of the radio button.
    LineFormat line3 = radio3.GetLine();
    line3.SetWeight(4);
    // Set the dash style of the radio button.
    line3.SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file.
    excelbook.Save(srcDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

La classe [**Aspose::Cells::Drawing::ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode appelée [**AddComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addcombobox/), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/). La classe [**Aspose::Cells::Drawing::ComboBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/) représente une liste déroulante. Elle possède des membres importants :

- La propriété [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée à la liste déroulante.
- La propriété [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La propriété [**GetDropDownLines()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getdropdownlines/) spécifie le nombre de lignes de la liste affichées dans la partie déroulante d'une liste déroulante.
- La propriété [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/combobox/getshadow/) indique si la liste déroulante a un ombrage en 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook.
    Workbook workbook;

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection.
    Cells cells = sheet.GetCells();

    // Input a value.
    Cell cellB3 = cells.Get(u"B3");
    cellB3.PutValue(u"Employee:");

    // Set it bold.
    Style style = cellB3.GetStyle();
    style.SetIsBorderApplied(true);
    cellB3.SetStyle(style);

    // Input some values that denote the input range for the combo box.
    cells.Get(u"A2").PutValue(u"Emp001");
    cells.Get(u"A3").PutValue(u"Emp002");
    cells.Get(u"A4").PutValue(u"Emp003");
    cells.Get(u"A5").PutValue(u"Emp004");
    cells.Get(u"A6").PutValue(u"Emp005");
    cells.Get(u"A7").PutValue(u"Emp006");

    // Add a new combo box.
    ComboBox comboBox = sheet.GetShapes().AddComboBox(2, 0, 2, 0, 22, 100);

    // Cleanup Aspose resources
    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Ajout de contrôle de libellé à une feuille de calcul**

Les libellés permettent de fournir aux utilisateurs des informations sur le contenu d'une feuille de calcul. Aspose.Cells permet d'ajouter et de manipuler des libellés dans une feuille de calcul. La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode appelée [**AddLabel**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlabel/), utilisée pour ajouter un contrôle de libellé à la feuille de calcul. La méthode renvoie un objet [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/). La classe [**Label**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/label/) représente un libellé dans la feuille de calcul. Elle possède des membres importants :

- La méthode [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie une chaîne de légende pour un libellé.
- La méthode [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie le [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la façon dont le libellé est attaché aux cellules dans la feuille de calcul.

L'exemple suivant montre comment ajouter un libellé à la feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new label to the worksheet
    Label label = sheet.GetShapes().AddLabel(2, 0, 2, 0, 60, 120);

    // Set the caption of the label
    label.SetText(u"This is a Label");

    // Set the Placement Type, the way the Label is attached to the cells
    label.SetPlacement(PlacementType::FreeFloating);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Label added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlistbox/), qui est utilisée pour ajouter un contrôle de liste déroulante à une feuille de calcul. La méthode renvoie un objet [**Aspose::Cells::Drawing::ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/). La classe [**ListBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/) représente une liste déroulante et possède certains membres importants :

- La méthode [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée à la liste déroulante.
- La méthode [**GetInputRange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getinputrange/) spécifie la plage de cellules de la feuille de calcul utilisée pour remplir la liste déroulante.
- La méthode [**SelectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/selectiontype/) spécifie le mode de sélection de la liste déroulante.
- La méthode [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/listbox/getshadow/) indique si la liste déroulante possède un ombrage 3D.

L'exemple suivant montre comment ajouter une liste déroulante à la feuille de calcul.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the worksheet cells collection
    Cells cells = sheet.GetCells();

    // Input a value
    cells.Get(U16String(u"B3")).PutValue(U16String(u"Choose Dept:"));

    // Set it bold
    Style style = cells.Get(U16String(u"B3")).GetStyle();
    Font font = style.GetFont();
    font.SetIsBold(true);
    cells.Get(U16String(u"B3")).SetStyle(style);

    // Input some values that denote the input range for the list box
    cells.Get(U16String(u"A2")).PutValue(U16String(u"Sales"));
    cells.Get(U16String(u"A3")).PutValue(U16String(u"Finance"));
    cells.Get(U16String(u"A4")).PutValue(U16String(u"MIS"));
    cells.Get(U16String(u"A5")).PutValue(U16String(u"R&D"));
    cells.Get(U16String(u"A6")).PutValue(U16String(u"Marketing"));
    cells.Get(U16String(u"A7")).PutValue(U16String(u"HRA"));

    // Add a new list box
    ListBox listBox = sheet.GetShapes().AddListBox(2, 0, 3, 0, 122, 100);

    // Set the placement type
    listBox.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell
    listBox.SetLinkedCell(U16String(u"A1"));

    // Set the input range
    listBox.SetInputRange(U16String(u"A2:A7"));

    // Set the selection type
    listBox.SetSelectionType(SelectionType::Single);

    // Set the list box with 3-D shading
    listBox.SetShadow(true);

    // Save the file
    workbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddButton**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addbutton/), utilisée pour ajouter un contrôle de bouton à la feuille de calcul. La méthode renvoie un objet [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/). La classe [**Aspose::Cells::Drawing::Button**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/button/) représente un bouton et possède certains membres importants :

- La propriété [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie la légende du bouton.
- La propriété [**Font**](https://reference.aspose.com/cells/cpp/aspose.cells/font/) spécifie les attributs de police pour l'étiquette du contrôle de bouton.
- La propriété [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie le [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), le mode d'attache du bouton aux cellules de la feuille de calcul.
- La propriété [**AddHyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/addhyperlink/) ajoute un lien hypertexte pour le contrôle de bouton. En cliquant sur le bouton, vous serez redirigé vers l'URL associée.

L'exemple suivant montre comment ajouter un bouton à la feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a new Workbook
    Workbook workbook;

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add a new button to the worksheet
    Drawing::Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);

    // Set the caption of the button
    button.SetText(u"Aspose");

    // Set the Placement Type, the way the Button is attached to the cells
    button.SetPlacement(PlacementType::FreeFloating);

    // Set the font name
    Font font = button.GetFont();
    font.SetName(u"Tahoma");

    // Set the caption string bold
    font.SetIsBold(true);

    // Set the color to blue
    font.SetColor(Color::Blue());

    // Set the hyperlink for the button
    button.AddHyperlink(u"http://www.aspose.com/");

    // Save the file
    workbook.Save(srcDir + u"book1.out.xls");

    std::cout << "Button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajout d'un contrôle de ligne dans la feuille de calcul**

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Formes automatiques**, pointez sur **Lignes**, et sélectionnez le style de ligne désiré.
1. Faites glisser pour dessiner la ligne.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre la ligne à être dessinée selon un angle de 15 degrés à partir de son point de départ, maintenez la touche MAJ enfoncée pendant le glissement.
   1. Pour allonger la ligne dans des directions opposées depuis le premier point d'extrémité, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addline/), qui est utilisée pour ajouter une forme de ligne à la feuille de calcul. La méthode retourne un objet [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/). La classe [**LineShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineshape/) représente une ligne. Elle possède des membres importants :

- La méthode [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) spécifie le format d'une ligne.
- La méthode [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie la [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la manière dont la ligne est attachée aux cellules de la feuille de calcul.

L'exemple suivant montre comment ajouter des lignes à la feuille de calcul. Il crée trois lignes avec différents styles.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a new line to the worksheet
    LineShape line1 = worksheet.GetShapes().AddLine(5, 0, 1, 0, 0, 250);

    // Set the line dash style
    line1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line1.SetPlacement(PlacementType::FreeFloating);

    // Add another line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line dash style
    line2.GetLine().SetDashStyle(MsoLineDashStyle::DashLongDash);

    // Set the weight of the line
    line2.GetLine().SetWeight(4);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Add the third line to the worksheet
    LineShape line3 = worksheet.GetShapes().AddLine(13, 0, 1, 0, 0, 250);

    // Set the line dash style
    line3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Set the placement
    line3.SetPlacement(PlacementType::FreeFloating);

    // Make the gridlines invisible in the first worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Lines added successfully to the worksheet!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Ajout d'une tête de flèche à une ligne**

Aspose.Cells vous permet également de dessiner des lignes fléchées. Il est possible d'ajouter une tête de flèche à une ligne et de formater la ligne. Par exemple, vous pouvez changer la couleur de la ligne ou spécifier l'épaisseur et le style de la ligne.

L'exemple suivant montre comment ajouter une tête de flèche à une ligne.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a line to the worksheet
    LineShape line2 = worksheet.GetShapes().AddLine(7, 0, 1, 0, 85, 250);

    // Set the line color
    line2.GetLine().SetFillType(FillType::Solid);
    line2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the weight of the line
    line2.GetLine().SetWeight(3);

    // Set the placement
    line2.SetPlacement(PlacementType::FreeFloating);

    // Set the line arrows
    line2.GetLine().SetEndArrowheadWidth(MsoArrowheadWidth::Medium);
    line2.GetLine().SetEndArrowheadStyle(MsoArrowheadStyle::Arrow);
    line2.GetLine().SetEndArrowheadLength(MsoArrowheadLength::Medium);
    line2.GetLine().SetBeginArrowheadStyle(MsoArrowheadStyle::ArrowDiamond);
    line2.GetLine().SetBeginArrowheadLength(MsoArrowheadLength::Medium);

    // Make the gridlines invisible in the first worksheet
    workbook.GetWorksheets().Get(0).SetIsGridlinesVisible(false);

    // Save the excel file
    workbook.Save(outDir + u"book1.out.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Ajout d'un contrôle de rectangle dans une feuille de calcul**

Aspose.Cells vous permet de dessiner des formes de rectangle dans vos feuilles de calcul. Vous pouvez créer un rectangle, un carré, etc. Vous avez également la possibilité de formater la couleur de remplissage et la couleur de la ligne de contrôle. Par exemple, vous pouvez changer la couleur du rectangle, définir la couleur de l'ombrage, spécifier le poids et le style du rectangle selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Rectangle**.
1. Faites glisser pour dessiner le rectangle.
1. Faites l'une ou les deux actions suivantes:
   1. Pour contraindre le rectangle à dessiner un carré depuis son point de départ, maintenez la touche SHIFT enfoncée pendant le glissement.
   1. Pour dessiner un rectangle à partir d'un point central, maintenez la touche CTRL enfoncée pendant le glissement.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddRectangle**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addrectangle/), qui est utilisée pour ajouter une forme de rectangle à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/). La classe [**Aspose.Cells.Drawing.RectangleShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/rectangleshape/) représente un rectangle. Elle possède certains membres importants:

- La propriété [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) spécifie les attributs de mise en forme de ligne d'un rectangle.
- La propriété [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie la manière dont le rectangle est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) spécifie les styles de mise en forme de remplissage d'un rectangle.

L'exemple suivant montre comment ajouter un rectangle à la feuille de calcul.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a rectangle control to the first worksheet
    RectangleShape rectangle = excelbook.GetWorksheets().Get(0).GetShapes().AddRectangle(3, 0, 2, 0, 70, 130);

    // Set the placement of the rectangle
    rectangle.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    rectangle.GetLine().SetWeight(4);

    // Set the dash style of the rectangle
    rectangle.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the Excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Rectangle shape added and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajout du Contrôle Arc à la Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes d'arc dans vos feuilles de calcul. Vous pouvez créer des arcs simples et pleins. Vous pouvez formater la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'arc, définir la couleur de dégradé, spécifier le poids et le style de la forme selon vos besoins.

### **Utilisation de Microsoft Excel**

1. Sur la barre d'outils **Dessin**, cliquez sur **Arc** dans les **Formes Automatiques**.
1. Faites glisser pour dessiner l'arc.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddArc**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addarc/), qui est utilisée pour ajouter une forme d'arc à une feuuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/). La classe [**Aspose.Cells.Drawing.ArcShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/arcshape/) représente un arc. Elle possède certains membres importants:

- La propriété [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) spécifie les attributs de mise en forme de ligne d'une forme d'arc.
- La propriété [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie la manière dont l'arc est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) spécifie les styles de format de remplissage de la forme.
- La propriété [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes d'arc à la feuille de calcul. L'exemple crée deux formes d'arc : l'une pleine et l'autre simple.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Add an arc shape
    ArcShape arc1 = worksheet.GetShapes().AddArc(2, 0, 2, 0, 130, 130);

    // Set the fill shape color
    arc1.GetFill().SetFillType(FillType::Solid);
    arc1.GetFill().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc1.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another arc shape
    ArcShape arc2 = worksheet.GetShapes().AddArc(9, 0, 2, 0, 130, 130);

    // Set the line color
    arc2.GetLine().SetFillType(FillType::Solid);
    arc2.GetLine().GetSolidFill().SetColor(Color::Blue());

    // Set the placement of the arc
    arc2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    arc2.GetLine().SetWeight(1);

    // Set the dash style of the arc
    arc2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    U16String outputPath = outDir + u"book1.out.xls";
    excelbook.Save(outputPath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Ajout du Contrôle Ovale à une Feuille de Calcul**

Aspose.Cells vous permet de dessiner des formes ovales dans les feuilles de calcul. Créez des formes ovales simples et pleines et formatez la couleur de remplissage et la couleur de la ligne de bordure du contrôle. Par exemple, vous pouvez spécifier / changer la couleur de l'ovale, définir la couleur de dégradé, spécifier le poids et le style de la forme.

### **Utilisation de Microsoft Excel**

- Sur la barre d'outils *Dessin*, cliquez sur *Ovale*.
- Faites glisser pour dessiner l'ovale.
- Faites l'une ou l'autre des choses suivantes :
- Pour contraindre l'ovale et dessiner un cercle à partir de son point de départ, maintenez la touche MAJ enfoncée tout en faisant glisser.
- Pour dessiner un ovale à partir d'un point central, maintenez la touche CTRL enfoncée tout en faisant glisser.

### **Utilisation d'Aspose.Cells**

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddOval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addoval/), qui permet d'ajouter une forme ovale à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/). La classe [**Aspose.Cells.Drawing.Oval**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oval/) représente une forme ovale. Elle possède des membres importants :

- La propriété [**LineFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/lineformat/) spécifie les attributs du format de ligne d'une forme ovale.
- La propriété [**GetPlacement()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getplacement/) spécifie la [**PlacementType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/placementtype/), la façon dont l'ovale est attaché aux cellules dans la feuille de calcul.
- La propriété [**FillFormat**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/fillformat/) spécifie les styles de format de remplissage de la forme.
- La propriété [**GetLowerRightRow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightrow/) spécifie l'index de la ligne du coin inférieur droit.
- La propriété [**GetLowerRightColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlowerrightcolumn/) spécifie l'index de la colonne du coin inférieur droit.

L'exemple suivant montre comment ajouter des formes ovales à la feuille de calcul. L'exemple crée deux formes ovales : une est un ovale rempli, l'autre est un simple cercle.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add an oval shape
    Oval oval1 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(2, 0, 2, 0, 130, 160);

    // Set the placement of the oval
    oval1.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval1.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another oval (circle) shape
    Oval oval2 = excelbook.GetWorksheets().Get(0).GetShapes().AddOval(9, 0, 2, 15, 130, 130);

    // Set the placement of the oval
    oval2.SetPlacement(PlacementType::FreeFloating);

    // Set the line weight
    oval2.GetLine().SetWeight(1);

    // Set the dash style of the oval
    oval2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    Aspose::Cells::Cleanup();
}
```

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode nommée [**AddSpinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addspinner/), qui permet d'ajouter un contrôle de type Spinner à une feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/). La classe [**Aspose.Cells.Drawing.Spinner**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/) représente un défilement. Elle possède des membres importants :

- La propriété [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée à la boîte de liste.
- La propriété [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmax/) spécifie la valeur maximale de la plage de la boîte de liste.
- La propriété [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getmin/) spécifie la valeur minimale de la plage de la boîte de liste.
- La propriété [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getincrementalchange/) spécifie la valeur pour laquelle un spinner est incrémenté lorsqu'une ligne est défilée.
- La propriété [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getshadow/) indique si la boîte de liste a un ombrage en 3D.
- La propriété [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/spinner/getcurrentvalue/) spécifie la valeur actuelle de la boîte de liste.

L'exemple suivant montre comment ajouter une boîte de liste à la feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a string value into A1 cell
    cells.Get(u"A1").PutValue(u"Select Value:");

    // Set the font color of the cell
    Style styleA1 = cells.Get(u"A1").GetStyle();
    styleA1.GetFont().SetColor(Color::Red());

    // Set the font text bold
    styleA1.GetFont().SetIsBold(true);

    // Input value into A2 cell
    cells.Get(u"A2").PutValue(0);

    // Set the shading color to black with solid background
    Style styleA2 = cells.Get(u"A2").GetStyle();
    styleA2.SetForegroundColor(Color::Black());
    styleA2.SetPattern(BackgroundType::Solid);

    // Set the font color of the cell
    styleA2.GetFont().SetColor(Color::White());

    // Set the font text bold
    styleA2.GetFont().SetIsBold(true);

    // Add a spinner control
    Spinner spinner = worksheet.GetShapes().AddSpinner(1, 0, 1, 0, 20, 18);

    // Set the placement type of the spinner
    spinner.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    spinner.SetLinkedCell(u"A2");

    // Set the maximum value
    spinner.SetMax(10);

    // Set the minimum value
    spinner.SetMin(0);

    // Set the incremental change for the control
    spinner.SetIncrementalChange(2);

    // Set it 3-D shading
    spinner.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode appelée [**AddScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addscrollbar/), qui est utilisée pour ajouter un contrôle de barre de défilement à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/). La classe [**Aspose.Cells.Drawing.ScrollBar**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/) représente une barre de défilement. Elle a quelques membres importants:

- La propriété [**GetLinkedCell()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlinkedcell/) spécifie une cellule liée à la barre de défilement.
- La propriété [**GetMax()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmax/) spécifie la valeur maximale pour la plage de la barre de défilement.
- La propriété [**GetMin()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getmin/) spécifie la valeur minimale pour la plage de la barre de défilement.
- La propriété [**GetIncrementalChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getincrementalchange/) spécifie la quantité de valeur par laquelle une barre de défilement est incrémentée d'un défilement de ligne.
- La propriété [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getshadow/) indique si la barre de défilement a un ombrage en 3D.
- La propriété [**GetCurrentValue()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getcurrentvalue/) spécifie la valeur actuelle de la barre de défilement.
- La propriété [**GetPageChange()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/scrollbar/getpagechange/) spécifie de combien la valeur actuelle sera incrémentée si vous cliquez à l'intérieur de la barre de défilement de chaque côté de la boîte de défilement.

L'exemple suivant montre comment ajouter une barre de défilement à la feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Get the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);

    // Invisible the gridlines of the worksheet
    worksheet.SetIsGridlinesVisible(false);

    // Get the worksheet cells
    Cells cells = worksheet.GetCells();

    // Input a value into A1 cell
    cells.Get(u"A1").PutValue(1);

    // Set the font color of the cell
    cells.Get(u"A1").GetStyle().GetFont().SetColor(Color::Maroon());

    // Set the font text bold
    cells.Get(u"A1").GetStyle().GetFont().SetIsBold(true);

    // Set the number format
    cells.Get(u"A1").GetStyle().SetNumber(1);

    // Add a scrollbar control
    ScrollBar scrollbar = worksheet.GetShapes().AddScrollBar(0, 0, 1, 0, 125, 20);

    // Set the placement type of the scrollbar
    scrollbar.SetPlacement(PlacementType::FreeFloating);

    // Set the linked cell for the control
    scrollbar.SetLinkedCell(u"A1");

    // Set the maximum value
    scrollbar.SetMax(20);

    // Set the minimum value
    scrollbar.SetMin(1);

    // Set the incr. change for the control
    scrollbar.SetIncrementalChange(1);

    // Set the page change attribute
    scrollbar.SetPageChange(5);

    // Set it 3-D shading
    scrollbar.SetShadow(true);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "Scrollbar added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

La classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) fournit une méthode appelée [**AddGroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addgroupbox/), qui est utilisée pour ajouter un contrôle de zone de groupe à la feuille de calcul. La méthode renvoie un objet [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/). De plus, la méthode [**Group**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/group/) de la classe [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) regroupe les formes, elle prend un tableau [**Shape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) en paramètre et renvoie un objet [**GroupShape**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupshape/). La classe [**Aspose.Cells.Drawing.GroupBox**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/) représente une zone de groupe. Elle possède quelques membres importants :

- La propriété [**GetText()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettext/) spécifie la chaîne de légende de la zone de groupe.
- La propriété [**GetShadow()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/groupbox/getshadow/) indique si la zone de groupe a un ombrage 3D.

L'exemple suivant montre comment ajouter une zone de groupe et regrouper les contrôles dans la feuille de calcul.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook excelbook;

    // Add a group box to the first worksheet
    Worksheet worksheet = excelbook.GetWorksheets().Get(0);
    GroupBox box = worksheet.GetShapes().AddGroupBox(1, 0, 1, 0, 300, 250);

    // Set the caption of the group box
    box.SetText(u"Age Groups");
    box.SetPlacement(PlacementType::FreeFloating);

    // Make it 2-D box
    box.SetShadow(false);

    // Add a radio button
    RadioButton radio1 = worksheet.GetShapes().AddRadioButton(3, 0, 2, 0, 30, 110);

    // Set its text string
    radio1.SetText(u"20-29");

    // Set A1 cell as a linked cell for the radio button
    radio1.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio1.SetShadow(true);

    // Set the weight of the radio button
    radio1.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio1.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio2 = worksheet.GetShapes().AddRadioButton(6, 0, 2, 0, 30, 110);

    // Set its text string
    radio2.SetText(u"30-39");

    // Set A1 cell as a linked cell for the radio button
    radio2.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio2.SetShadow(true);

    // Set the weight of the radio button
    radio2.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio2.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Add another radio button
    RadioButton radio3 = worksheet.GetShapes().AddRadioButton(9, 0, 2, 0, 30, 110);

    // Set its text string
    radio3.SetText(u"40-49");

    // Set A1 cell as a linked cell for the radio button
    radio3.SetLinkedCell(u"A1");

    // Make the radio button 3-D
    radio3.SetShadow(true);

    // Set the weight of the radio button
    radio3.GetLine().SetWeight(4);

    // Set the dash style of the radio button
    radio3.GetLine().SetDashStyle(MsoLineDashStyle::Solid);

    // Get the shapes
    Vector<Shape> shapeobjects{ box, radio1, radio2, radio3 };

    // Group the shapes
    GroupShape group = worksheet.GetShapes().Group(shapeobjects);

    // Save the excel file
    excelbook.Save(outDir + u"book1.out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Ajouter des contrôles ActiveX à l'aide de Aspose.Cells](/cells/fr/cpp/add-activex-controls-using-aspose-cells/)
- [Supprimer le contrôle ActiveX](/cells/fr/cpp/remove-activex-control/)
- [Mise à jour du contrôle ComboBox ActiveX](/cells/fr/cpp/update-activex-combobox-control/)
{{< app/cells/assistant language="cpp" >}}
