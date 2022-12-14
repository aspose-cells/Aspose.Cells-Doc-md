---
title: Obtenir le numéro de version de l'application qui a créé le document Excel
type: docs
weight: 150
url: /fr/java/get-the-version-number-of-the-application-that-created-the-excel-document/
---
{{% alert color="primary" %}}

 Souvent, vous devez connaître le numéro de version de l'application qui a créé un document Excel Microsoft. Aspose.Cells fournit le[**Classeur.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version) propriété à cet effet.

{{% /alert %}}

 L'exemple de code suivant illustre l'utilisation du[**Classeur.getBuiltInDocumentProperties().getVersion()**](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#Version)propriété. Il charge les fichiers Excel créés avec Microsoft Excel 2003, 2007, 2010 et 2013 et imprime le numéro de version de l'application qui a créé ces documents Excel.

Pour votre référence, vous trouverez ci-dessous la sortie de la console créée par l'exemple de code.

{{< highlight "java" >}}

Excel 2003 XLS Version: 726502

Excel 2007 XLS Version: 786432

Excel 2010 XLS Version: 917504

Excel 2013 XLS Version: 983040

Excel 2007 XLSX Version: 12.0000

Excel 2010 XLSX Version: 14.0300

Excel 2013 XLSX Version: 15.0300

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetVersionNumberofApplication-GetVersionNumberofApplication.java" >}}
