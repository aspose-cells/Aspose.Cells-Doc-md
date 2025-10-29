---
title: Spécifier les séparateurs décimal et de groupe personnalisé pour le classeur avec Golang via C++
linktitle: Spécifiez les séparateurs décimaux et de groupe personnalisés
type: docs
weight: 110
url: /fr/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifier le séparateur décimal et de groupe des nombres dans MS Excel avec Golang via C++ en utilisant l API Aspose.Cells for C++.
keywords: spécifier séparateur décimal personnalisé excel, spécifier séparateur décimal personnalisé excel c++, spécifier séparateur de groupe personnalisé excel, spécifier séparateur de groupe personnalisé excel c++, spécifier séparateur décimal et de groupe personnalisé excel, spécifier séparateur décimal et de groupe personnalisé excel c++, changer le séparateur décimal et de groupe dans excel, changer le séparateur décimal dans excel, changer le séparateur de groupe dans excel c++, changer le séparateur de groupe dans excel c++
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et de milliers personnalisés au lieu d'utiliser les Séparateurs Système à partir des **Options Excel Avancées** comme indiqué dans la capture d'écran ci-dessous.

Aspose.Cells fournit les propriétés [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) et [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) pour définir les séparateurs personnalisés pour le formatage/analyse des nombres.

{{% /alert %}}

## **Spécification des séparateurs personnalisés à l'aide de Microsoft Excel**

La capture d'écran suivante montre les **Options Excel Avancées** et met en évidence la section pour spécifier les **Séparateurs Personnalisés**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification des séparateurs personnalisés à l'aide de Aspose.Cells**

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Il spécifie les séparateurs de décimales et de groupes numériques personnalisés comme point et espace respectivement.

### Code C++ pour spécifier les séparateurs décimaux et de groupe personnalisés

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
