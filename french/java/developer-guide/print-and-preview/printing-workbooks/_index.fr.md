---
title: Impression des Classeurs
type: docs
weight: 20
url: /fr/java/printing-workbooks/
description: Impression des feuilles de calcul et des classeurs à l aide de Java. Cet article fournit le code Java pour imprimer des feuilles de calcul et des classeurs à l aide de l API Aspose.Cells for Java.
keywords: imprimer des classeurs, imprimer des feuilles de calcul, imprimer des feuilles de classeur, imprimer un classeur, imprimer un classeur en java, imprimer des feuilles de calcul en java, imprimer un classeur excel en java, imprimer une feuille de calcul excel, imprimer un classeur, imprimer une feuille de calcul
---

{{% alert color="primary" %}}

Ce document est conçu pour fournir aux développeurs une compréhension (de manière compacte) de la façon d'imprimer des feuilles de calcul.

{{% /alert %}}

## Scénario d'utilisation

Après avoir terminé la création de votre feuille de calcul, vous voudrez probablement imprimer une copie papier de la feuille selon vos besoins. Lors de l'impression, MS Excel suppose que vous voulez imprimer toute la zone de la feuille de calcul, sauf si vous précisez votre sélection. La capture d'écran suivante montre la boîte de dialogue pour imprimer le classeur avec Excel.

![todo:image_alt_text](printing-workbooks_1.png)

**Figure :** Boîte de dialogue d'impression

## Impression des classeurs à l'aide d'Aspose.Cells

Aspose.Cells for Java offre une méthode [**toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) de la classe [**SheetRender**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender). En utilisant la méthode [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-), vous pouvez fournir le nom de l'imprimante ainsi que le nom du travail d'impression.

## Code d'exemple

### Imprimer la feuille de calcul sélectionnée

L'exemple de code suivant illustre l'utilisation de la méthode [**SheetRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetrender#toPrinter-java.lang.String-) pour imprimer votre feuille de calcul sélectionnée.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingSelectedWorksheet-PrintingSelectedWorksheet.java" >}}

### Imprimer l'ensemble du classeur

Vous pouvez également utiliser la méthode [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) pour imprimer l'ensemble du classeur. L'exemple de code suivant illustre l'utilisation de la méthode [**WorkbookRender.toPrinter**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookrender#toPrinter-java.lang.String-) pour imprimer l'ensemble du classeur.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PrintingWholeWorkbook-PrintingWholeWorkbook.java" >}}

## Articles Connexes

- [Spécifier le nom du travail ou du document lors de l'impression avec Aspose.Cells](/cells/fr/java/specify-job-or-document-name-while-printing-with-aspose-cells/)
{{< app/cells/assistant language="java" >}}
