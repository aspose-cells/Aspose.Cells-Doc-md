---
title: Police du thème pour les titres et le corps en C++
linktitle: Police de thème pour les en têtes et le corps
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de tableur. Elle supporte la définition des polices de thème pour les titres et le corps dans les documents Excel, permettant aux utilisateurs de personnaliser l apparence et le style du document. Cet article présentera comment utiliser la bibliothèque Aspose.Cells pour travailler avec les polices de thème pour les titres et le corps dans les documents Excel.
keywords: Aspose.Cells, Document Excel, En tête, Corps, Police de thème, Apparence, Style
type: docs
weight: 120
url: /fr/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

La police par défaut changera automatiquement lorsque le paramètre régionale est modifié.

Si la police par défaut est modifiée, la hauteur de la ligne et la largeur de la colonne seront également modifiées, et cela pourrait même perturber la mise en page.

Qu'est-ce qui a causé le changement de la police par défaut?

Si la police de thème Excel est définie, Excel basculera automatiquement entre différentes polices en fonction de l'environnement linguistique actuel.

{{% /alert %}}

## **Polices de thème pour les en-têtes et le corps dans Excel**

Dans Excel, sélectionnez l'onglet Accueil, cliquez sur la liste déroulante de police, vous verrez "Polices de thème" avec deux polices de thème : Calibri Light (Titres) et Calibri (Corps) en haut avec le paramètre régional en anglais.

**![Polices de thème](Theme-Fonts.png)**

Si la police de thème est sélectionnée, le nom de la police s'affichera différemment selon les régions.
Si vous ne souhaitez pas que la police soit automatiquement modifiée dans différentes régions, ne sélectionnez pas les deux polices de thème.

## **Modifier la police des titres et du corps de manière programmée**
Avec Aspose.Cells for C++, nous pouvons vérifier si la police par défaut est une police de thème ou définir la police de thème avec la propriété [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/).

Le code d'exemple suivant montre comment manipuler la police de thème.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Récupération dynamique de la police de thème locale de manière programmatique**
Parfois, nos serveurs et les machines des utilisateurs ne sont pas dans la même région. Comment pouvons-nous obtenir la même police que les utilisateurs souhaitent pour le traitement de fichiers?

Nous devons définir les paramètres régionaux du système avant de charger le fichier avec la propriété [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/).

Le code d'exemple suivant montre comment obtenir la police de thème locale.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
