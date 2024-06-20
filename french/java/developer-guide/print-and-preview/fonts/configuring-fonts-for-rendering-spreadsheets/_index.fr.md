---
title: Configuration des polices pour le rendu des feuilles de calcul
type: docs
weight: 10
url: /fr/java/configuring-fonts-for-rendering-spreadsheets/
---

## **Scénarios d'utilisation possibles**

Les API Aspose.Cells offrent la possibilité de rendre les feuilles de calcul sous forme d'images et de les convertir en formats PDF et XPS. Afin de maximiser la fidélité de la conversion, il est nécessaire que les polices utilisées dans la feuille de calcul soient disponibles dans le répertoire de polices par défaut du système d'exploitation. Si les polices requises ne sont pas présentes, les API Aspose.Cells tenteront de substituer les polices requises par celles disponibles.

## **Sélection des polices**

Voici le processus suivi par les API Aspose.Cells en arrière-plan.

1. L'API tente de trouver les polices sur le système de fichiers correspondant exactement au nom de police utilisé dans la feuille de calcul.
1. Si l'API ne parvient pas à trouver les polices portant le même nom exact, elle tente d'utiliser la police par défaut spécifiée dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) du classeur.
1. Si l'API ne parvient pas à localiser la police définie dans la propriété [**DefaultStyle.Font**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Font) du classeur, elle tente d'utiliser la police spécifiée dans la propriété [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) ou [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont).
1. Si l'API ne parvient pas à localiser la police définie dans [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveoptions#DefaultFont) ou [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions#DefaultFont), elle tente d'utiliser la police spécifiée dans [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName).
1. Si l'API ne parvient pas à localiser la police définie dans [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs#DefaultFontName), elle tente de sélectionner les polices les plus adaptées parmi toutes les polices disponibles.
1. Enfin, si l'API ne trouve pas de polices sur le système de fichiers, elle rend la feuille de calcul en utilisant Arial.

{{% alert color="primary" %}}

Les APIs Aspose.Cells scannent toujours le répertoire de polices par défaut du système d'exploitation à une exception près, à savoir ; lorsque les arguments JVM **-DAspose.Cells.FontDirExc="VotreDossierPolice"** sont définis. Dans ce cas, les APIs Aspose.Cells ignoreront le scan du répertoire de polices par défaut du système d'exploitation et ne chercheront que le chemin spécifié dans les arguments JVM mentionnés ci-dessus.

{{% /alert %}}

## **Définir des dossiers de polices personnalisés**

Les APIs Aspose.Cells recherchent le répertoire de polices par défaut du système d'exploitation pour les polices requises. Si les polices requises ne sont pas disponibles dans le répertoire de polices du système, alors les APIs recherchent dans les répertoires personnalisés (définis par l'utilisateur). La classe [**FontConfigs**](https://reference.aspose.com/cells/java/com.aspose.cells/FontConfigs) a exposé plusieurs façons de définir les répertoires de polices personnalisés comme détaillé ci-dessous.

1. [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)): Cette méthode est utile s'il n'y a qu'un seul dossier à définir.
1. [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)): Cette méthode est utile lorsque les polices résident dans des dossiers multiples et que l'utilisateur souhaite définir tous les dossiers séparément plutôt que de combiner toutes les polices dans un seul dossier.
1. [**FontConfigs.setFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontSources(com.aspose.cells.FontSourceBase[])): Ce mécanisme est utile lorsque l'utilisateur souhaite charger des polices à partir de dossiers multiples ou d'un seul fichier de police ou de données de police à partir d'un tableau d'octets.

{{% alert color="primary" %}}

Les deux méthodes [**FontConfigs.setFontFolder**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolder(java.lang.String,%20boolean)) & [**FontConfigs.setFontFolders**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#setFontFolders(java.lang.String[],%20boolean)) acceptent un deuxième paramètre de type booléen. Passer **true** comme second paramètre dirigera les API Aspose.Cells pour rechercher les sous-dossiers pour les fichiers de polices.

{{% /alert %}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetCustomFontFolders-SetCustomFontFolders.java" >}}

{{% alert color="primary" %}}

Veuillez utiliser l'une des méthodes mentionnées ci-dessus au début de l'application, c'est-à-dire; avant d'invoquer tout autre objet des API Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Si plus d'une des méthodes susmentionnées sont utilisées pour définir les sources de polices, seuls les derniers paramètres auront un effet.

{{% /alert %}}

## **Mécanisme de substitution de polices**

Les API Aspose.Cells fournissent également la capacité de spécifier la police de substitution à des fins de rendu. Ce mécanisme est utile lorsqu'une police requise n'est pas disponible sur la machine où la conversion doit avoir lieu. Les utilisateurs peuvent fournir une liste de noms de polices en alternative à la police initialement requise. Pour ce faire, les API Aspose.Cells ont exposé la méthode FontConfigs.setFontSubstitutes, qui accepte 2 paramètres. Le premier paramètre est de type **String**, qui devrait être le nom de la police qui doit être remplacée. Le deuxième paramètre est un tableau de type **String**. Les utilisateurs peuvent fournir une liste de noms de polices comme substituts à la police initiale (spécifiée dans le premier paramètre).

Voici un scénario d'utilisation simple.

{{< highlight java >}}

 //Substituting the Arial font with Times New Roman & Calibri

FontConfigs.setFontSubstitutes("Arial", new String[] { "Times New Roman", "Calibri" });

{{< /highlight >}}

## **Collecte d'informations**

En plus des méthodes mentionnées ci-dessus, les APIs Aspose.Cells ont également fourni des moyens de recueillir des informations sur les sources et les substitutions qui ont été définies.

1. [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--): Cette méthode retourne un tableau de type [**FontSourceBase**](https://reference.aspose.com/cells/java/com.aspose.cells/FileFontSource) contenant la liste des sources de polices spécifiées. Au cas où aucune source n'aurait été définie, la méthode [**FontConfigs.getFontSources**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSources--) retournera un tableau vide.
1. [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)): Cette méthode accepte un paramètre de type **String** permettant de spécifier le nom de la police pour laquelle une substitution a été définie. Au cas où aucune substitution n'aurait été définie pour le nom de police spécifié, alors la méthode [**FontConfigs.getFontSubstitutes**](https://reference.aspose.com/cells/java/com.aspose.cells/fontconfigs#getFontSubstitutes(java.lang.String)) retournera null.
