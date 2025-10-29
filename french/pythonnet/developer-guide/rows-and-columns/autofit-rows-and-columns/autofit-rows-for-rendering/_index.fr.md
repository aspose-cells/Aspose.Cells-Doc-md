---
title: Ajuster automatiquement les lignes pour le rendu
type: docs
weight: 130
url: /fr/python-net/autofit-rows-for-rendering/
description: Apprenez à ajuster automatiquement les lignes pour le rendu grâce à l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Ajuster automatiquement les lignes pour le rendu en Python, Ajuster automatiquement la hauteur de la ligne lors de l ouverture du fichier Excel. 
---

En général, lorsque vous souhaitez afficher tout le texte dans une cellule, vous pouvez ajuster automatiquement la ligne en mode Normal avec un zoom à 100% dans Microsoft Excel. Cela permet au texte d'être entièrement visible en mode Normal, et même lorsque vous imprimez ou enregistrez le fichier au format PDF, le texte sera affiché correctement.

Cependant, dans certains cas, l'ajustement automatique de la ligne fonctionne bien en mode Normal, mais lorsque vous passez en mode d'impression ou enregistrez le fichier au format PDF, le texte est tronqué. Veuillez vérifier le fichier source [Book1.xlsx](Book1.xlsx) et les captures d'écran.

![le texte est tronqué en mode d'impression](text_clipped_in_printview.png)

Si vous voulez empêcher que le texte soit coupé dans le fichier PDF enregistré, vous pouvez ajuster automatiquement la ligne avec l'option [AutoFitterOptions.for_rendering](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/for_rendering/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-AutofitRowsForRendering.py" >}}

Maintenant, le texte n'est pas tronqué dans le fichier PDF de sortie.

![le texte n'est pas tronqué dans le PDF enregistré](text_not_clipped_in_saved_pdf.png)
{{< app/cells/assistant language="python-net" >}}
