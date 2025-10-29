---
title: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul, qui supporte la vérification des formats numériques personnalisés lors du stylage. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats numériques personnalisés afin de garantir que le style est correct.
keywords: Aspose.Cells, bibliothèques Python, feuilles de calcul, stylage, formats numériques personnalisés, vérification, validation
type: docs
weight: 170
url: /fr/python-net/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous attribuez un format de nombre personnalisé invalide à la propriété [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom), alors Aspose.Cells ne lancera aucune exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format de nombre personnalisé attribué est valide ou non, veuillez définir la propriété [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) sur ** true **.

## **Vérifier le format de nombre personnalisé lors du réglage de la propriété Style.Custom**

Le code d'exemple suivant attribue un format de nombre personnalisé invalide à la propriété [**Style.custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Puisque nous avons déjà défini la propriété [**Workbook.settings.check_custom_number_format**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/check_custom_number_format/) sur ** true **, elle lance donc une exception par exemple Format de nombre invalide. Veuillez lire les commentaires dans le code pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CheckCustomFormatPattern.py" >}}

{{< app/cells/assistant language="python-net" >}}
