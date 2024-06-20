---
title: Convertir Excel a CSV, TSV y Txt
linktitle: Guardar como CSV, TSV y Txt
type: docs
weight: 40
url: /es/net/convert-excel-to-csv-tsv-and-txt/
---

{{% alert color="primary" %}}

Aspose.Cells hace posible convertir archivos de Excel, ods, json y otros formatos a CSV, TSV y TXT.

{{% /alert %}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, deseas convertir o guardar un libro con múltiples hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada, [**TxtSaveOptions.Separator**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator) es la coma, por lo que no especifique un separador al guardar en formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Temas avanzados**
- [Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV](/cells/es/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
