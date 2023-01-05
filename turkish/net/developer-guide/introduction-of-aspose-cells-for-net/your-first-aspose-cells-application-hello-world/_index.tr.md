---
title: İlk Başvurunuz Aspose.Cells - Hello World
type: docs
weight: 30
url: /tr/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

Bu öğretici, Aspose.Cells' basit API'i kullanarak ilk uygulamanın (Hello World) nasıl oluşturulacağını gösterir. Bu basit uygulama, belirtilen bir çalışma sayfası hücresinde 'Hello World' metniyle bir Microsoft Excel dosyası oluşturur.

{{% /alert %}}

## **Hello World Uygulamasını Oluşturma**

Aşağıdaki adımlar, Aspose.Cells API'i kullanarak Hello World uygulamasını oluşturur:

1.  örneğini oluşturun[Çalışma kitabı](https://reference.aspose.com/cells/net/aspose.cells/workbook) sınıf.
1.  Ehliyetin varsa o zaman[uygula](/cells/tr/net/licensing/).
 Değerlendirme sürümünü kullanıyorsanız, lisansla ilgili kod satırlarını atlayın.
1. Yeni bir Excel dosyası oluşturun veya mevcut bir Excel dosyasını açın.
1. Excel dosyasındaki bir çalışma sayfasının istediğiniz herhangi bir hücresine erişin.
1.  kelimeleri ekle**Hello World!** erişilen bir hücreye
1. Değiştirilen Microsoft Excel dosyasını oluşturun.

Yukarıdaki adımların uygulanması aşağıdaki örneklerde gösterilmektedir.

### **Kod Örneği: Yeni Bir Çalışma Kitabı Oluşturma**

Aşağıdaki örnek sıfırdan yeni bir çalışma kitabı oluşturur, Hello World yazar! ilk çalışma sayfasındaki A1 hücresine girer ve Excel dosyasını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Kod Örneği: Mevcut Bir Dosyayı Açma**

Aşağıdaki örnek, "Sample.xlsx" adlı mevcut bir Microsoft Excel şablon dosyasını açar ve "Hello World!" girer. metni ilk çalışma sayfasındaki A1 hücresine kaydeder ve çalışma kitabını kaydeder.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
