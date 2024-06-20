---
title: Çalışsayfaları Kopyala
type: docs
weight: 60
url: /tr/net/copy-worksheets/
---

## **Göç Tavsiyesi:**
1. Çalışma Kitabı nesnesi oluşturun ve Çalışma Sayfasını alın.
2. Çalışma sayfasında metin ekleyin.
3. Yeni Çalışma Sayfası oluşturun ve Önceki oluşturulan çalışma sayfasına kopyalayın.
### **VSTO**
'code' adlı hata görüntüleme makrosu: Geçersiz parametre değeri belirtilmiştir
### **Aspose.Cells**
{{< highlight csharp >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **İndir**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
