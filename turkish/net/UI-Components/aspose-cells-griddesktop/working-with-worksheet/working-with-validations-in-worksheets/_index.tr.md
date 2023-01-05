---
title: Çalışma Sayfalarında Doğrulamalarla Çalışma
type: docs
weight: 70
url: /tr/net/working-with-validations-in-worksheets/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop, bir çalışma sayfasının hücrelerine doğrulama (veya doğrulama kuralları) eklemeyi de destekler. Geliştiriciler, hücrelere doğrulama kuralları uygulayarak, kullanıcıların Grid'e belirli bir biçimde veri girmesini kısıtlayabilir. Farklı doğrulama modları Aspose.Cells.GridDesktop tarafından desteklenir. Bu konuda, yalnızca bu doğrulama modlarını tartışmayacağız, aynı zamanda bu doğrulamaların manipülasyonunu da açıklayacağız.

{{% /alert %}} 
## **Doğrulama Modları**
Aspose.Cells.GridDesktop tarafından aşağıdaki gibi desteklenen üç doğrulama modu vardır:

- Gerekli Doğrulama Modu
- Normal İfadeler Doğrulama Modu
- Özel Doğrulama Modu
### **Gerekli Doğrulama Modu**
 Bu doğrulama modunda, kullanıcıların belirtilen hücrelere değer girmeleri kısıtlanır. Bir kere**Doğrulama Gerekli mi** bir çalışma sayfası hücresine uygulandığında, kullanıcının o hücreye değer girmesi zorunlu hale gelir.
### **Normal İfadeler Doğrulama Modu**
 Bu modda, kullanıcıların verileri hücrelere belirli bir biçimde göndermeleri için çalışma sayfası hücrelerine kısıtlamalar uygulanır. Veri formatının kalıbı bir formda sağlanır.**Düzenli ifade**.
### **Özel Doğrulama Modu**
 Kullanmak**Özel Doğrulama** , Geliştiricilerin Aspose.Cells.GridDesktop.ICustomValidation arabirimini uygulaması zorunludur. Arayüz bir sağlar**Doğrula** yöntem. Bu yöntem, veri geçerliyse doğru, aksi takdirde yanlış döndürür.
## **Aspose.Cells.GridDesktop'ta Doğrulamalarla Çalışma**
### **Doğrulama Ekleme**
Bir çalışma sayfası hücresine herhangi bir doğrulama türü eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
-  İstenen bir doğrulamayı şuraya ekleyin:**Doğrulamalar** koleksiyonu**Çalışma kağıdı** hangi hücreye hangi doğrulamanın uygulanacağını belirtmek için.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

 Yukarıdaki şekilde, bu doğrulama kurallarının uygulandığı hücrelerin önünde doğrulama kurallarından da bahsetmiştik. Geçersiz bir değer (o hücre için tanımlanan doğrulama kuralına göre geçerli olmayan) girilirse,**Mesaj Kutusu** kullanıcıyı geçersiz giriş hakkında bilgilendiriyor gibi görünür.

{{% /alert %}} 
### **ICustomValidation'ı Uygulama**
 Yukarıdaki kod parçacığında, içine özel bir doğrulama ekledik.**A8**cell, ancak bu özel doğrulamayı henüz uygulamadık. Bu konunun başında açıkladığımız gibi, özel doğrulama uygulamak için uygulamamız gerekir.**Özel Doğrulama** arayüz. Öyleyse, uygulamak için bir sınıf oluşturmayı deneyelim**Özel Doğrulama** arayüz.

Aşağıda verilen kod parçacığında, aşağıdaki kontrolleri gerçekleştirmek için özel bir doğrulama uyguladık:

- Doğrulamanın eklendiği hücrenin adresinin doğru olup olmadığını kontrol edin
- Hücrenin değerinin veri türünün çift olup olmadığını kontrol edin
- Hücrenin değerinin 100'den büyük olup olmadığını kontrol edin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Doğrulamaya Erişim**
Belirli bir çalışma sayfası hücresine bir doğrulama eklendiğinde, geliştiricilerin çalışma zamanında belirli bir doğrulamanın özniteliklerine erişmesi ve bunları değiştirmesi gerekebilir. Aspose.Cells.GridDesktop, geliştiricilerin bu görevi gerçekleştirmesini kolaylaştırdı.

Belirli bir doğrulamaya erişmek için lütfen aşağıdaki adımları izleyin:

-  İstenilen erişim**Çalışma kağıdı**
-  Belirli bir erişim**Doğrulama**doğrulamanın uygulandığı hücre adını belirterek çalışma sayfasında
-  Düzenlemek**Doğrulama** İstenirse nitelikler



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Doğrulamalar** koleksiyonun iki indeksleyicisi vardır. Bir indeksleyici (aşağıdaki örnekte kullanılan), bir**Doğrulama** diğer dizin oluşturucu aynı görevi gerçekleştirmek için iki parametre (yani satır ve sütun numaraları) alırken, bir hücre adını dizini olarak alarak nesne.

{{% /alert %}} 
### **Doğrulamayı Kaldırma**
Belirli bir doğrulamayı çalışma sayfasından kaldırmak için lütfen aşağıdaki adımları izleyin:

-  İstenilen erişim**Çalışma kağıdı**
-  Belirli bir öğeyi kaldır**Doğrulama** dan**Çalışma kağıdı** doğrulamanın uygulandığı hücre adını belirterek



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
