---
title: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour Python via .NET pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** dans un classeur, Microsoft Excel désactive AutoRecover (Autosave) sur ce fichier Excel.

Aspose.Cells pour Python via .NET fournit la propriété [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) pour activer ou désactiver cette option.

{{% /alert %}}

Le code suivant explique comment utiliser la propriété [**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover) du classeur. Le code lit d'abord la valeur par défaut de cette propriété, qui est **true**, puis la définit comme **false** et enregistre le classeur. Ensuite, il relit le classeur et lit de nouveau la valeur de cette propriété, qui est **false** à ce moment.

## Code C# pour définir la propriété AutoRecover du classeur

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **Sortie**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
