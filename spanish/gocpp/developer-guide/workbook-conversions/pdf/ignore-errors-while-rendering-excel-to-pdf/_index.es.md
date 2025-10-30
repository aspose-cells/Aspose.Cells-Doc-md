---
title: Ignorar errores al convertir Excel a PDF con Golang vía C++
linktitle: Ignorar Errores al Renderizar Excel a PDF
type: docs
weight: 80
url: /es/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Aprende cómo ignorar errores durante la conversión de Excel a PDF usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

A veces, al convertir su archivo Excel a PDF, ocurren errores o excepciones y el proceso de conversión termina. Puede ignorar todos esos errores durante el proceso de conversión usando la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/). De esta manera, el proceso de conversión se completará sin lanzar ningún error o excepción, pero puede ocurrir pérdida de datos. Por lo tanto, use esta propiedad solo si la pérdida de datos no es crítica para usted.

## **Ignorar errores al renderizar Excel a PDF**

El siguiente código carga el [archivo de ejemplo de Excel](55541778.xlsx), pero el archivo de ejemplo es erróneo y genera un error durante [la conversión a PDF](55541779.pdf) en 17.11, pero dado que estamos usando la propiedad [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/), no genera error. Sin embargo, una *forma de flecha roja redondeada* como se muestra en esta captura de pantalla se pierde.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
