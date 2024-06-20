---
title: Extensiones Web  Complementos de Office
type: docs
weight: 120
url: /es/java/web-extensions-office-add-ins/
---

Las extensiones web extienden las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las extensiones web añaden funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puede agregar Extensiones Web (Complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego haciendo clic en el enlace **Tienda**/**Obtener complementos**. En el cuadro de complementos, busque el que desea y agréguelo.

Aspose.Cells también proporciona la función de agregar Extensiones Web mediante las clases WebExtension y WebExtensionTaskPane. El siguiente ejemplo de código demuestra el uso de WebExtension y WebExtensionTaskPane para agregar una extensión web a un archivo de Excel. Consulte el [archivo de Excel de salida](AddWebExtension_Out.xlsx) generado por el código para referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Acceder a la Información de la Extensión Web**

Aspose.Cells proporciona la capacidad de acceder a la información de las Extensiones Web en un archivo de Excel. El siguiente ejemplo de código demuestra cómo acceder a la información de la extensión web cargando el [archivo de Excel de ejemplo](WebExtensionsSample.xlsx). Consulte la salida de la consola generada por el código para referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **Salida de la consola**

{{< highlight java >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
