---
title: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** pour un classeur, Microsoft Excel désactive la récupération automatique (sauvegarde automatique) sur ce fichier Excel.

Aspose.Cells fournit la propriété [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) pour activer ou désactiver cette option.

{{% /alert %}}

Le code suivant explique comment utiliser la propriété [**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) du classeur. Le code lit d'abord la valeur par défaut de cette propriété qui est **true**, puis la définit comme **false** et enregistre le classeur. Ensuite, il lit à nouveau le classeur et lit la valeur de cette propriété qui est **false** à ce moment-là.

## Code C# pour définir la propriété AutoRecover du classeur

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Sortie**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
