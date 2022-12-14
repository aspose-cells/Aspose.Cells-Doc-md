---
title: Controle la carga de recursos externos en el libro de trabajo de MS Excel mientras se procesa en PDF
type: docs
weight: 40
url: /es/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Posibles escenarios de uso**

 Su archivo de Excel puede contener recursos externos, por ejemplo, imágenes u objetos vinculados. Cuando convierte su archivo de Excel a PDF, Aspose.Cells recupera estos recursos externos y los convierte en PDF. Pero a veces, no quieres cargar estos recursos externos y más que eso, quieres manipularlos. Puedes hacer esto usando[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)que implementa la[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaz.

## **Controle la carga de recursos externos en el libro de trabajo de MS Excel mientras se procesa en PDF**

 El siguiente código de ejemplo explica cómo hacer uso de[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) para controlar la carga de recursos externos y manipularlos. Por favor, checa el[ejemplo de archivo de Excel](50528322.xlsx) utilizado dentro del código y el[PDF de salida](50528325.pdf)generado por el código. los[captura de pantalla](50528326.png) muestra cómo el[imagen externa antigua](50528324.png) en el archivo de ejemplo de Excel se reemplazó con un[nueva imagen](50528323.png) en el PDF de salida.

![todo:imagen_alternativa_texto](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}
