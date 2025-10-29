---
title: Changer le chemin absolu de la source de données du lien externe avec C++
linktitle: Changer le chemin absolu du fichier source des données de lien externe
type: docs
weight: 290
url: /fr/cpp/change-the-absolute-path-of-external-link-data-source-file/
description: Modifier le chemin absolu du fichier source de lien externe dans Aspose.Cells avec C++.
---

## Scénarios d'utilisation possibles

Si vous souhaitez changer le chemin absolu du fichier source de lien externe, veuillez utiliser la méthode [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/). Initialement, cette propriété sera définie sur le chemin à partir duquel le fichier Excel a été chargé. Mais vous pouvez la définir comme une chaîne vide ou la définir sur un chemin de dossier local ou un chemin de réseau distant. Chaque fois que vous modifierez cette propriété, le chemin du fichier source de lien externe sera également modifié.

## Changer le chemin absolu du fichier source des données de lien externe

Le code suivant charge le fichier Excel d'exemple qui contient un lien externe. Il affiche d'abord la source de données du lien externe qui affiche le chemin distant. Ensuite, il supprime le chemin distant et affiche à nouveau, cette fois-ci, il affiche la source de données du lien externe avec le chemin local. Ensuite, il change la méthode [**GetAbsolutePath()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/getabsolutepath/) en un chemin local et distant et affiche à nouveau la source de données du lien externe, et les changements sont reflétés dans la sortie de la console.

Voici la sortie console ou de débogage après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5115146.xlsx).

{{< highlight cpp >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
