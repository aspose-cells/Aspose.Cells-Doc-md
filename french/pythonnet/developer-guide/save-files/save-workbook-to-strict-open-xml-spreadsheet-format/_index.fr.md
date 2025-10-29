---
title: Enregistrer le classeur au format de feuille de calcul strict Open XML
type: docs
weight: 150
url: /fr/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells pour Python via .NET vous permet d’enregistrer le classeur au format *Strict Open XML Spreadsheet*. À cette fin, il propose la propriété [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Si vous définissez sa valeur sur [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance), alors le fichier Excel de sortie sera enregistré au format Strict Open XML Spreadsheet.

## **Enregistrer le classeur au format strict Open XML Spreadsheet**

Le code d'exemple suivant crée un classeur et définit la valeur de la propriété [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) comme [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) et l'enregistre sous la forme de [fichier Excel de sortie](67338272.xlsx). Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue Enregistrer sous..., vous verrez son format comme *Strict Open XML Spreadsheet* comme indiqué dans cette capture d'écran.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}
