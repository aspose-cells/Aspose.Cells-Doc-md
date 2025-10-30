---
title: Establecer el código de formato de valores de la serie del gráfico con Golang a través de C++
linktitle: Formato de número
type: docs
weight: 100
url: /es/go-cpp/set-the-values-format-code-of-chart-series/
description: Aprende cómo establecer el código de formato de valores de la serie del gráfico en Aspose.Cells for C++. Nuestra guía te ayudará a entender cómo formatear los datos de la serie del gráfico usando el código de formato apropiado, permitiéndote presentar tus datos de manera precisa y profesional.
keywords: Aspose.Cells for C++, serie de gráfico, código de formato de valores, formato, presentación de datos, precisión, profesionalismo.
---

## **Escenarios de uso posibles**
Puede establecer el código de formato de valores de la serie del gráfico usando la propiedad [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/). Esta propiedad no solo es útil para la serie basada en el rango dentro de la hoja de cálculo, sino que también funciona bien para la serie creada con una matriz de valores.

## **Establecer el código de formato de valores de la serie del gráfico**
El siguiente ejemplo de código agrega una serie en el gráfico vacío que no tenía series antes. Agrega la serie utilizando un arreglo de valores. Una vez que agrega la serie, la da formato con el código `$#,##0` usando la propiedad [Series.GetValuesFormatCode()](https://reference.aspose.com/cells/go-cpp/series/getvaluesformatcode/) y el número `10000` se convierte en `$10,000`. La captura de pantalla muestra el efecto del código en el [archivo Excel de muestra](51740712.xlsx) y el [archivo Excel de salida](51740713.xlsx) después de ejecutar.

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **Código de muestra**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-NumberFormat.go" >}}
