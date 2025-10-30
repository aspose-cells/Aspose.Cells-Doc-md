---
title: Copiar el Diseñador de Almacenamiento de Macros VBA de la Plantilla al Libro de Trabajo Destino
type: docs
weight: 130
url: /es/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET te permite copiar un proyecto VBA de un archivo de Excel a otro. El proyecto VBA consiste en varios tipos de módulos, es decir, Documento, Procedimental, Diseñador, etc. Todos los módulos se pueden copiar con un código simple, pero para el módulo Diseñador, hay datos adicionales llamados Almacenamiento del Diseñador que necesitan ser accedidos o copiados. Los siguientes dos métodos tratan con el Almacenamiento del Diseñador.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino**

Por favor ve el siguiente código de muestra. Copia el proyecto VBA del [archivo de Excel de plantilla](50528345.xlsm) en un libro vacío y lo guarda como el [archivo de Excel de salida](50528346.xlsm). Si abres el proyecto VBA dentro del archivo de Excel de plantilla, verás un Formulario de Usuario como se muestra a continuación. El Formulario de Usuario consta de Almacenamiento de Diseñador, así que se copiará usando los métodos [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) y [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

La siguiente captura de pantalla muestra el archivo de Excel de salida y sus contenidos que fueron copiados del archivo de Excel de plantilla. Cuando haces clic en el Botón 1, se abre el Formulario de Usuario de VBA que a su vez tiene un botón de comando que muestra un cuadro de mensaje al hacer clic.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}

{{< app/cells/assistant language="python-net" >}}
