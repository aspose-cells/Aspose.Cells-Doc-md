---
title: Cargar o Importar archivo CSV con Fórmulas
type: docs
weight: 350
url: /es/python-net/load-or-import-csv-file-with-formulas/
description: Cargar o importar un archivo CSV con fórmulas utilizando Aspose.Cells for Python via .NET API.
keywords: Cargar o importar un archivo CSV con fórmulas en Python, convertir CSV con fórmulas a Excel en Python via NET, convertir CSV con fórmulas a xlsx en Python, Cargar CSV con fórmulas a archivo de Excel en Python.
---

{{% alert color="primary" %}} 

El archivo CSV contiene principalmente datos textuales y no contiene fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Estos archivos CSV deben cargarse configurando la propiedad [TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) como **verdadero**. Una vez que esta propiedad se establezca en **verdadero**, Aspose.Cells no tratará las fórmulas como texto simple. Se tratarán como fórmulas y el motor de cálculo de fórmulas de Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 

El siguiente código ilustra cómo puedes cargar e importar un archivo CSV con fórmulas. Puedes usar cualquier archivo CSV. Para fines ilustrativos, usamos el [archivo csv simple](5115034.csv) que contiene estos datos. Como puedes ver, contiene una fórmula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto del libro en formato XSLX. El [archivo XLSX de salida](5115052.xlsx) se ve así. Como puedes ver, la celda C3 y F4 contienen una fórmula y su resultado es 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="python-net" >}}
