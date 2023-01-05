---
title: Différentes façons d'ouvrir des fichiers
linktitle: Différentes façons d'ouvrir des fichiers
type: docs
weight: 10
url: /fr/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Avec Aspose.Cells, il est possible d'ouvrir des fichiers, par exemple pour récupérer des données, ou d'utiliser un modèle de concepteur pour accélérer le processus de développement. Aspose.Cells peut ouvrir une gamme de fichiers différents, tels que les feuilles de calcul Excel Microsoft (XLS, XLSX, XLSM, XLSB), CSV ou TabDelimited.

{{% /alert %}} 
## **Ouvrir un fichier via un chemin**
 Les développeurs peuvent ouvrir un fichier Excel Microsoft en utilisant son chemin de fichier sur l'ordinateur local en le spécifiant dans le[IClasseur](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook)constructeur de classe. Passez simplement le chemin dans le constructeur en tant que String. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath.cpp" >}}

## **Ouverture d'un fichier à l'aide d'un flux**
 Il est également possible d'ouvrir un fichier Excel sous forme de flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend le*Flux*objet qui contient le fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream.cpp" >}}

