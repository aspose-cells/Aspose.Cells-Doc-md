##Protecting Worksheets in Python
## **Aspose.Cells - Protecting Worksheets**
To protect worksheet using **Aspose.Cells Java for Python**, call **protect_worksheet** method of **protection** module.
**Python Code**
#Instantiating a Excel object by excel file path
excel = self.Workbook(self.dataDir + "Book1.xls")
#Accessing the first worksheet in the Excel file
worksheets = excel.getWorksheets()
worksheet = worksheets.get(0)
protection = worksheet.getProtection()
#The following 3 methods are only for Excel 2000 and earlier formats
protection.setAllowEditingContent(False)
protection.setAllowEditingObject(False)
protection.setAllowEditingScenario(False)
#Protects the first worksheet with a password "1234"
protection.setPassword("1234")
#Saving the modified Excel file in default format
excel.save(self.dataDir + "output.xls")
#Print Message
print "Sheet protected successfully."
## **Download Running Code**
Download **Protecting Worksheets (Aspose.Cells)** from any of the below mentioned social coding sites:
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
