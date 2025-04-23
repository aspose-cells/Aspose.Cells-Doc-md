---
title: Mostrar u Ocultar Pestañas en Aspose.Cells
type: docs
weight: 80
url: /es/net/display-or-hide-tabs-in-aspose-cells/
---

{{% alert color="primary" %}} 

Si observas detenidamente en la parte inferior de un archivo de Microsoft Excel, verás una serie de controles. Estos incluyen:

- Pestañas de hojas.
- Botones de desplazamiento de pestañas.

Las pestañas de hojas representan las hojas de cálculo en el archivo de Excel. Haz clic en cualquier pestaña para cambiar a esa hoja de cálculo. Cuantas más hojas de cálculo tenga el libro, más pestañas de hojas habrá. Si el archivo de Excel tiene un buen número de hojas de cálculo, necesitas botones para navegar a través de ellas. Por lo tanto, Microsoft Excel proporciona botones de desplazamiento de pestañas para desplazarse por las pestañas de hojas.

**Pestañas de hojas y botones de desplazamiento de pestañas** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_1.png)

Utilizando Aspose.Cells, los desarrolladores pueden controlar la visibilidad de las pestañas de hojas y los botones de desplazamiento en archivos de Excel. 

{{% /alert %}} 

A continuación se muestra un ejemplo completo que abre un archivo de Excel (book1.xls), oculta sus pestañas y guarda el archivo modificado como output.xls.

Puedes ver que el archivo Book1.xls contiene pestañas en la figura de abajo. Después de ejecutar el código de ejemplo, las pestañas están ocultas, como se puede ver en la captura de pantalla del archivo output.xls de abajo.

**book1.xls: Archivo de Excel antes de cualquier modificación** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls: Archivo de Excel después de la modificación** 

![todo:image_alt_text](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Controlando el Ancho de la Barra de Pestañas**
**C#**

{{< highlight csharp >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
