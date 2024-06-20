---
title: Convertir Excel a PDF
type: docs
weight: 50
url: /es/python-java/convert-excel-to-pdf/
description: Cómo convertir Excel a PDF con Python. Este artículo demuestra cómo convertir archivos Excel a PDF utilizando Python y la API fácil de usar Aspose.Cells para Python via Java.
keywords: excel to pdf python, python convert excel to pdf, python excel to pdf, convert excel to pdf python, convert excel to pdf in python, convert excel to pdf using python, excel to pdf in python, excel to pdf using python, aspose excel to pdf, aspose convert excel to pdf
---

## **Convertir Excel a PDF**

Los documentos PDF son ampliamente utilizados como formato estándar para intercambiar documentos entre organizaciones, sectores gubernamentales e individuos. Los desarrolladores de software a menudo se les pide idear una forma de convertir fácilmente archivos de Microsoft Excel a documentos PDF. La API de Aspose.Cells para Python via Java proporciona la capacidad de convertir archivos Excel a documentos PDF (incluyendo PDF/A). Aspose.Cells convierte hojas de cálculo a PDF con un alto grado de precisión y fidelidad.

### **Conversión Directa**

Para guardar un archivo Excel directamente a PDF, puede utilizar el método [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) y pasar [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) como segundo parámetro.

El siguiente fragmento de código demuestra el uso de [**SaveFormat.PDF**](https://reference.aspose.com/cells/python/asposecells.api/saveformat#PDF) y el método [**Workbook.save**](https://reference.aspose.com/cells/python/asposecells.api/workbook#save(java.lang.String,%20com.aspose.cells.SaveOptions)) para convertir Excel al formato PDF.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-ConvertingToPDFFiles.py" >}}

### **Conversión Avanzada**

Para tener más control sobre la conversión a PDF, la API proporciona la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions). La clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) se puede utilizar para configurar diferentes atributos para la conversión. Establecer diferentes propiedades de la clase [**PdfSaveOptions**](https://reference.aspose.com/cells/python/asposecells.api/PdfSaveOptions) te dará control sobre la configuración de Impresión, Fuente, Seguridad y Compresión para el archivo PDF resultante. La propiedad más notable es [**Compliance**](https://reference.aspose.com/cells/python/asposecells.api/pdfsaveoptions#Compliance), que te permite guardar los archivos de Excel como archivos PDF/A compatibles.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "LoadingSavingConvertingAndManaging-AdvancedConversiontoPdf.py" >}}

{{% alert color="primary" %}}

Si tu hoja de cálculo contiene fórmulas, llama al método [**Workbook.calculateFormula**](https://reference.aspose.com/cells/python-java/asposecells.api/workbook#calculateFormula()) justo antes de renderizar la hoja de cálculo a PDF. Esto asegura que los valores dependientes de la fórmula se recalculen y se representen los valores correctos en el PDF.

{{% /alert %}}
