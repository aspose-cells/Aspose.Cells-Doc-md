---
title: Obtener y establecer estilo para celdas
description: Descubre cómo realizar formato de datos y estilos en Aspose.Cells for Node.js via C++, incluyendo formato de texto, formato numérico, formato de fecha y otras opciones de estilo. Nuestra guía te ayudará a crear hojas de cálculo de apariencia profesional con un formato atractivo.
keywords: Aspose.Cells for Node.js via C++, formato de datos, estilo, formato de texto, formato numérico, formato de fecha, opciones de estilo, hojas de cálculo, formato atractivo, de apariencia profesional.
linktitle: Estilos
type: docs
weight: 50
url: /es/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ introdujo dos nuevos métodos para formatear celdas: Cell.getStyle y Cell.setStyle. Este artículo examina el enfoque Cell.getStyle/setStyle para ayudarte a decidir qué técnica se adapta mejor a ti.

{{% /alert %}} 
## **Formato de celdas**
Hay dos formas de dar formato a una celda, ilustradas a continuación.
### **Usando getStyle()**
Con el siguiente fragmento de código, se inicia un objeto Style para cada celda al formatearla. Si se formatean muchas celdas, se consume mucha memoria porque el objeto Style es grande. Estos objetos Style no se liberarán hasta que se llame al método Workbook.save.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **Usando setStyle()**
El primer enfoque es fácil y directo, ¿entonces por qué añadimos el segundo enfoque?

Agregamos el segundo enfoque para optimizar el uso de memoria. Después de usar el método Cell.getStyle para obtener un objeto Style, modifícalo y usa el método Cell.setStyle para devolverlo a esta celda. Este objeto Style no se mantendrá y el recolector de basura de JavaScript lo recopilará cuando no tenga referencias.

Al llamar al método Cell.setStyle, el objeto Style no se guarda para cada celda. En cambio, comparamos este objeto Style con un grupo interno de objetos Style para ver si puede reutilizarse. Solo los objetos Style que difieren de los existentes se mantienen para cada objeto Workbook. Esto significa que hay solo unos pocos cientos de objetos Style para cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice del grupo de objetos Style.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/nodejs-cpp/modify-an-existing-style/)
- [Reutilización de objetos de estilo](/cells/es/nodejs-cpp/reusing-style-objects/)
- [Uso de estilos incorporados](/cells/es/nodejs-cpp/using-built-in-styles/)

