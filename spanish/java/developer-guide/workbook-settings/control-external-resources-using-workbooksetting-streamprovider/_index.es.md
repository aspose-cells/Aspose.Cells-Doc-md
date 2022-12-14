---
title: Controle los recursos externos mediante WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /es/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **Posibles escenarios de uso**
A veces, su archivo de Excel contiene recursos externos, por ejemplo, imágenes vinculadas, etc. Aspose.Cells le permite controlar estos recursos externos usando[Libro de trabajo.Configuración.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)que lleva la implementación de[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)interfaz. Cada vez que intente representar su hoja de trabajo que contiene recursos externos, por ejemplo, imágenes vinculadas, los métodos de[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)Se invocará la interfaz que le permitirá tomar las medidas adecuadas para sus recursos externos.
## **Controle los recursos externos mediante WorkbookSetting.StreamProvider**
El siguiente código de ejemplo explica el uso de[Libro de trabajo.Configuración.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). carga el[ejemplo de archivo de Excel](61767877.xlsx)que contiene una imagen vinculada. El código reemplaza la imagen vinculada con[Aspose Logotipo](61767874.png)y convierte toda la hoja en una sola imagen usando[HojaRenderizar](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)clase. La siguiente captura de pantalla muestra el archivo de ejemplo de Excel y su[imagen de salida renderizada](61767874.png)para una referencia. Como puede ver, la imagen vinculada rota se reemplaza con el logotipo Aspose.

![todo:imagen_alternativa_texto](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
