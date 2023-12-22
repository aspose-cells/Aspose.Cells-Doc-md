---
title: Convertir Excel en JSON
type: docs
weight: 20
url: /fr/java/convert-excel-to-json/
description: Découvrez comment convertir un fichier Excel en json avec les API Aspose.Cells for Java.
keywords: Java Export Workbook to json, Convert Excel to JSON using Java, Save Excel to JSON in Java, Convert Workbook to JSON using Java, Save Workbook to JSON in Java, Export Excel to JSON via Java.
---
{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json (JavaScript Object Notation).

{{% /alert %}}

##  **Comment convertir un classeur Excel en JSON**

 Pas besoin de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells Java a la meilleure décision. Le Aspose.Cells Java API prend en charge la conversion de feuilles de calcul au format JSON. Pour exporter le classeur vers JSON, passez[**EnregistrerFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) comme deuxième paramètre de[**Classeur.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) méthode. Vous pouvez également utiliser[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) classe pour spécifier des paramètres supplémentaires pour l’exportation de la feuille de calcul vers JSON.

 L'exemple de code suivant montre l'exportation d'un classeur Excel vers Json. Veuillez consulter le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 L'exemple de code suivant qui utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires illustre l'exportation d'un classeur Excel vers Json. Veuillez consulter le code pour convertir[fichier source](sample.xlsx) au fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
