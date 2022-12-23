---
title: Convertir Excel en Word
type: docs
weight: 300
url: /fr/python-java/convert-excel-to-word/
description: Convertir un fichier excel en word en utilisant Python.
keywords: Exporting Workbook to word without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java prend en charge la conversion des fichiers Excel (.xls, xlsx, .xlsb, xlsm), CSV et OpenOffice (.ods) en fichier Word.

{{% /alert %}}

## **Convertir un classeur Excel en Word**

 Pas besoin de se demander comment convertir Excel Workbook en Word, car la bibliothèque Aspose.Cells for Python via Java a la meilleure décision. Le Aspose.Cells for Python via Java API prend en charge la conversion des feuilles de calcul au format Word. Pour exporter le classeur vers Word, passez[**EnregistrerFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) comme deuxième paramètre de[**Classeur.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ) méthode. Vous pouvez également utiliser[**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions)classe pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul vers un fichier .docx.

 L'exemple de code suivant illustre l'exportation du classeur Excel vers Word. S'il vous plaît voir le code pour convertir[fichier source](sample.xlsx) au fichier Word généré par le code pour référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


