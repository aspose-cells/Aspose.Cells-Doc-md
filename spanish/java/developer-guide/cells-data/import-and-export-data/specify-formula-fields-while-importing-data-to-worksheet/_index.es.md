---
title: Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo
type: docs
weight: 220
url: /es/java/specify-formula-fields-while-importing-data-to-worksheet/
---

## **Escenarios de uso posibles**

Puede especificar campos de fórmula al importar datos en su hoja de cálculo utilizando el método [**ImportTableOptions.setFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/importtableoptions#IsFormulas). Este método toma la matriz booleana donde el valor **true** significa que el campo es un campo de fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, entonces el tercer valor en la matriz será **true**.

## **Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo**

Consulte el siguiente código de muestra que explica cómo especificar el campo de fórmula al importar datos a una hoja de cálculo. Consulte el [archivo de Excel de salida](61767850.xlsx) generado por el código y la captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-SpecifyFormulaFieldsWhileImportingDataToWorksheet.java" >}}
