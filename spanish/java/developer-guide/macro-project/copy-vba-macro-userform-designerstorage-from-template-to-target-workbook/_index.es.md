---
title: Copiar el Diseñador de Almacenamiento de Macros VBA de la Plantilla al Libro de Trabajo Destino
type: docs
weight: 60
url: /es/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Escenarios de uso posibles**

Aspose.Cells le permite copiar el proyecto VBA de un archivo de Excel a otro archivo de Excel. El proyecto VBA consta de varios tipos de módulos, es decir, Documento, Procedural, Diseñador, etc. Todos los módulos se pueden copiar con un código simple, pero para el módulo Diseñador, hay algunos datos adicionales denominados Almacenamiento del Diseñador que deben ser accedidos o copiados. Los siguientes dos métodos se ocupan del Almacenamiento del Diseñador.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino**

Consulte el siguiente código de ejemplo. Copia el proyecto VBA del [archivo de Excel de plantilla](50528367.xlsm) a un libro de trabajo vacío y lo guarda como el [archivo de Excel de salida](50528366.xlsm). Si abre el proyecto VBA dentro del archivo de Excel de plantilla, verá un cuadro de usuario como se muestra a continuación. El formulario de usuario consta de Almacenamiento del Diseñador, por lo que se copiará utilizando los métodos [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) y [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])).

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

La siguiente captura de pantalla muestra el archivo de Excel de salida y su contenido que se copiaron del archivo de Excel de plantilla. Cuando hace clic en el Botón 1, se abre el Formulario de usuario VBA que a su vez tiene un botón de comando que muestra un cuadro de mensajes al hacer clic.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
