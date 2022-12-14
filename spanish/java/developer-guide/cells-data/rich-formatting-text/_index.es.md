---
title: Acceda y actualice las porciones de texto enriquecido de Cell
linktitle: Texto con formato enriquecido
type: docs
weight: 440
url: /es/java/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}} 

Aspose.Cells le permite acceder y actualizar las partes del texto enriquecido de la celda. Para ello, puede utilizar los métodos Cell.getCharacters() y Cell.setCharacters(). Estos métodos devolverán y aceptarán la matriz de objetos FontSetting que puede usar para acceder y actualizar varias propiedades de la fuente, como el nombre de la fuente, el color de la fuente, la negrita, etc.

{{% /alert %}} 
## **Acceda y actualice las porciones de texto enriquecido de Cell**
 El siguiente código demuestra el uso de los métodos Cell.getCharacters() y Cell.setCharacters() usando el[archivo fuente excel](5472937.xlsx) que puede descargar desde el enlace proporcionado. El archivo fuente de Excel tiene un texto enriquecido en la celda A1. Tiene 3 porciones y cada porción tiene una fuente diferente. Accederemos a estas partes y actualizaremos la primera parte con un nuevo nombre de fuente. Finalmente guarda el libro de trabajo como[archivo de salida de Excel](5472930.xlsx) . Cuando lo abra, encontrará que la fuente de la primera parte del texto ha cambiado a**"arial"**.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AccessAndUpdatePortions-AccessAndUpdatePortions.java" >}}




## **Salida de consola**
 Aquí está la salida de la consola del código de muestra anterior usando el[archivo fuente excel](5472937.xlsx).

{{< highlight "java" >}}

 Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
