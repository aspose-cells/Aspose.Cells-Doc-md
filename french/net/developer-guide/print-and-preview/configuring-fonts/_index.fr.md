---
title: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/net/configuring-fonts-for-rendering-spreadsheets/
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells offrent la possibilité de rendre les feuilles de calcul sous forme d'images et de les convertir en formats PDF et XPS. Afin de maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells tenteront de substituer les polices requises par celles disponibles.

## **Sélection des polices**

Voici le processus suivi par les API Aspose.Cells en arrière-plan.

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne parvient pas à trouver les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) du classeur.
1. Si l'API ne parvient pas à localiser la police définie dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font) du classeur, elle tente d'utiliser la police spécifiée dans la propriété [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) ou [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont).
1. Si l'API ne parvient pas à localiser la police définie dans [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont) ou [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont), elle tente d'utiliser la police spécifiée dans [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname).
1. Si l'API ne parvient pas à localiser la police définie dans [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname), elle tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si l'API ne trouve pas de polices sur le système de fichiers, elle rend la feuille de calcul en utilisant Arial.

{{% alert color="primary" %}}

En général, les API Aspose.Cells analysent par défaut les répertoires de polices par défaut du système d'exploitation sous Windows, Linux, MacOS. À partir de [Aspose.Cells for .NET 24.7](https://releases.aspose.com/cells/net/release-notes/2024/aspose-cells-for-net-24-7-release-notes/), les API analysent également par défaut les répertoires de polices en cache dans le cloud Office.

{{% /alert %}}

## **Définir des dossiers de polices personnalisés**

Les APIs Aspose.Cells recherchent le répertoire de police par défaut du système d'exploitation pour les polices requises. Si les polices requises ne sont pas disponibles dans le répertoire de police du système, les APIs recherchent dans les répertoires personnalisés (définis par l'utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs) a exposé plusieurs façons de définir des répertoires de polices personnalisées comme détaillé ci-dessous.

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders): Cette méthode est utile lorsque les polices résident dans des dossiers multiples et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de dossiers multiples ou d'un seul fichier de police ou de données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

Les deux méthodes [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder) et [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders) acceptent un deuxième paramètre de type Boolean. Passer **true** en tant que deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers des fichiers de polices.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'appeler d'autres objets des APIs Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de polices, seuls les derniers réglages prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les APIs Aspose.Cells offrent également la possibilité de spécifier la police de substitution à des fins de rendu. Ce mécanisme est utile lorsque la police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de police en remplacement de la police initialement requise. Pour ce faire, les APIs Aspose.Cells ont exposé la méthode [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes), qui accepte 2 paramètres. Le premier paramètre est de type **string**, qui devrait être le nom de la police qui doit être remplacée. Le deuxième paramètre est un tableau de type **string**. Les utilisateurs peuvent fournir une liste de noms de police en substitution au nom de police d'origine (spécifié dans le premier paramètre).

Voici un scénario d'utilisation simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **Collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les APIs Aspose.Cells ont également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. La méthode [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase) contenant la liste des sources de police spécifiées. Au cas où aucune source n'a été définie, la méthode [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources) renverra un tableau vide.
1. La méthode [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) accepte un paramètre de type **string** permettant de spécifier le nom de la police pour laquelle la substitution a été définie. Dans le cas où aucune substitution n'a été définie pour le nom de police spécifié, la méthode [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes) renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont des PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/net/supported-font-formats/)
- [Feuille de calcul vers Image - Définir le format de pixel pour l'image rendue](/cells/fr/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
{{< app/cells/assistant language="csharp" >}}
