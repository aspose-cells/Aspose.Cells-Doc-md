##HTML with C++
Convert Excel to HTML and MHTML format using Aspose.Cells with C++.
## **Converting Excel Workbook to HTML**
The Aspose.Cells API provides support for exporting spreadsheets to HTML format. For this purpose, Aspose.Cells uses the [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) class to provide the flexibility to control several aspects of the output HTML.
The code example below shows how to save a workbook as an HTML file using C++:
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Load your source workbook
Workbook workbook(u"Book1.xlsx");
// Save file to HTML format
workbook.Save(u"out.html");
std::cout << "Workbook saved to HTML format successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Converting Excel Workbook to MHTML Files**
MHTML combines normal HTML with external resources (that is, content that is usually linked in, like images, animations, audio, and so on) into one file. They are used for emails with the .mht file extension. Aspose.Cells supports reading and writing MHTML files.
The code example below shows how to save a workbook as an MHTML file using C++:
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
// Load your source workbook
U16String inputFilePath(u"Book1.xlsx");
std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);
// Save file to mhtml format
U16String outputFilePath(u"out.mht");
workbook->Save(outputFilePath, SaveFormat::MHtml);
std::cout << "Workbook saved to MHTML format successfully!" << std::endl;
Aspose::Cells::Cleanup();
}
```
## **Advance topics**
- [AutoFit Columns and Rows while loading HTML in Workbook](https://docs.aspose.com/cells/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [Avoid exponential notation of large numbers while importing from HTML](https://docs.aspose.com/cells/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [Change the HTML Link Target Type](https://docs.aspose.com/cells/cpp/change-the-html-link-target-type/)
- [Convert Excel to HTML with tooltip](https://docs.aspose.com/cells/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](https://docs.aspose.com/cells/cpp/create-transparent-image-of-excel-worksheet/)
- [Delete redundant spaces after line break while importing HTML](https://docs.aspose.com/cells/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [Disable Downlevel Revealed Comments while saving to HTML](https://docs.aspose.com/cells/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [Disable Exporting Frame Scripts and Document Properties](https://docs.aspose.com/cells/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel to HTML - Use PresentationPreference Option for Better Layout](https://docs.aspose.com/cells/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [Exclude Unused Styles during Excel to HTML conversion](https://docs.aspose.com/cells/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [Expanding text from right to left while exporting Excel file to HTML](https://docs.aspose.com/cells/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [Export DataBar, ColorScale and IconSet Conditional Formatting while Excel to HTML Conversion](https://docs.aspose.com/cells/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [Export Comments while Saving Excel file to HTML](https://docs.aspose.com/cells/cpp/export-comments-while-saving-excel-file-to/)
- [Export Document Workbook and Worksheet Properties in Excel to HTML conversion](https://docs.aspose.com/cells/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [Export Excel to HTML with GridLines](https://docs.aspose.com/cells/cpp/export-excel-to-html-with-gridlines/)
- [Export print area range to HTML](https://docs.aspose.com/cells/cpp/export-print-area-range-to/)
- [Export similar Border Style when Border Style is not supported by Web Browsers](https://docs.aspose.com/cells/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [Export Worksheet CSS Separately in Output HTML](https://docs.aspose.com/cells/cpp/export-worksheet-css-separately-in-output/)
- [Hiding Overlaid Content with CrossHideRight while saving to HTML](https://docs.aspose.com/cells/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [Prefix Table Elements Styles with HtmlSaveOptions.TableCssId property](https://docs.aspose.com/cells/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Prevent Exporting Hidden Worksheet Contents on Saving to HTML](https://docs.aspose.com/cells/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [Recognise Self Closing Tags](https://docs.aspose.com/cells/cpp/recognise-self-closing-tags/)
- [Render Gradient Fill for the WordArt while Converting Spreadsheets to HTML](https://docs.aspose.com/cells/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [Set column width to scalable unit like em or percent](https://docs.aspose.com/cells/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [Set Default Font while rendering spreadsheet to HTML](https://docs.aspose.com/cells/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [Specify how to cross string in output HTML using HtmlCrossType](https://docs.aspose.com/cells/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [Support the layout of DIV tags while loading HTML to excel workbook](https://docs.aspose.com/cells/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [Enable CSS Custom Properties while saving to HTML](https://docs.aspose.com/cells/cpp/enable-css-custom-properties-while-saving-to-html/)
