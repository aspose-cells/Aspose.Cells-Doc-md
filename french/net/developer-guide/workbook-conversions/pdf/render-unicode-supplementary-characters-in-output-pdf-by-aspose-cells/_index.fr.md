---
title: Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells
type: docs
weight: 350
url: /fr/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}}

Les caractères Unicode normaux ont une longueur de 2 octets tandis que les caractères Unicode supplémentaires ont une longueur de 4 octets. Aspose.Cells prend maintenant en charge le rendu de ces caractères Unicode de 4 octets.

Dans la norme des caractères Unicode, les Caractères supplémentaires sont les caractères aux points de code de U+10000 à U+10FFFF. En d'autres termes, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères ont une longueur de 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités de 16 bits).

{{% /alert %}}

## Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells

La capture d'écran suivante montre comment Aspose.Cells a rendu le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf). Comme vous pouvez le voir, les trois caractères Unicode supplémentaires ont été rendus exactement de la même manière que par Microsoft Excel.

![todo:image_alt_text](output.png)

## Code d'exemple

Vous pouvez utiliser ce code d'exemple pour convertir le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
