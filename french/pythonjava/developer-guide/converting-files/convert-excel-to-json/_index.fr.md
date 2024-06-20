---
title: Convertir Excel en JSON
type: docs
weight: 300
url: /fr/python-java/convert-excel-to-json/
description: Apprenez comment convertir un fichier Excel en JSON avec Aspose.Cells for Python via Java.
keywords: Exporter le classeur au format JSON sans office 2013, office 2016, office 2019 et office 365
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

{{% /alert %}}

## **Convertir un classeur Excel en JSON**

Pas besoin de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for Python via Java propose la meilleure solution. L'API Aspose.Cells for Python via Java prend en charge la conversion de feuilles de calcul au format JSON. Pour exporter le classeur au format JSON, passez [**SaveFormat.JSON**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) comme deuxième paramètre de la méthode [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/JsonSaveOptions) pour spécifier des paramètres supplémentaires pour exporter la feuille de calcul au format JSON.

L'exemple de code suivant montre comment exporter un classeur Excel en Json. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en le fichier Json généré par le code à titre de référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON.py" >}}

L'exemple de code suivant qui utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires démontre l'exportation du classeur Excel en Json. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-JSON2.py" >}}
