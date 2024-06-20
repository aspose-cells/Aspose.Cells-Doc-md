---
title: Hücre Doğrulamalarını Ekleyin
type: docs
weight: 70
url: /tr/net/aspose-cells-gridweb/add-cell-validations/
keywords: GridWeb,GridValidation,liste doğruluma,özel ifade doğruluma
description: Bu makale, GridWeb de liste doğrulama, açılır liste doğrulama ve özel ifade doğrulama eklemenin nasıl yapılacağını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb'ün gelişmiş özelliklerinden biri, hücreler için giriş doğrulama kuralları eklemektir. Geliştiriciler, giriş değerlerini kontrol etmek ve doğrulamak için hücreler için farklı tiplerde doğrulama kuralları oluşturabilir. Bu konu, desteklenen doğrulama tiplerini ve bunları nasıl oluşturacaklarını ele almaktadır.

{{% /alert %}} 
## **Doğrulama Türleri**
Aspose.Cells.GridWeb kullanarak uygulanabilecek üç çeşit doğrulama vardır:

- Liste doğrulama.
- Açılır liste doğrulama.
- Özel ifade doğrulama.

Her biri aşağıda detaylı olarak ele alınmaktadır.
### **Liste Doğrulama**
Liste doğrulama, kullanıcıların hücre girişini yazarak veya bir menüden bir değer seçerek yapmasına olanak tanır. Bir hücre için liste doğrulama oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Geçerlilik eklemek için hücreye erişin.
1. Hücre için geçerliliği oluşturun ve doğrulama türünü Liste olarak belirtin.
1. Liste geçerliliği için değerler ekleyin.

Örnek kod, C1'e liste geçerliliği ekler. Kullanıcı hücreye tıkladığında bir liste görünür.

**Çıktı: listeden bir değer seçme** 

![todo:image_alt_text](add-cell-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddListValidation.aspx-AddListValidation.cs" >}}
### **Açılır Liste Doğrulaması**
Açılır liste doğrulaması, kullanıcıların önceden tanımlanmış bir listeden bir değer seçerek hücrelere giriş yapmasını sağlar. Açılır liste doğrulaması oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Doğrulama oluşturmak için hücreye erişin.
1. Hücre için doğrulama oluşturun ve türü AçılırListe olarak belirtin.
1. Doğrulama için değerler ekleyin.

Örnek kod, C1'e açılır liste doğrulaması ekler. Kullanıcı hücreye tıkladığında bir açılır liste görünür ve kullanıcılar bundan bir değer seçebilir.

**Açılır listeden bir değer seçme** 

![todo:image_alt_text](add-cell-validations_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDropdownListValidation.aspx-AddDropDownListValidation.cs" >}}
### **Özel İfade Doğrulaması**
Özel ifade doğrulaması, geliştiricilere kendi özel düzenli ifadelerini kullanarak girdi değerlerini doğrulamalarına izin verir. Özel ifade doğrulaması oluşturmak için:

1. Aspose.Cells.GridWeb denetimini bir Web Formuna ekleyin.
1. Bir çalışsayı açın.
1. Doğrulama oluşturmak için hücreye erişin.
1. Hücre için doğrulama oluşturun ve türü Özelİfade olarak belirtin.
1. Doğrulamanın düzenli ifadesini belirleyin.

Örnek kod, C1'e özel ifade doğrulaması ekler. Kullanıcılar, belirtilen düzenli ifade formatına uygun olarak sadece bir tarih girebilirler.

**Düzenli ifadeye göre C1'e tarih değeri ekleniyor** 

![todo:image_alt_text](add-cell-validations_3.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddCustomValidation.aspx-AddCustomValidation.cs" >}}
### **Doğrulamayı Zorlama**
Aspose.Cells.GridWeb kullanarak, kullanıcılar giriş verilerini bir sunucuya gönderebilir. Farklı hücreler için doğrulama kuralları olsa bile GridWeb denetiminin ForceValidation özelliği true olarak ayarlanmazsa, yanlış giriş verileri de sunucuya gönderilir ve doğrulama zorlanmaz. GridWeb'in ForceValidation özelliği daima varsayılan olarak true olarak ayarlanmıştır.

ForceValidation özelliği true olduğunda, kontrol, tüm hücrelerin giriş değerleri geçerli olana kadar verileri web sunucusuna göndermez. Örneğin, birisi bir hücreye geçersiz bir giriş değeri girerse veya bir değer girmeyi unutursa, istemci tarafı doğrulama etkinleştirilir ve kullanıcılar **Gönder** düğmesine tıklasalar bile veri gönderemezler.

**GridWeb tarafından vurgulanan yanlış giriş değeri** 

![todo:image_alt_text](add-cell-validations_4.png)
