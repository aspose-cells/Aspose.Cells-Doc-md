---
title: Obtener advertencias al cargar archivo de Excel
type: docs
weight: 60
url: /es/java/get-warnings-while-loading-excel-file/
---

## **Escenarios de uso posibles**

A veces, el usuario intenta cargar el libro de trabajo que está algo dañado pero es cargable. En ese caso, Aspose.Cells lanza advertencias al cargar el libro de trabajo. Puede capturar estas advertencias implementando la interfaz [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) y configurando la propiedad [**LoadOptions.WarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#WarningCallback).

## **Obtener advertencias al cargar archivo de Excel**

El siguiente código de muestra explica cómo obtener advertencias al cargar un archivo de Excel. El código carga el [archivo de Excel de muestra](sampleDuplicateDefinedName.xlsx) que lanza [**DuplicateDefinedName**](https://reference.aspose.com/cells/java/com.aspose.cells/warningtype#DUPLICATE-DEFINED-NAME) advertencias al cargar. Estas advertencias son luego atrapadas por el método [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/java/com.aspose.cells/iwarningcallback#warning-com.aspose.cells.WarningInfo-) que imprime los mensajes de advertencia en la consola. Luego, el código guarda el libro de trabajo como [archivo de Excel de salida](outputDuplicateDefinedName.xlsx). Si abre el archivo de Excel de muestra en Microsoft Excel, también le mostrará esta advertencia como se muestra en esta captura de pantalla. Consulte también la salida de la consola del código que se muestra a continuación para comprender mejor.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-WarningCallback-WarningCallback.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-GetWarningLoadingAnExcel-GetWarningLoadingAnExcel.java" >}}

## **Salida de la consola**

Aquí está la salida de la consola del código anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
