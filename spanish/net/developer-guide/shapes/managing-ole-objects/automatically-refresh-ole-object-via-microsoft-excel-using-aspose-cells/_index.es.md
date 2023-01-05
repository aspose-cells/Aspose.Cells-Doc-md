---
title: Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells
type: docs
weight: 270
url: /es/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona el[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) propiedad para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Debido a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.

{{% /alert %}}

 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Word Microsoft, pero el archivo de muestra de Excel muestra la imagen del animal en lugar de la imagen de Word Microsoft. Pero si abres el[archivo de salida de Excel](5115225.xlsx), verá Microsoft Excel muestra la imagen OLE correcta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
