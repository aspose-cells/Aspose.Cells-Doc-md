---
title: Especificar campos de fórmula al importar datos a la hoja de trabajo
type: docs
weight: 300
url: /es/net/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Posibles escenarios de uso**

Puede especificar campos de fórmula cuando importa datos a su hoja de trabajo usando el[**ImportTableOptions.IsFormulas**](https://reference.aspose.com/cells/net/aspose.cells/importtableoptions/properties/isformulas) . Esta propiedad toma la matriz booleana donde el valor**verdadero**significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en la matriz será**verdadero**.

## **Especificar campos de fórmula al importar datos a la hoja de trabajo**

 Consulte el siguiente código de ejemplo que explica cómo especificar el campo de fórmula al importar datos a una hoja de trabajo. Por favor vea el[archivo de salida de Excel](61767838.xlsx)generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.cs" >}}
