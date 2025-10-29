---
title: Désactiver le vérificateur de compatibilité dans Excel
type: docs
weight: 170
url: /fr/python-net/disable-compatibility-checker-in-excel/
description: Cet article montre comment désactiver le vérificateur de compatibilité via l API Aspose.Cells for Python via .NET.
keywords: Python Désactiver le Vérificateur de compatibilité, Excel Désactiver le Vérificateur de compatibilité en C#, Désactiver le Vérificateur de compatibilité dans le classeur. 
---

## Désactiver le Vérificateur de compatibilité dans les feuilles Excel en Python 

{{% alert color="primary" %}}

Le vérificateur de compatibilité de Microsoft Excel signale lorsque la sauvegarde d'un fichier dans un format de fichier antérieur pourrait entraîner des problèmes de fonctionnalité ou une perte de fidélité. Le vérificateur de compatibilité est une fonctionnalité de Microsoft Office Excel 2007 et de Microsoft Excel 2010.

Lorsque vous enregistrez un classeur dans une version antérieure, Excel 97 à Excel 2003, à partir d'Excel 2007 ou d'Excel 2010, le vérificateur de compatibilité analyse le classeur pour voir s'il contient des fonctionnalités qui ne sont pas prises en charge par la version antérieure. Pour vous aider à prendre des décisions sur la manière de gérer les problèmes de compatibilité, le vérificateur de compatibilité affiche des boîtes de dialogue avec des options. Il peut également être utilisé pour créer un rapport sur les problèmes dans le classeur, ou désactiver la fonctionnalité.

Parfois, vous devez désactiver le Vérificateur de compatibilité pour une feuille de calcul particulière. Avec Aspose.Cells pour Python via .NET, vous pouvez le faire de manière programmatique afin que les utilisateurs ne soient pas frustrés ou confus par la boîte de dialogue du Vérificateur de compatibilité qui apparaît lorsqu'ils enregistrent manuellement le fichier dans Microsoft Excel.

{{% /alert %}}

## **Comment désactiver le vérificateur de compatibilité à l'aide de Microsoft Excel**

Pour désactiver le vérificateur de compatibilité dans Microsoft Excel (par exemple Microsoft Excel 2007/2010) :

- (Excel 2007) Sur le bouton Office, cliquez sur **Préparer**, puis sur **Exécuter le vérificateur de compatibilité**, puis désactivez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.
- (Excel 2010) Sur l'onglet **Fichier**, cliquez sur **Informations**, puis **Vérifier les problèmes**, cliquez sur **Vérifier la compatibilité**, et enfin, désélectionnez l'option **Vérifier la compatibilité lors de l'enregistrement de ce classeur**.

## **Comment désactiver le vérificateur de compatibilité à l'aide des API Aspose.Cells**

Définissez la propriété [**Workbook.settings.check_compatibility**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_compatibility) sur **False** pour désactiver le vérificateur de compatibilité de Microsoft Excel.

### **Exemples de code**

Les exemples de code suivants montrent comment désactiver le Vérificateur de compatibilité avec Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-DisableCompatibilityChecker-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
