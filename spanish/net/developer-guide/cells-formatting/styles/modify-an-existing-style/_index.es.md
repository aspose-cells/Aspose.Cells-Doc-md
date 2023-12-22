---
title: Modificar un estilo existente
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo que permite a los usuarios modificar estilos de celda existentes. Este artículo presentará cómo modificar un estilo de celda existente con la biblioteca Aspose.Cells para que los usuarios puedan cambiar la apariencia de las celdas según lo necesiten.
keywords: Modify existing styles, customize the look and feel of your application, guides, tutorials, help documentation, development documentation, API references, sample code, downloads, support.
type: docs
weight: 90
url: /es/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

Para aplicar las mismas opciones de formato a las celdas, cree un nuevo objeto de estilo de formato. Un objeto de estilo de formato es una combinación de características de formato, como fuente, tamaño de fuente, sangría, número, borde, patrones, etc., nombradas y almacenadas como un conjunto. Cuando se aplica, se aplican todos los formatos de ese estilo.

También puede usar un estilo existente, guardarlo con el libro de trabajo y usarlo para formatear información con los mismos atributos.

 Cuando las celdas no tienen formato explícito, el**Normal** Se aplica el estilo (el estilo predeterminado del libro). Microsoft Excel predefine varios estilos además del estilo Normal, incluidos coma, moneda y porcentaje.

Aspose.Cells permite modificar cualquiera de estos estilos o cualquier otro estilo que definas con los atributos deseados.

{{% /alert %}}

##  **Usando Microsoft Excel**

Para actualizar un estilo en Microsoft Excel 97-2003:

1.  Sobre el**Formato** menú, haga clic en *Estilo**.
1.  Seleccione el estilo que desea modificar desde el**Nombre de estilo** lista.
1. Haga clic en *Modificar**.
1. Seleccione las opciones de estilo que desee utilizando las pestañas en el cuadro de diálogo Formato Cells.
1. Haga clic en Aceptar**.
1. En *El estilo incluye**, especifique las características de estilo que desee.
1.  Hacer clic**OK** para guardar el estilo y aplicarlo al rango seleccionado.

##  **Usando Aspose.Cells**

 Los siguientes ejemplos demuestran cómo utilizar[**Estilo.Actualizar**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)método.

###  **Crear y modificar un estilo**

 Este ejemplo crea una[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) objeto, lo aplica a un rango de celdas y modifica el[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style)objeto. Las modificaciones se aplican automáticamente a la celda y al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

###  **Modificar un estilo existente**

Este ejemplo utiliza un archivo de plantilla de Excel simple en el que ya se ha aplicado un estilo llamado Porcentaje a un rango. El ejemplo:

1. obtiene el estilo,
1. crea un objeto de estilo y
1. modifica el formato del estilo.

Las modificaciones se aplican automáticamente al rango al que se aplicó el estilo.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}
