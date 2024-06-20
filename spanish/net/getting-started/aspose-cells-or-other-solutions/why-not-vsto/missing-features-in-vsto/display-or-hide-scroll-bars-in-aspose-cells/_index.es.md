---
title: Mostrar u Ocultar Barras de Desplazamiento en Aspose.Cells
type: docs
weight: 70
url: /es/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

Las barras de desplazamiento son muy útiles para navegar por el contenido de cualquier archivo. Normalmente, hay dos tipos de barras de desplazamiento:

- Barras de desplazamiento verticales
- Barras de desplazamiento horizontales

Microsoft Excel también proporciona barras de desplazamiento horizontales y verticales para que los usuarios puedan desplazarse por el contenido de la hoja de cálculo. Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de ambos tipos de barras de desplazamiento en los archivos de Excel.

{{% /alert %}}

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) que representa un archivo de Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) proporciona una amplia gama de propiedades y métodos para gestionar un archivo de Excel. Para controlar la visibilidad de las barras de desplazamiento, utiliza las propiedades [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) de la clase [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings). [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) y [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) son propiedades Booleanas, lo que significa que estas propiedades solo pueden almacenar valores **true** o **false**.

A continuación, se muestra un código completo que abre un archivo de Excel, book1.xls, oculta ambas barras de desplazamiento y luego guarda el archivo modificado como output.xls.

La captura de pantalla siguiente muestra el archivo Book1.xls que contiene ambas barras de desplazamiento. El archivo modificado se guarda como archivo output.xls, también se muestra a continuación.

**Book1.xls: Archivo de Excel antes de cualquier modificación**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: Archivo de Excel después de la modificación**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Descargar Código en Ejecución**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Descargar Código de Ejemplo**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
