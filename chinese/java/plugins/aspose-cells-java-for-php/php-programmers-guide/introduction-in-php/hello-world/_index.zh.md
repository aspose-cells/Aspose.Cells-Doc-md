---
title: Hello World
type: docs
weight: 10
url: /zh/java/hello-world/
---
## **Aspose.Cells - Hello World**
要在 PHP 中使用 Aspose.Cells for Java 在电子表格文档中写入任何内容，只需调用 HelloWorld 模块。

**PHP代码**

{{< highlight "ruby" >}}

 # Instantiating a Workbook object that represents a Microsoft Excel file.

$workbook = new Workbook();

\# Note when you create a new workbook, a default worksheet,

\# "Sheet1", is by default added to the workbook.

\# Accessing the first worksheet in the book ("Sheet1").

$sheet = $workbook->getWorksheets()->get(0);

\# Access cell "A1" in the sheet.

$cell = $sheet->getCells()->get("A1");

\# Input the "Hello World!" text into the "A1" cell

$cell->setValue("Hello World!");

\# Saving the modified Excel file in default (that is Excel 2003) format

$file_format_type = new FileFormatType();

$workbook.save($data_dir . "HelloWorld.xls", $file_format_type->EXCEL_97_TO_2003);

print "Document has been saved, please check the output file.";

{{< /highlight >}}
## **下载运行代码**
下载**Hello World (Aspose.Cells)**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/quickstart/HelloWorld.php)
