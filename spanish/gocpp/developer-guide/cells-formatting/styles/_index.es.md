---
title: Obtener y establecer el estilo en celdas con Golang a través de C++
linktitle: Estilos
type: docs
weight: 50
url: /es/go-cpp/styling-and-data-formatting/
description: Descubra cómo realizar formato y estilo de datos en Aspose.Cells for C++, incluyendo formato de texto, formato de números, formato de fechas y otras opciones de estilo. Nuestra guía le ayudará a crear hojas de cálculo con apariencia profesional y formato atractivo.
keywords: Aspose.Cells for C++, formato de datos, estilo, formato de texto, formato de números, formato de fechas, opciones de estilo, hojas de cálculo, formato atractivo, aspecto profesional.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ introdujo dos nuevos métodos para formatear celdas: `Cell.GetStyle` y `Cell.SetStyle`. Este artículo examina el enfoque `Cell.GetStyle`/`SetStyle` para ayudarte a decidir qué técnica se adapta mejor a ti.

{{% /alert %}}

## **Formato de celdas**
Hay dos formas de dar formato a una celda, ilustradas a continuación.

### **Usando GetStyle()**
Con el siguiente fragmento de código, se inicia un objeto `Style` para cada celda al formatearla. Si se formatean muchas celdas, se consume una gran cantidad de memoria porque el objeto `Style` es grande. Estos objetos `Style` no serán liberados hasta que se llame al método `Workbook.Save`.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles.go" >}}
### **Usando SetStyle()**
El primer enfoque es fácil y directo, ¿por qué añadimos el segundo enfoque?

Agregamos el segundo enfoque para optimizar el uso de memoria. Después de usar el método `Cell.GetStyle` para obtener un objeto `Style`, modifícalo y usa el método `Cell.SetStyle` para volver a establecerlo en esa celda. Este objeto `Style` no se conservará y el runtime de C++ lo recopilará cuando no se haga referencia a él.

Al llamar al método `Cell.SetStyle`, el objeto `Style` no se guarda para cada celda. En su lugar, comparamos este objeto `Style` con un pool interno de objetos `Style` para ver si puede ser reutilizado. Solo se conservan los objetos `Style` que difieren de los existentes. Esto significa que hay solo unos pocos cientos de objetos `Style` por cada archivo de Excel en lugar de miles. Para cada celda, solo se conserva un índice del pool de objetos `Style`.

**C++**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Styles-1.go" >}}
## **Temas avanzados**
- [Crear objeto de estilo usando la clase CellsFactory](/cells/es/cpp/create-style-object-using-cellsfactory-class/)
- [Modificar un estilo existente](/cells/es/cpp/modify-an-existing-style/)
- [Reutilización de objetos de estilo](/cells/es/cpp/reusing-style-objects/)
- [Uso de estilos incorporados](/cells/es/cpp/using-built-in-styles/)
