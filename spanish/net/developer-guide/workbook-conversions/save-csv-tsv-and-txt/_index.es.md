---
title: Convierta Excel a CSV,TSV y Txt
linktitle: Guardar como CSV,TSV y Txt
type: docs
weight: 40
url: /es/net/convert-excel-to-csv-tsv-and-txt/
---
{{% alert color="primary" %}}

Aspose.Cells permite convertir excel, ods, json y otros archivos de formato a CSV, TSV y TXT.

{{% /alert %}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, desea convertir o guardar un libro de trabajo con varias hojas de trabajo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), de forma predeterminada, tanto Microsoft Excel como Aspose.Cells guardan solo el contenido de la hoja de trabajo activa.

El siguiente ejemplo de código explica cómo guardar un libro completo en formato de texto. Cargue el libro de origen, que podría ser cualquier archivo de hoja de cálculo de Excel u OpenOffice Microsoft (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puede modificar el mismo ejemplo para guardar su archivo en CSV. De forma predeterminada,**[TxtSaveOptions.Separator](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/separator)**es una coma, así que no especifique un separador si guarda en formato CSV.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveWorkbookToTextCSVFormat-1.cs" >}}

## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de hojas de cálculo sin formato. El archivo es una especie de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingTextFilewithCustomSeparator-1.cs" >}}


## **Temas avanzados**
- [Mantenga separadores para filas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recorte las filas y columnas en blanco iniciales al exportar hojas de cálculo al formato CSV](/cells/es/net/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
