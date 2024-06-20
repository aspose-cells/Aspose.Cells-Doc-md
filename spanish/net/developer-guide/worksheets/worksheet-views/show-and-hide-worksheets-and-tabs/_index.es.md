---
title: Mostrar y Ocultar Hojas de Cálculo y Pestañas
type: docs
weight: 10
url: /es/net/show-and-hide-worksheets-and-tabs/
description: Este artículo proporciona un código de muestra para utilizar la API de C# o la Biblioteca .NET para mostrar y ocultar de forma programática una hoja de cálculo de Excel. Además, cómo mostrar y ocultar las pestañas de libro de trabajo de Excel.
---

{{% alert color="primary" %}}

Aspose.Cells permite al usuario mostrar y ocultar elementos de un libro de trabajo, incluidas las hojas de cálculo y las pestañas.

{{% /alert %}}

## **Mostrar y ocultar una hoja de cálculo**

Un archivo de Excel puede tener una o más hojas de cálculo. Siempre que creamos un archivo de Excel, agregamos hojas de cálculo al archivo de Excel en el que trabajamos. Cada hoja de cálculo en un archivo de Excel es independiente de las demás hojas de cálculo al tener sus propios datos, configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de cálculo y mostrar otras en el archivo de Excel por su propio interés. Entonces, **Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de cálculo en sus archivos de Excel.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para controlar la visibilidad de una hoja de cálculo, utilice la propiedad [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

### **Hacer visible una hoja de cálculo**

Hacer visible una hoja de trabajo estableciendo la propiedad [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **true**

### **Ocultar una hoja de trabajo**

Oculta una hoja de cálculo estableciendo la propiedad [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) a **false**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Mostrar y Ocultar Pestañas**

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:

- Pestañas de hojas.
- Botones de desplazamiento de pestañas.

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.

Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de hojas y los botones de desplazamiento en archivos de Excel.

Aspose.Cells ofrece una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar la propiedad [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

### **Hacer pestañas visibles**

Haz visibles las pestañas con la propiedad [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) a **true**.

### **Ocultar pestañas**

Oculta las pestañas en un archivo de Excel estableciendo la propiedad [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) a false.

A continuación, se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls. Después de la ejecución del código, verás que las pestañas del libro están ocultas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Controlando el Ancho de la Barra de Pestañas**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
