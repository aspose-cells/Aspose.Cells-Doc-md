---
title: Jython da Merhaba Dünya
type: docs
weight: 10
url: /tr/java/hello-world-in-jython/
---

## **Aspose.Cells - Hello World**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from asposewords import Settings

from com.aspose.Cells import Document

from com.aspose.Cells import ImportFormatMode

class HelloWorld:

    def __init__(self):

        dataDir = Settings.dataDir + 'quickstart/'



        workbook = Workbook()



        sheet = workbook.getWorksheets().get(0)



        cell = sheet.getCells().get("A1")



        cell.setValue("Hello World!")



        file_format_type = FileFormatType



        workbook.save(dataDir + "HelloWorld.xls" , file_format_type.EXCEL_97_TO_2003 )



        print "Document has been saved, please check the output file.";

if __name__ == '__main__':        

    HelloWorld()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/quickstart/HelloWorld.py)
