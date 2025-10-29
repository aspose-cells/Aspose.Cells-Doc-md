---
title: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
linktitle: Vérifier le format de nombre personnalisé lors du réglage de Style.Custom Property
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de feuille de calcul, qui supporte la vérification des formats numériques personnalisés lors de la mise en style. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats numériques personnalisés afin de s assurer que le style est correct.
keywords: Aspose.Cells, Bibliothèques Node.js, Feuilles de calcul, Style, Format numérique personnalisé, Vérification, Validation
type: docs
weight: 170
url: /fr/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous attribuez un format numérique personnalisé invalide à la méthode [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-), alors Aspose.Cells for Node.js via C++ ne throwera aucune exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format numérique personnalisé attribué est valable ou non, veuillez définir la méthode [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) sur **true**.

## **Vérifiez le format personnalisé du numéro lors de la définition de la méthode Style.setCustom(string)**

Le code d'exemple suivant attribue un format de numéro personnalisé invalide à [**Style.setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-). Étant donné que nous avons déjà défini la méthode [**Workbook.getSettings().setCheckCustomNumberFormat(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setCheckCustomNumberFormat-boolean-) sur **true**, cela génère une exception, par exemple Format de nombre invalide. Veuillez lire les commentaires dans le code pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-CheckCustomNumberFormat.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
