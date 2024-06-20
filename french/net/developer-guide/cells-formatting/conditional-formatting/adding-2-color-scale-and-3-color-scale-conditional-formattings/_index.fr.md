---
title: Ajout de formats conditionnels 2 couleurs et 3 couleurs
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour ajouter un formatage conditionnel pour deux ratios de couleurs et trois ratios de couleurs. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Format conditionnel, C#, Ratio de couleurs, Échelle de couleurs à deux couleurs, Échelle de couleurs à trois couleurs
type: docs
weight: 20
url: /fr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/
---

{{% alert color="primary" %}}

Les formats conditionnels **2 couleurs** et **3 couleurs** sont ajoutés de la même manière, sauf qu'ils sont différenciés par la propriété [**FormatCondition.ColorScale.Is3ColorScale**](https://reference.aspose.com/cells/net/aspose.cells/colorscale/properties/is3colorscale). Cette propriété est **false** pour les formats conditionnels 2 couleurs et **true** pour les formats conditionnels 3 couleurs.

{{% /alert %}}

Le code d'exemple suivant ajoute des formats conditionnels 2 couleurs et 3 couleurs. Il génère le [fichier Excel en sortie](5115058.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-AddColorScales-AddColorScales.cs" >}}
