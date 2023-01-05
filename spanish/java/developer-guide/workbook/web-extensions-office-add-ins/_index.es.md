---
title: "Extensiones web: complementos de Office"
type: docs
weight: 120
url: /es/java/web-extensions-office-add-ins/
---
Las extensiones web amplían las aplicaciones de Office e interactúan con el contenido de los documentos de Office. Web Extensions agrega funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también ofrece la posibilidad de trabajar con Web Extensions.

## **Agregar extensión web**

Puede agregar extensiones web (complementos de Office) en Excel haciendo clic en el**Insertar**pestaña y luego haciendo clic en el**Almacenar**/**Obtener complementos**Enlace. En el cuadro Complementos, busque el complemento que desee y agréguelo.

Aspose.Cells también proporciona la función para agregar Web Extensions mediante las clases WebExtension y WebExtensionTaskPane. El siguiente ejemplo de código demuestra el uso de las clases WebExtension y WebExtensionTaskPane para agregar una extensión web a un archivo de Excel. Por favor vea el[archivo de salida de Excel](AddWebExtension_Out.xlsx)generado por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Acceder a la información de la extensión web**

Aspose.Cells brinda la posibilidad de acceder a la información de Web Extensions en un archivo de Excel. El siguiente ejemplo de código demuestra cómo acceder a la información de la extensión web cargando el[ejemplo de archivo de Excel](WebExtensionsSample.xlsx). Consulte la salida de la consola generada por el código como referencia.

### **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

### **Salida de consola**

Ancho: 350

EsVisible: Verdadero

Está bloqueado: falso

DockState: derecho

Nombre de la tienda: es-ES

Tipo de tienda: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
