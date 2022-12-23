---
title: التحويل إلى ملفات Mhtml في جايثون
type: docs
weight: 20
url: /ar/java/converting-to-mhtml-files-in-jython/
---
## **Aspose.Cells - التحويل إلى ملفات Mhtml**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import HtmlSaveOptions

from com.aspose.cells import SaveFormat


class ConvertingToMhtmlFiles:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/ConvertingToMhtmlFiles/'



        saveFormat = SaveFormat

        #Specify the file path

        filePath = dataDir + "Book1.xlsx"

        #Specify the HTML saving options

        sv = HtmlSaveOptions(saveFormat.M_HTML)

        #Instantiate a workbook and open the template XLSX file

        wb = Workbook(filePath)

        #Save the MHT file

        wb.save(filePath + ".out.mht", sv)

        # Print message

        print "Excel to MHTML conversion performed successfully."



if __name__ == '__main__':        

    ConvertingToMhtmlFiles()

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/ConvertingToMhtmlFiles.py)
