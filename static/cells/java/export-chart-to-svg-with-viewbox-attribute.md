##Export Chart to SVG with viewBox attribute
By default, when the chart is export to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.setSVGFitToViewPort()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#SVGFitToViewPort) property which when set to **true** exports the chart to SVG with viewBox attribute.
If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.
xmlns:xlink="http://www.w3.org/1999/xlink"
width="100%" height="100%"
viewBox="0 0 480 288">
## Code Snippet
## Related Articles
- [Chart Rendering](https://docs.aspose.com/cells/java/chart-rendering/)
- [Export Worksheet or Chart into Image with Desired Width and Height](https://docs.aspose.com/cells/java/export-worksheet-or-chart-into-image-with-desired-width-and-height/)
