---
title: Satır veya Sütunun Yazı Tipi ve Rengini Değiştirme
type: docs
weight: 110
url: /tr/net/aspose-cells-griddesktop/change-the-font-and-color-of-a-row-or-column/
keywords: GridDesktop, yazı tipi, renk
description: Bu makale, GridDesktop te satır veya sütunda yazı tipi ve rengini değiştirmeyi tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konuda, Geliştiricilere çalışsayfalarını daha sunulabilir hale getirmek için görünümünü özelleştirmelerini sağlayan Aspose.Cells.GridDesktop tarafından sunulan temel düzey bir biçimlendirme özelliği olan çalışsayfaların satır ve sütunlarının yazı tipi ve yazı rengini değiştirme hakkında konuşacağız.

{{% /alert %}} 
## **Bir Sütunun Yazı Tipi ve Rengini Değiştirme**
Aspose.Cells.GridDesktop kullanarak bir sütunun yazı tipini ve rengini değiştirmek için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Yazı tipi ve rengi değiştirilecek olan bir **Sütuna** erişin
- Özelleştirilmiş bir **Yazı Tipi** oluşturun
- **Sütunun** Yazı Tipini özelleştirilmiş olanla ayarlayın
- Son olarak, **Sütunun Yazı Rengini** istenilen herhangi bir **Renk** ile ayarlayın



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first column of the worksheet

GridColumn column = sheet.Columns[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Bold);

//Setting the font of the column to the customized Font object

column.SetFont(font);

//Setting the font color of the column to Blue

column.SetFontColor(Color.Blue);

{{< /highlight >}}
## **Bir Satırın Yazı Tipi ve Rengini Değiştirme**
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Yazı tipi ve rengi değiştirilecek olan bir **Sıraya** erişin
- Özelleştirilmiş bir **Yazı Tipi** oluşturun
- **Sıranın** Yazı Tipini özelleştirilmiş olanla ayarlayın
- Son olarak, **Sıranın Yazı Rengini** istenilen herhangi bir **Renk** ile ayarlayın



{{< highlight csharp >}}

 //Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

//Accessing the first row of the worksheet

GridRow row = sheet.Rows[0];

//Creating a customized Font object

Font font = new Font("Arial", 10, FontStyle.Underline);

//Setting the font of the column to the customized Font object

row.SetFont(font);

//Setting the font color of the column to Green

row.SetFontColor(Color.Green);

{{< /highlight >}}
