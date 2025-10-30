---
title: Extensiones web  Complementos de Office con Golang vía C++
linktitle: Extensiones Web  Complementos de Office
type: docs
weight: 130
url: /es/go-cpp/web-extensions-office-add-ins/
description: Aprende cómo agregar y acceder a extensiones web (Complementos de Office) en archivos de Excel usando Aspose.Cells con Golang vía C++
---

Las Extensiones web amplían las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las Extensiones web agregan funcionalidad adicional a los clientes de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puedes agregar Extensiones Web (Complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En la caja de Complementos, busca el complemento que deseas y agrégalo.

Aspose.Cells también ofrece la función de agregar Extensiones Web utilizando las clases [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). La siguiente muestra de código demuestra cómo usar las clases [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) para agregar una extensión web a un archivo Excel. Consulta el [archivo Excel de salida](89849869.xlsx) generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Acceder a la Información de la Extensión Web**

Aspose.Cells permite acceder a la información de las Extensiones Web en un archivo Excel. La siguiente muestra de código demuestra cómo acceder a la información de la extensión web cargando el [archivo Excel de ejemplo](89849870.xlsx). Consulta la salida de la consola generada por el código.

### **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
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
