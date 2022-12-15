---
title: Obtener y establecer estilo para celdas
linktitle: Estilos
type: docs
weight: 50
url: /es/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 introdujo dos nuevos métodos para formatear celdas: Cell.GetStyle y Cell.SetStyle. Este artículo examina el enfoque Cell.GetStyle/SetStyle para ayudarlo a juzgar qué técnica se adapta mejor a sus necesidades.

{{% /alert %}} 
## **Formateo Cells**
Hay dos formas de formatear una celda, ilustradas a continuación.
### **Usando GetStyle()**
Con la siguiente pieza de código, se inicia un objeto Style para cada celda al formatearla. Si se formatea una gran cantidad de celdas, se consume una gran cantidad de memoria porque el objeto Style es un objeto grande. Estos objetos Style no se liberarán hasta que se llame al método Workbook.Save.



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **Usando SetStyle()**
El primer enfoque es fácil y directo, entonces, ¿por qué agregamos el segundo enfoque?

Agregamos el segundo enfoque para optimizar el uso de la memoria. Después de usar el método Cell.GetStyle para recuperar un objeto Style, modifíquelo y use el método Cell.SetStyle para volver a configurarlo en esta celda. Este objeto Style no se conservará y .NET GC lo recopilará cuando no se haga referencia a él.

Al llamar al método Cell.SetStyle, el objeto Style no se guarda para cada celda. En su lugar, comparamos este objeto de estilo con un grupo de objetos de estilo interno para ver si se puede reutilizar. Solo los objetos Style que difieren de los existentes se conservan para cada objeto Workbook. Esto significa que solo hay varios cientos de objetos Style para cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice para el conjunto de objetos de estilo.



**C#**

{{< highlight "csharp" >}}

 Estilo estilo = celda.GetStyle();

estilo.Fuente.IsBold = verdadero;

celda.SetStyle(estilo);


## **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/net/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/net/modify-an-existing-style/)
- [Reutilización de objetos de estilo](/cells/es/net/reusing-style-objects/)
- [Uso de estilos integrados](/cells/es/net/using-built-in-styles/)


