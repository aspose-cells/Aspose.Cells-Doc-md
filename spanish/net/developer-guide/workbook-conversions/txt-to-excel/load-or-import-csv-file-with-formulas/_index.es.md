---
title: Cargar o Importar archivo CSV con Fórmulas
type: docs
weight: 350
url: /es/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Los archivos CSV principalmente contienen datos textuales y no contienen fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Estos archivos CSV deben ser cargados configurando [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) como **true**. Una vez que esta propiedad esté configurada como **true**, Aspose.Cells no tratará la fórmula como texto simple. Las tratará como fórmula y el motor de cálculo de fórmulas de Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 

El siguiente código ilustra cómo puedes cargar e importar un archivo CSV con fórmulas. Puedes usar cualquier archivo CSV. Para fines ilustrativos, usamos el [archivo csv simple](5115034.csv) que contiene estos datos. Como puedes ver, contiene una fórmula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto del libro en formato XSLX. El [archivo XLSX de salida](5115052.xlsx) se ve así. Como puedes ver, la celda C3 y F4 contienen una fórmula y su resultado es 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

{{< app/cells/assistant language="csharp" >}}
