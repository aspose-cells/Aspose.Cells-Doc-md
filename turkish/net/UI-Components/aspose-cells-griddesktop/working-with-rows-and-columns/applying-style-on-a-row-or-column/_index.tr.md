---
title: Satır veya Sutun Üzerine Stil Uygulama
type: docs
weight: 50
url: /tr/net/aspose-cells-griddesktop/apply-style-on-a-row-or-column/
keywords: GridDesktop, stili, satır, sütun
description: Bu makale, GridDesktop te satır veya sütunda stil uygulamanın nasıl yapıldığını tanıtıyor.
---

{{% alert color="primary" %}} 

Bu konuda, Geliştiricilere çalışsayfalarını daha sunulabilir hale getirmek için görünümünü özelleştirmelerini sağlayan Aspose.Cells.GridDesktop tarafından sunulan temel düzey bir biçimlendirme özelliği olan çalışsayfaların satır ve sütunlarının yazı tipi ve yazı rengini değiştirme hakkında konuşacağız.

{{% /alert %}} 
## **Sütun Üzerine Stil Uygulama**
Aspose.Cells.GridDesktop kullanarak sütun üzerine özel bir stil uygulamak için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Üzerine **Stil** uygulamak istediğiniz bir **Sütun** a erişin
- **Sütunun Stilini** alın
- Özel ihtiyaçlarınıza göre **Stil** özelliklerini ayarlayın
- Son olarak, **Sütunun Stilini** güncellenmiş olanla ayarlayın

Geliştiricilerin gereksinimlerine göre stili özelleştirmek için kullanılabilecek **Stil** nesnesi tarafından sunulan birçok kullanışlı özellik ve yöntem bulunmaktadır.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-ApplyingStyleOnRowColumn-AddingColumnStyle.cs" >}}
## **Satır Üzerine Stil Uygulama**
Aspose.Cells.GridDesktop kullanarak satır üzerine özel bir stil uygulamak için lütfen aşağıdaki adımları izleyin:

- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Üzerine **Stil** uygulamak istediğiniz bir **Satır** a erişin
- **Satırın Stilini** alın
- Özel ihtiyaçlarınıza göre **Stil** özelliklerini ayarlayın
- Son olarak, **Satırın Stilini** güncellenmiş olanla ayarlayın

Geliştiricilerin gereksinimlerine göre stili özelleştirmek için kullanılabilecek **Stil** nesnesi tarafından sunulan birçok kullanışlı özellik ve yöntem bulunmaktadır.



{{< highlight csharp >}}

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
