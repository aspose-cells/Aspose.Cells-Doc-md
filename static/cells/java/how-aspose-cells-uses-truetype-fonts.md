##How Aspose.Cells uses TrueType Fonts
Aspose.Cells requires TrueType fonts when rendering spreadsheets to formats such as PDF, XPS and images.
When Aspose.Cells renders a spreadsheet, it requires access to the TrueType fonts used in the spreadsheet. This is a normal practice during PDF, XPS and image generation and ensures the converted document or image appears identical for any viewer.
## **About Fonts**
### **Font Availability and Substitution**
A spreadsheet may be formatted using various fonts such as Arial, Times New Roman, Verdana and others. When Aspose.Cells renders a spreadsheet it attempts to select the fonts that are used in the spreadsheet. However there are situations when the exact font may not be available so Aspose.Cells have to substitute a similar font instead.
Below is the process that Aspose.Cells follow behind the scene.
1. Aspose.Cells tries to find the fonts on the file system matching the exact font name used in the spreadsheet.
1. If Aspose.Cells cannot find fonts with the exact same name, it attempts to use the default font specified under the Workbook's DefaultStyle.Font property.
1. If Aspose.Cells cannot locate the font defined under the workbook's DefaultStyle.Font property, it attempts to select the most suitable fonts from all of the available fonts.
1. Finally, if Aspose.Cells cannot find any fonts on the file system, it renders the spreadsheet using Arial.
### **Where Aspose.Cells Looks for Fonts**
Aspose.Cells attempts to find TrueType fonts on the file system automatically. Most of the time you can rely on Aspose.Cell's default behavior to find TrueType fonts, but sometimes you may need to specify folders that containing the TrueType fonts using the FontConfigs.setFontFolder factory method.
### **Typical Font-Related Problems and Solutions**
This table lists some of the problems that you might encounter when rendering spreadsheets to PDF using Aspose.Cells and their solutions.
Keep in mind when copying any fonts that most fonts are copyrighted. First locate the license of a font before hand and verify they can be freely transferred to another machine.
|**Problem** |**Reason** |**Solution** |
| :- | :- | :- |
|The layout and fonts in the rendered document is different from the original. |You are using Aspose.Cells on Linux or Mac OS where TureType fonts are not present by default so Aspose.Cells cannot locate fonts on your computer. |Copy TrueType font files from a Windows machine or install a TrueType font package. Use the FontConfigs.setFontFolder factory method to specify the location of the font files.|
Check the detailed articles on
- [How to place TrueType fonts on Linux](https://docs.aspose.com/cells/java/how-to-install-truetype-fonts-on-linux/).
- [How to specify TrueType fonts location](https://docs.aspose.com/cells/java/how-to-specify-truetype-fonts-location/).
- [How to get warnings when font substitution occurs](https://docs.aspose.com/cells/java/get-warnings-for-font-substitution-while-rendering-excel-file/)
