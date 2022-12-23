---
title: Ignorer les erreurs lors du rendu d'Excel en PDF
type: docs
weight: 80
url: /fr/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Scénarios d'utilisation possibles**

 Parfois, lorsque vous convertissez votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant le processus de conversion en utilisant le[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)la propriété. De cette façon, le processus de conversion se terminera en douceur sans générer d'erreur ou d'exception, mais la perte de données peut se produire. Par conséquent, veuillez n'utiliser cette propriété que si la perte de données n'est pas critique pour vous.

## **Ignorer les erreurs lors du rendu d'Excel en PDF**

 Le code suivant charge le[exemple de fichier Excel](55541778.xlsx) mais l'exemple de fichier Excel est erroné et génère une erreur lors de[conversion en PDF](55541779.pdf) en 17.11 mais puisque nous utilisons[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)propriété, il ne génère pas d'erreur. Cependant, un*forme de flèche rouge arrondie*comme indiqué dans cette capture d'écran est perdu.

![tâche : image_autre_texte](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
