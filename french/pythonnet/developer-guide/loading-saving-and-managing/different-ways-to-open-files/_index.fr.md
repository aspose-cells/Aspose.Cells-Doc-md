---
title: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/python-net/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple, pour récupérer des données ou pour utiliser un modèle de conception afin d'accélérer le processus de développement.

{{% /alert %}}

## **Ouvrir un fichier via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en utilisant le chemin d'accès du fichier sur l'ordinateur local en le spécifiant dans le constructeur de la classe **Workbook**. Il suffit de passer le chemin dans le constructeur en tant que *chaîne*. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Ouvrir un fichier via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *BufferStream* contenant le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Ouvrir un fichier avec uniquement des données**

Pour ouvrir un fichier avec seulement des données, utilisez les classes **LoadOptions** et **LoadFilter** pour définir l'attribut et les options liés des classes pour le fichier de modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d'ouvrir des fichiers Excel non natifs ou d'autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) avec Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Il y a de fortes chances que le constructeur **Workbook** puisse déclencher *System.OutOfMemoryException* lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul en mémoire, donc la feuille de calcul doit être chargée tout en activant les préférences de mémoire.

{{% /alert %}}
