---
title: Copiar el Diseñador de Almacenamiento de Macros VBA de la Plantilla al Libro de Trabajo Destino
type: docs
weight: 130
url: /es/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells te permite copiar un proyecto VBA de un archivo de Excel a otro archivo de Excel. El proyecto VBA consta de varios tipos de módulos, es decir, Documento, Procedural, Diseñador, etc. Todos los módulos se pueden copiar con un código simple, pero para el módulo Diseñador, hay algunos datos adicionales llamados Almacenamiento de Diseñador que deben ser accedidos o copiados. Los siguientes dos métodos tratan con el Almacenamiento de Diseñador.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino**

Por favor ve el siguiente código de muestra. Copia el proyecto VBA del [archivo de Excel de plantilla](50528345.xlsm) en un libro vacío y lo guarda como el [archivo de Excel de salida](50528346.xlsm). Si abres el proyecto VBA dentro del archivo de Excel de plantilla, verás un Formulario de Usuario como se muestra a continuación. El Formulario de Usuario consta de Almacenamiento de Diseñador, así que se copiará usando los métodos [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) y [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La siguiente captura de pantalla muestra el archivo de Excel de salida y sus contenidos que fueron copiados del archivo de Excel de plantilla. Cuando haces clic en el Botón 1, se abre el Formulario de Usuario de VBA que a su vez tiene un botón de comando que muestra un cuadro de mensaje al hacer clic.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}
