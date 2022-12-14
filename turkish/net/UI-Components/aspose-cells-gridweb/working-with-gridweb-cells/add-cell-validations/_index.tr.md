---
title: Cell Doğrulamaları Ekle
type: docs
weight: 70
url: /tr/net/add-cell-validations/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'in gelişmiş özelliklerinden biri, hücreler için giriş doğrulama kuralları eklemektir. Geliştiriciler, hücrelerin giriş değerlerini kontrol etmesi ve doğrulaması için farklı türde doğrulama kuralları oluşturabilir. Bu konu, desteklenen doğrulama türlerini ve bunların nasıl oluşturulacağını tartışır.

{{% /alert %}} 
## **Doğrulama Türleri**
Aspose.Cells.GridWeb kullanılarak üç tür doğrulama uygulanabilir:

- Liste doğrulama.
- Açılır liste doğrulaması.
- Özel ifade doğrulaması.

Her biri aşağıda ayrıntılı olarak tartışılmaktadır.
### **Liste Doğrulaması**
Liste doğrulama, kullanıcıların yazarak veya bir menüden bir değer seçerek hücre girişi sağlamasına olanak tanır. Bir hücre için liste doğrulaması oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Doğrulama eklemek için hücreye erişin.
1. Hücre için doğrulama oluşturun ve doğrulama türünü Liste olarak belirtin.
1. Liste doğrulaması için değerler ekleyin.

Örnek kod, C1'e bir liste doğrulaması ekler. Bir kullanıcı hücreyi tıkladığında bir liste görünür.

**Çıktı: listeden bir değer seçmek** 

![yapılacaklar:resim_alternatif_Metin](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Açılır Liste Doğrulaması**
Açılır liste doğrulama, kullanıcıların önceden tanımlanmış bir listeden bir değer seçerek hücreler için girdi sağlamasına olanak tanır. Açılır liste doğrulaması oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Doğrulamayı oluşturmak için hücreye erişin.
1. Hücre için bir doğrulama oluşturun ve türü DropDownList olarak belirtin.
1. Doğrulama için değerler ekleyin.

Örnek kod, C1'e bir açılır liste doğrulaması ekler. Bir kullanıcı hücreyi tıkladığında, bir açılır menü belirir ve kullanıcılar buradan bir değer seçebilir.

**Açılır listeden bir değer seçme** 

![yapılacaklar:resim_alternatif_Metin](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Özel İfade Doğrulaması**
Özel ifade Doğrulama, geliştiricilerin girdi değerlerini doğrulamak için kendi özel normal ifadelerini yazmalarına olanak tanır. Özel bir ifade doğrulaması oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışma sayfasına erişin.
1. Doğrulama oluşturmak için hücreye erişin.
1. Hücre için bir doğrulama oluşturun ve türü CustomExpression olarak belirtin.
1. Doğrulamanın normal ifadesini ayarlayın.

Örnek kod, C1'e özel bir ifade doğrulaması ekler. Kullanıcılar, hücreye yalnızca normal ifade tarafından belirtilen biçime göre bir tarih ekleyebilir.

**Düzenli bir ifadeye göre C1'e tarih değeri ekleme** 

![yapılacaklar:resim_alternatif_Metin](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Zorunlu Doğrulama**
Aspose.Cells.GridWeb'i kullanarak, kullanıcılar giriş verilerini bir sunucuya gönderebilir. Farklı hücreler için doğrulama kuralları olsa da, ancak GridWeb kontrolünün ForceValidation özelliği doğru olarak ayarlanmamış olsa bile, yanlış olan giriş verileri de sunucuya gönderilir ve doğrulama yapılmaya zorlanmaz. GridWeb'in ForceValidation özelliği varsayılan olarak her zaman true olarak ayarlanmıştır.

 ForceValidation özelliği true olduğunda, kontrol, tüm hücrelerin giriş değerleri geçerli olana kadar verileri web sunucusuna göndermez. Örneğin, birisi bir hücreye geçersiz bir giriş değeri girerse veya bir değer girmezse, istemci tarafı doğrulama etkinleştirilir ve kullanıcılar, tıklasalar bile veri gönderemezler.**Göndermek**.

**GridWeb tarafından vurgulanan yanlış giriş değeri** 

![yapılacaklar:resim_alternatif_Metin](add-cell-validations_4.png)
