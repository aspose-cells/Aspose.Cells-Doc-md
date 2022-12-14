---
title: Controle la carga de recursos externos en el libro de trabajo de MS Excel mientras se procesa en PDF
type: docs
weight: 40
url: /es/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Posibles escenarios de uso**

Su archivo de Excel puede contener recursos externos, por ejemplo, imágenes u objetos vinculados. Cuando convierte su archivo de Excel a PDF, Aspose.Cells recupera estos recursos externos y los convierte en PDF. Pero a veces, no quieres cargar estos recursos externos y más que eso, quieres manipularlos. Puedes hacer esto usando[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)que implementa la[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaz.

## **Controle la carga de recursos externos en el libro de trabajo de MS Excel mientras se procesa en PDF**

El siguiente código de ejemplo explica cómo hacer uso de[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)para controlar la carga de recursos externos y manipularlos. Por favor, checa el[ejemplo de archivo de Excel](50528353.xlsx)utilizado dentro del código y el[PDF de salida](50528354.pdf)generado por el código. los[captura de pantalla](50528357.png)muestra cómo el[imagen externa antigua](50528356.png)en el archivo de ejemplo de Excel se reemplazó con un[nueva imagen](50528355.png)en el PDF de salida.

![todo:imagen_alternativa_texto](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}
