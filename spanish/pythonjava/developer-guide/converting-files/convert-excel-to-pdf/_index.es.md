---
title: Convertir Excel a PDF
type: docs
weight: 50
url: /es/python-java/convert-excel-to-pdf/
description: Cómo convertir Excel a PDF con Python. Este artículo demuestra cómo convertir archivos de Excel a PDF usando Python y fácil de usar Aspose.Cells para Python a través de Java API.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---
## **Convertir Excel a PDF**

Los documentos PDF se utilizan ampliamente como formato estándar para el intercambio de documentos entre organizaciones, sectores gubernamentales e individuos. A los desarrolladores de software a menudo se les pide que ideen una forma de convertir fácilmente Microsoft archivos de Excel en documentos PDF. Aspose.Cells para Python a través de Java API brinda la capacidad de convertir archivos de Excel a documentos PDF (incluido PDF/A). Aspose.Cell convierte hojas de cálculo a PDF con un alto grado de precisión y fidelidad.

### **Conversión Directa**

Para guardar un archivo de Excel directamente en PDF, puede usar el[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)método y pasar[**GuardarFormato.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) como segundo parámetro.

El siguiente fragmento de código demuestra el uso de[**GuardarFormato.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF)y el[**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) método para convertir Excel a formato PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversión avanzada**

Para tener más control sobre la conversión a PDF, el API proporciona la[**PdfGuardarOpciones**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)clase. los[**PdfGuardarOpciones**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)La clase se puede utilizar para establecer diferentes atributos para la conversión. Configuración de diferentes propiedades del[**PdfGuardarOpciones**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions)class le dará control sobre las configuraciones de Impresión, Fuente, Seguridad y Compresión para el archivo PDF resultante. La propiedad más notable es la[**Cumplimiento**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance)que le permite guardar los archivos de Excel en archivos PDF compatibles con PDF/A.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

 si su hoja de cálculo contiene fórmulas, llame al[**Workbook.calculateFormula**](https://reference.aspose.com/cells/python/asposecells.api/workbook#calculateFormula()) justo antes de convertir la hoja de cálculo en PDF. Esto garantiza que los valores dependientes de la fórmula se vuelvan a calcular y que los valores correctos se representen en el PDF.

{{% /alert %}}
