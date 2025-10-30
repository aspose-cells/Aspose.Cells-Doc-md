---
title: Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV
type: docs
weight: 160
url: /es/python-net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
description: Mantener Separadores para Filas en Blanco al exportar hojas de cálculo al formato CSV utilizando Aspose.Cells para Python via .NET API.
keywords: Python Maintener Separadores para Filas en Blanco al exportar hojas de cálculo al formato CSV, Mantener Separadores para Filas en Blanco al guardar excel al formato CSV en Python via NET, Python Mantener Separadores para Filas en Blanco al exportar excel al formato CSV.
---

## **Mantener separadores para filas en blanco al exportar hojas de cálculo a formato CSV**

Aspose.Cells para Python via .NET proporciona la capacidad de mantener separadores de línea al convertir hojas de cálculo al formato CSV. Para esto, puede usar la propiedad [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) de la clase [**TxtSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/). [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) es una propiedad booleana. Para mantener los separadores para líneas en blanco al convertir el archivo de Excel a CSV, ajuste la propiedad [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) a **true**.

El siguiente código de ejemplo carga el [archivo de Excel de origen](84378743.xlsx). Establece la propiedad [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) en **true** y lo guarda como [output.csv](84378744.csv). La captura de pantalla muestra la comparación entre el archivo de Excel de origen, el resultado de salida predeterminado generado al convertir la hoja de cálculo a CSV y el resultado generado configurando [**keep_separators_for_blank_row**](https://reference.aspose.com/cells/python-net/aspose.cells/txtsaveoptions/keep_separators_for_blank_row/) en **true**

![todo:image_alt_text](result.jpg)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "CSV-TSV-TXT-KeepSeparatorsForBlankRow-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
