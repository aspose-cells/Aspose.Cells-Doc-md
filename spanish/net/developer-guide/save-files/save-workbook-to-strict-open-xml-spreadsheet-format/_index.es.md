---
title: Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto
type: docs
weight: 150
url: /es/net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite guardar el libro de trabajo en formato de hoja de cálculo Open XML estricto. Para ese propósito, proporciona la propiedad [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance). Si estableces su valor como [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance), entonces el archivo de Excel de salida se guardará en formato estricto de hoja de cálculo Open XML.

## **Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto**

El siguiente código de ejemplo crea un libro de trabajo y establece el valor de la propiedad [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/compliance) como [**OoxmlCompliance.Iso29500_2008_Strict**](https://reference.aspose.com/cells/net/aspose.cells/ooxmlcompliance) y lo guarda como [archivo de Excel de salida](67338272.xlsx). Si abres el archivo de Excel de salida en Microsoft Excel y abres el cuadro de diálogo Guardar como..., verás que su formato es de hoja de cálculo Open XML estricto como se muestra en esta captura de pantalla.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.cs" >}}
