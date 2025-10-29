---
title: Obtenir le numéro de version de l application qui a créé le document Excel
type: docs
weight: 210
url: /fr/python-net/get-the-version-number-of-the-application-that-created-the-excel-document/
---

{{% alert color="primary" %}}

Souvent, vous avez besoin de connaître le numéro de version de l'application qui a créé un document Microsoft Excel. Aspose.Cells pour Python via .NET fournit la propriété [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version) à cet effet.

{{% /alert %}}

Le code d'exemple suivant montre l'utilisation de la propriété [**Workbook.built_in_document_properties.version**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/version). Il charge les fichiers Excel créés avec Microsoft Excel 2003, 2007, 2010 et 2013 et affiche le numéro de version de l'application qui a créé ces documents Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-GetApplicationVersion-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
