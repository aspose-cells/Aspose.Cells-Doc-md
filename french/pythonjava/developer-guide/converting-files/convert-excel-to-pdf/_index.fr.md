---
title: Convertir Excel en PDF
type: docs
weight: 50
url: /fr/python-java/convert-excel-to-pdf/
description: Comment convertir Excel en PDF avec Python. Cet article montre comment convertir des fichiers Excel en PDF en utilisant Python et l API facile à utiliser Aspose.Cells for Python via Java.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Convertir Excel en PDF**

Les documents PDF sont largement utilisés comme format standard d'échange de documents entre les organisations, les secteurs gouvernementaux et les particuliers. Les développeurs de logiciels sont souvent invités à concevoir un moyen de convertir facilement les fichiers Microsoft Excel en documents PDF. L'API Aspose.Cells for Python via Java permet de convertir des fichiers Excel en documents PDF (y compris PDF/A) avec un haut degré de précision et de fidélité.

### **Conversion directe**

Pour enregistrer un fichier Excel directement au format PDF, vous pouvez utiliser la méthode [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) et passer [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) comme deuxième paramètre.

L'extrait de code suivant illustre l'utilisation de [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) et de la méthode [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) pour convertir un Excel au format PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversion avancée**

Pour avoir plus de contrôle sur la conversion en PDF, l'API fournit la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions). La classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) peut être utilisée pour définir différentes attributs pour la conversion. En définissant différentes propriétés de la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions), vous aurez le contrôle sur les paramètres d'impression, de police, de sécurité et de compression pour le fichier PDF résultant. La propriété la plus notable est [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance) qui vous permet de sauvegarder les fichiers Excel au format PDF/A conforme.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, appelez la méthode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) juste avant de rendre la feuille de calcul au format PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
