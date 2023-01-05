---
title: Modifier le chemin absolu du fichier de source de données de lien externe
type: docs
weight: 290
url: /fr/net/change-the-absolute-path-of-external-link-data-source-file/
---
## Scénarios d'utilisation possibles

 Si vous souhaitez modifier le chemin absolu du fichier de source de données du lien externe, veuillez utiliser le[**Workbook.AbsolutePathWorkbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)la propriété. Initialement, cette propriété sera définie sur le chemin à partir duquel le fichier Excel a été chargé. Mais vous pouvez le définir sur une chaîne vide ou vous pouvez le définir sur un chemin de dossier local ou un chemin de réseau distant. Chaque fois que vous modifierez cette propriété, le chemin du fichier de source de données de lien externe sera également modifié.

## Modifier le chemin absolu du fichier de source de données de lien externe

 L'exemple de code suivant charge le[exemple de fichier excel](5115146.xlsx) qui contient un lien externe. Il imprime d'abord la source de données du lien externe qui imprime le chemin distant. Ensuite, il supprime le chemin distant et imprime à nouveau, cette fois, il imprime la source de données du lien externe avec le chemin local. Ensuite, il change le[**Workbook.AbsolutePathWorkbook.AbsolutePath**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/absolutepath)propriété à un chemin local et distant et imprime à nouveau la source de données du lien externe et les modifications sont reflétées dans la sortie de la console.

Voici la console ou la sortie de débogage après l'exécution de l'exemple de code ci-dessus avec le[exemple de fichier excel](5115146.xlsx).

{{< highlight "java" >}}

External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
