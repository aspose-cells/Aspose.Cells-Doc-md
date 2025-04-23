---
title: Changer le chemin absolu du fichier source des données de lien externe
type: docs
weight: 290
url: /fr/python-net/change-the-absolute-path-of-external-link-data-source-file/
---

## Scénarios d'utilisation possibles

Si vous souhaitez changer le chemin absolu du fichier source des données de lien externe, veuillez utiliser la propriété [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path). Initialement, cette propriété sera définie sur le chemin à partir duquel le fichier Excel a été chargé. Mais vous pouvez la définir sur une chaîne vide ou sur un chemin de dossier local ou distant. Chaque fois que vous changerez cette propriété, le chemin du fichier source des données de lien externe sera également modifié.

## Changer le chemin absolu du fichier source des données de lien externe

Le code d'exemple suivant charge le [fichier Excel d'exemple](5115146.xlsx) qui contient un lien externe. Il affiche d'abord la source de données du lien externe qui affiche le chemin distant. Puis il supprime le chemin distant et affiche à nouveau, cette fois, il affiche la source de données du lien externe avec le chemin local. Ensuite, il change la propriété [**Workbook.absolute_path**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/absolute_path) en un chemin local et distant et affiche à nouveau la source de données du lien externe et les modifications sont reflétées dans la sortie de la console.

Voici la sortie console ou de débogage après l'exécution du code d'exemple ci-dessus avec le [fichier Excel d'exemple](5115146.xlsx).

{{< highlight java >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}

