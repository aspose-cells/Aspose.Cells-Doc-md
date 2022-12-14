---
title: Especificar campos de fórmula al importar datos a la hoja de trabajo
type: docs
weight: 220
url: /es/java/specify-formula-fields-while-importing-data-to-worksheet/
---
## **Posibles escenarios de uso**

 Puede especificar campos de fórmula cuando importa datos a su hoja de trabajo usando el[**ImportTableOptions.setFórmulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas) método. Este método toma la matriz booleana donde el valor**verdadero**significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en la matriz será**verdadero**.

## **Especificar campos de fórmula al importar datos a la hoja de trabajo**

 Consulte el siguiente código de ejemplo que explica cómo especificar el campo de fórmula al importar datos a una hoja de cálculo. Por favor vea el[archivo de salida de Excel](61767850.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
