---
title: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
type: docs
weight: 160
url: /fr/java/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous attribuez un format de nombre personnalisé non valide à la propriété [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom), alors Aspose.Cells ne lèvera aucune exception. Mais si vous voulez que Aspose.Cells vérifie si le format de nombre personnalisé attribué est valide ou non, veuillez alors définir la propriété [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) sur **true**.

## **Vérifiez le format de nombre personnalisé lors du paramétrage de la propriété Style.Custom.**

Le code d'exemple suivant attribue un format de nombre personnalisé non valide à la propriété [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Puisque nous avons déjà défini la propriété [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) sur **true**, par conséquent, l'API lèvera une exception CellsException telle que *Format de nombre non valide*.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
