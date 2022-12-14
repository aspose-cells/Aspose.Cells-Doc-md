---
title: Rendre la feuille de calcul dans le contexte graphique
type: docs
weight: 300
url: /fr/net/render-worksheet-to-graphic-context/
---
{{% alert color="primary" %}}

Aspose.Cells peut désormais rendre la feuille de calcul dans un contexte graphique. Le contexte graphique peut être quelque chose comme un fichier image, un écran ou une imprimante, etc. Veuillez utiliser l'une des deux méthodes suivantes pour rendre la feuille de calcul dans le contexte graphique.

- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/1)
- [**SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)**](https://reference.aspose.com/cells/net/aspose.cells.rendering.sheetrender/toimage/methods/2)

{{% /alert %}}

 Le code suivant illustre comment utiliser Aspose.Cells pour afficher la feuille de calcul dans un contexte graphique. Une fois que vous aurez exécuté un code, il imprimera toute la feuille de calcul et remplira l'espace vide restant avec une couleur bleue dans le contexte graphique et enregistrera l'image sous**OutputImage_out_.png** dossier. Vous pouvez utiliser n'importe quel fichier Excel source pour essayer ce code. Veuillez également lire les commentaires à l'intérieur du code pour une meilleure compréhension.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-RenderWorksheetToGraphicContext-RenderWorksheetToGraphicContext.cs" >}}
