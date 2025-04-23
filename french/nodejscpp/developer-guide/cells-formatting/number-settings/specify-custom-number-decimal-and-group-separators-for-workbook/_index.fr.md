---
title: Spécifier les séparateurs de décimales et de groupes de nombres personnalisés pour le classeur
linktitle: Spécifier les séparateurs de décimales et de groupes de nombres personnalisés pour le classeur
type: docs
weight: 110
url: /fr/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Modifier les séparateurs décimaux et de groupe dans Excel à l aide de Aspose.Cells for Node.js via C++. 
keywords: spécifier le séparateur décimal personnalisé excel node.js via C++, spécifier le séparateur de groupe personnalisé excel node.js via C++, changer le séparateur décimal et de groupe excel node.js via C++
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et de milliers personnalisés au lieu d'utiliser les Séparateurs Système à partir des **Options Excel Avancées** comme indiqué dans la capture d'écran ci-dessous.

Aspose.Cells fournit les méthodes [**WorkbookSettings.setNumberDecimalSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberDecimalSeparator-string-) et [**WorkbookSettings.setNumberGroupSeparator(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#setNumberGroupSeparator-string-) pour définir les séparateurs personnalisés pour le formatage/analyse des nombres.

{{% /alert %}}

## **Spécification des séparateurs personnalisés à l'aide de Microsoft Excel**

La capture d'écran suivante montre les **Options Excel Avancées** et met en évidence la section pour spécifier les **Séparateurs Personnalisés**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification de séparateurs personnalisés en utilisant Aspose.Cells for Node.js via C++**

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés à l'aide de l'API Aspose.Cells. Il spécifie les séparateurs de décimales et de groupes numériques personnalisés comme point et espace respectivement.

### Code Node.js pour spécifier les séparateurs décimal et de groupe Personnalisés pour les nombres

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-SpecifyCustomNumberDecimalAndGroupSeparators.js" >}}


