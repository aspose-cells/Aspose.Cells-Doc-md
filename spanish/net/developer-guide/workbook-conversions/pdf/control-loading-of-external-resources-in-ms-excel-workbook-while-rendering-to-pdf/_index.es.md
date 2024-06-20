---
title: Controlar la carga de recursos externos en el libro de Excel de MS al renderizar a PDF
type: docs
weight: 40
url: /es/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Escenarios de uso posibles**

Su archivo de Excel puede contener recursos externos como imágenes u objetos vinculados. Cuando convierte su archivo de Excel a PDF, Aspose.Cells recupera estos recursos externos y los renderiza a PDF. Pero a veces, no desea cargar estos recursos externos y, además, desea manipularlos. Puede hacerlo usando [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) que implementa la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider).

## **Controlar la carga de recursos externos en el libro de Excel de MS al renderizar a PDF**

El siguiente código de muestra explica cómo hacer uso de [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) para controlar la carga de recursos externos y manipularlos. Por favor revise el [archivo de Excel de muestra](50528322.xlsx) usado en el código y el [PDF generado](50528325.pdf) por el código. La [captura de pantalla](50528326.png) muestra cómo la [imagen externa antigua](50528324.png) en el archivo de Excel de muestra fue reemplazada por una [nueva imagen](50528323.png) en el PDF generado.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
