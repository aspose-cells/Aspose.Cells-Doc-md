---
title: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/net/different-ways-to-open-files/
description: Cet article explique comment ouvrir un fichier Excel en utilisant l API Aspose.Cells for .NET.
keywords: Ouverture d un fichier Excel sans Excel en utilisant C#, Comment ouvrir un fichier Excel.
---

{{% alert color="primary" %}}

Avec Aspose.Cells, il est simple d'ouvrir des fichiers, par exemple, pour récupérer des données ou pour utiliser un modèle de conception afin d'accélérer le processus de développement.

{{% /alert %}}

## **Comment ouvrir un fichier Excel via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en spécifiant son chemin d'accès sur l'ordinateur local en le spécifiant dans le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). Il suffit de passer le chemin dans le constructeur en tant que *chaîne*. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughPath-1.cs" >}}

## **Comment ouvrir un fichier Excel via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *Stream* contenant le fichier.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilesThroughStream-1.cs" >}}

## **Comment ouvrir un fichier avec des données uniquement**

Pour ouvrir un fichier avec uniquement des données, utilisez les classes [**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions) et [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) pour définir l'attribut et les options associés des classes pour charger le fichier modèle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-OpeningFilewithDataOnly-1.cs" >}}

## **Comment charger uniquement les feuilles visibles**

Lors du chargement d'un [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), parfois, vous ne avez besoin que des données dans les feuilles de calcul visibles dans un classeur. Aspose.Cells vous permet de ignorer les données dans les feuilles de calcul invisibles lors du chargement d'un classeur. Pour cela, créez une fonction personnalisée qui hérite de la classe [**LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadfilter) et passez une instance à la propriété [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-1.cs" >}}

Voici la mise en œuvre de la classe *CustomLoad* référencée dans l'extrait ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-LoadVisibleSheetsOnly-2.cs" >}}

{{% alert color="primary" %}}

Une exception sera levée si vous essayez d'ouvrir des fichiers Excel non natifs ou d'autres formats de fichiers (par exemple PPT/PPTX, DOC/DOCX, etc.) avec Aspose.Cells.

{{% /alert %}} {{% alert color="primary" %}}

Il y a de fortes chances que le constructeur [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) puisse générer une *System.OutOfMemoryException* lors du chargement de grandes feuilles de calcul. Cette exception suggère que la mémoire disponible est insuffisante pour charger complètement la feuille de calcul en mémoire. Par conséquent, la feuille de calcul doit être chargée en activant les préférences de mémoire.

{{% /alert %}}
