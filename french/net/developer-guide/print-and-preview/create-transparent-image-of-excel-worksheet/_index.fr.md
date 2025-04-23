---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /fr/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleur de remplissage. Aspose.Cells fournit la propriété [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **fausse**, les cellules sans couleur de remplissage sont dessinées en blanc et lorsqu'elle est **true**, les cellules sans couleur de remplissage sont dessinées de manière transparente.

{{% /alert %}} 

Dans l'image de la feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

|**Sortie sans transparence : l'arrière-plan de la cellule est blanc**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Alors que dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

|**Sortie avec transparence activée**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Le code d'exemple suivant génère une image transparente à partir d'une feuille de calcul Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
