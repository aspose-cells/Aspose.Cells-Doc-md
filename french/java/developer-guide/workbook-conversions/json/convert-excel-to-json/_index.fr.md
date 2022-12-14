---
title: Convertir Excel en JSON
type: docs
weight: 20
url: /fr/java/convert-excel-to-json/
description: Apprenez à convertir un fichier excel en json avec Aspose.Cells.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

{{% /alert %}}

## **Convertir un classeur Excel en JSON**

 Pas besoin de se demander comment convertir Excel Workbook en JSON, car la bibliothèque Aspose.Cells Java a la meilleure décision. Le Aspose.Cells Java API prend en charge la conversion des feuilles de calcul au format JSON. Pour exporter le classeur vers JSON, passez[**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) comme deuxième paramètre de[**Classeur.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) méthode. Vous pouvez également utiliser[**JsonSaveOptionsJsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) class pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul vers JSON.

 L'exemple de code suivant illustre l'exportation du classeur Excel vers Json. S'il vous plaît voir le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 L'exemple de code suivant qui utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires illustre l'exportation du classeur Excel vers Json. S'il vous plaît voir le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
