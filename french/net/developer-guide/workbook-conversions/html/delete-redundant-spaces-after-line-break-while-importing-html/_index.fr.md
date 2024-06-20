---
title: Supprimez les espaces redondants après un saut de ligne lors de l importation du HTML
type: docs
weight: 20
url: /fr/net/delete-redundant-spaces-after-line-break-while-importing/
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) et définissez-la sur **true** pour supprimer tous les espaces redondants après la balise de saut de ligne. Par défaut, cette propriété est **false** et les espaces redondants sont conservés dans les fichiers Excel de sortie.

{{% /alert %}}

## Effet de la définition de la propriété HTMLLoadOptions.DeleteRedundantSpaces à false et true

La capture d'écran suivante montre l'effet de définir cette propriété sur **false** et **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Supprimer les espaces redondants après un saut de ligne lors de l'importation du HTML

### Exemple de programmation

Le code d'exemple suivant montre l'utilisation de la propriété [**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces). Veuillez le définir sur **true** ou **false** pour obtenir le résultat tel qu'indiqué dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
