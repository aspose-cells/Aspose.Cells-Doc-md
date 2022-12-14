---
title: Especificación de dígitos significativos que se almacenarán en un archivo de Excel
type: docs
weight: 30
url: /es/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Posibles escenarios de uso**

De forma predeterminada, Aspose.Cells almacena 17 dígitos significativos de valores dobles dentro del archivo de Excel, a diferencia de MS-Excel, que almacena solo 15 dígitos significativos. Puede cambiar el comportamiento predeterminado de Aspose.Cells de 17 dígitos significativos a 15 dígitos significativos usando el[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)propiedad.

## **Especificación de dígitos significativos que se almacenarán en un archivo de Excel**

 El siguiente código de muestra exige que Aspose.Cells use 15 dígitos significativos mientras almacena valores dobles dentro del archivo de Excel. Por favor, checa el[archivo de salida de Excel](22774105.xlsx) . Cambie su extensión a .zip y descomprímalo y verá que solo se almacenan 15 dígitos significativos dentro del archivo de Excel. La siguiente captura de pantalla explica el efecto de[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)propiedad en el archivo de salida de Excel.

![todo:imagen_alternativa_texto](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
