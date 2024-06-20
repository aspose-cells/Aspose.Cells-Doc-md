---
title: مرحبًا بالعالم في Jython
type: docs
weight: 10
url: /ar/java/hello-world-in-jython/
---

## **Aspose.Cells - Hello World**
لإلحاق المستندات باستخدام **Aspose.Cells Java for Jython**. هنا يمكنك رؤية رمز المثال.

**رمز Jython**

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
## **تحميل رمز التشغيل**
قم بتنزيل **مستندات الإضافة (Aspose.Cells)** من أي من المواقع الاجتماعية للترميز الواردة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/quickstart/HelloWorld.py)
