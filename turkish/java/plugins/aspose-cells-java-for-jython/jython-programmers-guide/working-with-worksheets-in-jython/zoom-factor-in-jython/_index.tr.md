---
title: Jython da Yakınlaştırma Oranı
type: docs
weight: 170
url: /tr/java/zoom-factor-in-jython/
---

## **Aspose.Cells - Yakınlaştırma Faktörü**
**Aspose.Cells Java for Jython** ile belgeler eklemek için. Burada örnek kodu görebilirsiniz.

**Jython Kodu**

{{< highlight java >}}

 from aspose-cells import Settings

from com.aspose.cells import Workbook

from com.aspose.cells import SaveFormat


class ZoomFactor:

    def __init__(self):

        dataDir = Settings.dataDir + 'WorkingWithWorksheets/ZoomFactor/'



        workbook = Workbook(dataDir + "Book1.xls")

        #Accessing the first worksheet in the Excel file

        worksheets = workbook.getWorksheets()

        worksheet = worksheets.get(0)

        #Setting the zoom factor of the worksheet to 75

        worksheet.setZoom(75)

        #Saving the modified Excel file in default format

        workbook.save(dataDir + "output.xls")

        # Print message

        print "Zoom factor set to 75% for sheet 1, please check the output document."

if __name__ == '__main__':        

    ZoomFactor()

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Append Documents (Aspose.Cells)** indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose-Cells-Java-for-Jython/asposecells/WorkingWithWorksheets/ZoomFactor.py)
