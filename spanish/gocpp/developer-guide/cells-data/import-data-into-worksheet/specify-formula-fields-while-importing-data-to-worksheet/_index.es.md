---
title: Especificar campos de fórmulas al importar datos a una hoja de cálculo con Golang a través de C++
linktitle: Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo
type: docs
weight: 300
url: /es/go-cpp/specify-formula-fields-while-importing-data-to-worksheet/
description: Aprende cómo especificar Campos de Fórmula al importar datos a la hoja mediante la API Aspose.Cells for C++.
keywords: Especificar campos de fórmula al importar datos a la hoja de cálculo, establecer campos de fórmula al agregar datos a la hoja de cálculo
---

## **Escenarios de uso posibles**

Puedes especificar campos de fórmula al importar datos en tu hoja de cálculo usando el [**ImportTableOptions.GetIsFormulas()**](https://reference.aspose.com/cells/go-cpp/importtableoptions/getisformulas/). Esta propiedad toma un array de booleanos donde el valor **true** significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en el array será **true**.

## **Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo**

Consulta el siguiente código de ejemplo que explica cómo especificar el campo de fórmula al importar datos a una hoja de cálculo. Consulta el [archivo de Excel de salida](61767838.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyFormulaFieldsWhileImportingDataToWorksheet.go" >}}
