---
title: Convertir Excel a Word
type: docs
weight: 300
url: /es/python-java/convert-excel-to-word/
description: Convertir archivo de Excel a Word usando Python
keywords: Exportar libro de trabajo a Word sin Office 2013, Office 2016, Office 2019 y Office 365
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java admite la conversión de archivos de Excel (.xls, xlsx, .xlsb, .xlsm), CSV y OpenOffice (.ods) a archivos de Word.

{{% /alert %}}

## **Convertir libro de trabajo de Excel a Word**

No es necesario preguntarse cómo convertir un libro de trabajo de Excel a Word, porque la biblioteca Aspose.Cells for Python via Java tiene la mejor solución. La API de Aspose.Cells for Python via Java proporciona soporte para convertir hojas de cálculo al formato de Word. Para exportar el libro de trabajo a Word, pasa [**SaveFormat.DOCX**](https://reference.aspose.com/cells/python-java/asposecells.api/saveformat) como segundo parámetro del método [**Workbook.save**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#save\(java.lang.String,%20int\)). También puedes usar la clase [**DocxSaveOptions**](https://reference.aspose.com/cells/python-java/asposecells.api/DocxSaveOptions) para especificar ajustes adicionales para exportar la hoja de cálculo a un archivo .docx.

El siguiente ejemplo de código demuestra cómo exportar un libro de Excel a Word. Por favor, consulte el código para convertir [archivo fuente](sample.xlsx) al archivo de Word generado por el código para referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Convert-Excel-to-Word.py" >}}


