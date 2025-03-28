---
title: Automatically refresh OLE object via Microsoft Excel using Aspose.Cells
type: docs
weight: 270
url: /net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) property to refresh the OLE object when the excel file is opened in Microsoft Excel. Because of this property, the OLE object will display the correct OLE image generated by Microsoft Excel.

{{% /alert %}}

The following sample code loads the [sample excel file](5115231.xlsx) which has a non-real OLE image. The OLE object is actually a Microsoft Word document but the sample excel file shows the animal image instead of Microsoft Word image. But if you open the [output excel file](5115225.xlsx), you will see Microsoft Excel displays the correct OLE image.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}