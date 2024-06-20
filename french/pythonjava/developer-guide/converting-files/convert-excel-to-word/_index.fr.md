---
title: Convertir Excel en Word
type: docs
weight: 300
url: /fr/python-java/convert-excel-to-word/
description: Convertir un fichier Excel en Word en utilisant Python.
keywords: Exportation du classeur en Word sans Office 2013, Office 2016, Office 2019 et Office 365
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java prend en charge la conversion de fichiers Excel (.xls, xlsx, .xlsb, xlsm), CSV et OpenOffice (.ods) en fichier Word.

{{% /alert %}}

## **Convertir le classeur Excel en Word**

Pas besoin de se demander comment convertir un classeur Excel en Word, car la bibliothèque Aspose.Cells for Python via Java propose la meilleure solution. L'API Aspose.Cells for Python via Java prend en charge la conversion de feuilles de calcul au format Word. Pour exporter le classeur au format Word, passez [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) comme second paramètre de la méthode [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). Vous pouvez également utiliser la classe [**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions) pour spécifier des paramètres supplémentaires pour exporter la feuille de calcul au format .docx.

L'exemple de code suivant démontre l'exportation du classeur Excel vers Word. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) au fichier Word généré par le code pour référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


