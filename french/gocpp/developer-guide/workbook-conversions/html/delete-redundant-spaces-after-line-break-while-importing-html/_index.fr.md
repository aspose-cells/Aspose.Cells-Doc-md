---
title: Supprimer les espaces redondants après le saut de ligne lors de l importation de HTML avec Golang via C++
linktitle: Supprimez les espaces redondants après un saut de ligne lors de l importation du HTML
type: docs
weight: 20
url: /fr/go-cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Apprenez comment supprimer les espaces redondants après les sauts de ligne lors de l importation HTML en utilisant Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Veuillez utiliser la propriété [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/) et la définir sur **true** pour supprimer tous les espaces redondants après la balise de saut de ligne. Par défaut, cette propriété est **false** et les espaces redondants sont conservés dans les fichiers Excel en sortie.

{{% /alert %}}

## Effet de la définition de la propriété HTMLLoadOptions.DeleteRedundantSpaces à false et true

La capture d'écran suivante montre l'effet de définir cette propriété sur **false** et **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Supprimer les espaces redondants après un saut de ligne lors de l'importation du HTML

### Exemple de programmation

Le code d'exemple suivant montre l'utilisation de la propriété [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/go-cpp/htmlloadoptions/getdeleteredundantspaces/). Veuillez le définir sur **true** ou **false** pour obtenir le résultat tel qu'indiqué dans la capture d'écran ci-dessus.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DeleteRedundantSpacesAfterLineBreakWhileImportingHtml.go" >}}
