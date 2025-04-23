---
title: Thèmes et couleurs d Excel avec C++
linktitle: Thèmes et couleurs Excel
type: docs
weight: 100
url: /fr/cpp/excel-themes-and-colors/
description: Code C++ pour utiliser le schéma de couleurs d Excel avec l API Aspose.Cells for C++
keywords: C++ pour créer et appliquer des schémas de couleurs, créer programmétiquement un schéma de couleurs personnalisé, appliquer un schéma de couleurs personnalisé de manière programmatique, comment utiliser un schéma de couleurs dans Excel en C++
---

## **Comment appliquer et créer un schéma de couleurs dans Excel**
Les thèmes de document facilitent la coordination des couleurs, polices et effets de formatage graphique des documents Excel et permettent de les mettre à jour rapidement. 
Les thèmes fournissent un aspect unifié avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1, par exemple, a un aspect différent dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document, puis vous le modifiez selon vos souhaits.

### **Comment appliquer un schéma de couleurs dans Excel**
1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".
<br>
<img src="color.png" width=70% />
1. Choisissez une palette de couleurs qui correspond à vos besoins ou survolez un schéma pour voir un aperçu en direct.

### **Comment créer un schéma de couleurs personnalisé dans Excel**
Vous pouvez créer votre propre jeu de couleurs pour donner à votre document un aspect frais et unique ou pour respecter les normes de votre organisation.

1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".
1. Cliquez sur le bouton "Personnaliser les couleurs...".
<br>
<img src="color2.png" width=70% />

1. Dans la boîte de dialogue "Créer de nouveaux thèmes de couleurs", vous pouvez sélectionner des couleurs pour chaque élément en cliquant sur les listes déroulantes de couleurs à côté. Vous pouvez choisir des couleurs dans la palette ou définir des couleurs personnalisées à l'aide de l'option "Plus de couleurs".
<br>
<img src="color3.png" width=70% />
1. Après avoir sélectionné toutes les couleurs souhaitées, donnez un nom à votre schéma de couleurs personnalisé dans le champ "Nom".

1. Cliquez sur le bouton "Enregistrer" pour enregistrer votre schéma de couleurs personnalisé. Votre schéma de couleurs personnalisé sera désormais disponible dans le menu déroulant "Couleurs" pour une utilisation future.

## **Comment créer et appliquer un schéma de couleurs dans Aspose.Cells**
Aspose.Cells offre des fonctionnalités pour personnaliser les thèmes et les couleurs.

### **Comment créer un thème de couleurs personnalisé dans Aspose.Cells**
Si des couleurs de thème sont utilisées dans le fichier, nous n'avons pas besoin de modifier chaque cellule individuellement, nous devons simplement modifier les couleurs dans le thème.

L'exemple suivant montre comment appliquer des thèmes personnalisés avec vos couleurs souhaitées. Nous utilisons un fichier modèle d'exemple créé manuellement dans Microsoft Excel 2007.

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Define Color array (of 12 colors) for Theme
    Vector<Aspose::Cells::Color> carr(12);
    carr[0] = Color::AntiqueWhite(); // Background1
    carr[1] = Color::Brown();       // Text1
    carr[2] = Color::AliceBlue();   // Background2
    carr[3] = Color::Yellow();      // Text2
    carr[4] = Color::YellowGreen(); // Accent1
    carr[5] = Color::Red();         // Accent2
    carr[6] = Color::Pink();        // Accent3
    carr[7] = Color::Purple();      // Accent4
    carr[8] = Color::PaleGreen();   // Accent5
    carr[9] = Color::Orange();      // Accent6
    carr[10] = Color::Green();      // Hyperlink
    carr[11] = Color::Gray();       // Followed Hyperlink

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Instantiate a Workbook and open the template file
    Workbook workbook(inputFilePath);

    // Set the custom theme with specified colors
    workbook.CustomTheme(u"CustomeTheme1", carr);

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Save as the excel file
    workbook.Save(outputFilePath);

    std::cout << "Custom theme applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment appliquer les couleurs de thème dans Aspose.Cells**

L'exemple suivant applique les couleurs d'avant-plan et de police d'une cellule en fonction des types de couleurs de thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook
    Workbook workbook;

    // Get cells collection in the first (default) worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get the D3 cell
    Cell c = cells.Get(u"D3");

    // Get the style of the cell
    Style s = c.GetStyle();

    // Set foreground color for the cell from the default theme Accent2 color
    s.SetForegroundThemeColor(ThemeColor(ThemeColorType::Accent2, 0.5));

    // Set the pattern type
    s.SetPattern(BackgroundType::Solid);

    // Get the font for the style
    Font f = s.GetFont();

    // Set the theme color
    f.SetThemeColor(ThemeColor(ThemeColorType::Accent4, 0.1));

    // Apply style
    c.SetStyle(s);

    // Put a value
    c.PutValue(u"Testing1");

    // Save the excel file
    workbook.Save(outDir + u"output.out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Comment obtenir et définir les couleurs de thème dans Aspose.Cells**
 Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.

- [**Style.GetForegroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getforegroundthemecolor/): Utilisé pour définir la couleur avant-plan.
- [**Style.GetBackgroundThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getbackgroundthemecolor/): Utilisé pour définir la couleur arrière-plan.
- [**Font.GetThemeColor()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getthemecolor/): Utilisé pour définir la couleur de la police.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getthemecolor/): Utilisé pour obtenir une couleur de thème.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/setthemecolor/): Utilisé pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir les couleurs de thème.

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Microsoft Excel.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the Background1 theme color
    Color c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the color
    std::cout << "theme color Background1: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Get the Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the color
    std::cout << "theme color Accent2: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Background1 theme color
    workbook.SetThemeColor(ThemeColorType::Background1, Color::Red());

    // Get the updated Background1 theme color
    c = workbook.GetThemeColor(ThemeColorType::Background1);

    // Print the updated color for confirmation
    std::cout << "theme color Background1 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Change the Accent2 theme color
    workbook.SetThemeColor(ThemeColorType::Accent2, Color::Blue());

    // Get the updated Accent2 theme color
    c = workbook.GetThemeColor(ThemeColorType::Accent2);

    // Print the updated color for confirmation
    std::cout << "theme color Accent2 changed to: " << c.r << ", " << c.g << ", " << c.b << std::endl;

    // Save the updated file
    workbook.Save(outputFilePath);

    std::cout << "Theme colors updated and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Sujets avancés**
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/cpp/extract-theme-data-from-excel-file/)
