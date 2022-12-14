---
title: Différentes façons d'ouvrir des fichiers
type: docs
weight: 10
url: /fr/python-net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple pour récupérer des données, ou d'utiliser un modèle de concepteur pour accélérer le processus de développement.

{{% /alert %}}

## **Ouvrir un fichier via un chemin**

 Les développeurs peuvent ouvrir un fichier Excel Microsoft en utilisant son chemin de fichier sur l'ordinateur local en le spécifiant dans le**Cahier**constructeur de classe. Passez simplement le chemin dans le constructeur en tant que*chaîne de caractères*. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaPath.py" >}}

## **Ouvrir un fichier via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend le*BufferStream*objet qui contient le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFileViaStream.py" >}}

## **Ouvrir un fichier contenant uniquement des données**

 Pour ouvrir un fichier contenant uniquement des données, utilisez la**ChargerOptions** et**ChargerFiltre**classes pour définir l'attribut associé et les options des classes pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d'ouvrir des fichiers Excel non natifs ou d'autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) par Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Il y a de bonnes chances que le**Cahier** le constructeur peut jeter*System.OutOfMemoryException* lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire. Par conséquent, la feuille de calcul doit être chargée tout en activant les Préférences de la mémoire.

{{% /alert %}}
