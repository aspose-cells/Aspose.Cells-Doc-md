---
title: Mostrar u ocultar barras de desplazamiento en Aspose.Cells
type: docs
weight: 70
url: /es/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Las barras de desplazamiento son muy utilizadas para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de trabajo. Usando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en archivos de Excel.

{{% /alert %}}

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook)que representa un archivo de Excel. Él[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) La clase proporciona una amplia gama de propiedades y métodos para administrar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, utilice el[**Configuración del libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) clase'[**EsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) propiedades.[**EsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) son propiedades booleanas, lo que significa que estas propiedades solo pueden almacenar**verdadero** o**falso** valores.

A continuación se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.

La siguiente captura de pantalla muestra el archivo Book1.xls que contiene ambas barras de desplazamiento. El archivo modificado se guarda como archivo de salida.xls, también se muestra a continuación.

**Book1.xls: archivo de Excel antes de cualquier modificación**

![todo:imagen_alternativa_texto](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: archivo de Excel después de la modificación**

![todo:imagen_alternativa_texto](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Descargar código de ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Descargar código de muestra**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
