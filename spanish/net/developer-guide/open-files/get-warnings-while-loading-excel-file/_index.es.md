---
title: Recibe advertencias al cargar un archivo de Excel
type: docs
weight: 110
url: /es/net/get-warnings-while-loading-excel-file/
---
## **Posibles escenarios de uso**

 veces, el usuario intenta cargar el libro de trabajo que está algo corrupto pero se puede cargar. En tal caso, Aspose.Cells arroja advertencias al cargar el libro de trabajo. Puede detectar estas advertencias implementando el**[IWarningCallback](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback)** interfaz y configuración**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/warningcallback)**propiedad.

## **Recibe advertencias al cargar un archivo de Excel**

 El siguiente código de ejemplo explica cómo recibir advertencias al cargar un archivo de Excel. El código carga el[ejemplo de archivo de Excel](sampleDuplicateDefinedName.xlsx) que lanza**[Nombre definido duplicado] (https://reference.aspose.com/cells/net/aspose.cells/warningtype)** advertencia en la carga. Esta advertencia es captada por**[IWarningCallback.Warning()](https://reference.aspose.com/cells/net/aspose.cells/iwarningcallback/methods/warning)** método que imprime los mensajes de advertencia en la consola. Luego, el código guarda el libro de trabajo como[archivo de salida de Excel](outputDuplicateDefinedName.xlsx)Si abre el archivo de muestra de Excel en Microsoft Excel, también le mostrará esta advertencia como se muestra en esta captura de pantalla. Consulte también la salida de la consola del código que se proporciona a continuación para obtener más información.

![todo:imagen_alternativa_texto](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-GetWarningsWhileLoadingExcelFile.cs" >}}

## **Salida de consola**

 Aquí está la salida de la consola del código anterior cuando se ejecuta con el proporcionado[ejemplo de archivo de Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
