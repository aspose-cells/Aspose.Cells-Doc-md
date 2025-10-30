---
title: Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto
type: docs
weight: 150
url: /es/python-net/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET permite guardar el libro en formato *Strict Open XML Spreadsheet*. Para ello, proporciona la propiedad [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance). Si estableces su valor como [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance), el archivo de Excel de salida se guardará en formato Strict Open XML Spreadsheet.

## **Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto**

El siguiente código de ejemplo crea un libro de trabajo y establece el valor de la propiedad [**Workbook.settings.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/compliance) como [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/python-net/aspose.cells/ooxmlcompliance) y lo guarda como [archivo de Excel de salida](67338272.xlsx). Si abres el archivo de Excel de salida en Microsoft Excel y abres el cuadro de diálogo Guardar como..., verás que su formato es de hoja de cálculo Open XML estricto como se muestra en esta captura de pantalla.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Save-files-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.py" >}}

{{< app/cells/assistant language="python-net" >}}
