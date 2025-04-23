---
title: Copiar Formas entre Hojas de Cálculo en Aspose.Cells
type: docs
weight: 30
url: /es/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

A veces, necesitas copiar elementos en una hoja de cálculo, como imágenes, gráficos y otros objetos de dibujo, entre hojas de cálculo. Aspose.Cells admite esta característica. Los gráficos, imágenes y otros objetos se pueden copiar con el más alto grado de precisión.

Este artículo te brinda una comprensión detallada de cómo copiar formas entre hojas de cálculo. Para ilustrar, crea una aplicación de consola en Visual Studio.Net, copia imágenes, gráficos y otros objetos de dibujo entre hojas de cálculo utilizando Aspose.Cells.

{{% /alert %}} 

A continuación se muestra el código para copiar un gráfico de una hoja de cálculo a otra

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Nota:** Para obtener más detalles sobre cómo copiar múltiples formas, debes visitar [aquí](/cells/es/net/copy-shapes-between-worksheets/)
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Descargar Ejemplo en Ejecución**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
