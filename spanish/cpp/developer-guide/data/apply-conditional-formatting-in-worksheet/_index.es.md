---
title: Aplicar formato condicional en la hoja de trabajo
type: docs
weight: 40
url: /es/cpp/apply-conditional-formatting-in-worksheet/
---
## **Escenario de uso posible**
 Aspose.Cells le permite agregar todo tipo de Formato condicional, por ejemplo, Fórmula, Por encima del promedio, Escala de color, Barra de datos, Conjunto de iconos, Top10, etc. Proporciona la[IFormatCondition](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition)class que tiene todos los métodos necesarios para aplicar el formato condicional de su elección. Aquí está la lista de algunos de los métodos Get.

- [GetIAbovePromedio()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#aff550fd834cd78967ec440492ff012d5)
- [ObtenerEscalaIColor()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a3348a7c447dc564ceabc22c9c89bd6f5)
- [ObtenerIDataBar()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a4415a87833c41386ed1595e742485e07)
- [ObtenerConjuntoIIcon()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a011b2c7dbaaf671819d09f5d1df865e3)
- [ObtenerITop10()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_format_condition#a64388aaf1b43811f5ee1ee3090c9bd4a)
## **Aplicar formato condicional en la hoja de trabajo**
 El siguiente código de ejemplo muestra cómo agregar un formato condicional de valor Cell en las celdas A1 y B2. Por favor vea el[archivo de salida de Excel](23167004.xlsx) generado por el código y la siguiente captura de pantalla que explica el efecto del código en el[archivo de salida de Excel](23167004.xlsx). Si coloca un valor superior a 100 en la celda A2 y B2, el color de relleno rojo de la celda A1 y B2 desaparecerá.

![todo:imagen_alternativa_texto](apply-conditional-formatting-in-worksheet_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Data-ApplyConditionalFormattingInWorksheet.cpp" >}}
