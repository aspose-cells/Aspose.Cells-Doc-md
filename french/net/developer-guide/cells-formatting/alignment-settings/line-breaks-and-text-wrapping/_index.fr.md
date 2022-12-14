---
title: Sauts de ligne et retour à la ligne
type: docs
weight: 60
url: /fr/net/line-breaks-and-text-wrapping/
---
{{% alert color="primary" %}}

Pour s'assurer que le texte d'une cellule peut être lu, des sauts de ligne et des retours à la ligne explicites peuvent être appliqués. L'habillage du texte transforme une ligne en plusieurs dans une cellule, que les sauts de ligne explicites placent exactement là où vous le souhaitez.

{{% /alert %}}

## **Pour envelopper du texte dans un Cell**

 Pour envelopper du texte dans une cellule, utilisez la[**Aspose.Cells.Style.IsTextWrapped**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/istextwrapped)propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-WrapText-1.cs" >}}

## **Pour utiliser des sauts de ligne explicites**

Vous pouvez utiliser '\n' dans C# et 'vbLf' dans VB.NET pour insérer des sauts de ligne explicites dans une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LineBreakTextWrapping-UseExplicitLineBreaks-1.cs" >}}
