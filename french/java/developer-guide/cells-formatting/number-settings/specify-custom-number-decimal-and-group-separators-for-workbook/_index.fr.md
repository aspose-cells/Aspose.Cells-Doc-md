---
title: Spécifier des séparateurs décimaux et de groupe personnalisés pour le classeur
type: docs
weight: 100
url: /fr/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cet article montre comment modifier la décimale numérique et le séparateur de groupe dans MS Excel et avec le code Java en utilisant le Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 Dans Microsoft Excel, vous pouvez spécifier les séparateurs décimaux et des milliers personnalisés au lieu d'utiliser des séparateurs système à partir du**Options Excel avancées** comme indiqué dans la capture d'écran ci-dessous.

 Aspose.Cells fournit le[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator) et[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator) properties pour définir les séparateurs personnalisés pour le formatage/l'analyse des nombres.

{{% /alert %}}

## **Spécification de séparateurs personnalisés à l'aide de Microsoft Excel**

1.  Ouvrir**Choix** dans le**Dossier** languette.
1. Ouvrez le**Avancé** languette.
1.  Modifiez les paramètres dans le**Options d'édition** section.

La capture d'écran suivante montre le**Options Excel avancées** et met en surbrillance la section pour spécifier le**Séparateurs personnalisés**.

![tâche : image_autre_texte](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Spécification de séparateurs personnalisés à l'aide de Aspose.Cells**

 L'exemple de code suivant illustre comment spécifier les séparateurs personnalisés à l'aide de Aspose.Cells API. Il spécifie les séparateurs décimaux et de groupe personnalisés comme point et espace respectivement. Donc le nombre**123,456.789** sera affiché comme**123 456.789** comme indiqué dans la capture d'écran qui montre la sortie PDF générée par le code.

![tâche : image_autre_texte](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
