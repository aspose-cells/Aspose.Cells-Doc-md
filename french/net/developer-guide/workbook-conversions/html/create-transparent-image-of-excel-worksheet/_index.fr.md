---
title: Créer une image transparente de la feuille de calcul Excel
type: docs
weight: 170
url: /fr/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Parfois, vous devez générer l'image de votre feuille de calcul sous forme d'image transparente. Vous souhaitez appliquer la transparence à toutes les cellules qui n'ont pas de couleurs de remplissage. Aspose.Cells fournit le[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)propriété pour appliquer la transparence à l'image de la feuille de calcul. Lorsque cette propriété est**faux** , les cellules sans couleur de remplissage sont dessinées en blanc et quand c'est le cas**vrai**, les cellules sans couleur de remplissage sont dessinées en transparence.

{{% /alert %}} 

Dans l'image de feuille de calcul suivante, la transparence n'a pas été appliquée. Les cellules sans couleur de remplissage sont dessinées en blanc.

|**Sortie sans transparence : le fond de la cellule est blanc**|
|:- |
|![tâche : image_autre_texte](create-transparent-image-of-excel-worksheet_1.png)|

Tandis que, dans l'image de feuille de calcul suivante, la transparence a été appliquée. Les cellules sans couleur de remplissage sont transparentes.

|**Sortie avec transparence activée**|
|:- |
|![tâche : image_autre_texte](create-transparent-image-of-excel-worksheet_2.png)|

L'exemple de code suivant génère une image transparente à partir d'une feuille de calcul Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
