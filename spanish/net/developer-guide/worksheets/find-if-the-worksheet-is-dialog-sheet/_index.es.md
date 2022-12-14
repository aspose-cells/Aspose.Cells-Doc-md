---
title: Averigüe si la hoja de trabajo es una hoja de diálogo
type: docs
weight: 90
url: /es/net/find-if-the-worksheet-is-dialog-sheet/
---
## **Posibles escenarios de uso**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Dicha hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:imagen_alternativa_texto](find-if-the-worksheet-is-dialog-sheet_1.png)

Puede encontrar si la hoja es una hoja de diálogo o algún otro tipo de hoja con[**Hoja de trabajo.Tipo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)propiedad proporcionada por Aspose.Cells. Si devuelve el valor de enumeración[**SheetType.Diálogo**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), entonces significa que está tratando con una hoja de diálogo.

## **Averigüe si la hoja de trabajo es una hoja de diálogo**

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716820.xlsx) que contiene una hoja de diálogo. Comprueba el[**Hoja de trabajo.Tipo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)la propiedad la compara con[**SheetType.Diálogo**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) y luego imprime el mensaje. Consulte la salida de la consola del código de muestra que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
