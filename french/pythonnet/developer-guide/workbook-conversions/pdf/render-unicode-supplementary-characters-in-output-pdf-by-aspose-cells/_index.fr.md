---
title: Rendre des caractères Unicode supplémentaires dans le PDF de sortie avec Aspose.Cells pour Python via .NET
type: docs
weight: 350
url: /fr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Apprenez à rendre des caractères Unicode supplémentaires lors de la conversion d Excel en PDF avec Aspose.Cells pour Python via .NET API.
keywords: Rendre des caractères Unicode supplémentaires avec Python lors de l enregistrement du fichier au format PDF, Afficher des caractères Unicode supplémentaires lors de l enregistrement d Excel au format PDF en utilisant Python, Python Afficher des caractères Unicode supplémentaires lors de la conversion d Excel en PDF, Rendre des caractères Unicode supplémentaires pour excel en pdf
---

{{% alert color="primary" %}}

Les caractères Unicode normaux ont une longueur de 2 octets, tandis que les caractères Unicode supplémentaires ont une longueur de 4 octets. Aspose.Cells pour Python via .NET prend désormais en charge le rendu de ces caractères Unicode sur 4 octets.

Dans la norme des caractères Unicode, les Caractères supplémentaires sont les caractères aux points de code de U+10000 à U+10FFFF. En d'autres termes, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères ont une longueur de 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités de 16 bits).

{{% /alert %}}

## Rendre des caractères Unicode supplémentaires dans le PDF de sortie avec Aspose.Cells pour Python via .NET

La capture d'écran suivante montre comment Aspose.Cells pour Python via .NET a rendu le [fichier Excel source](5115563.xlsx) dans le [PDF de sortie](5115564.pdf). Comme vous pouvez le constater, tous les trois caractères Unicode supplémentaires ont été rendus exactement de la même manière que par Microsoft Excel.

![todo:image_alt_text](output.png)

## Code d'exemple

Vous pouvez utiliser ce code d'exemple pour convertir le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
