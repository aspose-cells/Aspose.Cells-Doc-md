---
title: Sauts de ligne et retour à la ligne du texte
description: Comment implémenter le retour à la ligne et le retour à la ligne du texte en utilisant la bibliothèque Aspose.Cells en C#. En utilisant la bibliothèque Aspose.Cells, vous pouvez facilement insérer du texte dans des cellules et définir la méthode de retour à la ligne du texte, tel que le retour à la ligne manuel, le retour à la ligne automatique, etc. Ce document détaille comment mettre en œuvre ces fonctionnalités et fournit un code d exemple à titre de référence.
keywords: Aspose.Cells, sauts de ligne, retours à la ligne, mise en page du texte
type: docs
weight: 60
url: /fr/net/line-breaks-and-text-wrapping/
---

{{% alert color="primary" %}}

Pour vous assurer que le texte dans une cellule peut être lu, des sauts de ligne explicites et un retour à la ligne du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, tandis que les sauts de ligne explicites insérés les mettent exactement où vous le souhaitez.

{{% /alert %}}

## **Pour retourner le texte dans une cellule**

Pour retourner le texte dans une cellule, utilisez la propriété [**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Pour utiliser des sauts de ligne explicites**

Vous pouvez utiliser '\n' en C# et 'vbLf' en VB.NET pour insérer des sauts de ligne explicites dans une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
