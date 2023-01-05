---
title: Çalışma Sayfalarını Kopyala
type: docs
weight: 60
url: /tr/net/copy-worksheets/
---
## **Geçiş İpucu:**
\1. Çalışma Kitabı nesnesi oluşturun ve Çalışma Sayfası'nı edinin.
\2. Çalışma sayfasına metin ekleyin.
\3. Yeni Çalışma Sayfası oluşturun ve daha önce yapılan çalışma sayfasına kopyalayın.
### **VSTO**
Makro 'kodu' oluşturulurken hata oluştu: Parametre dili için geçersiz değer belirtildi
### **Aspose.Cells**
{{< highlight "csharp" >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **İndirmek**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
