---
title: Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo
type: docs
weight: 300
url: /es/net/specify-formula-fields-while-importing-data-to-worksheet/
description: Aprende cómo especificar campos de fórmula al importar datos a la hoja de cálculo a través de la API Aspose.Cells for .NET.
keywords: Especificar campos de fórmula al importar datos a la hoja de cálculo, establecer campos de fórmula al agregar datos a la hoja de cálculo
---

## **Escenarios de uso posibles**

Puedes especificar campos de fórmula al importar datos en tu hoja de cálculo usando el [**ImportTableOptions.IsFormulas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/isformulas). Esta propiedad toma un array de booleanos donde el valor **true** significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en el array será **true**.

## **Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo**

Consulta el siguiente código de ejemplo que explica cómo especificar el campo de fórmula al importar datos a una hoja de cálculo. Consulta el [archivo de Excel de salida](61767838.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
