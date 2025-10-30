---
title: Cómo establecer una serie como invisible con Golang a través de C++
linktitle: Cómo establecer la serie como invisible
description: En un gráfico de Excel, puede ser necesario ocultar una serie. Este artículo describe cómo usar Aspose.Cells con Golang a través de C++ para lograrlo.
keywords: Gráficos de Excel, Series, Invisible, EstáFiltrado.
type: docs
weight: 74
url: /es/go-cpp/how-to-set-series-invisible/
---

## Cómo hacer que una serie sea invisible en un gráfico de Excel

En un gráfico de Excel, puedes hacer clic derecho en el gráfico, seleccionar "Seleccionar datos", y en la ventana emergente, puedes definir si una serie está visible marcándola o desmarcándola. Puedes descargar el siguiente [archivo de ejemplo](SeriesFiltered.xlsx) y operarlo en Excel como se muestra en la figura para lograr esta función. A continuación, te explicaremos cómo lograrlo usando la biblioteca Aspose.Cells.

![todo:image_alt_text](series-invisible.png)

## Cómo hacer que una serie sea invisible usando Aspose.Cells 

Usamos el siguiente código para hacer que una serie sea invisible usando Aspose.Cells:

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetSeriesInvisible.go" >}}
Puedes obtener el [archivo de entrada](SeriesFiltered.xlsx) y el [archivo de salida](output.xlsx).

Como se muestra en la figura a continuación, las dos primeras series que originalmente estaban visibles, se han vuelto invisibles en el archivo de salida.  
![todo:image_alt_text](output.png)
