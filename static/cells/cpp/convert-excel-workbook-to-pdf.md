##Convert Excel Workbook to PDF
## **Converting Excel Workbook to PDF**
PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.
Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.
Aspose.Cells directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for C++ populates the **Application** field with value 'Aspose.Cells' and **PDF Producer** field with value, e.g 'Aspose.Cells v18.5.0'.
### **Direct Conversion**
Aspose.Cells supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method. The [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method provides the [SaveFormat_Pdf](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) enumeration member that converts the native Excel files to PDF format.
Follow the below steps to directly convert the Excel spreadsheets to PDF format:
1. Instantiate an object of the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class by calling its empty constructor.
1. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.
1. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.
1. When the spreadsheet code is complete, call the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class' [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method to save the spreadsheet.
The file format should be PDF so select relevant PDF (a pre-defined value) from the SaveFormat enumeration to generate the final PDF document
Please see the following sample code, its [sample Excel file](67338368.xlsx) and [output PDF](67338369.pdf) for your reference.
### **Advanced Conversion**
You may also opt to use the [PdfSaveOptions](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) class to set different attributes for the conversion. Setting different properties of the **PdfSaveOptions** class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [SetCompliance](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/setcompliance/) which enables you to save the Excel files to PDF/A compliant PDF files.
#### **Saving Workbook to PDF/A Complied Files**
The following code snippet demonstrates how to use the **PdfSaveOptions** class to save Excel files to PDF/A compliant PDF format
Please see the following sample code and its [output PDF](67338370.pdf) for your reference.
#### **Set the PDF Creation Time**
With the **IPdfSaveOptions** class, you can get or set the PDF creation time.
Please see the following sample code and its [output PDF](67338371.pdf) for your reference.
