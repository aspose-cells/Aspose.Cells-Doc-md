---
title: Jython でパスワード保護されたワークシートの保護を解除する
type: docs
weight: 150
url: /ja/java/unprotecting-password-protected-worksheet-in-jython/
---
## **Aspose.Cells - ドキュメントの追加**
を使用してドキュメントを追加するには**Aspose.Cells Jython の場合は Java**.ここでサンプルコードを見ることができます。

**Jython コード**

{{< highlight "java" >}}

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
## **実行中のコードをダウンロード**
ダウンロード**添付書類 (Aspose.Cells)**以下のソーシャルコーディングサイトのいずれかから：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/UnprotectingPasswordProtectedWorksheet.py)
