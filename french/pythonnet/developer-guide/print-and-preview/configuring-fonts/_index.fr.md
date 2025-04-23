---
title: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/python-net/configuring-fonts-for-rendering-spreadsheets/
---

## **Scénarios d'utilisation possibles**

Les APIs Aspose.Cells pour Python via .NET permettent de rendre les feuilles de calcul sous forme d’images ainsi que de les convertir en formats PDF et XPS. Pour maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d’exploitation. Si les polices requises ne sont pas présentes, les APIs Aspose.Cells pour Python via .NET tenteront de substituer les polices nécessaires par celles disponibles.

## **Sélection des polices**

Voici le processus que suivent les APIs Aspose.Cells pour Python via .NET en coulisses.

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne parvient pas à trouver les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) du classeur.
1. Si l'API ne parvient pas à localiser la police définie dans la propriété [**DefaultStyle.font**](https://reference.aspose.com/cells/python-net/aspose.cells/style/font) du classeur, elle tente d'utiliser la police spécifiée dans la propriété [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) ou [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font).
1. Si l'API ne parvient pas à localiser la police définie dans [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) ou [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font), elle tente d'utiliser la police spécifiée dans [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name).
1. Si l'API ne parvient pas à localiser la police définie dans [**FontConfigs.default_font_name**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/default_font_name), elle tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si l'API ne trouve pas de polices sur le système de fichiers, elle rend la feuille de calcul en utilisant Arial.

## **Définir des dossiers de polices personnalisés**

Les APIs Aspose.Cells pour Python via .NET recherchent dans le répertoire de polices par défaut du système d’exploitation pour les polices requises. Si ces polices ne sont pas disponibles dans le répertoire, elles recherchent dans des répertoires personnalisés (définis par l’utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs) expose plusieurs moyens de définir des répertoires de polices personnalisés comme détaillé ci-dessous.

1. [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/): Cette méthode est utile lorsque les polices résident dans des dossiers multiples et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.set_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_sources/#list): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de dossiers multiples ou d'un seul fichier de police ou de données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

Les méthodes [**FontConfigs.set_font_folder**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folder/) et [**FontConfigs.set_font_folders**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_folders/) acceptent toutes deux un second paramètre de type Boolean. Passer **true** comme second paramètre indicera aux APIs Aspose.Cells pour Python via .NET de rechercher dans les sous-dossiers les fichiers de police.

{{% /alert %}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-1.py" >}}

{{% alert color="primary" %}}

Veillez à utiliser l’une des méthodes mentionnées ci-dessus au début de l’application, c’est-à-dire avant d’invoquer d’autres objets de l’API Aspose.Cells pour Python via .NET.

{{% /alert %}} {{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de polices, seuls les derniers réglages prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les APIs Aspose.Cells pour Python via .NET offrent également la possibilité de spécifier une police de substitution pour le rendu. Ce mécanisme est utile lorsqu’une police requise n’est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices comme alternative à la police initialement requise. Pour ce faire, les APIs Aspose.Cells pour Python via .NET ont exposé la méthode [**FontConfigs.set_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/set_font_substitutes/#str-list) qui accepte 2 paramètres. Le premier paramètre est de type **string**, qui doit être le nom de la police à substituer. Le second est un tableau de type **string**. Les utilisateurs peuvent fournir une liste de noms de police comme substitution à la police d’origine (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetCustomFontFolders-FontSubstitution.py" >}}

## **Collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les APIs Aspose.Cells pour Python via .NET ont également fourni des moyens de recueillir des informations sur les sources et substitutions qui ont été configurées.

1. La méthode [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsourcebase) contenant la liste des sources de police spécifiées. Au cas où aucune source n'a été définie, la méthode [**FontConfigs.get_font_sources**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_sources/#) renverra un tableau vide.
1. La méthode [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) accepte un paramètre de type **string** permettant de spécifier le nom de la police pour laquelle la substitution a été définie. Dans le cas où aucune substitution n'a été définie pour le nom de police spécifié, la méthode [**FontConfigs.get_font_substitutes**](https://reference.aspose.com/cells/python-net/aspose.cells/fontconfigs/get_font_substitutes/#str) renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/python-net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont des PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/python-net/supported-font-formats/)
- [Feuille de calcul vers Image - Définir le format de pixel pour l'image rendue](/cells/fr/python-net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)

