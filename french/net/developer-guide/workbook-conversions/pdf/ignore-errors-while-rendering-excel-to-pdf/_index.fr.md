---
title: Ignorer les erreurs lors de la conversion Excel en PDF
type: docs
weight: 80
url: /fr/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Scénarios d'utilisation possibles**

Parfois, lors de la conversion de votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion s'arrête. Vous pouvez ignorer toutes ces erreurs pendant le processus de conversion en utilisant la propriété [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror). De cette façon, le processus de conversion se terminera sans problème sans générer d'erreur ou d'exception, mais une perte de données peut se produire. Par conséquent, veuillez utiliser cette propriété uniquement si la perte de données n'est pas critique pour vous.

## **Ignorer les erreurs lors du rendu Excel vers PDF**

Le code suivant charge le fichier Excel d'exemple mais le fichier Excel d'exemple est erroné et génère une erreur lors de la conversion en PDF en 17.11 mais puisque nous utilisons la propriété [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror), cela ne génère pas d'erreur. Cependant, une forme de flèche rouge arrondie comme indiqué dans cette capture d'écran est perdue.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
