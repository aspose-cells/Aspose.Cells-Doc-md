---
title: Extensiones Web  Complementos de Office
type: docs
weight: 130
url: /es/python-net/web-extensions-office-add-ins/
---

Las extensiones web extienden las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las extensiones web añaden funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells para Python via .NET también ofrece la capacidad de trabajar con Extensiones Web.

## **Agregar Extensión Web**

Puedes agregar extensiones web (complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En el cuadro de complementos, busca el complemento que desees y añádelo.

Aspose.Cells para Python via .NET también proporciona la función para agregar Extensiones Web usando las clases [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane). El siguiente ejemplo de código demuestra el uso de las clases [**WebExtension**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/python-net/aspose.cells.webextensions/webextensiontaskpane) para agregar una extensión web al archivo de Excel. Consulte el [archivo Excel de salida](89849869.xlsx) generado por el código para referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AddWebExtension-1.py" >}}

## **Acceder a la Información de la Extensión Web**

Aspose.Cells para Python via .NET permite acceder a la información de las Extensiones Web en el archivo Excel. El siguiente ejemplo de código demuestra cómo acceder a la información de la extensión web cargando el [archivo Excel de muestra](89849870.xlsx). Consulte la salida de la consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-WebExtension-Workbook-AccessWebExtensionInformation-1.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
