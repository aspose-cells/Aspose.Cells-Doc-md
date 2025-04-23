---
title: Différentes façons d ouvrir des fichiers
linktitle: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/go-cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}}

Avec Aspose.Cells, vous pouvez ouvrir des fichiers, par exemple, pour récupérer des données ou utiliser un modèle de concepteur pour accélérer le processus de développement. Aspose.Cells peut ouvrir une gamme de fichiers différents, tels que les feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), CSV ou fichiers délimités par tabulation.

{{% /alert %}}

## **Ouvrir un fichier via un chemin**

Les développeurs peuvent ouvrir un fichier Microsoft Excel en utilisant son chemin d'accès local en le spécifiant dans le constructeur de la classe [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/). Passez le chemin dans le constructeur sous forme de chaîne. Aspose.Cells détectera automatiquement le type de format du fichier.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingPath.go" >}}

## **Ouverture d'un fichier à l'aide d'un flux**

Il est également possible d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *Stream* qui contient le fichier.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadWorkbookUsingStream.go" >}}
