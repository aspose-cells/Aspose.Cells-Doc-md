---
title: Différentes façons d'ouvrir des fichiers
linktitle: Différentes façons d'ouvrir des fichiers
type: docs
weight: 10
url: /fr/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Avec le Aspose.Cells, il est possible d'ouvrir des fichiers, par exemple pour récupérer des données, ou d'utiliser un modèle de concepteur pour accélérer le processus de développement. Aspose.Cells peut ouvrir une gamme de fichiers différents, tels que des feuilles de calcul Excel Microsoft (XLS, XLSX, XLSM, XLSB), des fichiers CSV ou TabDelimited.

{{% /alert %}} 
##  **Ouverture d'un fichier via un chemin**
 Les développeurs peuvent ouvrir un fichier Excel Microsoft en utilisant son chemin d'accès sur l'ordinateur local en le spécifiant dans le champ[Cahier d'exercices](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)constructeur de classe. Transmettez simplement le chemin dans le constructeur sous forme de chaîne. Aspose.Cells détectera automatiquement le type de format de fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Ouverture d'un fichier à l'aide d'un flux**
 Il est également possible d'ouvrir un fichier Excel sous forme de flux. Pour ce faire, utilisez une version surchargée du constructeur qui prend le*Flux*objet qui contient le fichier.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

