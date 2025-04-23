---
title: Especificar cómo cruzar cadenas en PDF de salida e imagen
type: docs
weight: 120
url: /es/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o una cadena pero es más grande que el ancho de la celda, entonces la cadena desborda si la siguiente celda en la siguiente columna es nula o vacía. Al guardar tu archivo de Excel en PDF/Imagen, puedes controlar este desbordamiento especificando el tipo de cruce utilizando la enumeración [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Tiene los siguientes valores

- **TextCrossType.Default**: Muestra el texto como MS Excel, que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o se truncará

- **TextCrossType.CrossKeep**: Muestra la cadena como MS Excel exportando PDF/Imagen

- **TextCrossType.CrossOverride**: Muestra todo el texto cruzando otras celdas y anulando el texto de las celdas cruzadas

- **TextCrossType.StrictInCell**: Solo muestra la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en el PDF/Imagen de salida utilizando TextCrossType**

El siguiente código de ejemplo carga el archivo de Excel de ejemplo y lo guarda en formato PDF/Imagen especificando diferentes [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). El archivo de Excel de ejemplo y los archivos de salida se pueden descargar desde los siguientes enlaces

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Código de Ejemplo

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
