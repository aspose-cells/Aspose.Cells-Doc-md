---
title: عرض تقسيم الصفحة في Jython
type: docs
weight: 90
url: /ar/java/page-break-preview-in-jython/
---

## **Aspose.Cells - معاينة كسر الصفحات**
لإلحاق المستندات باستخدام **Aspose.Cells Java for Jython**. هنا يمكنك رؤية رمز المثال.

**رمز Jython**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook


class PageBreakPreview:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/PageBreakPreview/'



        workbook = Workbook(dataDir + "Book1.xls")



        #Adding a new worksheet to the Workbook object

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Displaying the worksheet in page break preview

        worksheet.setPageBreakPreview(True)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Page break preview is enabled for sheet 1, please check the output document." 

if __name__ == '__main__':        

    PageBreakPreview()

{{< /highlight >}}
## **تحميل رمز التشغيل**
قم بتنزيل **مستندات الإضافة (Aspose.Cells)** من أي من المواقع الاجتماعية للترميز الواردة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/PageBreakPreview.py)
