---
title: Aplicar formato condicional en la hoja de cálculo
type: docs
weight: 40
url: /es/cpp/apply-conditional-formatting-in-worksheet/
---

## **Escenario de Uso Posible**
Aspose.Cells te permite agregar todo tipo de formato condicional, por ejemplo: Fórmula, Por encima del promedio, Escala de colores, Barra de datos, Conjunto de íconos, Top10, etc. Proporciona la clase [FormatCondition](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/) que tiene todos los métodos necesarios para aplicar formato condicional de tu elección. A continuación se muestra la lista de algunos de los métodos Get.

- [GetAboveAverage()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getaboveaverage/)
- [GetColorScale()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getcolorscale)
- [GetDataBar()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/getdatabar)
- [GetIconSet()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/geticonset)
- [GetTop10()](https://reference.aspose.com/cells/cpp/aspose.cells/formatcondition/gettop10)
## **Aplicar formato condicional en la hoja de cálculo**
El siguiente código de ejemplo muestra cómo agregar formato condicional de valor de celda en las celdas A1 y B2. Consulta el [archivo de Excel de salida](23167004.xlsx) generado por el código y la siguiente captura de pantalla que explica el efecto del código en el [archivo de Excel de salida](23167004.xlsx). Si colocas un valor mayor que 100 en las celdas A2 y B2, el color de relleno rojo de las celdas A1 y B2 desaparecerá.

![todo:image_alt_text](apply-conditional-formatting-in-worksheet_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
