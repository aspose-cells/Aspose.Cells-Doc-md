---
title: Comment définir la propriété AutoRecover du classeur
type: docs
weight: 160
url: /fr/java/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Vous pouvez utiliser Aspose.Cells pour définir la propriété AutoRecover du classeur. La valeur par défaut de cette propriété est **true**. Lorsque vous la définissez sur **false** sur un classeur, Microsoft Excel désactive l'autorécupération (autosauve) sur ce fichier Excel.

Aspose.Cells fournit la propriété [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) pour activer ou désactiver cette option.

{{% /alert %}}

## Code Java pour définir la propriété AutoRecover du classeur

Le code suivant explique comment utiliser la propriété [**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover) du classeur. Le code lit d'abord la valeur par défaut de cette propriété qui est **true**, puis la définit comme **false** et enregistre le classeur. Ensuite, il lit à nouveau le classeur et lit la valeur de cette propriété qui est fausse à ce moment.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## Sortie générée par le code d'exemple

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
