##Export similar Border Style when Border Style is not supported by Web Browsers
## **Possible Usage Scenarios**
Microsoft Excel supports some type of dashed borders which are not supported by Web Browsers. When you convert such an Excel file into HTML using Aspose.Cells for Python via .NET, such borders are removed. However, Aspose.Cells for Python via .NET can also support to display such borders with [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) property. Please set its value as **true** and the unsupported borders will also be exported to HTML file.
## **Export similar Border Style when Border Style is not supported by Web Browsers**
The following sample code loads the [sample Excel file](64716806.xlsx) that contains some unsupported borders as shown in the following screenshot. The screenshot further illustrates the effect of [**HtmlSaveOptions.export_similar_border_style**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_similar_border_style) property inside the [output HTML](64716804.zip).
![todo:image_alt_text](1.png)
## **Sample Code**
