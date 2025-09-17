##Headings And Body Theme Font
Aspose.Cells is a Node.js library for working with spreadsheet files. It supports setting heading and body theme fonts in Excel documents, enabling users to customize the appearance and style of the document. This article will introduce how to use the Aspose.Cells library to work with heading and body theme fonts in Excel documents.
The default font will automatically change when the region setting is changed.
If the default font is changed, the row height and column width is also changed, and it may even mess up the page layout.
What caused the default font to change?
If Excel theme font is set, Excel will automatically switch between different fonts based on the current language environment.
## **Headings And Body Theme Font In Excel**
In Excel, select Home tab, click on the font dropdown box, you will see "Theme Fonts" with two theme fonts: Calibri Light (Headings) and Calibri (Body) on the top with English region setting.
If Theme Font is selected, the font name will display differently in different regions. If you do not want the font to automatically change in different regions, don't select the two Theme Fonts.
## **Changing Headings And Body Font Programmatically**
With Aspose.Cells for Node.js via C++, we can check whether the default font is a theme font or set the theme font with [**Font.setSchemeType(FontSchemeType)**](https://reference.aspose.com/cells/nodejs-cpp/font/#setSchemeType-fontschemetype-) method.
The following sample code shows how to manipulate the theme font.
## **Dynamically Gets Local Theme Font Programmatically**
Sometimes, our servers and users' machines are not in the same region. How can we obtain the same font that users want for file processing?
We have to set the system regional settings before loading the file with [**LoadOptions.setRegion(CountryCode)**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#setRegion-countrycode-) method.
The following sample code shows how to get local theme font.
