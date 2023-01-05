---
title: Modificar un estilo existente
type: docs
weight: 50
url: /es/java/modify-an-existing-style/
description: Aprende a cambiar estilos en Excel con Microsoft Excel y con Aspose.Cells for Java API.
keywords: modify an existing style excel, modify an existing style excel java, modify existing style excel, modify existing style excel java, change existing style in excel, change existing style in excel java, how to change style in excel, how to change style in excel with java, how to change style in excel with java, how to change style in excel using java, changing existing style in excel java, changing existing style in excel
---
{{% alert color="primary" %}}

Para aplicar las mismas opciones de formato a las celdas, cree un nuevo objeto de estilo de formato. Un objeto de estilo de formato es una combinación de características de formato, como fuente, tamaño de fuente, sangría, número, borde, patrones, etc., nombradas y almacenadas como un conjunto. Cuando se aplica, se aplica todo el formato de ese estilo.

También puede usar un estilo existente, guardarlo con el libro de trabajo y usarlo para dar formato a la información con los mismos atributos.

 Cuando las celdas no tienen un formato explícito, el**Normal** se aplica el estilo (el estilo predeterminado del libro). Microsoft Excel predefine varios estilos además del estilo Normal, incluidos Coma, Moneda y Porcentaje.

Aspose.Cells permite modificar cualquiera de estos estilos o cualquier otro estilo que defina con sus atributos deseados.

{{% /alert %}}

## **Usando Microsoft Excel**

Para actualizar un estilo en Microsoft Excel 97-2003:

1.  Sobre el**Formato** menú, haga clic**Estilo**.
1.  Seleccione el estilo que desea modificar de la**Nombre de estilo** lista.
1.  Hacer clic**Modificar**.
1. Seleccione las opciones de estilo que desee utilizando las pestañas del cuadro de diálogo Formato Cells.
1.  Hacer clic**DE ACUERDO**.
1.  Bajo**El estilo incluye**, especifique las características de estilo que desee.
1.  Hacer clic**DE ACUERDO** para guardar el estilo y aplicarlo al rango seleccionado.

## **Usando Aspose.Cells**

 Aspose.Cells proporciona el[**Actualización de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) método para actualizar un estilo existente.

 Para cambiar un estilo con nombre, ya sea creado dinámicamente usando Aspose.Cells o predefinido, llame al[**Actualización de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update()) para reflejar cualquier cambio en el estilo aplicado a una celda o rango.

 Él[**Actualización de estilo**](https://reference.aspose.com/cells/java/com.aspose.cells/style#update() ) se comporta como el método**DE ACUERDO** botón en el cuadro de diálogo Estilo: después de realizar cambios en un estilo existente, llame para implementar el cambio. Si ya ha aplicado un estilo a un rango de celdas, modifique los atributos de estilo y llame al método, el formato de esas celdas se actualiza automáticamente

### **Crear y modificar un estilo**

Este ejemplo crea un objeto de estilo, lo aplica a un rango de celdas y modifica el objeto de estilo. Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatingStyle-CreatingStyle.java" >}}

### **Modificación de un estilo existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo denominado Porcentaje a un rango. El ejemplo:

1. consigue el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ModifyExistingStyle-ModifyExistingStyle.java" >}}
