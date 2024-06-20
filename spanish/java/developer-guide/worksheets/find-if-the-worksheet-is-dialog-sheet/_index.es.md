---
title: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 100
url: /es/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de la hoja que contiene un cuadro de diálogo. Esta hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003 como se muestra en esta captura de pantalla. También puede ser insertada con VBA en versiones más recientes, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puedes encontrar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) proporcionada por Aspose.Cells. Si devuelve el valor de enumeración [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), entonces significa que estás tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo Excel de muestra](64716841.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type), la compara con [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) y luego imprime el mensaje. Por favor, revisa la salida de la consola del código de ejemplo proporcionado a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
