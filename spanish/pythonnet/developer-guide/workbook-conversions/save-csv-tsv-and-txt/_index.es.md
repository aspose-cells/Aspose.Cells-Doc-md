---
title: Convertir Excel a CSV, TSV y Txt
linktitle: Guardar como CSV, TSV y Txt
type: docs
weight: 40
url: /es/python-net/convert-excel-to-csv-tsv-and-txt/
description: Convertir Excel a CSV, TSV y Txt utilizando la API de Aspose.Cells for Python via .NET.
keywords: Python Convertir Excel a CSV, TSV y TXT, Convertir Excel a CSV, TSV y TXT en Python via NET, Convertir libro a CSV, TSV y TXT en Python.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET hace posible convertir archivos de formato excel, ods, json y otros a CSV, TSV y TXT.

{{% /alert %}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada tanto Microsoft Excel como Aspose.Cells for Python via .NET guardan solo el contenido de la hoja de trabajo activa.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada, [**TxtSaveOptions.separator**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/) es la coma, por lo que no especifique un separador al guardar en formato CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


## **Temas avanzados**
- [Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV](/cells/es/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
