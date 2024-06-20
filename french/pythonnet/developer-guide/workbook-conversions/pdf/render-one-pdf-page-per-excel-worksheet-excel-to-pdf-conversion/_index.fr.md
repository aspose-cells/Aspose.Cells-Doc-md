---
title: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF
type: docs
weight: 100
url: /fr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Apprenez à rendre une page PDF par feuille de calcul Excel lors de la conversion d Excel en PDF avec Aspose.Cells pour Python via .NET API.
keywords: Rendre une page PDF par feuille de calcul Excel en enregistrant le fichier au format PDF avec Python, Une page PDF par feuille de calcul Excel lors de l enregistrement d Excel au format PDF en utilisant Python, Python montre une page par feuille de calcul lors de la conversion d Excel en PDF
---

{{% alert color="primary" %}} 

Lorsque vous travaillez avec de grands fichiers Microsoft Excel (par exemple, un classeur comportant de nombreuses feuilles, chacune comportant 50 colonnes et 300 lignes ou plus de données), vous souhaitez peut-être que la sortie PDF affiche une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. Cela signifierait que chaque page est susceptible d'avoir une taille de page radicalement différente. Cela peut être réalisé en utilisant Aspose.Cells pour Python via .NET API.

{{% /alert %}} 

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

Si l'option [PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)  est définie sur **true**, tout le contenu de la feuille sera rendu sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

Si votre feuille de calcul contient des formules, il est préférable d'appeler la méthode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
