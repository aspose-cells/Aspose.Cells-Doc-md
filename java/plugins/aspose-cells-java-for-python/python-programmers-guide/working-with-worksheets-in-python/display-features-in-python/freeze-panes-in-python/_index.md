---
title: Freeze Panes in Python
type: docs
weight: 40
url: /java/freeze-panes-in-python/
---

## **Aspose.Cells - Freeze Panes**
To Freeze Panes in the Spreadsheet Document using **Aspose.Cells Java for Python**, simply invoke **FreezePanes** module.

**Python Code**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Applying freeze panes settings

worksheet.freezePanes(3,2,3,2)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "book.out.xls")

#Print Message

print "Panes freeze successfull."

{{< /highlight >}}
## **Download Running Code**
Download **Hello World (Aspose.Cells)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
- [CodePlex](https://asposecellsjavapython.codeplex.com/releases/view/620185)
