---
title: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 70
url: /es/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Escenarios de uso posibles**
La hoja de diálogo es un formato antiguo de la hoja que contiene un cuadro de diálogo. Esta hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003 como se muestra en esta captura de pantalla. También puede ser insertada con VBA en versiones más recientes, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](DialogSheet.png)
## **Buscar si la hoja de trabajo es una hoja de diálogo**
Aspose.Cells for Python via Java te brinda la capacidad de comprobar si la hoja de cálculo es una hoja de diálogo. Para esto, proporciona la propiedad [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type). Si [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) devuelve el valor de enumeración [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), entonces significa que estás tratando con una hoja de diálogo.

El siguiente fragmento de código muestra cómo comprobar si es una hoja de diálogo. La salida de la consola generada por el código se muestra a continuación para referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Salida de la consola**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
