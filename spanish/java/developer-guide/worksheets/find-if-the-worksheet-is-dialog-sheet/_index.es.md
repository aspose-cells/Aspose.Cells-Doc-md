---
title: Averigüe si la hoja de trabajo es una hoja de diálogo
type: docs
weight: 100
url: /es/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Posibles escenarios de uso**

Hoja de diálogo es un formato antiguo de la hoja que contiene un cuadro de diálogo. Dicha hoja podría insertarse con una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:imagen_alternativa_texto](find-if-the-worksheet-is-dialog-sheet_1.png)

Puede encontrar si la hoja es una hoja de diálogo o algún otro tipo de hoja con[**Hoja de trabajo.Tipo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)propiedad proporcionada por Aspose.Cells. Si devuelve el valor de enumeración[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), entonces significa que está tratando con una hoja de diálogo.

## **Averigüe si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](64716841.xlsx)que contiene una hoja de diálogo. Comprueba el[**Hoja de trabajo.Tipo**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)la propiedad la compara con[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)y luego imprime el mensaje. Consulte la salida de la consola del código de muestra que se proporciona a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
