---
title: Configurer les polices pour le rendu des feuilles de calcul avec C++
linktitle: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Apprenez comment configurer les polices pour le rendu des feuilles de calcul en images, PDF et XPS à l aide de Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells offrent la possibilité de rendre les feuilles de calcul en formats image ainsi que de les convertir en formats PDF et XPS. Pour maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells tenteront de substituer les polices requises par celles disponibles.

## **Sélection des polices**

Voici le processus que suivent les API Aspose.Cells en coulisses :

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne trouve pas les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) du classeur.
1. Si l'API ne peut pas localiser la police définie dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) du classeur, elle tente d'utiliser la police spécifiée dans [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) ou la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/).
1. Si l'API ne peut pas localiser la police définie dans [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) ou la propriété [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), elle tente d'utiliser la police spécifiée dans la propriété [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/).
1. Si l'API ne peut pas localiser la police définie dans la propriété [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/), elle tente de sélectionner les polices les plus appropriées parmi toutes celles disponibles.
1. Enfin, si l'API ne trouve aucune police sur le système de fichiers, elle rend le classeur en utilisant Arial.

## **Définir des dossiers de polices personnalisés**

Les API Aspose.Cells recherchent dans le répertoire de polices par défaut du système d'exploitation les polices requises. Si les polices requises ne sont pas disponibles dans ce répertoire, les API recherchent dans des répertoires personnalisés (définis par l'utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) offre plusieurs méthodes pour définir des répertoires de polices personnalisés, détaillées ci-dessous :

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) : Cette méthode est utile lorsque les polices résident dans plusieurs dossiers, et que l'utilisateur souhaite définir chaque dossier séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/) : Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de plusieurs dossiers, d'un seul fichier de police ou de données de police provenant d'un tableau d'octets.

{{% alert color="primary" %}}

Les méthodes [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) et [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) acceptent toutes deux un second paramètre de type Boolean. Passer **true** comme second paramètre indiquera aux API Aspose.Cells de rechercher les fichiers de police dans les sous-dossiers.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au démarrage de l'application, c'est-à-dire avant d'invoquer d'autres objets des API Aspose.Cells.

{{% /alert %}}

{{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de polices, seuls les derniers réglages prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les API Aspose.Cells offrent également la possibilité de spécifier des polices de substitution à des fins de rendu. Ce mécanisme est utile lorsqu'une police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices en alternative à la police initialement requise. Pour cela, les API Aspose.Cells ont exposé la méthode [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/), qui accepte deux paramètres. Le premier est de type **string**, qui doit être le nom de la police à substituer. Le second est un tableau de type **string**. Les utilisateurs peuvent fournir une liste de noms de polices en substitution à la police originale (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple :

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les API Aspose.Cells offrent également des moyens de recueillir des informations sur les sources et substitutions qui ont été définies :

1. La méthode [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) contenant la liste des sources de police spécifiées. Si aucune source n'a été définie, la méthode [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) renverra un tableau vide.
1. La méthode [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) accepte un paramètre de type **string**, vous permettant de spécifier le nom de police pour laquelle une substitution a été définie. Si aucune substitution n'a été définie pour le nom de police spécifié, la méthode [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont des PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/cpp/supported-font-formats/)
{{< app/cells/assistant language="cpp" >}}
