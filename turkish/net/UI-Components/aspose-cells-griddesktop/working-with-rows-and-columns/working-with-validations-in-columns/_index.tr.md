---
title: Sütunlardaki Doğrulamalarla Çalışma
type: docs
weight: 80
url: /tr/net/working-with-validations-in-columns/
---
{{% alert color="primary" %}} 

 Önceki konularımızdan birinde doğrulamalar hakkında tartışmıştık ancak bu,[Çalışma Sayfalarındaki Doğrulamalar](/cells/tr/net/working-with-validations-in-worksheets/) (doğrulama ve doğrulama modları hakkında genel bilgi sahibi olmak için, geliştiriciler bu konuya başvurabilir). Bu konuda doğrulamaları sütunlara göre açıklayacağız. Bu özelliği kullanarak, geliştiricilerin çalışma sayfasının herhangi bir sütununa bir doğrulama kuralı uygulaması mümkündür. Ayrıntılı olarak tartışalım.

{{% /alert %}} 
## **Sütun Doğrulaması Ekleme**
Bir sütuna herhangi bir doğrulama türü eklemek için lütfen aşağıdaki adımları izleyin:

-  Aspose.Cells.GridDesktop kontrolünü ekleyin.**Biçim**
-  İstediğiniz herhangi birine erişin**Çalışma kağıdı**
- **Ekle** istenilen**Doğrulama** herhangi bir sütuna

**ÖNEMLİ:**Doğrulama türleri (veya doğrulama modları gibi) hakkında daha fazla bilgi için**Doğrulama Gerekli mi**, **Normal İfadeler Doğrulaması** ve**Özel Doğrulama** ) ve uygulanması**Özel Doğrulama** , bakınız[Çalışma Sayfalarında Doğrulamalarla Çalışma.](/cells/tr/net/working-with-validations-in-worksheets/)



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Sütun Doğrulamasına Erişim**
Belirli bir sütun doğrulamasına erişmek için lütfen aşağıdaki adımları izleyin:

-  İstenilen erişim**Çalışma kağıdı**
-  Belirli bir sütuna erişme**Doğrulama** içinde**Çalışma kağıdı**
-  Düzenlemek**Doğrulama** İstenirse nitelikler



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Accessing the Validation object applied on a specific column

Validation validation = sheet.Columns[2].Validation;

//Editing the attributes of Validation

validation.IsRequired = true;

validation.RegEx = "";

validation.CustomValidation = null;

{{< /highlight >}}
## **Sütun Doğrulamasını Kaldırma**
Çalışma sayfasından belirli bir sütun doğrulamasını kaldırmak için lütfen aşağıdaki adımları izleyin:

-  İstenilen erişim**Çalışma kağıdı**
-  Belirli bir sütunu kaldır**Doğrulama** dan**Çalışma kağıdı**



{{< highlight "csharp" >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
