---
title: Obtener y establecer estilo para celdas
description: Descubre cómo realizar formateo de datos y estilos en Aspose.Cells para Python via .NET, incluyendo formateo de texto, formateo numérico, formateo de fechas y otras opciones de estilo. Nuestra guía te ayudará a crear hojas de cálculo con aspecto profesional y formato atractivo.
keywords: Aspose.Cells para Python via .NET, formateo de datos, estilos, formateo de texto, formateo numérico, formateo de fechas, opciones de estilo, hojas de cálculo, formato atractivo, aspecto profesional.
linktitle: Estilos
type: docs
weight: 50
url: /es/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells para Python via .NET introdujo dos nuevos métodos para formatear celdas: Cell.GetStyle y Cell.SetStyle. Este artículo examina el enfoque de Cell.GetStyle/SetStyle para ayudarte a determinar qué técnica se adapta mejor a ti.

{{% /alert %}} 

## **Formato de celdas**
Hay dos formas de dar formato a una celda, ilustradas a continuación.

### **Usando GetStyle()**
Con el siguiente fragmento de código, se inicia un objeto Style para cada celda al dar formato. Si se están formateando muchas celdas, se consume una gran cantidad de memoria porque el objeto Style es grande. Estos objetos Style no se liberarán hasta que se llame al método Workbook.Save.


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **Usando SetStyle()**
El primer enfoque es fácil y directo, ¿entonces por qué añadimos el segundo enfoque?

Añadimos el segundo enfoque para optimizar el uso de memoria. Después de usar el método Cell.GetStyle para obtener un objeto Style, se modifica y se utiliza el método Cell.SetStyle para establecerlo de nuevo en esta celda. Este objeto Style no se conservará y .NET lo recolectará cuando no esté referenciado.

Al llamar al método Cell.SetStyle, el objeto Style no se guarda para cada celda. En su lugar, comparamos este objeto Style con una piscina interna de objetos Style para ver si se puede reutilizar. Solo se conservan los objetos Style que difieren de los existentes para cada objeto Workbook. Esto significa que solo hay varios cientos de objetos Style para cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice a la piscina de objetos Style.



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/python-net/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/python-net/modify-an-existing-style/)
- [Reutilización de objetos de estilo](/cells/es/python-net/reusing-style-objects/)
- [Uso de estilos incorporados](/cells/es/python-net/using-built-in-styles/)


{{< app/cells/assistant language="python-net" >}}
