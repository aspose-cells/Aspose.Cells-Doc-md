---
title: Convertir Excel en PDF
type: docs
weight: 50
url: /fr/python-java/convert-excel-to-pdf/
description: Comment convertir Excel en PDF avec Python. Cet article montre comment convertir des fichiers Excel en PDF en utilisant Python et facile à utiliser Aspose.Cells pour Python via Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Convertir Excel en PDF**

Les documents PDF sont largement utilisés comme format standard d'échange de documents entre les organisations, les secteurs gouvernementaux et les particuliers. Les développeurs de logiciels sont souvent invités à concevoir un moyen de convertir facilement des fichiers Excel Microsoft en documents PDF. Aspose.Cells pour Python via Java API offre la possibilité de convertir des fichiers Excel en documents PDF (y compris PDF/A). Aspose.Cell convertit les feuilles de calcul en PDF avec un degré élevé de précision et de fidélité.

### **Conversion directe**

Pour enregistrer un fichier Excel directement au format PDF, vous pouvez utiliser le[**Classeur.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)méthode et passe[**EnregistrerFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) comme deuxième paramètre.

L'extrait de code suivant illustre l'utilisation de[**EnregistrerFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)et le[**Classeur.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) méthode pour convertir Excel au format PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversion avancée**

Pour avoir plus de contrôle sur la conversion en PDF, le API fournit le[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)classer. La[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class peut être utilisé pour définir différents attributs pour la conversion. Définition de différentes propriétés du[**PdfEnregistrerOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class vous donnera le contrôle sur les paramètres d'impression, de police, de sécurité et de compression du fichier PDF résultant. La propriété la plus remarquable est la[**Conformité**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)qui vous permet d'enregistrer les fichiers Excel dans des fichiers PDF compatibles PDF/A.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 si votre feuille de calcul contient des formules, appelez le[**Workbook.calculateFormulaWorkbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
