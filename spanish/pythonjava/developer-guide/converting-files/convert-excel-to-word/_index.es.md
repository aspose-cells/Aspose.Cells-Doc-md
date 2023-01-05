---
title: Convertir Excel a Word
type: docs
weight: 300
url: /es/python-java/convert-excel-to-word/
description: Convierta un archivo de Excel a Word usando Python.
keywords: Exporting Workbook to word without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells for Python via Java admite la conversión de archivos de Excel (.xls, xlsx, .xlsb,xlsm), CSV y OpenOffice (.ods) a archivos de Word.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a Word**

 No hay necesidad de preguntarse cómo convertir Excel Workbook a Word, porque la biblioteca Aspose.Cells for Python via Java tiene la mejor decisión. El Aspose.Cells for Python via Java API brinda soporte para convertir hojas de cálculo a formato Word. Para exportar el libro de trabajo a Word, pase[**GuardarFormato.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) como segundo parámetro de[**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\) ) método. También puede usar[**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions)class para especificar configuraciones adicionales para exportar la hoja de trabajo a un archivo .docx.

 El siguiente ejemplo de código muestra cómo exportar un libro de Excel a Word. Por favor vea el código para convertir[archivo fuente](sample.xlsx) al archivo de Word generado por el código como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


