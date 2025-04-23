---
title: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 160
url: /es/net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV**

Aspose.Cells proporciona la capacidad de mantener los separadores de línea al convertir hojas de cálculo a formato CSV. Para esto, puede usar la propiedad [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) de la clase [**TxtSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions). [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) es una propiedad booleana. Para mantener los separadores para líneas en blanco al convertir el archivo de Excel a CSV, configure la propiedad [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) en **true**.

El siguiente código de ejemplo carga el [archivo de Excel de origen](84378743.xlsx). Establece la propiedad [**TxtSaveOptions.KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) en **true** y lo guarda como [output.csv](84378744.csv). La captura de pantalla muestra la comparación entre el archivo de Excel de origen, el resultado de salida predeterminado generado al convertir la hoja de cálculo a CSV y el resultado generado configurando [**KeepSeparatorsForBlankRow**](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow) en **true**

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
