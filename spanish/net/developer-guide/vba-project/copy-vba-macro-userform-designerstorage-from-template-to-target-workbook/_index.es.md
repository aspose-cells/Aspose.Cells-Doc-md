---
title: Copie VBA Macro UserForm DesignerStorage de la plantilla al libro de trabajo de destino
type: docs
weight: 130
url: /es/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Posibles escenarios de uso**

Aspose.Cells le permite copiar un proyecto VBA de un archivo de Excel a otro archivo de Excel. El proyecto de VBA consta de varios tipos de módulos, es decir, documento, procedimiento, diseñador, etc. Todos los módulos se pueden copiar con un código simple, pero para el módulo de diseñador, hay algunos datos adicionales llamados almacenamiento de diseñador a los que se debe acceder o copiar. Los dos métodos siguientes se ocupan de Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Copie VBA Macro UserForm DesignerStorage de la plantilla al libro de trabajo de destino**

Consulte el siguiente código de ejemplo. Copia el proyecto VBA del[plantilla de archivo de Excel](50528345.xlsm) en un libro de trabajo vacío y lo guarda como el[archivo de salida de Excel](50528346.xlsm). Si abre el proyecto de VBA dentro del archivo de plantilla de Excel, verá un formulario de usuario como se muestra a continuación. El formulario de usuario consta de Designer Storage, por lo que se copiará utilizando[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)y[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)métodos.

**![todo:image_alt_text](copiar-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La siguiente captura de pantalla muestra el archivo de salida de Excel y su contenido, que se copiaron del archivo de plantilla de Excel. Cuando hace clic en el botón 1, se abre el formulario de usuario de VBA, que a su vez tiene un botón de comando que muestra un cuadro de mensaje al hacer clic.

**![todo:image_alt_text](copiar-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
