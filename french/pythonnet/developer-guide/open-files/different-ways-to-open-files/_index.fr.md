---
title: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/python-net/different-ways-to-open-files/
description: Cet article explique comment ouvrir un fichier Excel en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Ouvrir un fichier Excel avec Python sans Excel, comment ouvrir un fichier Excel.
---

{{% alert color="primary" %}}

Avec Aspose.Cells pour Python via .NET, il est simple d'ouvrir des fichiers, par exemple, pour extraire des données, ou pour utiliser un modèle de conception afin d’accélérer le processus de développement.

{{% /alert %}}

## **Comment ouvrir un fichier Excel via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en utilisant son chemin d'accès local en le spécifiant dans le constructeur de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Il suffit de transmettre le chemin dans le constructeur sous forme de *chaîne*. Aspose.Cells pour Python via .NET détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughPath-1.py" >}}

## **Comment ouvrir un fichier Excel via un flux**

Il est également simple d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *Stream* contenant le fichier.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilesThroughStream-1.py" >}}

## **Comment ouvrir un fichier avec des données uniquement**

Pour ouvrir un fichier avec uniquement des données, utilisez les classes [**LoadOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions) et [**LoadFilter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadfilter) pour définir l'attribut et les options associés des classes pour charger le fichier modèle.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-OpeningFilewithDataOnly-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
