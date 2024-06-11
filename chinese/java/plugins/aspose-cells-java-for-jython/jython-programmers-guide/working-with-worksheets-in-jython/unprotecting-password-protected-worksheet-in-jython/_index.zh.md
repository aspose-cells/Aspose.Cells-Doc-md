---
title: 在 Jython 中去除受密码保护的工作表保护
type: docs
weight: 150
url: /zh/java/unprotecting-password-protected-worksheet-in-jython/
---

## **Aspose.Cells - 追加文档**
使用**Aspose.Cells Java for Jython**进行附加文档。这里可以看到示例代码。

**Jython 代码**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat

from com.aspose.cells import FileFormatType;


class UnprotectingPasswordProtectedWorksheet:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet/'



        filesFormatType = FileFormatType

        #Instantiating a Workbook object

        workbook = Workbook(dataDir + "book1.xls")

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        protection = worksheet.getProtection()

        #Unprotecting the worksheet with a password

        worksheet.unprotect("aspose")

        # Save the excel file.

        workbook.save(dataDir + "output.xls", filesFormatType.EXCEL_97_TO_2003)

        #Print Message

        print "Worksheet unprotected successfully."

if __name__ == '__main__':        

    UnprotectingPasswordProtectedWorksheet()

{{< /highlight >}}
## **下载运行代码**
从以下任何社交编码网站下载**Append Documents (Aspose.Cells)**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)
