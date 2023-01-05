---
title: Bir Satıra veya Sütuna Stil Uygulama
type: docs
weight: 50
url: /tr/net/applying-style-on-a-row-or-column/
---
{{% alert color="primary" %}} 

Bu konuda, bir çalışma sayfasının satır ve sütunlarının yazı tipini ve yazı rengini değiştirmeyi tartışacağız. Bu, Aspose.Cells.GridDesktop tarafından sunulan temel düzeyde bir biçimlendirme özelliğidir ve geliştiricilerin çalışma sayfalarının görünümünü daha şık hale getirmek için özelleştirmelerine olanak tanır.

{{% /alert %}} 
## **Bir Sütuna Stil Uygulamak**
Aspose.Cells.GridDesktop kullanarak bir sütuna özel bir stil uygulamak için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Erişim**Kolon** uygulamak istediğimiz**stil**
-  Elde etmek**stil** arasında**Kolon**
-  Ayarlamak**stil** özel ihtiyaçlarınıza göre özellikler
-  Son olarak ayarla**stil** arasında**Kolon** güncellenen ile

 tarafından sunulan birçok yararlı özellik ve yöntem vardır.**stil** geliştiriciler tarafından stili gereksinimlerine göre özelleştirmek için kullanılabilen nesne.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Satıra Stil Uygulamak**
Aspose.Cells.GridDesktop kullanarak bir satıra özel bir stil uygulamak için lütfen aşağıdaki adımları izleyin:

-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  Erişim**Sıra** uygulamak istediğimiz**stil**
-  Elde etmek**stil** arasında**Sıra**
-  Ayarlamak**stil** özel ihtiyaçlarınıza göre özellikler
-  Son olarak ayarla**stil** arasında**Sıra** güncellenen ile

 tarafından sunulan birçok yararlı özellik ve yöntem vardır.**stil** geliştiriciler tarafından stili gereksinimlerine göre özelleştirmek için kullanılabilen nesne.



{{< highlight "csharp" >}}

 // Accessing the worksheet of the Grid that is currently active

Worksheet sheet = gridDesktop1.GetActiveWorksheet();

// Accessing the first row of the worksheet

Aspose.Cells.GridDesktop.Data.GridRow row = sheet.Rows[0];

// Getting the Style object for the row

Style style = row.GetStyle();

// Setting Style properties i.e. border, color, alignment, background color etc.

style.SetBorderLine(BorderType.Right, BorderLineType.Thick);

style.SetBorderColor(BorderType.Right, Color.Blue);

style.HAlignment = HorizontalAlignmentType.Centred;

style.Color = Color.Yellow;

// Setting the style of the row with the customized Style object

row.SetStyle(style);

{{< /highlight >}}
