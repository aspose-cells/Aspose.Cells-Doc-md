---
title: Désactiver le vérificateur de compatibilité dans Excel
type: docs
weight: 170
url: /fr/net/disable-compatibility-checker-in-excel/
keywords: c# excel disable compatibility checke
---
## Désactiver le vérificateur de compatibilité dans les feuilles de calcul Excel dans C#

{{% alert color="primary" %}}

Microsoft Les indicateurs du vérificateur de compatibilité d'Excel lors de l'enregistrement d'un fichier dans un format de fichier antérieur peuvent entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007 et Microsoft Excel 2010.

Lorsque vous enregistrez un classeur dans une version précédente, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la façon de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur tous les problèmes du classeur ou désactiver la fonctionnalité.

Parfois, vous devez désactiver le vérificateur de compatibilité pour une feuille de calcul particulière. Avec les API Aspose.Cells ', vous pouvez le faire par programme afin que les utilisateurs ne soient pas frustrés ou confus par la boîte de dialogue Vérificateur de compatibilité qui apparaît lorsqu'ils réenregistrent manuellement le fichier dans Microsoft Excel.

{{% /alert %}}

## **Utilisation d'Excel Microsoft**

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :

-  (Excel 2007) Sur le bouton Office, cliquez sur**Préparer** , ensuite**Exécutez le vérificateur de compatibilité** , puis effacez le**Vérifier la compatibilité lorsque vous enregistrez ce classeur** option.
-  (Excel 2010) Dans l'onglet Fichier, cliquez sur**Info** , ensuite**Vérifier les problèmes** , Cliquez sur**Vérifier la compatibilité** , et, enfin, effacer le**Vérifier la compatibilité lorsque vous enregistrez ce classeur** option.

## **Utilisation des API Aspose.Cells**

 Met le[**Workbook.Settings.CheckComptiliblity**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcompatibility) propriété à**Faux** pour désactiver le vérificateur de compatibilité d'Excel Microsoft.

### **Exemples de codes**

Les exemples de code qui suivent montrent comment désactiver le vérificateur de compatibilité avec Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DisableCompatibilityChecker-1.cs" >}}
