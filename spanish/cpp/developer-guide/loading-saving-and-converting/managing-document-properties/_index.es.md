---
title: Gestión de Propiedades del Documento
type: docs
weight: 30
url: /es/cpp/managing-document-properties/
---

## **Escenario de Uso Posible**
Aspose.Cells te permite trabajar con Propiedades de Documentos Integradas y Personalizadas. Aquí tienes la interfaz de Microsoft Excel para abrir estas *Propiedades de Documento*. Simplemente haz clic en *Propiedades Avanzadas* como se muestra en esta captura de pantalla y míralas.

![todo:image_alt_text](managing-document-properties_1.png)
## **Gestionando Propiedades del Documento**
El siguiente código de muestra carga el [archivo de Excel de muestra](23166989.xlsx) y lee las propiedades de documento integradas como *Título, Asunto* y luego las cambia. Luego, también lee la propiedad de documento personalizada es decir *MyCustom1* y luego agrega una nueva propiedad de documento personalizada es decir *MyCustom5* y escribe el [archivo de Excel de salida](23166986.xlsx). La siguiente captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra.

![todo:image_alt_text](managing-document-properties_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Salida de la consola**
Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](23166989.xlsx).

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
