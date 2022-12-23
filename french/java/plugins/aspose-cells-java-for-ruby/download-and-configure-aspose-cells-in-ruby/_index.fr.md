---
title: Télécharger et configurer Aspose.Cells en Ruby
type: docs
weight: 10
url: /fr/java/download-and-configure-aspose-cells-in-ruby/
---
## **Télécharger les bibliothèques requises**
Téléchargez les bibliothèques requises mentionnées ci-dessous. Ce sont les éléments requis pour exécuter Aspose.Cells Java pour les exemples Ruby.

- [Aspose.Cell for Java Composant](https://downloads.aspose.com/cells/java/)
## **Télécharger des exemples à partir de sites de codage social**
Les versions suivantes des exemples en cours d'exécution sont disponibles au téléchargement sur les sites de codage social mentionnés ci-dessous :

**GitHub**

- [Aspose.Cells Java pour rubis](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Ruby)
## **Installation**
Il est très simple et facile d'installer Aspose.cells Java pour Ruby gem, veuillez suivre ces étapes simples :

1.  Ajoutez cette ligne au Gemfile de votre application.

{{< highlight "java" >}}

 gem 'aspose-cellsjava'

{{< /highlight >}}

1. Et puis exécuter

{{< highlight "java" >}}

 $ bundle

{{< /highlight >}}

**OU ALORS**

1.  Exécutez la commande suivante.

{{< highlight "java" >}}

 $ gem install aspose-cellsjava

{{< /highlight >}}
## **En utilisant**
Incluez les fichiers requis pour travailler avec l'exemple helloworld.

{{< highlight "java" >}}

 require require File.dirname(File.dirname(File.dirname(__FILE__))) + '/lib/aspose-cellsjava'

include Asposecellsjava

include Asposecellsjava::HelloWorld

initialize_aspose_cells

{{< /highlight >}}

Comprenons le code ci-dessus.

1. La première ligne s'assure que les cellules aspose sont chargées et disponibles.
1. Incluez les fichiers nécessaires pour accéder aux cellules aspose.
1. Initialisez les bibliothèques. Les classes JAVA aspose sont chargées à partir du chemin fourni dans le fichier aspose.yml/
