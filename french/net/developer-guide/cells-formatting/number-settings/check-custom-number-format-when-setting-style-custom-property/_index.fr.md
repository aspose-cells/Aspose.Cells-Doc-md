---
title: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
description: Aspose.Cells est une bibliothèque .NET pour travailler avec des fichiers de feuille de calcul, qui prend en charge la vérification des formats de nombre personnalisés lors du stylage. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats de nombre personnalisés afin de garantir que le stylage est correct.
keywords: Aspose.Cells, bibliothèques .NET, feuilles de calcul, stylage, formatage de nombre personnalisé, vérification, validation
type: docs
weight: 170
url: /fr/net/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous attribuez un format de nombre personnalisé invalide à la propriété [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom), alors Aspose.Cells ne lancera aucune exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format de nombre personnalisé attribué est valide ou non, veuillez définir la propriété [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) sur ** true **.

## **Vérifier le format de nombre personnalisé lors du réglage de la propriété Style.Custom**

Le code d'exemple suivant attribue un format de nombre personnalisé invalide à la propriété [**Style.Custom**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom). Puisque nous avons déjà défini la propriété [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) sur ** true **, elle lance donc une exception par exemple Format de nombre invalide. Veuillez lire les commentaires dans le code pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
{{< app/cells/assistant language="csharp" >}}
