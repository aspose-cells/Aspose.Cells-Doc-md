---
title: Rendu d'une page PDF par feuille de calcul Excel - Conversion d'Excel en PDF
type: docs
weight: 100
url: /fr/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Découvrez comment afficher une page PDF par feuille de calcul Excel lors de la conversion d'Excel en PDF avec Aspose.Cells for Python via .NET API.
keywords: Python Render One PDF Page Per Excel Worksheet while saving file to PDF, One PDF Page Per Excel Worksheet while saving Excel to PDF using Python, Python show one page per worksheet when converting Excel to PDF
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec des fichiers Excel Microsoft volumineux (par exemple un classeur comportant de nombreuses feuilles, chacune comportant 50 colonnes et 300 lignes de données ou plus), vous souhaiterez peut-être que la sortie PDF affiche une page par feuille de calcul, quelle que soit la taille de la feuille de calcul. . Cela signifierait que chaque page aura probablement une taille de page radicalement différente. Ceci peut être réalisé en utilisant le Aspose.Cells for Python via .NET API.

{{% /alert %}} 

Veuillez consulter l'exemple de code suivant qui convertit un fichier Excel contenant plusieurs feuilles de calcul en PDF.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderOnePdfPagePerExcelWorksheet-1.py" >}}

{{% alert color="primary" %}} 

 Si la[PdfSaveOptions.one_page_per_sheet](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/one_page_per_sheet/)est définie sur *true**, tout le contenu de la feuille sera restitué sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}} 

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
