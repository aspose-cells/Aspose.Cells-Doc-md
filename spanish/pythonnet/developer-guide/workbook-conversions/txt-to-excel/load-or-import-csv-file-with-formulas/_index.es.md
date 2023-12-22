---
title: Cargar o importar archivo CSV con fórmulas
type: docs
weight: 350
url: /es/python-net/load-or-import-csv-file-with-formulas/
description: Cargue o importe el archivo CSV con fórmulas utilizando Aspose.Cells for Python via .NET API.
keywords: Python Load or Import CSV file with Formulas, Convert CSV with Formulas to Excel in Python via NET, Python convert CSV with Formulas to xlsx, Load CSV with Formulas to Excel file.
---
{{% alert color="primary" %}} 

 El archivo CSV contiene principalmente datos textuales y no contiene ninguna fórmula. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Dichos archivos CSV deben cargarse configurando el[TxtLoadOptions.has_formula](https://reference.aspose.com/cells/python-net/aspose.cells/txtloadoptions/has_formula/) como *verdadero**. Una vez que esta propiedad se establezca como *verdadera**, Aspose.Cells no tratará la fórmula como texto simple. Serán tratados como fórmula y el motor de cálculo de fórmulas Aspose.Cells los procesará como de costumbre.

{{% /alert %}} 

 El siguiente código ilustra cómo puede cargar e importar un archivo CSV con fórmulas. Puede utilizar cualquier archivo CSV. Con fines ilustrativos, utilizamos el[archivo csv sencillo](5115034.csv)que contiene estos datos. Como ves contiene una fórmula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Txt-ImportCSVWithFormulas-ImportCSVWithFormulas.py" >}}



 El código primero carga el archivo CSV y luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto del libro de trabajo en formato XSLX. El[salida del archivo XLSX](5115052.xlsx) Se ve como esto. Como puede ver, las celdas C3 y F4 contienen la fórmula y su resultado 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

