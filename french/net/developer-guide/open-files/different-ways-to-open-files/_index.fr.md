---
title: Différentes façons d'ouvrir des fichiers
type: docs
weight: 10
url: /fr/net/different-ways-to-open-files/
---
{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple pour récupérer des données, ou d'utiliser un modèle de concepteur pour accélérer le processus de développement.

{{% /alert %}}

## **Ouvrir un fichier via un chemin**

 Les développeurs peuvent ouvrir un fichier Excel Microsoft en utilisant son chemin de fichier sur l'ordinateur local en le spécifiant dans le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)**constructeur de classe. Passez simplement le chemin dans le constructeur en tant que*chaîne de caractères*. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Ouvrir un fichier via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend le*Flux*objet qui contient le fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Ouvrir un fichier contenant uniquement des données**

 Pour ouvrir un fichier contenant uniquement des données, utilisez la**[Options de chargement] (https://reference.aspose.com/cells/net/aspose.cells/loadoptions)** et**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classes pour définir l'attribut associé et les options des classes pour le fichier modèle à charger.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Chargement des feuilles visibles uniquement**

 Lors du chargement d'un**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)**parfois, vous n'avez besoin que de données dans des feuilles de calcul visibles dans un classeur. Aspose.Cells vous permet d'ignorer des données dans des feuilles de calcul invisibles lors du chargement d'un classeur. Pour ce faire, créez une fonction personnalisée qui hérite de la**[LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadfilter)**classe et passer son instance à**[LoadOptions.LoadFilter](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)**propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Voici la mise en œuvre de la*Charge personnalisée*classe référencée dans l'extrait ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d'ouvrir des fichiers Excel non natifs ou d'autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) par Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

 Il y a de bonnes chances que le**[Cahier](https://reference.aspose.com/cells/net/aspose.cells/workbook)** le constructeur peut jeter*System.OutOfMemoryException* lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul dans la mémoire. Par conséquent, la feuille de calcul doit être chargée tout en activant les Préférences de la mémoire.

{{% /alert %}}
