---
title: Enregistrer le classeur au format de feuille de calcul strict Open XML
type: docs
weight: 100
url: /fr/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'enregistrer le classeur au format *Strict Open XML Spreadsheet*. À cet effet, il fournit la propriété [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance). Si vous définissez sa valeur comme [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT), alors le fichier Excel de sortie sera enregistré au format *Strict Open XML Spreadsheet*.

## **Enregistrer le classeur au format strict Open XML Spreadsheet**

Le code d'exemple suivant crée un classeur et définit la valeur de la propriété [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance) comme [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT) et l'enregistre en tant que [fichier Excel de sortie](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue *Enregistrer sous...*, vous verrez son format comme *Strict Open XML Spreadsheet* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
{{< app/cells/assistant language="java" >}}
