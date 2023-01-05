---
title: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/java/configuring-fonts-for-rendering-spreadsheets/
---
## **Scénarios d'utilisation possibles**

Les API Aspose.Cells permettent de restituer les feuilles de calcul dans des formats d'image et de les convertir aux formats PDF et XPS. Afin de maximiser la fidélité de conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells essaieront de remplacer les polices requises par celles disponibles.

## **Sélection de polices**

Vous trouverez ci-dessous le processus suivi par les API Aspose.Cells en arrière-plan.

1. Le API essaie de trouver les polices sur le système de fichiers correspondant au nom de police exact utilisé dans la feuille de calcul.
1.  Si API ne trouve pas les polices portant exactement le même nom, il tente d'utiliser la police par défaut spécifiée sous le classeur.[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) la propriété.
1.  Si API ne peut pas localiser la police définie sous le classeur[**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) propriété, il tente d'utiliser la police spécifiée sous[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) ou alors[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) la propriété.
1.  Si API ne trouve pas la police définie sous[**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) ou alors[**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont) propriété, il tente d'utiliser la police spécifiée sous[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) la propriété.
1.  Si API ne trouve pas la police définie sous[**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName) propriété, il essaie de sélectionner les polices les plus appropriées parmi toutes les polices disponibles.
1. Enfin, si API ne trouve aucune police sur le système de fichiers, il affiche la feuille de calcul à l'aide d'Arial.

{{% alert color="primary" %}}

 Les API Aspose.Cells analysent toujours le répertoire de polices par défaut du système d'exploitation à une exception près, c'est-à-dire ; quand les arguments JVM**-DAspose.Cells.FontDirExc="VotreRepFont"**sont définis. Dans ce cas, les API Aspose.Cells ignoreront l'analyse du répertoire de polices par défaut du système d'exploitation et ne rechercheront que le chemin spécifié dans les arguments JVM susmentionnés.

{{% /alert %}}

## **Définir des dossiers de polices personnalisés**

 Aspose.Cells Les API recherchent dans le répertoire de polices par défaut du système d'exploitation les polices requises. Si les polices requises ne sont pas disponibles dans le répertoire des polices du système, les API recherchent dans les répertoires personnalisés (définis par l'utilisateur). Le[**Configurations de polices**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs)class a exposé un certain nombre de façons de définir des répertoires de polices personnalisés, comme indiqué ci-dessous.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) : cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)) : cette méthode est utile lorsque les polices résident dans plusieurs dossiers et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de plusieurs dossiers ou d'un seul fichier de police ou des données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

 Tous les deux[**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean) ) acceptent un deuxième paramètre de type booléen. Qui passe**vrai**comme deuxième paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers pour les fichiers de polices.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'invoquer tout autre objet des API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si plusieurs des méthodes mentionnées ci-dessus sont utilisées pour définir les sources de police, seuls les derniers paramètres prendront effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les API Aspose.Cells offrent également la possibilité de spécifier la police de substitution à des fins de rendu. Ce mécanisme est utile lorsqu'une police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices comme alternative à la police requise à l'origine. Pour ce faire, les API Aspose.Cells ont exposé la méthode FontConfigs.setFontSubstitutes qui accepte 2 paramètres. Le premier paramètre est de type**Chaîne de caractères** , qui doit être le nom de la police à remplacer. Le deuxième paramètre est un tableau de type**Chaîne de caractères**. Les utilisateurs peuvent fournir une liste de noms de polices en remplacement de la police d'origine (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple.

{{< highlight "java" >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[]{ "Times New Roman", "Calibri" });

{{< /highlight >}}

## **La collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les API Aspose.Cells ont également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources() ) : cette méthode renvoie un tableau de type[**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource)contenant la liste des sources de polices spécifiées. Si aucune source n'a été définie, le[**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources()) renverra un tableau vide.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String) ): Cette méthode accepte un paramètre de type**Chaîne de caractères** permettant de spécifier le nom de la police pour laquelle la substitution a été définie. Si aucune substitution n'a été définie pour le nom de police spécifié, le[**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) retournera null.
