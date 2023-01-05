---
title: Désactiver le vérificateur de compatibilité dans Excel
type: docs
weight: 270
url: /fr/java/disable-compatibility-checker-in-excel/
---
{{% alert color="primary" %}}

Microsoft Le vérificateur de compatibilité d'Excel signale lors de l'enregistrement d'un fichier dans un format de fichier antérieur que l'enregistrement du fichier peut entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007, 2010 et 2013.

Lorsque vous enregistrez un classeur dans une version précédente, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la façon de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur tous les problèmes du classeur ou désactiver la fonctionnalité.

Parfois, vous devez désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API Aspose.Cells ', vous pouvez le faire de manière dynamique afin que les utilisateurs ne soient pas frustrés ou confus par la boîte de dialogue Vérificateur de compatibilité qui apparaît lorsqu'ils réenregistrent manuellement le fichier dans Microsoft Excel.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :

-  (Excel 2007) Sur le bouton Office, cliquez sur**Préparer** , ensuite**Exécutez le vérificateur de compatibilité** , puis effacez le**Vérifier la compatibilité lorsque vous enregistrez ce classeur** option.
-  (Excel 2010 & 2013) Dans l'onglet Fichier, cliquez sur**Info** , ensuite**Vérifier les problèmes** , Cliquez sur**Vérifier la compatibilité** , et, enfin, effacer le**Vérifier la compatibilité lorsque vous enregistrez ce classeur** option.

## **Utilisation des API Aspose.Cells**

 Met le[**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) propriété à**Faux** pour désactiver le vérificateur de compatibilité d'Excel Microsoft.

Supposons que nous ayons un fichier modèle XLS. Lorsqu'un utilisateur l'enregistre ou l'enregistre à nouveau dans MS Excel 2007/2010/2013, la boîte de dialogue Vérificateur de compatibilité s'affiche, comme illustré dans la capture d'écran ci-dessous.

![tâche : image_autre_texte](disable-compatibility-checker-in-excel_1.png)

Le code suivant montre comment désactiver le vérificateur de compatibilité avec Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
