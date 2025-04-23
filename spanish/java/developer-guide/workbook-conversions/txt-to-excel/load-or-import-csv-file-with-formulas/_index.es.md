---
title: Cargar o Importar archivo CSV con Fórmulas
type: docs
weight: 500
url: /es/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

Los archivos CSV generalmente contienen datos textuales y no contienen fórmulas. Sin embargo, a veces sucede que los archivos CSV también contienen fórmulas. Estos archivos CSV deben cargarse configurando [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) a **true**. Una vez que esta propiedad se establezca en **true**, Aspose.Cells no tratará las fórmulas como texto simple. Se tratarán como fórmulas y el motor de cálculo de fórmulas de Aspose.Cells las procesará como de costumbre.

{{% /alert %}} 
## **Cargar o importar archivo CSV con fórmulas**
El siguiente código ilustra cómo se puede cargar e importar un archivo CSV con fórmulas. Se puede usar cualquier archivo CSV. Para fines ilustrativos, usamos el [archivo CSV simple](5472505.csv) que contiene estos datos. Como se puede ver, contiene una fórmula.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

El código primero carga el archivo CSV, luego lo importa nuevamente en la celda D4. Finalmente, guarda el objeto del libro de trabajo en formato XSLX. El [archivo XLSX de salida](5472503.xlsx) se ve así. Como se puede ver, la celda C3 y F4 contienen una fórmula y su resultado 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
{{< app/cells/assistant language="java" >}}
