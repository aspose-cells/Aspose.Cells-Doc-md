---
title: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/python-java/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple, pour récupérer des données ou pour utiliser un modèle de conception afin d'accélérer le processus de développement.

{{% /alert %}}

## **Ouvrir un fichier via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en spécifiant son chemin d'accès sur l'ordinateur local en le spécifiant dans le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook). Il suffit de passer le chemin dans le constructeur en tant que *chaîne*. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaPath.py" >}}

## **Ouvrir un fichier via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *BufferStream* contenant le fichier.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFileViaStream.py" >}}

## **Ouvrir un fichier avec uniquement des données**

Pour ouvrir un fichier avec uniquement des données, utilisez les classes [**LoadOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadOptions) et [**LoadFilter**](https://reference.aspose.com/cells/python-java/asposecells.api/LoadFilter) pour définir l'attribut et les options associés des classes pour charger le fichier modèle.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "OpenFilewithDataOnly.py" >}}

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d'ouvrir des fichiers Excel non natifs ou d'autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) avec Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Il y a de fortes chances que le constructeur [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook) puisse générer une *System.OutOfMemoryException* lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul en mémoire. Par conséquent, la feuille de calcul doit être chargée en activant les préférences de mémoire.

{{% /alert %}}
