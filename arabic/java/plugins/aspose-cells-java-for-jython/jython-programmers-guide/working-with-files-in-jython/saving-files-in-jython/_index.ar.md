---
title: حفظ الملفات في جايثون
type: docs
weight: 80
url: /ar/java/saving-files-in-jython/
---

## **Aspose.Cells - حفظ الملفات**
لإلحاق المستندات باستخدام **Aspose.Cells Java for Jython**. هنا يمكنك رؤية رمز المثال.

**رمز Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import FileFormatType


class SavingFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/SavingFiles/'



        fileFormatType = FileFormatType





        #Creating an Workbook object with an Excel file path

        workbook = Workbook(dataDir + "Book1.xls")

        #Save in default (Excel2003) format

        workbook.save(dataDir + "book.default.out.xls")

        #Save in Excel2003 format

        workbook.save(dataDir + "book.out.xls", fileFormatType.EXCEL_97_TO_2003)

        #Save in Excel2007 xlsx format

        workbook.save(dataDir + "book.out.xlsx", fileFormatType.XLSX)

        #Save in SpreadsheetML format

        workbook.save(dataDir + "book.out.xml", fileFormatType.EXCEL_2003_XML)



        #Print Message

        print("<BR>")

        print("Worksheets are saved successfully.")





if __name__ == '__main__':        

    SavingFiles()

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **مستندات الإضافة (Aspose.Cells)** من أي من المواقع الاجتماعية للترميز الواردة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/SavingFiles.py)
