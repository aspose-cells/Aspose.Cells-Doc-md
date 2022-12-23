---
title: Ignorer les erreurs lors du rendu d'Excel en PDF
type: docs
weight: 70
url: /fr/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Scénarios d'utilisation possibles**

Parfois, lorsque vous convertissez votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant le processus de conversion en utilisant le[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)la propriété. De cette façon, le processus de conversion se terminera en douceur sans générer d'erreur ou d'exception, mais la perte de données peut se produire. Par conséquent, veuillez n'utiliser cette propriété que si la perte de données n'est pas critique pour vous.

## **Ignorer les erreurs lors du rendu d'Excel en PDF**

Le code suivant charge le[exemple de fichier Excel](55541813.xlsx)mais l'exemple de fichier Excel est erroné et génère une erreur lors de la[conversion en PDF](55541814.pdf)en 17.11 mais puisque nous utilisons[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)propriété, il ne génère pas d'erreur. Cependant, une forme arrondie en forme de flèche rouge, comme illustré dans cette capture d'écran, est perdue.

![tâche : image_autre_texte](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
