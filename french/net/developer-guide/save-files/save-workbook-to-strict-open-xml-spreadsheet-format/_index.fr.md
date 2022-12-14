---
title: Enregistrer le classeur au format de feuille de calcul Open XML strict
type: docs
weight: 150
url: /fr/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells vous permet d'enregistrer le classeur dans*Feuille de calcul Open XML stricte*format. A cet effet, il fournit la**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)**propriété. Si vous définissez sa valeur comme**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)**, le fichier Excel de sortie sera enregistré au format Strict Open XML Spreadsheet.

## **Enregistrer le classeur au format de feuille de calcul Open XML strict**

L'exemple de code suivant crée un classeur et définit la valeur de**[Workbook.Settings.Compliance](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance)** propriété comme**[OoxmlCompliance.Iso29500_2008_Strict](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance)** et l'enregistre sous[fichier Excel de sortie](67338272.xlsx) . Si vous ouvrez le fichier Excel de sortie dans Microsoft Excel et ouvrez la boîte de dialogue Enregistrer sous..., vous verrez son format comme*Feuille de calcul Open XML stricte*comme le montre cette capture d'écran.

![tâche : image_autre_texte](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
