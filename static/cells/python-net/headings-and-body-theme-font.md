##Headings And Body Theme Font
Aspose.Cells is a Python library for working with spreadsheet files. It supports setting heading and body theme fonts in Excel documents, enabling users to customize the appearance and style of the document. This article will introduce how to use the Aspose.Cells for Python via .NET library to work with heading and body theme fonts in Excel documents.
The default font will automatically change when the regoin setting is changed.
If the default font is changed, the row height and column width is also changed, and it may even mess up the page layout.
What caused the default font to change?
If Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.
## **Headings And Body Theme Font In Excel**
In Excel, select Home tab, click on the font dropdown box ,you will see "Theme Fonts" with two theme fonts : Calibri Light (Headings) and Calibri (Body) on the top with English region setting.
If Theme Font is selected, the font name will display different in different regions .
If you do not want that the font is automitally changed in different regions, don't select the two Theme Fonts .
## **Changing Headings And Body Font Programally**
With Aspose.Cells for Python via .NET , we can check whether the default font is theme font or set theme font with  [**Font.scheme_type**](https://reference.aspose.com/cells/python-net/aspose.cells/font/scheme_type) property.
The following sample code shows how to manipulate theme font.
## **Dynamically Gets Local Theme Font Programally**
Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?
We have to set the system regional settings before loading the file with [**LoadOptions.region**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/region) property
The following sample code shows how to get local theme font.
