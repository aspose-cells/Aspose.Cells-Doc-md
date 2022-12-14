---
title: Especificación de dígitos significativos que se almacenarán en un archivo de Excel
type: docs
weight: 20
url: /es/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Posibles escenarios de uso**

De forma predeterminada, Aspose.Cells almacena 17 dígitos significativos de valores dobles en hojas de cálculo, a diferencia de la aplicación Excel, que almacena solo 15 dígitos significativos. Puede cambiar el comportamiento predeterminado de Aspose.Cells para este caso, es decir; puede cambiar el número de dígitos significativos de 17 a 15 mientras usa el[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)propiedad.

## **Especificación de dígitos significativos que se almacenarán en un archivo de Excel**

 El siguiente código de muestra exige que Aspose.Cells use 15 dígitos significativos mientras almacena valores dobles dentro del archivo de Excel. Por favor, checa el[archivo de salida de Excel](23166982.xlsx) . Cambie su extensión a .zip y descomprímalo y verá que solo se almacenan 15 dígitos significativos dentro del archivo de Excel. La siguiente captura de pantalla explica el efecto de[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)propiedad en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
