---
title: Acceder y Actualizar las Partes de Texto Enriquecido de la Celda
linktitle: Texto con Formato Enriquecido
type: docs
weight: 440
url: /es/java/access-and-update-the-portions-of-rich-text-of-cell/
---

{{% alert color="primary" %}} 

Aspose.Cells te permite acceder y actualizar las porciones de texto con formato rico en una celda. Para este propósito, puedes usar los métodos Cell.getCharacters() y Cell.setCharacters(). Estos métodos devolverán y aceptarán un arreglo de objetos FontSetting que puedes usar para acceder y actualizar varias propiedades de la fuente como el nombre de la fuente, color de la fuente, negrita, etc.

{{% /alert %}} 
## **Acceder y actualizar partes de texto enriquecido de la celda**
El siguiente código demuestra el uso de los métodos Cell.getCharacters() y Cell.setCharacters() utilizando el [archivo excel fuente](5472937.xlsx) que puedes descargar desde el enlace proporcionado. El archivo excel fuente tiene un texto con formato rico en la celda A1. Tiene 3 porciones y cada porción tiene una fuente diferente. Accederemos a estas porciones y actualizaremos la primera porción con un nuevo nombre de fuente. Finalmente guarda el libro como [archivo excel de salida](5472930.xlsx). Cuando lo abras, verás que la fuente de la primera porción del texto ha cambiado a **"Arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Salida de la consola**
Aquí está la salida en consola del código de ejemplo anterior usando el [archivo excel fuente](5472937.xlsx).

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
{{< app/cells/assistant language="java" >}}
