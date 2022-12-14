---
title: Mantenga separadores para filas en blanco mientras exporta hojas de cálculo a formato CSV
type: docs
weight: 110
url: /es/java/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---
## **Mantenga separadores para filas en blanco mientras exporta hojas de cálculo a formato CSV**

Aspose.Cells brinda la capacidad de mantener los separadores de línea al convertir hojas de cálculo al formato CSV. Para ello, puede utilizar el**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**propiedad de**[TxtSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/TxtSaveOptions)**clase.**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**es una propiedad booleana. Para mantener los separadores para las líneas en blanco al convertir el archivo de Excel a CSV, configure el**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**propiedad a**verdadero**.

El siguiente código de ejemplo carga el[archivo fuente de Excel](KeepSeparatorsForBlankRow.xlsx). se pone**[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**propiedad a**verdadero** y lo guarda como[KeepSeparatorsForBlankRow.out.csv](KeepSeparatorsForBlankRow.out.csv). La captura de pantalla muestra la comparación entre el archivo Excel de origen, la salida predeterminada generada al convertir la hoja de cálculo a CSV y la salida generada al configurar**[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/java/com.aspose.cells/txtsaveoptions#KeepSeparatorsForBlankRow)**a**verdadero**.

![todo:imagen_alternativa_texto](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-KeepSeparatorsForBlankRow-1.java" >}}
