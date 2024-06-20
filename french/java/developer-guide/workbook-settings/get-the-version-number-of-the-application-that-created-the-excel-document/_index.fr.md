---
title: Obtenir le numéro de version de l application qui a créé le document Excel
type: docs
weight: 150
url: /fr/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Souvent, vous avez besoin de connaître le numéro de version de l'application qui a créé un document Microsoft Excel. Aspose.Cells fournit la propriété [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) à cette fin.

{{% /alert %}}

Le code d'exemple suivant montre l'utilisation de la propriété [**Workbook.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version). Il charge les fichiers Excel créés avec Microsoft Excel 2003, 2007, 2010 et 2013 et affiche le numéro de version de l'application qui a créé ces documents Excel.

Pour votre référence, voici la sortie de la console que le code d'exemple crée.

{{< highlight java >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
