---
title: Convertir Excel en JSON
type: docs
weight: 20
url: /fr/java/convert-excel-to-json/
description: Apprenez comment convertir un fichier Excel en JSON avec Aspose.Cells for Java API.
keywords: Exporter un classeur Java vers JSON, Convertir Excel en JSON avec Java, Enregistrer Excel en JSON en Java, Convertir un classeur en JSON en utilisant Java, Enregistrer un classeur en JSON en Java, Exporter Excel en JSON via Java.
---

{{% alert color="primary" %}}

Aspose.Cells prend en charge la conversion d'un classeur en fichier Json(JavaScript Object Notation).

{{% /alert %}}

## **Comment Convertir un Classeur Excel en JSON**

Pas besoin de se demander comment convertir un classeur Excel en JSON, car la bibliothèque Aspose.Cells Java propose la meilleure solution. L'API Java Aspose.Cells prend en charge la conversion des feuilles de calcul au format JSON. Pour exporter le classeur au format JSON, passez [**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) en tant que deuxième paramètre de la méthode [**Workbook.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int)). Vous pouvez également utiliser la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) pour spécifier des paramètres supplémentaires pour l'exportation de la feuille de calcul au format JSON.

L'exemple de code suivant montre comment exporter un classeur Excel en Json. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en le fichier Json généré par le code à titre de référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

L'exemple de code suivant qui utilise la classe JsonSaveOptions pour spécifier des paramètres supplémentaires démontre l'exportation du classeur Excel en Json. Veuillez consulter le code pour convertir le [fichier source](sample.xlsx) en fichier Json généré par le code pour référence.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
