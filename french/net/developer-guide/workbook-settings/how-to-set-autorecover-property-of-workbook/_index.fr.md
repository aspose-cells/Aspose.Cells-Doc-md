---
title: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 220
url: /fr/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est**vrai** . Lorsque vous le réglez**faux** sur un classeur, Microsoft Excel désactive la récupération automatique (enregistrement automatique) sur ce fichier Excel.

 Aspose.Cells fournit[**Classeur.Paramètres.Récupération automatique**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) propriété pour activer ou désactiver cette option.

{{% /alert %}}

 Le code suivant explique comment utiliser[**Classeur.Paramètres.Récupération automatique**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover) propriété du classeur. Le code lit d'abord la valeur par défaut de cette propriété qui est**vrai** , puis il le définit comme**faux** et enregistre le classeur. Ensuite, il lit à nouveau le classeur et lit la valeur de cette propriété qui est**faux** en ce moment.

## C# code pour définir la propriété AutoRecover de Workbook

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **Production**

Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
