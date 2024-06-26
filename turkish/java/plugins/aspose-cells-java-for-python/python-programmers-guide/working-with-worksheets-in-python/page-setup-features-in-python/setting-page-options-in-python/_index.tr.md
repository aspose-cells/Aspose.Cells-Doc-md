---
title: Python da Sayfa Seçeneklerini Ayarlama
type: docs
weight: 10
url: /tr/java/setting-page-options-in-python/
---

## **Aspose.Cells - Sayfa Seçeneklerini Ayarlama**
### **Sayfa Yönlendirmesi**
**Aspose.Cells Java için Ruby** kullanarak sayfa yönlendirme ayarlarını uygulamak için **pagesetup** modülünün **page_orientation** yöntemini çağırın.

**Python Kodu**

{{< highlight java >}}

 def page_orientation(self):

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook()

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the orientation to Portrait

page_setup = sheet.getPageSetup()

page_orientation_type = self.PageOrientationType

page_setup.setOrientation(page_orientation_type.PORTRAIT)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Page_Orientation.xls")

print "Set page orientation, please check the output file."


{{< /highlight >}}
### **Ölçekleme Faktörü**
**Aspose.Cells Java for Python** kullanarak ölçeklendirme uygulamak için **pagesetup** modülündeki **scaling** yöntemini çağırın.

**Python Kodu**

{{< highlight python >}}

 def scaling(self):        

\# Instantiating a Workbook object by excel file path

workbook = self.Workbook(self.dataDir + 'Book1.xls')

\# Accessing the first worksheet in the Excel file

worksheets = workbook.getWorksheets()

sheet_index = worksheets.add()

sheet = worksheets.get(sheet_index)

\# Setting the scaling factor to 100

page_setup = sheet.getPageSetup()

page_setup.setZoom(100)

\# Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(self.dataDir + "Scaling.xls")

print "Set scaling, please check the output file."

{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Sayfa Seçeneklerini Ayarlama (Aspose.Cells)**'i indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Python-v1.0)
