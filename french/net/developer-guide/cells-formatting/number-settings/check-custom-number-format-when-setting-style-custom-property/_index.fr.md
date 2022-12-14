---
title: Vérifier le format numérique personnalisé lors de la définition de la propriété Style.Custom
type: docs
weight: 170
url: /fr/net/check-custom-number-format-when-setting-style-custom-property/
---
## **Scénarios d'utilisation possibles**

 Si vous attribuez un format de nombre personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)propriété, alors Aspose.Cells ne lèvera aucune exception. Mais si vous voulez que Aspose.Cells vérifie si le format de numéro personnalisé attribué est valide ou non, veuillez définir le[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propriété à**vrai**.

## **Vérifiez le format de nombre personnalisé lors de la définition de la propriété Style.Custom**

 L'exemple de code suivant attribue un format de nombre personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propriété. Depuis, nous avons déjà fixé[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) propriété à**vrai**, par conséquent, il lève une exception, par exemple Format de nombre invalide. Veuillez lire les commentaires à l'intérieur du code pour plus d'aide.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
