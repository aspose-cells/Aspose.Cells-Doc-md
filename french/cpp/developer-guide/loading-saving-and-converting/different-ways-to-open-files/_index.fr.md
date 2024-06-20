---
title: Différentes façons d ouvrir des fichiers
linktitle: Différentes façons d ouvrir des fichiers
type: docs
weight: 10
url: /fr/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Avec Aspose.Cells, il est possible d'ouvrir des fichiers, par exemple pour récupérer des données, ou pour utiliser un modèle de concepteur afin d'accélérer le processus de développement. Aspose.Cells peut ouvrir divers fichiers, tels que des feuilles de calcul Microsoft Excel (XLS, XLSX, XLSM, XLSB), des fichiers CSV ou des fichiers TabDelimited.

{{% /alert %}} 
## **Ouvrir un fichier via un chemin**
Les développeurs peuvent ouvrir un fichier Microsoft Excel en spécifiant son chemin d'accès sur l'ordinateur local en le spécifiant dans le constructeur de classe [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Passez simplement le chemin dans le constructeur en tant que chaîne. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Ouverture d'un fichier à l'aide d'un flux**
Il est également possible d'ouvrir un fichier Excel en tant que flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend l'objet *Stream* qui contient le fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

