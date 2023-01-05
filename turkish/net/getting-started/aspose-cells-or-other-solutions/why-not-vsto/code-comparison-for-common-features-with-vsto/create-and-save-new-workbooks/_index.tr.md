---
title: Yeni Çalışma Kitapları Oluşturun ve Kaydedin
type: docs
weight: 70
url: /tr/net/create-and-save-new-workbooks/
---
## **Geçiş İpuçları:**
\1. Çalışma Kitabı nesnesi oluştur
\2. Mevcut Çalışma Sayfasını alın.
\3. Herhangi bir hücreye biraz metin ekleyin.
\4. Çalışma Kitabını kaydedin.
### **VSTO**
Aşağıda VSTO için kod örneği verilmiştir

{{< highlight "csharp" >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Aspose.Cells için kod örneği aşağıdadır

{{< highlight "csharp" >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **İndirmek**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
