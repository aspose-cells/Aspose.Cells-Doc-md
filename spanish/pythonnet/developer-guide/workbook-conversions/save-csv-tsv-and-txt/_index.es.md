---
title: Convertir Excel a CSV,TSV y Txt
linktitle: Guardar como CSV,TSV y Txt
type: docs
weight: 40
url: /es/python-net/convert-excel-to-csv-tsv-and-txt/
description: Convierta Excel a CSV,TSV y Txt usando Aspose.Cells for Python via .NET API.
keywords: Python Convert Excel to CSV,TSV and Txt, Convert Excel to CSV,TSV and Txt in Python via NET, Python Convert Workbook to CSV,TSV and Txt.
---
{{% alert color="primary" %}}

Aspose.Cells for Python via .NET permite convertir archivos excel, ods, json y otros formatos a CSV, TSV y TXT.

{{% /alert %}}

##  **Guardar libro de trabajo en formato texto o CSV**

veces, desea convertir o guardar un libro con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells for Python via .NET guardan el contenido de la hoja de trabajo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (es decir, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier cantidad de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro al formato TXT.

 Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada,**[TxtSaveOptions.separator](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/separator/)**es una coma, así que no especifique un separador si guarda en formato CSV.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SaveWorkbookToTextCSVFormat-1.py" >}}

##  **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-SavingTextFilewithCustomSeparator-1.py" >}}


##  **Temas avanzados**
- [Mantenga separadores para filas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV](/cells/es/python-net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
