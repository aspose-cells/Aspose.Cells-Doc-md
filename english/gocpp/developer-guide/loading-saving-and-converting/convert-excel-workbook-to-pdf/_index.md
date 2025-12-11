---
title: Convert Excel Workbook to PDF
type: docs
weight: 80
url: /go-cpp/convert-excel-workbook-to-pdf/
---

## **Converting Excel Workbook to PDF**

Aspose.Cells supports converting Excel files to PDF and maintains high visual fidelity in the conversion.

{{% alert color="primary" %}}

Aspose.Cells directly writes information about the API and version number in output documents. For example, upon rendering the document to PDF, Aspose.Cells for Go via C++ populates the **Application** field with the value 'Aspose.Cells' and the **PDF Producer** field with the value, e.g., 'Aspose.Cells v24.12.0'.

Please note that you cannot instruct Aspose.Cells for Go via C++ to change or remove this information from output documents.

{{% /alert %}}

### **Direct Conversion**

Follow the below steps to directly convert the Excel spreadsheets to PDF format:

1. Instantiate an object of the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class by calling its empty constructor.  
2. You may open/load an existing template file or skip this step if you are creating the workbook from scratch.  
3. Do any work (input data, apply formatting, set formulas, insert pictures or other drawing objects, etc.) on the spreadsheet using Aspose.Cells' APIs.  
4. When the spreadsheet code is complete, call the [Workbook](https://reference.aspose.com/cells/go-cpp/workbook/) class's [Save](https://reference.aspose.com/cells/go-cpp/workbook/save/) method to save the spreadsheet.

The file format should be PDF, so select the relevant PDF (a pre-defined value) from the `SaveFormat` enumeration to generate the final PDF document.

Please see the following sample code, its [sample Excel file](67338368.xlsx) and the [output PDF](67338369.pdf) for your reference.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveWorkbookAsPDF.go" >}}