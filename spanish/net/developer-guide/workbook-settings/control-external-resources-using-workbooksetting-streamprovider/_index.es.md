---
title: Controle los recursos externos mediante WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /es/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **Posibles escenarios de uso**

A veces, su archivo de Excel contiene recursos externos, por ejemplo, imágenes vinculadas, etc. Aspose.Cells le permite controlar estos recursos externos usando[**Libro de trabajo.Configuración.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)que lleva la implementación de la[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)interfaz. Cada vez que intente representar su hoja de trabajo que contiene recursos externos, por ejemplo, imágenes vinculadas, los métodos del[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)Se invocará la interfaz que le permitirá tomar las medidas adecuadas para sus recursos externos.

## **Controle los recursos externos mediante WorkbookSetting.StreamProvider**

El siguiente código de ejemplo explica el uso de la[**Libro de trabajo.Configuración.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . carga el[ejemplo de archivo de Excel](61767863.xlsx) que contiene una imagen vinculada. El código reemplaza la imagen vinculada con[Aspose Logotipo](61767862.png) y convierte toda la hoja en una sola imagen usando[**HojaRenderizar**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) clase. La siguiente captura de pantalla muestra el archivo de ejemplo de Excel y su[imagen de salida renderizada](61767865.png) para una referencia. Como puede ver, la imagen vinculada rota se reemplaza con el logotipo Aspose.

![todo:imagen_alternativa_texto](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
