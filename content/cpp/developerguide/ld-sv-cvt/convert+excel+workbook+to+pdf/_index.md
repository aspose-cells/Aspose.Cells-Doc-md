---
title : "Convert Excel Workbook to PDF" 
description : "" 
weight : 12018 
toc : false
type: docs
url: /cpp/developerguide/ld-sv-cvt/convert+excel+workbook+to+pdf/
---

# Aspose.Cells for C++ : Convert Excel Workbook to PDF


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Converting Excel Workbook to PDF](#converting-excel-workbook-to-pdf)
    *   1.1 [Direct Conversion](#direct-conversion)
    *   1.2 [Advanced Conversion](#advanced-conversion)
        *   1.2.1 [Saving Workbook to PDF/A Complied Files](#saving-workbook-to-pdf/a-complied-files)
        *   1.2.2 [Set the PDF Creation Time](#set-the-pdf-creation-time)
{{< /panel >}}
 

## Converting Excel Workbook to PDF

PDF files are widely used to exchange documents between organizations, government sectors, and individuals. It is a standard document format and software developers are often asked to find a way to convert Microsoft Excel files into PDF documents.

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

Aspose.Cells directly writes the information about API and Version Number in output documents. For example, upon rendering Document to PDF, Aspose.Cells for C++ populates the **Application** field with value 'Aspose.Cells' and **PDF Producer** field with value, e.g 'Aspose.Cells v18.5.0'.

Please note that you cannot instruct Aspose.Cells for C++ to change or remove this information from output Documents.

### Direct Conversion

Aspose.Cells supports conversion from spreadsheets to PDF independently of other software. Simply save an Excel file to PDF using the [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class' [Save](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/#a77072cfb929787df9ad1f38b02f58349) method. The [Save](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/#a77072cfb929787df9ad1f38b02f58349) method provides the [SaveFormat\_Pdf](https://apireference.aspose.com/cpp/cells/namespace/aspose.cells/#a11cae527e4e68f1adcac8f47ea64481a) enumeration member that converts the native Excel files to PDF format.

Follow the below steps to directly convert the Excel spreadsheets to PDF format:

1.  Instantiate an object of the [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class by calling its empty constructor.
2.  You may open/load an existing template file or skip this step if you are creating the workbook from scratch.
3.  Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, and so on) on the spreadsheet using Aspose.Cells' APIs.
4.  When the spreadsheet code is complete, call the [IWorkbook](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/) class' [Save](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_workbook/#a77072cfb929787df9ad1f38b02f58349) method to save the spreadsheet.

The file format should be PDF so select relevant PDF (a pre-defined value) from the `SaveFormat` enumeration to generate the final PDF document

Please see the following sample code, its [sample Excel file](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338368.xlsx) and [output PDF](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338369.pdf) for your reference.

### Advanced Conversion

You may also opt to use the [IPdfSaveOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_pdf_save_options/) class to set different attributes for the conversion. Setting different properties of the [IPdfSaveOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_pdf_save_options/) class gives you control over the print, font, security and compression settings for the output PDF. The most important property is [SetCompliance](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_pdf_save_options/#a2158ff23d7c071f8224b1cd063233c07) which enables you to save the Excel files to PDF/A compliant PDF files.

#### Saving Workbook to PDF/A Complied Files

The following code snippet demonstrates how to use the [IPdfSaveOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_pdf_save_options/) class to save Excel files to PDF/A compliant PDF format

Please see the following sample code and its [output PDF](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338370.pdf) for your reference.

#### Set the PDF Creation Time

With the [IPdfSaveOptions](https://apireference.aspose.com/cpp/cells/class/aspose.cells.i_pdf_save_options/) class, you can get or set the PDF creation time.

Please see the following sample code and its [output PDF](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338371.pdf) for your reference.

## Attachments:

![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [sampleConvertExcelWorkbookToPDF.xlsx](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338368.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [outputConvertExcelWorkbookToPDF\_DirectConversion.pdf](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338369.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [outputConvertExcelWorkbookToPDF\_PdfCompliance\_PdfA1b.pdf](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338370.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/cpp/images/icons/bullet_blue.gif) [outputConvertExcelWorkbookToPDF\_PDFCreationTime.pdf](https://docs2.aspose.com/cells/cpp/attachments/66946026/67338371.pdf) (application/pdf)  

