---
title: İlk Aspose.Cells Başvurunuz - Hello World
type: docs
weight: 30
url: /tr/net/your-first-aspose-cells-application-hello-world/
description: Aspose.Cells for .NET'i kullanarak ilk Excel dosyanızı oluşturun, düzenleyin ve kaydedin ve bunun basitliğini ve gücünü C#'de deneyimleyin.
keywords: C# Hello World, Aspose.Cells for .NET Hello World, The first application using Aspose.Cells for .NET, The first program via Aspose.Cells for .NET.
---
{{% alert color="primary" %}}

Bu eğitimde, Aspose.Cells' basit API kullanılarak ilk uygulamanın (Hello World) nasıl oluşturulacağı gösterilmektedir. Bu basit uygulama, belirli bir çalışma sayfası hücresinde 'Hello World' metnini içeren bir Microsoft Excel dosyası oluşturur.

{{% /alert %}}

##  **Hello World Başvurusu Nasıl Oluşturulur**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  Bir örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf.
1.  Ehliyetin varsa o zaman[Uygula](/cells/tr/net/licensing/).
 Değerlendirme sürümünü kullanıyorsanız lisansla ilgili kod satırlarını atlayın.
1. Yeni bir Excel dosyası oluşturun veya mevcut bir Excel dosyasını açın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1.  Kelimeleri ekleyin**Hello World!** erişilen bir hücreye.
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmiştir.

###  **Yeni Bir Çalışma Kitabı Nasıl Oluşturulur**

Aşağıdaki örnekte sıfırdan yeni bir çalışma kitabı oluşturuluyor, Hello World yazıyor! ilk çalışma sayfasındaki A1 hücresine girer ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

###  **Mevcut Bir Dosya Nasıl Açılır**

Aşağıdaki örnek, "Sample.xlsx" adlı mevcut bir Microsoft Excel şablon dosyasını açar ve "Hello World!" girişini yapar. Metni ilk çalışma sayfasındaki A1 hücresine kopyalar ve çalışma kitabını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
