##How to Use Image Markers in Smart Markers
## **Possible Usage Scenarios**
Image markers are specialized placeholders in templating systems (like FoxPro, Handlebars, or modern UI frameworks) that dynamically inject images or visual assets into templates. Sometimes, you need to insert pictures using smart markers. Aspose.Cells makes it possible to add pictures to smart markers.
## **Image Parameters in Smart Markers**
Smart marker parameters for managing images.
- **Picture:FitToCell** - Auto-fit the image to the cell’s row height and column width.
- **Picture:ScaleN** - Scale height and width to N percent.
- **Picture:Width:Nin&Height:Nin** - Render the image N inches high and N inches wide. You can also specify Left and Top positions (in points).
## **How to Use Image Markers in Smart Markers**
Please see the following sample code which shows how to insert pictures using smart markers.
## **How to Use Image Markers while Grouping Data in Smart Markers**
The following sample creates a workbook and then adds the following smart marker tags in cells D2, E2 and F2 respectively.
&=Person.Name(group:normal,skip:1)
&=Person.City
&=Person.Photo(Picture:FitToCell)
Then it fills the data source with data and calls the [WorkbookDesigner.Process()](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) method to process smart marker tags. The code uses these images i.e [moon.png](5115492.png) and [moon2.png](5115491.png) but you can use any image.
