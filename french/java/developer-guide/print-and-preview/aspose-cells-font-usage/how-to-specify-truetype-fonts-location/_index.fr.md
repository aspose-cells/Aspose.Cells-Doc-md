---
title: Comment spécifier l emplacement des polices TrueType
type: docs
weight: 30
url: /fr/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

Cet article décrit :

1. [Où l'API Aspose.Cells recherche les polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [Comment spécifier explicitement un dossier de polices TrueType pour l'API Aspose.Cells](/cells/fr/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [Comment restreindre l'API Aspose.Cells à n'utiliser qu'un seul emplacement de polices TrueType](/cells/fr/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **Travailler avec les polices**

### **Où Aspose.Cells recherche les polices TrueType sur Windows**

Aspose.Cells recherche les polices dans le dossier **Windows\Fonts**. Ce paramètre par défaut fonctionne la plupart du temps, donc spécifiez vos propres dossiers de polices uniquement si c'est vraiment nécessaire.

### **Où Aspose.Cells recherche les polices TrueType sur Linux**

Par défaut, l'API Aspose.Cells recherche les polices dans tous les emplacements suivants, bien que différentes distributions Linux stockent les polices dans des dossiers différents.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

Ce comportement par défaut fonctionnera pour la plupart des distributions Linux, mais n'est pas garanti de fonctionner tout le temps. Vous pourriez avoir besoin de spécifier explicitement l'emplacement des polices TrueType. 

{{% /alert %}}

### **Comment spécifier explicitement un dossier de polices**

Les APIs Aspose.Cells ont exposé de nombreuses méthodes d'usine pour la classe FontConfigs afin de spécifier les polices ou dossiers de polices comme décrit ci-dessous.

1. La méthode setFontFolder accepte le premier paramètre de type String avec l'emplacement du répertoire des polices tandis que le deuxième paramètre de type Boolean sert à indiquer aux API Aspose.Cells de rechercher les dossiers de façon récursive pour les fichiers de polices.
1. La méthode setFontFolders accepte un tableau de type String afin que vous puissiez spécifier de nombreux répertoires de polices en utilisant cette approche. Vous pouvez également indiquer aux API Aspose.Cells de rechercher les dossiers de façon récursive en spécifiant true comme deuxième paramètre.
1. La méthode setFontSources accepte un tableau de type FontSourceBase pour spécifier une liste des emplacements individuels des polices.

{{% alert color="primary" %}}

Lorsque vous spécifiez le dossier de polices en utilisant l'une des méthodes mentionnées ci-dessus, nous recommandons de définir l'emplacement de la police au début de l'application, sinon vous pourriez obtenir des résultats mal formatés.

{{% /alert %}} {{% alert color="primary" %}}

Le fait de définir le dossier de polices en utilisant l'une des méthodes ci-dessus ne garantit pas que l'API Aspose.Cells ne cherchera pas les polices dans les emplacements par défaut tels que le dossier de polices du système.

{{% /alert %}}

### **Comment restreindre Aspose.Cells à utiliser uniquement un dossier de polices**

À partir de Aspose.Cells for Java 8.1.0, en définissant les arguments JVM comme **-DAspose.Cells.FontDirExc="VotreDossierPolice** garantira que l'API Aspose.Cells utilisera uniquement le chemin des polices spécifié.

Définissez les arguments spécifiés en utilisant la méthode System.setProperty comme illustré ci-dessous.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

Veuillez noter ce qui suit :

- La déclaration ci-dessus devrait être au début de votre application.
- En utilisant l'approche ci-dessus, il n'est pas nécessaire de définir le répertoire de polices en utilisant l'une des méthodes FontConfigs discutées ci-dessus.
- La chaîne "FontDirSet" devrait être le chemin complet vers le dossier contenant les polices requises.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
