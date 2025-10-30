---
title: Convertir Excel a CSV, TSV y Txt con Golang a través de C++
linktitle: Guardar como CSV, TSV y Txt
type: docs
weight: 40
url: /es/go-cpp/convert-excel-to-csv-tsv-and-txt/
description: Convierte fácilmente archivos de Excel a formatos CSV, TSV y TXT usando Aspose.Cells con Golang a través de C++.
---

{{% alert color="primary" %}}

Aspose.Cells hace posible convertir archivos de Excel, ODS, JSON y otros formatos a CSV, TSV y TXT.

{{% /alert %}}

## **Guardar libro de trabajo en formato de texto o CSV**

A veces, deseas convertir o guardar un libro con múltiples hojas de cálculo en formato de texto. Para formatos de texto (por ejemplo, TXT, TabDelim, CSV, etc.), tanto Microsoft Excel como Aspose.Cells guardan por defecto el contenido de la hoja de cálculo activa únicamente.

El siguiente ejemplo de código explica cómo guardar un libro de trabajo completo en formato de texto. Cargue el libro de trabajo fuente que podría ser cualquier archivo de hoja de cálculo de Microsoft Excel u OpenOffice (por ejemplo, XLS, XLSX, XLSM, XLSB, ODS, etc.) con cualquier número de hojas de trabajo.

Cuando se ejecuta el código, convierte los datos de todas las hojas del libro de trabajo al formato TXT.

Puedes modificar el mismo ejemplo para guardar tu archivo en CSV. Por defecto, [**TxtSaveOptions.GetSeparator()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getseparator/) es una coma, así que no especifiques un separador al guardar en formato CSV.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt.go" >}}
## **Guardar archivos de texto con separador personalizado**

Los archivos de texto contienen datos de la hoja de cálculo sin formato. El archivo es un tipo de archivo de texto sin formato que puede tener algunos delimitadores personalizados entre sus datos.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveCsvTsvAndTxt-1.go" >}}
## **Temas avanzados**
- [Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV](/cells/es/cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/)
- [Recortar filas y columnas en blanco al exportar hojas de cálculo al formato CSV](/cells/es/cpp/trim-leading-blank-rows-and-columns-while-exporting-spreadsheets-to-csv-format/)
