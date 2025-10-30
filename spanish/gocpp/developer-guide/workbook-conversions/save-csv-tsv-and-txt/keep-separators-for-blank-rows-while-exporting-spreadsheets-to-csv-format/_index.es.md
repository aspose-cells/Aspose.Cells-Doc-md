---
title: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV con Golang mediante C++
linktitle: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 160
url: /es/go-cpp/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Aprende cómo mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV usando Aspose.Cells con Golang mediante C++.
---

## **Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV**

Aspose.Cells proporciona la capacidad de mantener separadores de línea al convertir hojas de cálculo a formato CSV. Para ello, puede usar la propiedad [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) de la clase [**TxtSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/txtsaveoptions/). [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) es una propiedad booleana. Para mantener los separadores en líneas vacías al convertir el archivo Excel a CSV, configure la propiedad [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) a **true**.

El siguiente código de ejemplo carga el [archivo de Excel de origen](84378743.xlsx). Establece la propiedad [**TxtSaveOptions.GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) a **true** y lo guarda como [output.csv](84378744.csv). La captura de pantalla muestra la comparación entre el archivo Excel de origen, la salida predeterminada generada al convertir la hoja de cálculo a CSV y la salida generada al establecer [**GetKeepSeparatorsForBlankRow()**](https://reference.aspose.com/cells/go-cpp/txtsaveoptions/getkeepseparatorsforblankrow/) en **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-KeepSeparatorsForBlankRowsWhileExportingSpreadsheetsToCsvFormat.go" >}}
