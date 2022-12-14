---
title: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 160
url: /fr/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

 Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est**vrai** . Lorsque vous le réglez**faux**sur un classeur, Microsoft Excel désactive la récupération automatique (enregistrement automatique) sur ce fichier Excel.

 Aspose.Cells fournit[**Classeur.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) propriété pour activer ou désactiver cette option.

{{% /alert %}}

## Java code pour définir la propriété AutoRecover du classeur

 Le code suivant explique comment utiliser[**Classeur.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) propriété du classeur. Le code lit d'abord la valeur par défaut de cette propriété qui est**vrai** , puis il le définit comme**faux** et enregistre le classeur. Ensuite, il lit à nouveau le classeur et lit la valeur de cette propriété qui est fausse à ce moment.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Sortie générée par un exemple de code

Voici la sortie console de l'exemple de code ci-dessus.

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
