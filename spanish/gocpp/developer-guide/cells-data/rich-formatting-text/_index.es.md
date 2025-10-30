---
title: Acceder y actualizar las porciones de texto enriquecido de una celda con Golang a través de C++
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprende cómo acceder y actualizar las porciones del texto enriquecido de la celda a través de la API Aspose.Cells for C++.
keywords: Acceder y Actualizar Texto Enriquecido de la Celda, Obtener Texto Enriquecido de la Celda, Editar Texto Enriquecido de la Celda, Acceder a Texto Enriquecido de la Celda, Actualizar Texto Enriquecido de la Celda, Cambiar Texto Enriquecido de la Celda
---

{{% alert color="primary" %}}

Aspose.Cells te permite acceder y actualizar las porciones de texto enriquecido de la celda. Para este propósito, puedes usar los métodos [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) y [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Estos métodos devolverán y aceptarán el arreglo de objetos [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), que puedes usar para acceder y actualizar varias propiedades de fuente como el nombre de la fuente, color de la fuente, negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso de los métodos [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) y [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) usando el [archivo de Excel fuente](5112369.xlsx). El archivo de Excel fuente tiene un texto enriquecido en la celda A1 con 3 porciones, cada una con una fuente diferente. El código accede a estas porciones y actualiza la fuente de la primera porción a **"Arial"**. El libro modificado se guarda como [archivo de Excel de salida](5112366.xlsx).

### Código C++ para acceder y actualizar las porciones del texto enriquecido

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### Salida de consola generada por el código de ejemplo

Aquí está la salida de la consola al usar el [archivo de Excel fuente](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
