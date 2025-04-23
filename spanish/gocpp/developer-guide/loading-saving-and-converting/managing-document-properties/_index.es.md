---
title: Gestión de Propiedades del Documento
type: docs
weight: 30
url: /es/go-cpp/managing-document-properties/
---

## **Escenario de Uso Posible**

Aspose.Cells te permite trabajar con Propiedades de Documentos Integradas y Personalizadas. Aquí tienes la interfaz de Microsoft Excel para abrir estas *Propiedades de Documento*. Simplemente haz clic en *Propiedades Avanzadas* como se muestra en esta captura de pantalla y míralas.

![todo:image_alt_text](managing-document-properties_1.png)

## **Gestionando Propiedades del Documento**

El siguiente código de ejemplo carga [archivo de Excel de muestra](23166989.xlsx) y lee las propiedades integradas del documento, e.g., *Título y Asunto*, y luego las cambia. Luego, también lee la propiedad personalizada del documento, es decir, *MyCustom1*, y luego agrega una nueva propiedad personalizada del documento, e.g., *MyCustom5*, y escribe el [archivo de Excel de salida](23166986.xlsx). La siguiente captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de muestra.

![todo:image_alt_text](managing-document-properties_2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **Salida de la consola**

Esta es la salida de consola del código de ejemplo anterior cuando se ejecuta con el archivo de Excel de muestra proporcionado [23166989.xlsx](https://reference.aspose.com/cells/).

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
