---
title: تحويل Excel إلى Pdf في جايثون
type: docs
weight: 50
url: /ar/java/excel-to-pdf-conversion-in-jython/
---
## **Aspose.Cells - تحويل Excel إلى PDF**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat



class Excel2PdfConversion:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithFiles/Excel2PdfConversion/'



        saveFormat = SaveFormat

        workbook = Workbook(dataDir + "Book1.xls")

        #Save the document in PDF format

        workbook.save(dataDir + "OutBook1.pdf", saveFormat.PDF)

        # Print message

        print "\n Excel to PDF conversion performed successfully."



if __name__ == '__main__':        

    Excel2PdfConversion()

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithFiles/Excel2PdfConversion.py)
