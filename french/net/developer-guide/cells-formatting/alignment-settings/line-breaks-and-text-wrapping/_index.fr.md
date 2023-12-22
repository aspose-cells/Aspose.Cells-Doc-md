---
title: Sauts de ligne et retour à la ligne du texte
description: Comment implémenter l'habillage de texte et l'habillage de mots à l'aide de la bibliothèque Aspose.Cells dans C#. En utilisant la bibliothèque Aspose.Cells, vous pouvez facilement insérer du texte dans des cellules et définir la méthode d'habillage de texte, telle que l'habillage de texte manuel, l'habillage de mots, etc. Ce document détaille comment pour implémenter ces fonctionnalités et fournit un exemple de code pour votre référence.
keywords: Aspose.Cells, line breaks, text wraps, text layout
type: docs
weight: 60
url: /fr/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Pour garantir que le texte d'une cellule peut être lu, des sauts de ligne explicites et un habillage du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, les sauts de ligne explicites étant placés exactement là où vous le souhaitez.

{{% /alert %}}

##  **Pour envelopper du texte dans un Cell**

Pour envelopper du texte dans une cellule, utilisez l'option[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

##  **Pour utiliser des sauts de ligne explicites**

Vous pouvez utiliser '\n' dans C# et 'vbLf' dans VB.NET pour insérer des sauts de ligne explicites dans une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
