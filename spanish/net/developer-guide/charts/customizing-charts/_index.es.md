---
title: Personalización de gráficos
type: docs
weight: 40
url: /es/net/customizing-charts/
---
{{% alert color="primary" %}}

## **Creación de gráficos personalizados**

Hasta ahora, cuando hemos discutido los gráficos, hemos visto gráficos estándar que tienen su configuración de formato estándar. Solo definimos la fuente de datos, establecemos algunas propiedades y el gráfico se crea con su configuración de formato predeterminada. Pero las API Aspose.Cells también admiten la creación de gráficos personalizados que permiten a los desarrolladores crear gráficos con su propia configuración de formato.

Los desarrolladores pueden crear gráficos personalizados en tiempo de ejecución utilizando Aspose.Cells.

 Un gráfico se compone de una serie de datos. Cada serie de datos en Aspose.Cells está representada por un[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) objeto mientras que[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) objeto sirve como una colección de[**Serie**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)objetos. Al crear un gráfico personalizado, los desarrolladores tienen la libertad de usar diferentes tipos de gráficos para diferentes series de datos (recopilados en el[**SerieColección**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)objeto).

El siguiente código de ejemplo muestra cómo crear gráficos personalizados. En este ejemplo, vamos a utilizar un gráfico de columnas para la primera serie de datos y un gráfico de líneas para la segunda serie. El resultado es que agregamos un gráfico de columnas, combinado con un gráfico de líneas, a la hoja de trabajo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

Actualmente, Aspose.Cells solo admite gráficos personalizados que combinan gráficos circulares, de líneas, de columnas y de pila de columnas, pero se admitirán más gráficos en versiones futuras.

{{% /alert %}}
