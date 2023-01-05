---
title: Cargue o importe el archivo CSV con fórmulas
type: docs
weight: 350
url: /es/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 El archivo CSV contiene principalmente datos textuales y no contiene fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Dichos archivos CSV deben cargarse configurando el[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) como**verdadero** . Una vez establecida esta propiedad**verdadero**, Aspose.Cells no tratará la fórmula como texto simple. Se tratarán como fórmulas y el motor de cálculo de fórmulas Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 

 El siguiente código ilustra cómo puede cargar e importar un archivo CSV con fórmulas. Puede usar cualquier archivo CSV. Con fines ilustrativos, utilizamos el[archivo csv sencillo](5115034.csv) que contiene estos datos. Como ves contiene una fórmula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto del libro de trabajo en formato XSLX. Él[archivo de salida XLSX](5115052.xlsx) Se ve como esto. Como ve, las celdas C3 y F4 contienen fórmula y su resultado 800.

|![todo:imagen_alternativa_texto](load-or-import-csv-file-with-formulas_1.png)|
|:- |

