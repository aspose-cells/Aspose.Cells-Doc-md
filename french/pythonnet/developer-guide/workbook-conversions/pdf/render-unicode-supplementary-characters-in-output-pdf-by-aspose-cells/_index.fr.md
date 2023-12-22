---
title: Afficher les caractères supplémentaires Unicode dans la sortie PDF par Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /fr/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Découvrez comment restituer les caractères supplémentaires Unicode lors de la conversion d'Excel en PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

Les caractères Unicode normaux font 2 octets tandis que les caractères Unicode supplémentaires font 4 octets. Aspose.Cells for Python via .NET prend désormais en charge le rendu de ces caractères Unicode de 4 octets.

Dans la norme de caractères Unicode, les caractères supplémentaires sont les caractères auxquels sont attribués des points de code compris entre U+10000 et U+10FFFF. Autrement dit, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères font chacun 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités 16 bits).

{{% /alert %}}

##  Afficher les caractères supplémentaires Unicode dans la sortie PDF par Aspose.Cells for Python via .NET

 La capture d'écran suivante montre comment Aspose.Cells for Python via .NET a rendu le[fichier Excel source](5115563.xlsx) dans le[sortie PDF](5115564.pdf). Comme vous pouvez le constater, les trois caractères supplémentaires Unicode ont été rendus exactement de la même manière que par Microsoft Excel.

![tâche : image_alt_text](output.png)

##  Exemple de code

Vous pouvez utiliser cet exemple de code pour convertir[fichier Excel source](5115563.xlsx) dans[sortie PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
