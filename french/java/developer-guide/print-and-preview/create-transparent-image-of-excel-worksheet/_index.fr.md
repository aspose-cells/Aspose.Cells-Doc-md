---
title: Créer une image transparente de la feuille de calcul Excel
type: docs
weight: 80
url: /fr/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Parfois, vous devez générer l'image de votre feuille de calcul sous forme d'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleurs de remplissage. Aspose.Cells fournit le[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) propriété pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est**faux** , les cellules sans couleur de remplissage sont dessinées en blanc et quand c'est le cas**vrai**, les cellules sans couleur de remplissage sont dessinées en transparence.

{{% /alert %}}

Dans l'image de feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

**Image de feuille de calcul sans appliquer de transparence**

![tâche : image_autre_texte](create-transparent-image-of-excel-worksheet_1.png)

Tandis que, dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

**Image de la feuille de calcul après application de la transparence**

![tâche : image_autre_texte](create-transparent-image-of-excel-worksheet_2.png)

Vous pouvez utiliser l'exemple de code suivant pour générer une image transparente de votre feuille de calcul Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
