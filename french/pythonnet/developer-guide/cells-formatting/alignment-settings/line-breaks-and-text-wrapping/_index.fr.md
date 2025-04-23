---
title: Sauts de ligne et retour à la ligne du texte
description: Comment implémenter le retour à la ligne de texte et le saut de ligne en utilisant la bibliothèque Aspose.Cells pour Python via .NET. En utilisant la bibliothèque Aspose.Cells pour Python via .NET, vous pouvez facilement insérer du texte dans les cellules et définir la méthode de saut de ligne, comme le retour manuel à la ligne, le saut de ligne automatique, etc. Ce document détaille comment mettre en œuvre ces fonctionnalités et fournit un exemple de code pour référence.
keywords: Aspose.Cells pour Python via .NET, sauts de ligne, retour à la ligne, mise en page du texte
type: docs
weight: 60
url: /fr/python-net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Pour vous assurer que le texte dans une cellule peut être lu, des sauts de ligne explicites et un retour à la ligne du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, tandis que les sauts de ligne explicites insérés les mettent exactement où vous le souhaitez.

{{% /alert %}}

## **Pour retourner le texte dans une cellule**

Pour retourner le texte dans une cellule, utilisez la propriété [**Style.is_text_wrapped**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_text_wrapped).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-WrapText-1.py" >}}

## **Pour utiliser des sauts de ligne explicites**

Vous pouvez utiliser '\n' en C# et 'vbLf' en VB.NET pour insérer des sauts de ligne explicites dans une cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-LineBreakTextWrapping-UseExplicitLineBreaks-1.py" >}}

