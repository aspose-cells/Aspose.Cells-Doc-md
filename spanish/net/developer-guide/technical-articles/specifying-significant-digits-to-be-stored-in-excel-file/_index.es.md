---
title: Especificación de Dígitos Significativos a ser Almacenados en un Archivo de Excel
type: docs
weight: 30
url: /es/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Escenarios de uso posibles**

De forma predeterminada, Aspose.Cells almacena 17 dígitos significativos de valores de tipo double dentro del archivo de Excel, a diferencia de MS-Excel que almacena solo 15 dígitos significativos. Puede cambiar el comportamiento predeterminado de Aspose.Cells de 17 dígitos significativos a 15 dígitos significativos utilizando la propiedad [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**

El siguiente código de ejemplo obliga a Aspose.Cells a utilizar 15 dígitos significativos al almacenar valores de tipo double dentro del archivo de Excel. Por favor, consulte el [archivo de Excel de salida](22774105.xlsx). Cambie su extensión a .zip y descomprímalo, y verá que solo se almacenan 15 dígitos significativos dentro del archivo de Excel. La siguiente captura de pantalla explica el efecto de la propiedad [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) en el archivo de Excel de salida.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
{{< app/cells/assistant language="csharp" >}}
