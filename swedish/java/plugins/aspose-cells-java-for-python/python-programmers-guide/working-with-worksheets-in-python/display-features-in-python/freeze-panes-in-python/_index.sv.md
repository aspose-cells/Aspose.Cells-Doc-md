---
title: Frys rutor i Python
type: docs
weight: 40
url: /sv/java/freeze-panes-in-python/
---

## **Aspose.Cells - Frys rutor**
För att frysa rutor i kalkyldokumentet med **Aspose.Cells Java för Python**, helt enkelt anropa modulen **FreezePanes**.

**Python-kod**

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
## **Ladda ned körbar kod**
Ladda ner **Hello World (Aspose.Cells)** från någon av nedan nämnda sociala kodningssidor:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
