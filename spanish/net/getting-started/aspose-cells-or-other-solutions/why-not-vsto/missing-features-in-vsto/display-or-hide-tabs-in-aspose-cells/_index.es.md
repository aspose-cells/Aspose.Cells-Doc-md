---
title: Mostrar u ocultar pestañas en Aspose.Cells
type: docs
weight: 80
url: /es/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Si observa detenidamente la parte inferior de un archivo de Excel Microsoft, verá una serie de controles. Éstas incluyen:

- Pestañas de hoja.
- Botones de desplazamiento de pestañas.

Las pestañas de hoja representan las hojas de trabajo en el archivo de Excel. Haga clic en cualquier pestaña para cambiar a esa hoja de trabajo. Cuantas más hojas de trabajo haya en el libro de trabajo, más pestañas de hojas habrá. Si el archivo de Excel tiene una buena cantidad de hojas de trabajo, necesita botones para navegar por ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de las hojas.

**Fichas de hojas y botones de desplazamiento de fichas** 

![todo:imagen_alternativa_texto](display-or-hide-tabs-in-aspose-cells_1.png)

Con Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de las hojas y los botones de desplazamiento de las pestañas en los archivos de Excel.

{{% /alert %}} 

A continuación se muestra un ejemplo completo que abre un archivo de Excel (libro1.xls), oculta sus pestañas y guarda el archivo modificado como salida.xls.

Puede ver que el archivo Book1.xls contiene pestañas en la siguiente figura. Después de ejecutar el código de ejemplo, las pestañas se ocultan, como puede ver en la captura de pantalla del archivo output.xls a continuación.

**book1.xls: archivo de Excel antes de cualquier modificación** 

![todo:imagen_alternativa_texto](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: archivo de Excel después de la modificación** 

![todo:imagen_alternativa_texto](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Controlar el ancho de la barra de pestañas**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
