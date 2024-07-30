---
title: Mostrar y Ocultar Hojas de Cálculo y Pestañas
type: docs
weight: 10
url: /es/python-net/show-and-hide-worksheets-and-tabs/
description: Este artículo proporciona un código de muestra para usar la API de Aspose.Cells para Python via .NET para mostrar y ocultar programáticamente una hoja de cálculo de Excel. Además, cómo mostrar y ocultar las pestañas del libro de Excel.
keywords: Biblioteca de Excel de Python, Mostrar y Ocultar una Hoja de Cálculo de Python, Mostrar y Ocultar Pestañas de Python, Controlar el Ancho de la Barra de Pestañas de Python.
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET permite al usuario mostrar y ocultar elementos de un libro de trabajo incluidas hojas de cálculo y pestañas.

{{% /alert %}}

## **Mostrar y ocultar una hoja de cálculo**

Un archivo de Excel puede tener una o más hojas de cálculo. Siempre que creamos un archivo de Excel, agregamos hojas de cálculo al archivo de Excel en el que trabajamos. Cada hoja de cálculo en un archivo de Excel es independiente de la otra hoja de cálculo al tener sus propios datos y configuraciones de formato, etc. A veces, los desarrolladores pueden requerir ocultar algunas hojas de cálculo y mostrar otras en el archivo de Excel por su propio interés. Por lo tanto, **Aspose.Cells para Python via .NET** permite a los desarrolladores controlar la visibilidad de las hojas de cálculo en sus archivos de Excel.

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) colección que permite acceder a cada hoja de cálculo en el archivo de Excel.

Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona una amplia gama de propiedades y métodos para gestionar hojas de cálculo. Para controlar la visibilidad de una hoja de cálculo, utilice la propiedad [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

### **Hacer visible una hoja de cálculo**

Hacer visible una hoja de trabajo estableciendo la propiedad [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **true**

### **Ocultar una hoja de trabajo**

Oculta una hoja de cálculo estableciendo la propiedad [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) a **false**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Mostrar y Ocultar Pestañas**

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:

- Pestañas de hojas.
- Botones de desplazamiento de pestañas.

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.

Usando Aspose.Cells para Python via .NET, los desarrolladores pueden controlar la visibilidad de las fichas de hoja y los botones de desplazamiento de las fichas en los archivos de Excel.

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar la propiedad [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) es una propiedad booleana, lo que significa que solo puede almacenar un valor **true** o **false**.

### **Hacer pestañas visibles**

Haz visibles las pestañas con la propiedad [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) a **true**.

### **Ocultar pestañas**

Oculta las pestañas en un archivo de Excel estableciendo la propiedad [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) a false.

A continuación, se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls. Después de la ejecución del código, verás que las pestañas del libro están ocultas.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Controlando el Ancho de la Barra de Pestañas**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
