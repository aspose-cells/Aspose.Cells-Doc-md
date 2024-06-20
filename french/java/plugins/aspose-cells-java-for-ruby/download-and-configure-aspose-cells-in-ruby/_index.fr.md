---
title: Télécharger et configurer Aspose.Cells en Ruby
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-cells-in-ruby/
---

## **Télécharger les bibliothèques requises**
Téléchargez les bibliothèques requises mentionnées ci-dessous. Elles sont nécessaires pour exécuter les exemples Aspose.Cells Java pour Ruby.

- [Composant Aspose.Cells pour Java](https://downloads.aspose.com/cells/java/)
## **Téléchargez les exemples des sites de codage social**
Les versions suivantes des exemples en cours d'exécution sont disponibles en téléchargement sur les sites de codage social mentionnés ci-dessous:

**GitHub**

- [Aspose.Cells Java for Ruby](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installer**
Il est très simple et facile d'installer la gemme Aspose.cells Java pour Ruby, veuillez suivre ces étapes simples :

1. Ajoutez cette ligne à votre Gemfile d'application. 

{{< highlight java >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Et ensuite exécutez 

{{< highlight java >}}

 $ bundle

{{< /highlight >}}

**OU**

1. Exécutez la commande suivante. 

{{< highlight java >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **En utilisant**
Inclure les fichiers requis pour travailler avec l'exemple de helloworld.

{{< highlight java >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Comprendre le code ci-dessus.

1. La première ligne assure que les cellules aspose sont chargées et disponibles.
1. Inclure les fichiers nécessaires pour accéder aux cellules aspose.
1. Initialiser les bibliothèques. Les classes aspose JAVA sont chargées à partir du chemin fourni dans le fichier aspose.yml.
