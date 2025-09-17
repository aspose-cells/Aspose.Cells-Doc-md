##Export Chart to SVG with viewBox attribute
By default, when the chart is exported to SVG format, the **viewBox** attribute is not included in its XML. However, Aspose.Cells provides [**ImageOrPrintOptions.SVGFitToViewPort**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/svgfittoviewport) property which when set to **true** exports the chart to SVG with viewBox attribute.
## Export Chart to SVG with viewBox attribute
The following sample code exports the chart to SVG format with the viewBox attribute.
If you open the chart's SVG in notepad, you will find the **viewBox** attribute similar to this.
xmlns:xlink="http://www.w3.org/1999/xlink"
width="100%" height="100%"
viewBox="0 0 480 288">
