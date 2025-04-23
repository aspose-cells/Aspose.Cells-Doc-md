---
title: Controlar la carga de recursos externos en el libro de Excel de MS al renderizar a PDF
type: docs
weight: 40
url: /es/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Escenarios de uso posibles**

Su archivo de Excel puede contener recursos externos como imágenes vinculadas u objetos. Cuando convierte su archivo de Excel a PDF, Aspose.Cells recupera estos recursos externos y los renderiza a PDF. Pero a veces, no desea cargar estos recursos externos y, más que eso, desea manipularlos. Puede hacer esto usando [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) que implementa la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider).

## **Controlar la carga de recursos externos en el libro de Excel de MS al renderizar a PDF**

El siguiente código de ejemplo explica cómo hacer uso de [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) para controlar la carga de recursos externos y manipularlos. Por favor, revise el [archivo de Excel de muestra](50528353.xlsx) utilizado dentro del código y el [PDF de salida](50528354.pdf) generado por el código. La [captura de pantalla](50528357.png) muestra cómo la [imagen externa antigua](50528356.png) en el archivo de Excel de muestra fue reemplazada por una [nueva imagen](50528355.png) en el PDF de salida.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
{{< app/cells/assistant language="java" >}}
