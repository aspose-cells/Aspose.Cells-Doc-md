---
title: تجميد الألواح في جايثون
type: docs
weight: 60
url: /ar/java/freeze-panes-in-jython/
---
## **Aspose.Cells - تجميد الأجزاء**
 لإلحاق المستندات باستخدام**Aspose.Cells Java لـ Jython**. هنا يمكنك أن ترى رمز المثال.

**كود جايثون**

{{< highlight "java" >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class FreezePanes:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/FreezePanes/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Applying freeze panes settings

        worksheet.freezePanes(3,2,3,2)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "book.out.xls")

        #Print Message

        print "Panes freeze successfull."

if __name__ == '__main__':        

    FreezePanes()

{{< /highlight >}}
## **تحميل كود الجري**
 تحميل**إرفاق المستندات (Aspose.Cells)**من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/FreezePanes.py)
