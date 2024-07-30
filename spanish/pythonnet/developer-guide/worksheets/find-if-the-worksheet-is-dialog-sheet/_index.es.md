---
title: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 90
url: /es/python-net/find-if-the-worksheet-is-dialog-sheet/
description: La Hoja de Diálogo es un formato antiguo de hoja. Este artículo proporciona instrucciones y código de muestra para determinar de forma programática si una hoja de cálculo de Excel es una Hoja de Diálogo utilizando la Biblioteca de Aspose.Cells for Python via .NET.
keywords: Biblioteca de Python Excel, tipo de diálogo de hoja de cálculo en Python, hoja de diálogo en Python.
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Tal hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puede encontrar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) proporcionada por Aspose.Cells for Python via .NET. Si devuelve el valor de enumeración [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), entonces significa que está tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716820.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/) la compara con [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/), y luego imprime el mensaje. Consulte la salida de la consola del código de ejemplo a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Salida de la consola**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
