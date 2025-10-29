---
title: Comment lier les formes Excel aux cellules de la feuille de calcul
linktitle: Lier les formes Excel aux cellules
type: docs
description: « Comment lier les formes Excel aux cellules de la feuille de calcul »
weight: 3300
url: /fr/net/link-shapes-to-cells/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin d'afficher le contenu d'une cellule de feuille de calcul dans une forme, une zone de texte ou un élément de graphique. Parfois, lorsque les données dans une cellule ou une plage de cellules sont modifiées, vous devez synchroniser le contenu de la cellule avec le contenu d'une forme, d'une zone de texte ou d'un élément de graphique. Pour ce faire, vous pouvez lier une forme, une zone de texte ou un élément de graphique aux cellules contenant les données que vous souhaitez afficher.

{{% /alert %}}

## Comment lier des formes aux cellules dans Ms Excel

La figure suivante montre comment définir une cellule liée pour une forme.

![todo:image_alt_text](link-shapes-to-cells-1.png)

1. Sélectionnez une forme. La barre de formule est généralement vide.

2. Entrez la formule de la forme, comme « =A1 »

## Comment lier des formes aux cellules dans Aspose.Cells

Le code suivant montre comment utiliser la bibliothèque Aspose.Cells pour définir un lien pour une forme ou une zone de texte afin d'afficher dynamiquement le contenu de la cellule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-1.cs"  >}}

## Usage Avancé

Si vous souhaitez que le texte de la forme se compose de deux cellules ou plus, ou si vous souhaitez sélectionner le contenu souhaité en fonction d'une formule, le code d'exemple ci-dessus peut ne pas répondre à vos besoins. Dans ce cas, vous devez faire quelque chose de plus avancé. Vous devez d'abord placer la formule qui produit le résultat souhaité dans une cellule, puis lier la forme à la cellule contenant la formule.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "link-shapes-to-cells-2.cs"  >}}

{{< app/cells/assistant language="csharp" >}}
