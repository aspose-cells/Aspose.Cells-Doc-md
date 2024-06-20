---
title: Spécifier les séparateurs de décimales et de groupes de nombres personnalisés pour le classeur
type: docs
weight: 100
url: /fr/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cet article montre comment changer le séparateur de décimales et de groupes dans MS Excel et avec du code Java en utilisant l API Aspose.Cells for Java.
keywords: spécifier le séparateur de décimales personnalisé excel, spécifier le séparateur de décimales personnalisé excel java, spécifier le séparateur de groupes personnalisé excel, spécifier le séparateur de groupes personnalisé excel java, spécifier le séparateur de décimales et de groupes personnalisé excel, spécifier le séparateur de décimales et de groupes personnalisé excel java, changer le séparateur de décimales et de groupes excel java, changer le séparateur de décimales et de groupes excel, changer le séparateur de décimales excel, changer le séparateur de décimales excel java, changer le séparateur de groupes excel, changer le séparateur de groupes excel java
---

{{% alert color="primary" %}}

Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et de milliers personnalisés au lieu d'utiliser les Séparateurs Système à partir des **Options Excel Avancées** comme indiqué dans la capture d'écran ci-dessous.

Aspose.Cells fournit les propriétés [**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) et [WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) pour définir les séparateurs personnalisés pour le formatage/l'analyse des nombres.

{{% /alert %}}

## **Spécification des séparateurs personnalisés à l'aide de Microsoft Excel**

1. Ouvrez **Options** dans l'onglet **Fichier**.
1. Ouvrez l'onglet **Avancé**.
1. Modifiez les paramètres dans la section **Options de modification**.

La capture d'écran suivante montre les **Options Excel Avancées** et met en évidence la section pour spécifier les **Séparateurs Personnalisés**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification des séparateurs personnalisés à l'aide de Aspose.Cells**

Le code d'exemple suivant illustre comment spécifier les séparateurs personnalisés en utilisant l'API Aspose.Cells. Il spécifie les séparateurs personnalisés de décimales et de groupes comme point et espace respectivement. Ainsi, le nombre **123,456.789** sera affiché comme **123 456.789** comme le montre la capture d'écran qui montre le PDF généré en sortie par le code.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
