---
title: Actualizar automáticamente el objeto OLE a través de Microsoft Excel usando Aspose.Cells
type: docs
weight: 270
url: /es/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Gracias a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.

{{% /alert %}}

El siguiente código de ejemplo carga el [archivo de Excel de muestra](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Microsoft Word pero el archivo de Excel de muestra muestra la imagen de un animal en lugar de la imagen de Microsoft Word. Pero si abre el [archivo de Excel de salida](5115225.xlsx), verá que Microsoft Excel muestra la imagen OLE correcta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
