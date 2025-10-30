---
title: Guardar Cada Hoja de Cálculo en un Archivo PDF Diferente
type: docs
weight: 130
url: /es/python-net/save-each-worksheet-to-a-different-pdf-file/
description: Aprende cómo Guardar Cada Hoja de Trabajo en un Archivo PDF Diferente con la API de Aspose.Cells para Python via .NET.
keywords: Python Guardar Cada Hoja de Trabajo en un Archivo PDF Diferente
---

{{% alert color="primary" %}} 

Aspose.Cells para Python via .NET admite la conversión de archivos XLS (que contienen imágenes, gráficos, etc.) a documentos PDF. Aspose.Cells para Python via .NET puede trabajar de forma independiente para convertir una hoja de cálculo a PDF y no es necesario usar Aspose.PDF para .NET para la conversión. La conversión no requiere que el software cree o use archivos temporales, ya que todo el proceso puede hacerse en memoria.

{{% /alert %}} 
## **Guardar cada hoja de cálculo en un archivo PDF diferente**
Si necesita guardar cada hoja de cálculo en su archivo de plantilla de Excel para generar archivos PDF diferentes, puede lograrlo fácilmente. Puede intentar configurar un índice de hoja a la vez con la opción [**PdfSaveOptions.sheet_set**](https://reference.aspose.com/cells/python-net/aspose.cells/paginatedsaveoptions/sheet_set/) para renderizar a PDF.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SaveEachWorksheetToDifferentPDF-1.py" >}}

{{% alert color="primary" %}} 

Si su hoja de cálculo contiene fórmulas, es mejor llamar a [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) justo antes de renderizar la hoja de cálculo en formato PDF. Al hacerlo, se asegurará de que los valores dependientes de las fórmulas se recalculen y los valores correctos se muestren en el PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
