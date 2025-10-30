---
title: Cargar o importar archivo CSV con fórmulas usando C++
linktitle: Cargar o Importar archivo CSV con Fórmulas
type: docs
weight: 350
url: /es/go-cpp/load-or-import-csv-file-with-formulas/
description: Cargar o importar un archivo CSV que contiene fórmulas usando Aspose.Cells con Golang mediante C++.
---

{{% alert color="primary" %}} 

Los archivos CSV principalmente contienen datos de texto y generalmente no incluyen fórmulas. Sin embargo, hay casos en los que los archivos CSV pueden contener fórmulas. Estos archivos CSV deben cargarse configurando [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) en **true**. Una vez que esta propiedad está en **true**, Aspose.Cells no tratará las fórmulas como texto simple. Se tratarán como fórmulas, y el motor de cálculo de fórmulas de Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 

El siguiente código ilustra cómo cargar e importar un archivo CSV con fórmulas. Puede usar cualquier archivo CSV. Para fines ilustrativos, usamos el [archivo CSV simple](5115034.csv) que contiene estos datos. Como puede ver, contiene una fórmula.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto libro en formato XLSX. El [archivo XLSX de salida](5115052.xlsx) se ve así. Como puede ver, las celdas C3 y F4 contienen fórmulas y su resultado es 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
