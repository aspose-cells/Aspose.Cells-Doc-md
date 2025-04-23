---
title: Controlar Recursos Externos usando WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /es/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **Escenarios de uso posibles**
A veces, su archivo de Excel contiene recursos externos, como imágenes vinculadas, etc. Aspose.Cells le permite controlar estos recursos externos utilizando [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider), que toma la implementación de [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaz. Cada vez que intente mostrar su hoja de cálculo que contiene recursos externos, como imágenes vinculadas, se invocarán los métodos de [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) interfaz, lo que le permitirá tomar medidas apropiadas para sus recursos externos.
## **Controlar Recursos Externos usando WorkbookSetting.StreamProvider**
El siguiente código de muestra explica el uso de [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). Carga el [archivo Excel de muestra](61767877.xlsx) que contiene una imagen vinculada. El código reemplaza la imagen vinculada con el [logotipo de Aspose](61767874.png) y representa toda la hoja en una sola imagen usando la clase [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender). La siguiente captura de pantalla muestra el archivo Excel de muestra y su [imagen de salida representada](61767874.png) para su referencia. Como puede ver, la imagen vinculada rota se reemplaza con el logo de Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
{{< app/cells/assistant language="java" >}}
