---
title: Vérifier le format numérique personnalisé lors de la définition de la propriété Style.Custom avec Golang via C++
description: Aspose.Cells est une bibliothèque C++ pour travailler avec des fichiers de feuilles de calcul, qui supporte la vérification des formats numériques personnalisés lors du stylage. Cet article vous montrera comment utiliser la bibliothèque Aspose.Cells pour vérifier les formats numériques personnalisés afin de garantir que le style est correct.
keywords: Aspose.Cells, bibliothèques C++, feuilles de calcul, stylage, formatage numérique personnalisé, vérification, validation
type: docs
weight: 170
url: /fr/go-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Scénarios d'utilisation possibles**

Si vous assignez un format numérique personnalisé invalide à la propriété [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/), Aspose.Cells ne lancera pas d'exception. Mais si vous souhaitez que Aspose.Cells vérifie si le format numérique personnalisé assigné est valide ou non, veuillez définir la propriété [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) sur **true**.

## **Vérifier le format de nombre personnalisé lors du réglage de la propriété Style.Custom**

Le code d'exemple suivant assigne un format numérique personnalisé invalide à la propriété [**Style.GetCustom()**](https://reference.aspose.com/cells/go-cpp/style/getcustom/). Étant donné que nous avons déjà défini la propriété [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) sur **true**, une exception sera levée, par exemple, format numérique invalide. Veuillez lire les commentaires dans le code pour plus d'aide.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckCustomNumberFormatWhenSettingStyleCustomProperty.go" >}}
