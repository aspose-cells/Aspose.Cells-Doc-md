---
title: Aplicar formato condicional en la hoja de trabajo
type: docs
weight: 40
url: /es/cpp/apply-conditional-formatting-in-worksheet/
---
##  **Posible escenario de uso**
 Aspose.Cells le permite agregar todo tipo de formato condicional, por ejemplo, fórmula, superior al promedio, escala de color, barra de datos, conjunto de iconos, Top10, etc. Proporciona la[Condición de formato](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/)clase que tiene todos los métodos necesarios para aplicar el formato condicional de su elección. Aquí está la lista de algunos de los métodos Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
##  **Aplicar formato condicional en la hoja de trabajo**
 El siguiente código de muestra muestra cómo agregar un formato condicional de valor Cell en las celdas A1 y B2. Por favor vea el[archivo de excel de salida](23167004.xlsx) generado por el código y la siguiente captura de pantalla que explica el efecto del código en el[archivo de excel de salida](23167004.xlsx)Si coloca algún valor mayor que 100 en las celdas A2 y B2, el color de relleno rojo de las celdas A1 y B2 desaparecerá.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
##  **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
