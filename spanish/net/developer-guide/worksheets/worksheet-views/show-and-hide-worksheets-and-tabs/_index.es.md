---
title: Mostrar y ocultar hojas de trabajo y pestañas
type: docs
weight: 10
url: /es/net/show-and-hide-worksheets-and-tabs/
description: Este artículo proporciona un código de muestra para usar la biblioteca C# API o .NET para mostrar y ocultar una hoja de cálculo de Excel mediante programación. Además, cómo mostrar y ocultar las pestañas del libro de Excel.
---
{{% alert color="primary" %}}

Aspose.Cells permite al usuario mostrar y ocultar elementos de un libro de trabajo, incluidas hojas de trabajo y pestañas.

{{% /alert %}}

## **Mostrar y ocultar una hoja de trabajo**

 Un archivo de Excel puede tener una o más hojas de trabajo. Cada vez que creamos un archivo de Excel, agregamos hojas de trabajo al archivo de Excel en el que trabajamos. Cada hoja de trabajo en un archivo de Excel es independiente de la otra hoja de trabajo al tener sus propios datos y configuraciones de formato, etc. A veces, los desarrolladores pueden necesitar ocultar algunas hojas de trabajo y otras visibles en el archivo de Excel para su propio interés. Asi que,**Aspose.Cells** permite a los desarrolladores controlar la visibilidad de las hojas de trabajo en sus archivos de Excel.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)colección que permite el acceso a cada hoja de trabajo en el archivo de Excel.

 Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase. Él[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La clase proporciona una amplia gama de propiedades y métodos para administrar hojas de trabajo. Para controlar la visibilidad de una hoja de trabajo, use el[**Es visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propiedad de la[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase.[**Es visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso** valor.

### **Hacer una hoja de trabajo visible**

 Haga que una hoja de trabajo sea visible configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Es visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propiedad a**verdadero**

### **Ocultar una hoja de trabajo**

Oculte una hoja de trabajo configurando el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Es visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propiedad a**falso**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Mostrar y ocultar pestañas**

Si observa detenidamente la parte inferior de un archivo de Excel Microsoft, verá una serie de controles. Éstas incluyen:

- Pestañas de hoja.
- Botones de desplazamiento de pestañas.

Las pestañas de hoja representan las hojas de trabajo en el archivo de Excel. Haga clic en cualquier pestaña para cambiar a esa hoja de trabajo. Cuantas más hojas de trabajo haya en el libro de trabajo, más pestañas de hojas habrá. Si el archivo de Excel tiene una buena cantidad de hojas de trabajo, necesita botones para navegar por ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de las hojas.

Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de las hojas y los botones de desplazamiento de las pestañas en los archivos de Excel.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las pestañas en un archivo de Excel, los desarrolladores pueden usar el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) propiedad.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) es una propiedad booleana, lo que significa que solo puede almacenar una**verdadero** o**falso** valor.

### **Hacer pestañas visibles**

 Haz que las pestañas sean visibles con el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) propiedad a**verdadero**.

### **Ocultar pestañas**

 Ocultar pestañas en un archivo de Excel configurando el[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) clase'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)propiedad a falso.

A continuación se muestra un ejemplo completo que abre un archivo de Excel (libro1.xls), oculta sus pestañas y guarda el archivo modificado como salida.xls. Después de la ejecución del código, verá que las pestañas del libro de trabajo están ocultas.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Controlar el ancho de la barra de pestañas**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
