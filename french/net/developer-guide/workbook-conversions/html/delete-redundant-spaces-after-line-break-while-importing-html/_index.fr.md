---
title: Supprimer les espaces redondants après un saut de ligne lors de l'importation HTML
type: docs
weight: 20
url: /fr/net/delete-redundant-spaces-after-line-break-while-importing/
---
{{% alert color="primary" %}}

 Veuillez utiliser[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) propriété et définissez-la**vrai** pour supprimer tous les espaces redondants venant après la balise de saut de ligne. Par défaut, cette propriété est**faux**et les espaces redondants sont conservés dans les fichiers Excel de sortie.

{{% /alert %}}

## Effet de la définition de la propriété HTMLLoadOptions.DeleteRedundantSpaces sur false et true

 La capture d'écran suivante montre l'effet de la définition de cette propriété sur**faux** et**vrai**.

![tâche : image_autre_texte](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Supprimer les espaces redondants après un saut de ligne lors de l'importation HTML

### Exemple de programmation

 L'exemple de code suivant montre l'utilisation de[**HTMLLoadOptions.DeleteRedundantSpaces**](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/deleteredundantspaces) la propriété. Veuillez le régler**vrai** ou alors**faux** pour obtenir la sortie comme indiqué dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DeleteRedundantSpacesWhileImportingFromHtml-1.cs" >}}
