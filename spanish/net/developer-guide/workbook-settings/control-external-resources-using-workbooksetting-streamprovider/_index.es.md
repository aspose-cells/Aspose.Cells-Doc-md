---
title: Controlar Recursos Externos usando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /es/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Escenarios de uso posibles**

A veces, su archivo de Excel contiene recursos externos, como imágenes vinculadas, etc. Aspose.Cells le permite controlar estos recursos externos utilizando [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) que toma la implementación de la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider). Cada vez que intente renderizar su hoja de cálculo que contiene recursos externos, como imágenes vinculadas, se invocarán los métodos de la interfaz [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) que le permitirán tomar acciones apropiadas para sus recursos externos.

## **Controlar Recursos Externos usando WorkbookSetting.StreamProvider**

El siguiente código de muestra explica el uso del [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). Carga el [archivo Excel de muestra](61767863.xlsx) que contiene una imagen vinculada. El código reemplaza la imagen vinculada con el [Logo de Aspose](61767862.png) y renderiza toda la hoja en una sola imagen utilizando la clase [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). La siguiente captura de pantalla muestra el archivo Excel de muestra y su [imagen de salida renderizada](61767865.png) como referencia. Como puedes ver, la imagen vinculada rota es reemplazada por el Logo de Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
