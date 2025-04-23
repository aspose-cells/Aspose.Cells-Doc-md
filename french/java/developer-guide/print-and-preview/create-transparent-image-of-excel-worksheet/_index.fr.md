---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /fr/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de générer l'image de votre feuille de calcul en tant qu'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleurs de remplissage. Aspose.Cells fournit la propriété [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est **false**, alors les cellules sans couleurs de remplissage sont dessinées en blanc et quand elle est **true**, les cellules sans couleurs de remplissage sont dessinées en transparent.

{{% /alert %}}

Dans l'image de la feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

**Image de la feuille de calcul sans application de transparence**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Alors que dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

**Image de la feuille de calcul après application de la transparence**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Vous pouvez utiliser le code d'exemple suivant pour générer une image transparente de votre feuille de calcul Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
{{< app/cells/assistant language="java" >}}
