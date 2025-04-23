---
title: Especificar dígitos significativos que se almacenarán en el archivo de Excel
type: docs
weight: 20
url: /es/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Escenarios de uso posibles**

De forma predeterminada, Aspose.Cells almacena 17 dígitos significativos de valores dobles en hojas de cálculo, a diferencia de la aplicación Excel que almacena solo 15 dígitos significativos. Puede cambiar el comportamiento predeterminado de Aspose.Cells para este caso, es decir; puede cambiar el número de dígitos significativos de 17 a 15 mientras utiliza la propiedad [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits).

## **Especificar dígitos significativos que se almacenarán en el archivo de Excel**

El siguiente código de ejemplo obliga a Aspose.Cells a utilizar 15 dígitos significativos al almacenar valores dobles dentro del archivo de Excel. Consulte el [archivo de Excel de salida](23166982.xlsx). Cambie su extensión a .zip y descomprímalo, y verá que dentro del archivo de Excel solo se almacenan 15 dígitos significativos. La siguiente captura de pantalla explica el efecto de la propiedad [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) en el archivo de Excel de salida.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
