---
title: Python da Yakınlaştırma Faktörü
type: docs
weight: 80
url: /tr/java/zoom-factor-in-python/
---

## **Aspose.Cells - Yakınlaştırma Faktörü**
**Aspose.Cells Java for Python** kullanarak Yakınlaştırma Faktörü ayarlamak için sadece **ZoomFactor** modülünü çağırın.

**Python Kodu**

{{< highlight java >}}

 workbook = self.Workbook(self.dataDir + "Book1.xls")

#Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

worksheet = worksheets.get(0)

#Setting the zoom factor of the worksheet to 75

worksheet.setZoom(75)

#Saving the modified Excel file in default format

workbook.save(self.dataDir + "output.xls")

\# Print message

print "Zoom factor set to 75% for sheet 1, please check the output document."

{{< /highlight >}}
## **Çalışan Kodu İndir**
Herhangi aşağıdaki sosyal kodlama sitelerinden **Zoom Faktörü (Aspose.Cells)**'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
