---  
title: Sauts de ligne et retour à la ligne du texte
linktitle: Sauts de ligne et retour à la ligne du texte  
description: Comment implémenter le retour à la ligne du texte et le saut de ligne dans le library Aspose.Cells dans Node.js via C++. En utilisant la bibliothèque Aspose.Cells, vous pouvez facilement insérer du texte dans des cellules et définir la méthode de retour à la ligne, comme le saut de ligne manuel, le retour à la ligne automatique, etc. Ce document détaille comment implémenter ces fonctionnalités et fournit du code d exemple pour votre référence.  
keywords: Aspose.Cells, sauts de ligne, retour à la ligne du texte, disposition du texte Node.js via C++  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Pour vous assurer que le texte dans une cellule peut être lu, des sauts de ligne explicites et un retour à la ligne du texte peuvent être appliqués. Le retour à la ligne du texte transforme une ligne en plusieurs dans une cellule, tandis que les sauts de ligne explicites insérés les mettent exactement où vous le souhaitez.  
{{% /alert %}}  

## **Pour retourner le texte dans une cellule**  
 Pour sauter à la ligne dans une cellule, utilisez la méthode [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Pour utiliser des sauts de ligne explicites**  
 Vous pouvez utiliser '\n' en JavaScript pour insérer des sauts de ligne explicites dans une cellule.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



