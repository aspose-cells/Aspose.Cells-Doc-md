---
title: Çalışma Sayfalarında Doğrulamalarla Çalışmak
type: docs
weight: 70
url: /tr/net/aspose-cells-griddesktop/work-with-validations-in-worksheets/
keywords: GridDesktop, doğrulamalar, doğrulama
description: Bu makale, GridDesktop ta doğrulama ile nasıl çalışılacağını tanıtır.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop ayrıca çalışma sayfasının hücrelerine doğrulamalar (veya doğrulama kuralları) eklemeyi destekler. Doğrulama kurallarını hücrelere uygulayarak, geliştiriciler kullanıcıların Grid'e belirli bir formatta veri girmesini kısıtlayabilir. Aspose.Cells.GridDesktop tarafından farklı doğrulama modları desteklenmektedir. Bu konuda, yalnızca bu doğrulama modları hakkında değil, aynı zamanda bu doğrulamaların nasıl manipüle edileceği hakkında da konuşacağız.

{{% /alert %}} 
## **Doğrulama Modları**
Aspose.Cells.GridDesktop tarafından desteklenen üç doğrulama modu aşağıdaki gibidir:

- Gereklidir Doğrulama Modu
- Düzenli İfadeler Doğrulama Modu
- Özel Doğrulama Modu
### **Gereklidir Doğrulama Modu**
Bu doğrulama modunda, kullanıcılar belirtilen hücrelere değer girme konusunda kısıtlanır. Bir **Gereklidir Doğrulaması** bir çalışma sayfası hücresine uygulandığında, o hücreye değer girmek kullanıcı için zorunlu hale gelir.
### **Düzenli İfadeler Doğrulama Modu**
Bu modda, çalışma sayfası hücrelerine belirli bir formatta veri göndermek üzere kısıtlamalar uygulanır. Veri formatının deseni bir **Düzenli İfade** biçiminde sağlanır.
### **Özel Doğrulama Modu**
**Özel Doğrulama** kullanmak için, geliştiricilerin Aspose.Cells.GridDesktop.ICustomValidation arabirimini uygulaması gereklidir. Arabirim bir **Doğrula** yöntemi sağlar. Bu yöntem veri doğruysa true döndürür aksi takdirde false döndürür.
## **Aspose.Cells.GridDesktop'ta Doğrulamalarla Çalışmak**
### **Doğrulama Ekleme**
Çalışma sayfası hücresine herhangi bir doğrulama eklemek için lütfen aşağıdaki adımları takip edin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- **Çalışma Sayfası**'nın **Doğrulamalar** koleksiyonuna istenen doğrulamayı ekleyerek, hangi hücreye hangi doğrulamanın uygulanacağını belirtin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AddingValidation.cs" >}}

{{% alert color="primary" %}} 

Yukarıdaki şekilde, bu doğrulama kurallarını, bu kuralların hücrelere uygulandığı yerlerin önünde belirttik. Eğer herhangi bir geçersiz değer (o hücre için tanımlanan doğrulama kuralına uygun olmayan) girilirse, kullanıcıyı geçersiz giriş hakkında bilgilendirmek için bir **MessageBox** görünecektir.

{{% /alert %}} 
### **ICustomValidation Uygulama**
Yukarıdaki kod parçacığında, **A8** hücresine bir özel doğrulama ekledik ancak henüz bu özel doğrulamayı uygulamadık. Bu konunun başında açıkladığımız gibi özel doğrulama uygulamak için **ICustomValidation** arabirimini uygulamamız gerektiğini hatırlayalım. Bu yüzden **ICustomValidation** arabirimini uygulamak için bir sınıf oluşturmayı deneyelim.

Aşağıdaki kod parçacığında, aşağıdaki kontrolleri gerçekleştiren bir özel doğrulama uyguladık:

- Doğrulamanın eklenmiş olduğu hücre adresinin doğru olup olmadığını kontrol edin
- Hücre değerinin veri tipinin double olup olmadığını kontrol edin
- Hücre değerinin 100'den büyük olup olmadığını kontrol edin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-ImplementingICustomInterface.cs" >}}
### **Doğrulamaya Erişme**
Bir doğrulama belirli bir çalışma sayfası hücresine eklenmişse, geliştiricilerin çalışma zamanında belirli bir doğrulamanın özelliklerini erişip değiştirmesi gerekebilir. Bu görevi gerçekleştirmek için Aspose.Cells.GridDesktop, geliştiriciler için bu işlemi basit hale getirmiştir.

Belirli bir doğrulamaya erişmek için lütfen aşağıdaki adımları izleyin:

- İstenen **Çalışma Sayfasına** erişin
- Hücreye uygulanan doğrulamayı belirterek çalışma sayfasındaki belirli bir **Doğrulamaya** erişin
- İstenirse **Doğrulama** özelliklerini düzenleyin



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-AccessingValidation.cs" >}}

{{% alert color="primary" %}} 

**Doğrulamalar** koleksiyonunun iki indeksleyicisi bulunmaktadır. Aşağıdaki örnekte kullanılan bir indeksleyici, bir hücre adını endeks olarak alarak bir **Doğrulama** nesnesine erişmeye izin verirken diğer indeksleyici aynı görevi yapmak için iki parametre alır (yani satır ve sütun numaraları).

{{% /alert %}} 
### **Doğrulamayı Kaldırma**
Çalışma sayfasından belirli bir doğrulamayı kaldırmak için lütfen aşağıdaki adımları izleyin:

- İstenen **Çalışma Sayfasına** erişin
- Doğrulamanın uygulandığı hücre adını belirterek **Çalışma Sayfasından** belirli bir **Doğrulamayı** kaldırın



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ValidationInWorksheets-RemoveValidation.cs" >}}
