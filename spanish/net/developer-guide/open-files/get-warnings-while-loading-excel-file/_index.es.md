---
title: Obtener advertencias al cargar archivo de Excel
type: docs
weight: 110
url: /es/net/get-warnings-while-loading-excel-file/
---

## **Escenarios de uso posibles**

A veces, el usuario intenta cargar el libro de trabajo que está algo dañado pero es cargable. En ese caso, Aspose.Cells lanza advertencias al cargar el libro de trabajo. Puede capturar estas advertencias implementando la interfaz [**IWarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback) y configurando la propiedad [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback).

## **Obtener advertencias al cargar archivo de Excel**

El siguiente código de muestra explica cómo obtener advertencias al cargar un archivo de Excel. El código carga el [archivo de Excel de muestra](sampleDuplicateDefinedName.xlsx) que lanza [**DuplicateDefinedName**](https://reference.aspose.com/cells/net/aspose.cells/warningtype) advertencias al cargar. Estas advertencias son luego atrapadas por el método [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning) que imprime los mensajes de advertencia en la consola. Luego, el código guarda el libro de trabajo como [archivo de Excel de salida](outputDuplicateDefinedName.xlsx). Si abre el archivo de Excel de muestra en Microsoft Excel, también le mostrará esta advertencia como se muestra en esta captura de pantalla. Consulte también la salida de la consola del código que se muestra a continuación para comprender mejor.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
