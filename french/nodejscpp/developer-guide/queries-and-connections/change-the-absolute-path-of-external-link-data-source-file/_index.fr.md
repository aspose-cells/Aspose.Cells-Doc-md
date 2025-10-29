---
title: Modifier le chemin absolu de la source de données du lien externe avec Node.js via C++
linktitle: Changer le chemin absolu du fichier source des données de lien externe
type: docs
weight: 290
url: /fr/nodejs-cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Apprenez comment changer le chemin absolu du fichier de source de données du lien externe en utilisant Aspose.Cells for Node.js via C++. 
---

## Scénarios d'utilisation possibles

Si vous souhaitez changer le chemin absolu du fichier de source de données du lien externe, utilisez la propriété [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--). Initialement, cette propriété sera définie sur le chemin à partir duquel le fichier Excel a été chargé. Mais vous pouvez la définir à une chaîne vide, ou la définir sur un chemin de dossier local ou un chemin réseau distant. Chaque fois que vous changez cette propriété, le chemin du fichier source de données du lien externe sera également modifié.

## Changer le chemin absolu du fichier source des données de lien externe

Le code d'exemple suivant charge le fichier Excel [exemple](5115146.xlsx) contenant un lien externe. Il affiche d'abord la source des données de lien externe, qui indique le chemin distant. Ensuite, il supprime le chemin distant et l'affiche à nouveau ; cette fois, il affiche la source de données du lien externe avec le chemin local. Ensuite, il change la propriété [**Workbook.getAbsolutePath()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getAbsolutePath--) vers un chemin local et distant et affiche à nouveau la source de données du lien externe, et les modifications sont reflétées dans la sortie console.

Voici la sortie de la console ou du débogage après l'exécution du code d'exemple ci-dessus avec le [fichier Excel](5115146.xlsx).

{{< highlight javascript >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
