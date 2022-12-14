---
title: Vérifier le format numérique personnalisé lors de la définition de la propriété Style.Custom
type: docs
weight: 160
url: /fr/java/check-custom-number-format-when-setting-style-custom-property/
---
## **Scénarios d'utilisation possibles**

 Si vous attribuez un format de nombre personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom)propriété alors Aspose.Cells ne lèvera aucune exception. Mais si vous voulez que Aspose.Cells vérifie si le format de numéro personnalisé attribué est valide ou non, veuillez définir le[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) propriété à**vrai**.

## **Vérifiez le format de nombre personnalisé lors de la définition de la propriété Style.Custom**

 L'exemple de code suivant attribue un format de nombre personnalisé non valide à[**Style.Personnalisé**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) propriété. Puisque nous avons déjà défini[**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) propriété à**vrai** , donc le API lancera CellsException par exemple*Format de nombre invalide*.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
