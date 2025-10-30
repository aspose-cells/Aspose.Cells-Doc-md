---
title: Obtener y establecer estilo para celdas
description: Descubre cómo realizar el formateo y estilo de datos en Aspose.Cells for JavaScript mediante C++, incluyendo formateo de texto, formateo numérico, formateo de fechas y otras opciones de estilo. Nuestra guía te ayudará a crear hojas de cálculo con aspecto profesional y formato atractivo.
keywords: Aspose.Cells for JavaScript mediante C++, formateo de datos, estilo, formateo de texto, formateo numérico, formateo de fechas, opciones de estilo, hojas de cálculo, formato atractivo, aspecto profesional.
linktitle: Estilos
type: docs
weight: 50
url: /es/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

 Aspose.Cells for JavaScript mediante C++ introdujo dos métodos nuevos para formatear celdas: Cell.style y Cell.style. Este artículo examina el enfoque Cell.style/style para ayudarte a decidir qué técnica se adapta mejor a ti.

{{% /alert %}} 
## **Formato de celdas**
Hay dos formas de dar formato a una celda, ilustradas a continuación.
### **Uso del estilo**
Con el siguiente fragmento de código, se inicia un objeto Style para cada celda al formatearla. Si se formatean muchas celdas, se consume mucha memoria porque el objeto Style es grande. Estos objetos Style no se liberarán hasta que se llame al método Workbook.save.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Uso del estilo**
El primer enfoque es fácil y directo, ¿entonces por qué añadimos el segundo enfoque?

Agregamos el segundo método para optimizar el uso de memoria. Después de usar la propiedad Cell.style para recuperar un objeto Style, modifícalo y asígnalo de nuevo usando la propiedad Cell.style a esta celda. Este objeto Style no se conservará y el recolector de basura de JavaScript lo recogerá cuando ya no se consulte.

Al asignar la propiedad Cell.style, el objeto Style no se guarda para cada celda. En cambio, comparamos este objeto Style con un grupo interno de objetos Style para ver si puede ser reutilizado. Solo los objetos Style que difieren de los existentes se mantienen para cada objeto Workbook. Esto significa que hay solo unos pocos cientos de objetos Style en cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice al grupo de objetos Style.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/javascript-cpp/modify-an-existing-style/)
- [Reutilización de objetos de estilo](/cells/es/javascript-cpp/reusing-style-objects/)
- [Uso de estilos incorporados](/cells/es/javascript-cpp/using-built-in-styles/)
