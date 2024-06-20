---
title: Désactiver le vérificateur de compatibilité dans Excel
type: docs
weight: 270
url: /fr/java/disable-compatibility-checker-in-excel/
---

{{% alert color="primary" %}}

Le vérificateur de compatibilité de Microsoft Excel signale que lors de l'enregistrement d'un fichier dans un format antérieur, l'enregistrement du fichier pourrait causer des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007, 2010 et 2013.

Lorsque vous enregistrez un classeur dans une version antérieure, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la manière de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur les problèmes dans le classeur, ou désactiver la fonctionnalité.

Parfois, vous devez désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API Aspose.Cells, vous pouvez le faire dynamiquement afin que les utilisateurs ne soient pas frustrés ou déroutés par la boîte de dialogue du vérificateur de compatibilité qui apparaît lorsqu'ils réenregistrent le fichier dans Microsoft Excel manuellement.

{{% /alert %}}

## **Utilisation de Microsoft Excel**

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :

- (Excel 2007) Sur le bouton Office, cliquez sur **Préparer**, puis sur **Exécuter le vérificateur de compatibilité**, puis désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.
- (Excel 2010 et 2013) Dans l'onglet Fichier, cliquez sur **Informations**, puis sur **Rechercher des problèmes**, cliquez sur **Vérifier la compatibilité**, et enfin, désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.

## **Utilisation des API Aspose.Cells**

Définissez la propriété [**WorkbookSettings.CheckComptiliblity**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckComptiliblity) sur **False** pour désactiver le vérificateur de compatibilité de Microsoft Excel.

Supposons que nous ayons un fichier XLS modèle. Lorsqu'un utilisateur l'enregistre ou le réenregistre dans MS Excel 2007/2010/2013, la boîte de dialogue du vérificateur de compatibilité est affichée, comme le montre la capture d'écran ci-dessous.

![todo:image_alt_text](disable-compatibility-checker-in-excel_1.png)

Le code suivant montre comment désactiver le vérificateur de compatibilité avec Aspose.Cells for Java.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DisableCompatibilityChecker-DisableCompatibilityChecker.java" >}}
