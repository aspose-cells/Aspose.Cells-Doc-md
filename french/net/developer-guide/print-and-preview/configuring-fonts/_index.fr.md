---
title: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/net/configuring-fonts-for-rendering-spreadsheets/
---
## **Scénarios d'utilisation possibles**

Les API Aspose.Cells permettent de restituer les feuilles de calcul dans des formats d'image et de les convertir aux formats PDF et XPS. Afin de maximiser la fidélité de conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells essaieront de remplacer les polices requises par celles disponibles.

## **Sélection de polices**

Vous trouverez ci-dessous le processus suivi par les API Aspose.Cells en arrière-plan.

1. Le API essaie de trouver les polices sur le système de fichiers correspondant au nom de police exact utilisé dans la feuille de calcul.
1.  Si API ne trouve pas les polices portant exactement le même nom, il tente d'utiliser la police par défaut spécifiée sous le classeur.**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** la propriété.
1.  Si API ne peut pas localiser la police définie sous le classeur**[DefaultStyle.Font](https://reference.aspose.com/cells/net/aspose.cells/style/properties/font)** propriété, il tente d'utiliser la police spécifiée sous**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** ou alors**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** la propriété.
1.  Si API ne trouve pas la police définie sous**[PdfSaveOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/defaultfont)** ou alors**[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/defaultfont)** propriété, il tente d'utiliser la police spécifiée sous**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** la propriété.
1.  Si API ne trouve pas la police définie sous**[FontConfigs.DefaultFontName](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/properties/defaultfontname)** propriété, il essaie de sélectionner les polices les plus appropriées parmi toutes les polices disponibles.
1. Enfin, si API ne trouve aucune police sur le système de fichiers, il affiche la feuille de calcul à l'aide d'Arial.

## **Définir des dossiers de polices personnalisés**

 Aspose.Cells Les API recherchent dans le répertoire de polices par défaut du système d'exploitation les polices requises. Si les polices requises ne sont pas disponibles dans le répertoire des polices du système, les API recherchent dans les répertoires personnalisés (définis par l'utilisateur). Le**[FontConfigs](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs)**class a exposé un certain nombre de façons de définir des répertoires de polices personnalisés, comme indiqué ci-dessous.

1. **[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)**: Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)**: Cette méthode est utile lorsque les polices résident dans plusieurs dossiers et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. **[FontConfigs.SetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsources)**: Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de plusieurs dossiers ou d'un seul fichier de police ou des données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

 Tous les deux**[FontConfigs.SetFontFolder](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolder)** & **[FontConfigs.SetFontFolders](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontfolders)** acceptent un deuxième paramètre de type booléen. Qui passe**vrai** car le deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers des fichiers de polices.

{{% /alert %}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-1.cs" >}}

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'invoquer tout autre objet des API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si toutes les méthodes mentionnées ci-dessus sont utilisées pour définir les sources de police, seuls les derniers paramètres prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

 Les API Aspose.Cells offrent également la possibilité de spécifier la police de substitution à des fins de rendu. Ce mécanisme est utile lorsqu'une police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices comme alternative à la police requise à l'origine. Pour ce faire, les API Aspose.Cells ont exposé le**[FontConfigs.SetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/setfontsubstitutes)** méthode qui accepte 2 paramètres. Le premier paramètre est de type**chaîne de caractères** , qui doit être le nom de la police à remplacer. Le deuxième paramètre est un tableau de type**chaîne de caractères**Les utilisateurs peuvent fournir une liste de noms de polices en remplacement du nom de police d'origine (spécifié dans le premier paramètre).

Voici un scénario d'utilisation simple.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-SetCustomFontFolders-FontSubstitution.cs" >}}

## **La collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les API Aspose.Cells ont également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. **[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)** la méthode renvoie un tableau de type**[FontSourceBase](https://reference.aspose.com/cells/net/aspose.cells/fontsourcebase)**contenant la liste des sources de polices spécifiées. Si aucune source n'a été définie, le**[FontConfigs.GetFontSources](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsources)**méthode renverra un tableau vide.
1. **[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)** la méthode accepte un paramètre de type**chaîne de caractères** permettant de spécifier le nom de la police pour laquelle la substitution a été définie. Si aucune substitution n'a été définie pour le nom de police spécifié, le**[FontConfigs.GetFontSubstitutes](https://reference.aspose.com/cells/net/aspose.cells/fontconfigs/methods/getfontsubstitutes)**méthode renverra null.

## **Sujets avancés**
- [Définir la police par défaut lors du rendu de la feuille de calcul en images](/cells/fr/net/set-default-font-while-rendering-spreadsheet-to-images/)
- [Définir la propriété DefaultFont de PdfSaveOptions et ImageOrPrintOptions pour avoir la priorité](/cells/fr/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Formats de police pris en charge](/cells/fr/net/supported-font-formats/)
- [Feuille de calcul à l'image - Définir le format de pixel pour l'image rendue](/cells/fr/net/worksheet-to-image-set-pixel-format-for-the-rendered-image/)
