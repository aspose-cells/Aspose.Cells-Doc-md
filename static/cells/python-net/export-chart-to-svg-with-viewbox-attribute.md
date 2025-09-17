##Export Chart to SVG with viewBox attribute
Export Chart to SVG with viewBox attribute by using Aspose.Cells for Python via .NET API.
By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells for Python via .NET provides [**ImageOrPrintOptions.svg_fit_to_view_port**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/svg_fit_to_view_port/) property which when set to **true** exports the chart to SVG with viewBox attribute.
## Export Chart to SVG with viewBox attribute
The following sample code exports the chart to SVG format with the viewBox attribute.
If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.
xmlns:xlink="http://www.w3.org/1999/xlink"
width="100%" height="100%"
viewBox="0 0 480 288">
