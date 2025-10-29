---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /fr/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Parfois, vous souhaitez générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules sans couleur de remplissage. Aspose.Cells pour Python via .NET fournit la propriété [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **fausse**, les cellules sans couleur de remplissage sont dessinées en blanc, et lorsqu'elle est **vraie**, les cellules sans couleur de remplissage sont dessinées transparentes.

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
