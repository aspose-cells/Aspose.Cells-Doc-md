---
title: Enregistrer le classeur au format de feuille de calcul XML ouvert strict avec Golang via C++
linktitle: Enregistrer le classeur au format de feuille de calcul strict Open XML
type: docs
weight: 150
url: /fr/go-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: Apprenez comment enregistrer un classeur au format XML strict en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells permet d'enregistrer le classeur au format *Strict Open XML Spreadsheet*. À cette fin, il fournit la propriété [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/). Si vous définissez sa valeur à [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), le fichier Excel de sortie sera enregistré au format Strict Open XML Spreadsheet.

## **Enregistrer le classeur au format strict Open XML Spreadsheet**

Le code d'exemple suivant crée un classeur et définit la valeur de la propriété [**GetCompliance()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getcompliance/) à [**OoxmlCompliance::Iso29500_2008_Strict**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompliance/), puis l'enregistre en tant que [fichier Excel de sortie](67338272.xlsx). Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue Enregistrer sous..., vous verrez son format comme *Strict Open XML Spreadsheet* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookToStrictOpenXmlSpreadsheetFormat.go" >}}
