---
title: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 90
url: /es/net/find-if-the-worksheet-is-dialog-sheet/
description: La hoja de diálogo es un formato antiguo de hoja. Este artículo proporciona instrucciones y código de muestra para determinar programáticamente si una hoja de cálculo de Excel es una hoja de diálogo utilizando la API de C# o la biblioteca .NET.
keywords: buscar tipo de cuadro de diálogo de hoja de cálculo de Excel c#, cuadro de diálogo de hoja de cálculo c#
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Tal hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puede encontrar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) proporcionada por Aspose.Cells. Si devuelve el valor de enumeración [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), entonces significa que está tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716820.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type) la compara con [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), y luego imprime el mensaje. Consulte la salida de la consola del código de ejemplo a continuación para obtener más ayuda.

## **Código de muestra**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
