---
title: Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto
type: docs
weight: 100
url: /es/java/save-workbook-to-strict-open-xml-spreadsheet-format/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite guardar el libro de trabajo en formato de hoja de cálculo de Open XML estricto. Para este propósito, proporciona la propiedad [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance). Si estableces su valor como [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT), entonces el archivo Excel de salida se guardará en formato de hoja de cálculo de Open XML estricto.

## **Guardar libro de trabajo en formato de hoja de cálculo de Open XML estricto**

El siguiente código de ejemplo crea un libro de trabajo y establece el valor de la propiedad [**Workbook.Settings.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Compliance) como [**OoxmlCompliance.ISO_29500_2008_STRICT**](https://reference.aspose.com/cells/java/com.aspose.cells/ooxmlcompliance#ISO-29500-2008-STRICT) y lo guarda como [archivo de Excel de salida](outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx). Si abres el archivo de Excel de salida en Microsoft Excel y abres el cuadro de diálogo *Guardar como...*, verás su formato como *Hojas de cálculo de Open XML estricto* como se muestra en esta captura de pantalla.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "LoadingSavingConvertingAndManaging-SaveWorkbookToStrictOpenXMLSpreadsheetFormat.java" >}}
{{< app/cells/assistant language="java" >}}
