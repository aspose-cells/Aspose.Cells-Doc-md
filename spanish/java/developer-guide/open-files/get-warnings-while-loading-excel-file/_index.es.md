---
title: Recibe advertencias al cargar un archivo de Excel
type: docs
weight: 60
url: /es/java/get-warnings-while-loading-excel-file/
---
## **Posibles escenarios de uso**

 veces, el usuario intenta cargar el libro de trabajo que está algo corrupto pero se puede cargar. En tal caso, Aspose.Cells arroja advertencias al cargar el libro de trabajo. Puede detectar estas advertencias implementando el**[IWarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)** interfaz y configuración**[LoadOptions.WarningCallback](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback)**propiedad.

## **Recibe advertencias al cargar un archivo de Excel**

 El siguiente código de ejemplo explica cómo recibir advertencias al cargar un archivo de Excel. El código carga el[ejemplo de archivo de Excel](sampleDuplicateDefinedName.xlsx) que lanza**[Nombre definido duplicado] (https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE_DEFINED_NAME)** advertencia en la carga. Esta advertencia es captada por**[IWarningCallback.Warning()](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning(com.aspose.cells.WarningInfo))** método que imprime los mensajes de advertencia en la consola. Luego, el código guarda el libro de trabajo como[archivo de salida de Excel](outputDuplicateDefinedName.xlsx)Si abre el archivo de muestra de Excel en Microsoft Excel, también le mostrará esta advertencia como se muestra en esta captura de pantalla. Consulte también la salida de la consola del código que se proporciona a continuación para obtener más información.

![todo:imagen_alternativa_texto](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Salida de consola**

 Aquí está la salida de la consola del código anterior cuando se ejecuta con el proporcionado[ejemplo de archivo de Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight "java" >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
