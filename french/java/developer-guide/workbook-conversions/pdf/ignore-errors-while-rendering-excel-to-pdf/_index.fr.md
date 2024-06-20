---
title: Ignorer les erreurs lors de la conversion Excel en PDF
type: docs
weight: 70
url: /fr/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Scénarios d'utilisation possibles**

Parfois, lors de la conversion de votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant le processus de conversion en utilisant la propriété [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError). De cette manière, le processus de conversion se terminera correctement sans générer d'erreur ou d'exception, mais la perte de données peut survenir. Par conséquent, veuillez utiliser cette propriété uniquement si la perte de données n'est pas critique pour vous.

## **Ignorer les erreurs lors du rendu Excel vers PDF**

Le code suivant charge le [fichier Excel d'exemple](55541813.xlsx) mais le fichier Excel d'exemple est erroné et génère une erreur lors de la [conversion en PDF](55541814.pdf) en 17.11 mais comme nous utilisons la propriété [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError), il ne génère pas d'erreur. Cependant, une forme de flèche rouge arrondie comme indiqué dans cette capture d'écran est perdue.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
