---
title: Especificando dígitos significativos para ser almacenados en archivo Excel con Golang vía C++
linktitle: Especificando Dígitos Significativos
type: docs
weight: 30
url: /es/go-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aprenda cómo especificar dígitos significativos para archivos Excel usando Aspose.Cells con Golang vía C++.
---

## **Escenarios de uso posibles**

Por defecto, Aspose.Cells almacena 17 dígitos significativos de valores doble dentro del archivo Excel, a diferencia de MS-Excel que almacena solo 15 dígitos significativos. Puedes cambiar el comportamiento predeterminado de Aspose.Cells de 17 a 15 dígitos significativos usando la propiedad [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/).

## **Especificación de Dígitos Significativos a ser almacenados en un archivo de Excel**

El siguiente código de ejemplo fuerza a Aspose.Cells a usar 15 dígitos significativos al almacenar valores doble dentro del archivo Excel. Comprueba el [archivo Excel de salida](22774105.xlsx). Cambia su extensión a .zip y descomprímelo, verás que solo se almacenan 15 dígitos significativos. La siguiente captura de pantalla explica el efecto de la propiedad [**GetSignificantDigits()**](https://reference.aspose.com/cells/go-cpp/cellshelper/getsignificantdigits/) en el archivo Excel de salida.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingSignificantDigitsToBeStoredInExcelFile.go" >}}
