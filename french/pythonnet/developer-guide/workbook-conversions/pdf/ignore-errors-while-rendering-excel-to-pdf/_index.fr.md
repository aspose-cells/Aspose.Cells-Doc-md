---
title: Ignorer les erreurs lors du rendu d'Excel vers PDF
type: docs
weight: 80
url: /fr/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Découvrez comment ignorer les erreurs lors du rendu d'Excel au format PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Scénarios d'utilisation possibles**

 Parfois, lorsque vous convertissez votre fichier Excel en PDF, des erreurs ou des exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant le processus de conversion en utilisant le[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)propriété. De cette façon, le processus de conversion se terminera sans problème sans générer d'erreur ou d'exception, mais une perte de données peut survenir. Par conséquent, veuillez utiliser cette propriété uniquement si la perte de données n'est pas critique pour vous.

##  **Ignorer les erreurs lors du rendu d'Excel vers PDF**

 Le code suivant charge le[exemple de fichier Excel](55541778.xlsx) mais l'exemple de fichier Excel est erroné et génère une erreur lors[conversion en PDF](55541779.pdf) en 17.11 mais puisque nous utilisons[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)propriété, cela ne génère pas d’erreur. Cependant, un*forme de flèche rouge arrondie*comme le montre cette capture d'écran est perdu.

![tâche : image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Exemple de code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
