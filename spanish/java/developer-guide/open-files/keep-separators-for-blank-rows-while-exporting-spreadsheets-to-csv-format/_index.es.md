---
title: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 110
url: /es/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV**

Aspose.Cells proporciona la capacidad de mantener los separadores de línea al convertir hojas de cálculo a formato CSV. Para esto, puede usar la propiedad [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) de la clase [**TxtSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) es una propiedad booleana. Para mantener los separadores para líneas en blanco al convertir el archivo de Excel a CSV, configure la propiedad [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) en **true**.

El siguiente código de muestra carga el [archivo de Excel de origen](KeepSeparatorsForBlankRow.xlsx). Configura la propiedad [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) a **true** y lo guarda como [KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). La captura de pantalla muestra la comparación entre el archivo de Excel de origen, la salida predeterminada generada al convertir la hoja de cálculo a CSV y la salida generada configurando [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow) a **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
{{< app/cells/assistant language="java" >}}
