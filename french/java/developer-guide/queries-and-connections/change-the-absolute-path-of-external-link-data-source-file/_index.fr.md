---
title: Changer le chemin absolu du fichier source des données de lien externe
type: docs
weight: 1020
url: /fr/java/change-the-absolute-path-of-external-link-data-source-file/
---

## **Scénarios d'utilisation possibles**
Si vous souhaitez modifier le chemin absolu du fichier source de données de lien externe, veuillez utiliser la propriété [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath). Initialement, cette propriété sera définie sur le chemin à partir duquel le fichier Excel a été chargé. Mais vous pouvez la définir sur une chaîne vide ou vous pouvez la définir sur un chemin de dossier local ou un chemin de réseau distant. Chaque fois que vous modifierez cette propriété, le chemin du fichier source de données de lien externe sera également modifié.
## **Changer le chemin absolu du fichier source de données de lien externe**
Le code d'exemple suivant charge le [fichier excel d'exemple](5472589.xlsx) qui contient un lien externe. Il affiche d'abord le fichier source de données du lien externe qui affiche le chemin distant. Ensuite, il supprime le chemin distant et affiche à nouveau, cette fois, il affiche le fichier source de données du lien externe avec le chemin local. Ensuite, il change la propriété [Workbook.AbsolutePath](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#AbsolutePath) sur un chemin local et distant et affiche à nouveau le fichier source de données du lien externe et les modifications sont reflétées dans la sortie de la console.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ChangeAbsolutePathofExternalLink-ChangeAbsolutePathofExternalLink.java" >}}
## **Sortie console**
Voici la sortie console ou de débogage après l'exécution du code d'exemple ci-dessus avec le [fichier excel d'exemple](5472589.xlsx).

{{< highlight java >}}

 External Link Data Source: http:\\ws874dmErit\WebFiles\Files\300\ExternalAccounts.xlsx

External Link Data Source After Removing Remote Path: D:\Downloads\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Local Path: C:\Files\Extra\ExternalAccounts.xlsx

External Link Data Source After Changing Workbook.AbsolutePath to Remote Path: http://www.aspose.com/WebFiles/ExcelFiles/ExternalAccounts.xlsx

{{< /highlight >}}
