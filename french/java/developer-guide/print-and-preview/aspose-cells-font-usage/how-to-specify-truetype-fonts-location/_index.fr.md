---
title: Comment spécifier l'emplacement des polices TrueType
type: docs
weight: 30
url: /fr/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

Cet article décrit :

1. [Où le Aspose.Cells API recherche les polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Comment spécifier explicitement un dossier de polices TrueType pour Aspose.Cells API](/cells/fr/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Comment restreindre le Aspose.Cells API pour n'utiliser qu'un seul emplacement de polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Travailler avec des polices**

### **Où Aspose.Cells recherche les polices TrueType sur Windows**

 Aspose.Cells recherche les polices dans**Windows\Polices** dossier. Ce paramètre par défaut fonctionne la plupart du temps, donc ne spécifiez vos propres dossiers de polices que si vous en avez vraiment besoin.

### **Où Aspose.Cells recherche les polices TrueType sous Linux**

Par défaut, Aspose.Cells API recherche les polices dans tous les emplacements suivants, bien que différentes distributions Linux stockent les polices dans différents dossiers.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

 Ce comportement par défaut fonctionnera pour la plupart des distributions Linux, mais il n'est pas garanti qu'il fonctionne tout le temps. Vous devrez peut-être spécifier explicitement l'emplacement des polices TrueType.

{{% /alert %}}

### **Comment spécifier explicitement un dossier de polices**

Les API Aspose.Cells ont exposé de nombreuses méthodes d'usine pour la classe FontConfigs afin de spécifier les polices ou les dossiers de polices comme décrit ci-dessous.

1. La méthode setFontFolder accepte le premier paramètre de type String avec un emplacement dans le répertoire des polices, tandis que le deuxième paramètre de type booléen consiste à ordonner à l'API Aspose.Cells de rechercher les fichiers de police de manière récursive dans les dossiers.
1. La méthode setFontFolders accepte un tableau de type String afin que vous puissiez spécifier plusieurs répertoires de polices en utilisant cette approche. Vous pouvez également demander à l'API Aspose.Cells de rechercher les dossiers de manière récursive en spécifiant true comme deuxième paramètre.
1. La méthode setFontSources accepte un tableau de type FontSourceBase pour vous permettre de spécifier une liste d'emplacements de polices individuelles.

{{% alert color="primary" %}}

Lorsque vous spécifiez le dossier des polices à l'aide de l'une des méthodes mentionnées ci-dessus, nous vous recommandons de définir l'emplacement de la police au démarrage de l'application, sinon vous risquez d'obtenir des résultats mal formatés.

{{% /alert %}} {{% alert color="primary" %}}

La définition du dossier de polices à l'aide de l'une des méthodes ci-dessus ne garantit pas que le Aspose.Cells API ne recherchera pas les polices dans les emplacements par défaut tels que le dossier de polices du système.

{{% /alert %}}

### **Comment limiter le Aspose.Cells à n'utiliser qu'un seul dossier de polices**

 À partir de Aspose.Cells for Java 8.1.0, définir les arguments JVM comme**-DAspose.Cells.FontDirExc="VotreRepPolice**veillera à ce que le Aspose.Cells API n'utilise que l'emplacement des polices spécifié.

Définissez les arguments spécifiés à l'aide de la méthode System.setProperty comme indiqué ci-dessous.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Veuillez noter ce qui suit :

- La déclaration ci-dessus doit figurer au début de votre candidature.
- L'utilisation de l'approche ci-dessus ne nécessite pas la définition du répertoire de polices à l'aide de l'une des méthodes FontConfigs décrites ci-dessus.
- La chaîne "FontDirSet" doit être le chemin complet vers le dossier contenant les polices requises.

{{% /alert %}}
