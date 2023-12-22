---
title: Ajustement automatique des lignes pour le rendu
type: docs
weight: 130
url: /fr/java/autofit-rows-for-rendering/
---
Généralement, lorsque vous souhaitez afficher tout le texte d'une cellule, vous pouvez ajuster automatiquement la ligne en mode Normal avec un zoom de 100 % dans Microsoft Excel. Cela permet au texte d'être entièrement visible en mode Normal, et même lorsque vous imprimez ou enregistrez le fichier sous le numéro PDF, le texte s'affichera correctement.

 Cependant, dans certains cas, l'ajustement automatique de la ligne fonctionne correctement en mode Normal, mais lorsque vous passez en mode impression ou enregistrez le fichier sous le numéro PDF, le texte est tronqué. Veuillez vérifier le fichier source[Livre1.xlsx](Book1.xlsx) et des captures d'écran.

![le texte est tronqué en mode impression](text_clipped_in_printview.png)

Si vous souhaitez éviter que le texte ne soit tronqué dans le fichier PDF enregistré, vous pouvez ajuster automatiquement la ligne avec le[AutoFitterOptions.ForRendering](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions/#setForRendering-boolean-) option.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Autofit-AutofitRowsForRendering.java" >}}

Désormais, le texte n'est plus tronqué dans le fichier de sortie PDF.

![le texte n'est pas tronqué dans le pdf enregistré](text_not_clipped_in_saved_pdf.png)