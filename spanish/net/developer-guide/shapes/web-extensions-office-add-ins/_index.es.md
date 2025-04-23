---
title: Extensiones Web  Complementos de Office
type: docs
weight: 130
url: /es/net/web-extensions-office-add-ins/
---

Las extensiones web extienden las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las extensiones web añaden funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puedes agregar extensiones web (complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En el cuadro de complementos, busca el complemento que desees y añádelo.

Aspose.Cells también proporciona la función de agregar extensiones web mediante las clases [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane). El siguiente código de ejemplo demuestra el uso de las clases [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) para agregar una extensión web al archivo de Excel. Consulta el [archivo de Excel de salida](89849869.xlsx) generado por el código para más detalles.

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Acceder a la Información de la Extensión Web**

Aspose.Cells proporciona la capacidad de acceder a la información de las extensiones web en un archivo de Excel. El siguiente código de ejemplo demuestra cómo acceder a la información de la extensión web cargando el [archivo de Excel de ejemplo](89849870.xlsx). Consulta la salida de la consola generada por el código para más detalles.

### **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
{{< app/cells/assistant language="csharp" >}}
