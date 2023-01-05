---
title: Satır veya Sütunun Yazı Tipini ve Rengini Değiştirme
type: docs
weight: 110
url: /tr/net/changing-the-font-and-color-of-a-row-or-column/
---
{{% alert color="primary" %}} 

Bu konuda, bir çalışma sayfasının satır ve sütunlarının yazı tipini ve yazı rengini değiştirmeyi tartışacağız. Bu, Aspose.Cells.GridDesktop tarafından sunulan temel düzeyde bir biçimlendirme özelliğidir ve geliştiricilerin çalışma sayfalarının görünümünü daha şık hale getirmek için özelleştirmelerine olanak tanır.

{{% /alert %}} 
## **Bir Sütunun Yazı Tipini ve Rengini Değiştirme**
Aspose.Cells.GridDesktop kullanarak bir sütunun yazı tipini ve rengini değiştirmek için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Erişim**Kolon** yazı tipi ve rengi değiştirilecek olan
-  özelleştirilmiş oluşturun**Yazı tipi**
-  Yı kur**Yazı tipi** arasında**Kolon** özelleştirilmiş olana
-  Son olarak ayarla**Yazı rengi** arasında**Kolon** istenilen herhangi**Renk**



{{< highlight "csharp" >}}

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
## **Bir Satırın Yazı Tipini ve Rengini Değiştirme**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Erişim**Sıra** yazı tipi ve rengi değiştirilecek olan
-  özelleştirilmiş oluşturun**Yazı tipi**
-  Yı kur**Yazı tipi** arasında**Sıra** özelleştirilmiş olana
-  Son olarak ayarla**Yazı rengi** arasında**Sıra** istenilen herhangi**Renk**



{{< highlight "csharp" >}}

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
