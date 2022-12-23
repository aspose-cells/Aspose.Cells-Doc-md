---
title: Modificar un estilo existente
type: docs
weight: 90
url: /es/net/modify-an-existing-style/
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

 Los siguientes ejemplos muestran cómo usar[**Estilo.Actualizar**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)método.

### **Crear y modificar un estilo**

 Este ejemplo crea un[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto, lo aplica a un rango de celdas y modifica el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto. Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **Modificación de un estilo existente**

Este ejemplo utiliza un archivo de Excel de plantilla simple en el que ya se ha aplicado un estilo denominado Porcentaje a un rango. El ejemplo:

1. consigue el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
