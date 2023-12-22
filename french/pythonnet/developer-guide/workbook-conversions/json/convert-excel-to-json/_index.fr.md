---
title: Convertir Excel en JSON
type: docs
weight: 300
url: /fr/python-net/convert-excel-to-json/
description: Apprenez à convertir un fichier Excel en json avec Aspose.Cells for Python via .NET API.
keywords: Python Convert excel to json, Convert excel to json Pyton via NET, Export Workbook to json, Convert excel file to json
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

{{% /alert %}}

##  **Convertir un classeur Excel en JSON**

Pas besoin de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells for Python via .NET a la meilleure décision. Le Aspose.Cells API prend en charge la conversion des feuilles de calcul au format JSON. Pour exporter le classeur vers JSON, passez[**EnregistrerFormat.JSON**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat) comme deuxième paramètre de[**Classeur.save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveOptions) méthode. Vous pouvez également utiliser[**JsonSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/JsonSaveoptions) classe pour spécifier des paramètres supplémentaires pour l’exportation de la feuille de calcul vers JSON.

 L'exemple de code suivant montre l'exportation d'un classeur Excel vers Json. Veuillez consulter le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New.py" >}}

 L'exemple de code suivant qui utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires illustre l'exportation d'un classeur Excel vers Json. Veuillez consulter le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Excel-to-JSON-New2.py" >}}

