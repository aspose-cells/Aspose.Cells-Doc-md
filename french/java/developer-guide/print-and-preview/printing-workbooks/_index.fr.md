---
title: Impression de classeurs
type: docs
weight: 20
url: /fr/java/printing-workbooks/
description: Comment imprimer des feuilles de calcul et un classeur à l'aide de Java. Cet article fournit le code Java pour imprimer des feuilles de calcul et un classeur à l'aide de Aspose.Cells for Java API.
keywords: printing workbooks, printing worksheets, printing workbook sheets, printing a workbook, printing workbook java, printing worksheets java, printing excel workbook java, print excel worksheet java, print workbook, print worksheet
---
{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension (de manière compacte) sur la façon d'imprimer des feuilles de calcul.

{{% /alert %}}

## Scénario d'utilisation

Après avoir fini de créer votre feuille de calcul, vous souhaiterez probablement imprimer une copie papier de la feuille selon vos besoins. Lorsque vous imprimez, MS Excel suppose que vous souhaitez imprimer toute la zone de la feuille de calcul, sauf si vous spécifiez votre sélection. La capture d'écran suivante montre la boîte de dialogue d'impression du classeur avec Excel.

![tâche : image_autre_texte](printing-workbooks_1.png)

**Chiffre:** Boîte de dialogue Imprimer

## Impression de classeurs à l'aide de Aspose.Cells

 Aspose.Cells for Java fournit un[**versImprimante**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String) ) méthode de la[**FeuilleRendu**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender) classe. En utilisant le[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)), vous pouvez fournir le nom de l'imprimante ainsi que le nom du travail d'impression.

## Exemple de code

### Imprimer la feuille de calcul sélectionnée

 L'extrait de code suivant illustre l'utilisation de[**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter(java.lang.String)) méthode pour imprimer votre feuille de calcul sélectionnée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Imprimer le classeur entier

 Vous pouvez également utiliser le[**WorkbookRender.toPrinterWorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String) ) méthode pour imprimer tout le classeur. L'extrait de code suivant illustre l'utilisation de[**WorkbookRender.toPrinterWorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter(java.lang.String)) méthode pour imprimer tout le classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Articles Liés

- [Spécifiez le nom du travail ou du document lors de l'impression avec Aspose.Cells](/cells/fr/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
