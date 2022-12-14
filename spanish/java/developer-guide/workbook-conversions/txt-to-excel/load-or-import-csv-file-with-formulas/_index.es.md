---
title: Cargue o importe un archivo CSV con fórmulas
type: docs
weight: 500
url: /es/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 El archivo CSV contiene principalmente datos textuales y no contiene fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Dichos archivos CSV deben cargarse configurando el[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) a**verdadero** . Una vez que esta propiedad se establezca en**verdadero**, Aspose.Cells no tratará la fórmula como texto simple. Se tratarán como fórmulas y el motor de cálculo de fórmulas Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 
## **Cargue o importe un archivo CSV con fórmulas**
 El siguiente código ilustra cómo puede cargar e importar un archivo CSV con fórmulas. Puede utilizar cualquier archivo CSV. Con fines ilustrativos, utilizamos el[archivo csv sencillo](5472505.csv) que contiene estos datos. Como ves contiene una fórmula.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

 El código primero carga el archivo CSV y luego lo vuelve a importar en la celda D4. Finalmente, guarda el objeto del libro de trabajo en formato XSLX. los[archivo XLSX de salida](5472503.xlsx) Se ve como esto. Como ve, las celdas C3 y F4 contienen fórmula y su resultado 800.

![todo:imagen_alternativa_texto](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
