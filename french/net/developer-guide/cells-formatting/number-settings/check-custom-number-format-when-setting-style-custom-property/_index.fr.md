---
title: Vérifiez le format de numéro personnalisé lors de la définition de la propriété Style.Custom
description: Aspose.Cells est une bibliothèque .NET permettant de travailler avec des feuilles de calcul, qui prend en charge la vérification des formats de nombres personnalisés lors du style. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats de nombres personnalisés afin de garantir que le style est correct.
keywords: Aspose.Cells, NET libraries, spreadsheets, styling, custom number formatting, checking, validation
type: docs
weight: 170
url: /fr/net/check-custom-number-format-when-setting-style-custom-property/
---
##  **Scénarios d'utilisation possibles**

 Si vous attribuez un format de numéro personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propriété, alors Aspose.Cells ne lèvera aucune exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format de numéro personnalisé attribué est valide ou non, veuillez définir le[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propriété à *true**.

##  **Vérifiez le format de numéro personnalisé lors de la définition de la propriété Style.Custom**

 L'exemple de code suivant attribue un format de numéro personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propriété. Depuis, nous avons déjà défini[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propriété à *true**, donc il lève une exception, par exemple Format de nombre invalide. Veuillez lire les commentaires à l'intérieur du code pour plus d'aide.

##  **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
