---
title: Enregistrez chaque feuille de calcul dans un fichier PDF différent
type: docs
weight: 130
url: /fr/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Découvrez comment enregistrer chaque feuille de calcul dans un fichier PDF différent avec Aspose.Cells for Python via .NET API.
keywords: Python Save Each Worksheet to a Different PDF File
---
{{% alert color="primary" %}} 

Aspose.Cells for Python via .NET prend en charge la conversion de fichiers XLS (contenant des images, des graphiques, etc.) en documents PDF. Aspose.Cells for Python via .NET peut fonctionner indépendamment pour convertir une feuille de calcul en PDF et vous n'avez pas besoin d'utiliser Aspose.PDF for .NET pour la conversion. La conversion ne nécessite pas que le logiciel crée ou utilise des fichiers temporaires car l'ensemble du processus peut être effectué en mémoire.

{{% /alert %}} 
##  **Enregistrez chaque feuille de calcul dans un fichier PDF différent**
 Si vous devez enregistrer chaque feuille de calcul dans votre modèle de fichier Excel pour générer différents fichiers PDF, vous pouvez y parvenir facilement. Vous pouvez essayer de définir un index de feuille sur**[`PdfSaveOptions.sheet_set`](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/)** option à la fois pour rendre au PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

 Si votre feuille de calcul contient des formules, il est préférable d'appeler[**Classeur.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
