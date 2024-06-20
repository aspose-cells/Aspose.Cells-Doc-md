---
title: Bonjour tout le monde
type: docs
weight: 10
url: /fr/java/hello-world/
---

## **Aspose.Cells - Hello World**
Pour écrire n'importe quoi dans le document de classeur en utilisant Aspose.Cells for Java en PHP, invoquez simplement le module HelloWorld.

**Code PHP**

{{< highlight ruby >}}

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
## **Télécharger le code en cours d'exécution**
Télécharger **Hello World (Aspose.Cells)** de n'importe lequel des sites de codage social mentionnés ci-dessous:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_PHP/src/aspose/cells/quickstart/HelloWorld.php)
