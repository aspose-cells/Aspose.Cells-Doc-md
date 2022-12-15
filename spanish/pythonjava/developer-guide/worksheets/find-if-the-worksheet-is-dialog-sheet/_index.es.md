---
title: Averigüe si la hoja de trabajo es una hoja de diálogo
type: docs
weight: 70
url: /es/python-java/find-if-the-worksheet-is-dialog-sheet/
---
## **Posibles escenarios de uso**
Hoja de diálogo es un formato antiguo de la hoja que contiene un cuadro de diálogo. Dicha hoja podría insertarse con una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:imagen_alternativa_texto](DialogSheet.png)
## **Averigüe si la hoja de trabajo es una hoja de diálogo**
Aspose.Cells for Python via Java le brinda la posibilidad de verificar si la hoja de trabajo es una hoja de diálogo. Para ello, proporciona la[Hoja de trabajo.Tipo](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)propiedad. Si[Hoja de trabajo.Tipo](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type)devuelve el valor de enumeración[SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG), entonces significa que está tratando con una hoja de diálogo.

El siguiente fragmento de código muestra cómo buscar una hoja de diálogo. La salida de la consola generada por el código se proporciona a continuación como referencia.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Salida de consola**
La hoja de trabajo es una hoja de diálogo.
