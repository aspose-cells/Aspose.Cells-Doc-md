---
title: Yeni Çalışma Kitapları Oluştur ve Kaydet
type: docs
weight: 70
url: /tr/net/create-and-save-new-workbooks/
---

## **Geçiş İpuçları:**
\1. Workbook nesnesi oluştur
\2. Mevcut çalışma sayfasını al
\3. Herhangi bir hücreye metin ekleyin
\4. Çalışma kitabını kaydedin
### **VSTO**
Aşağıda VSTO için kod örneği bulunmaktadır

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Aşağıda Aspose.Cells için kod örneği bulunmaktadır

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **İndir**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
