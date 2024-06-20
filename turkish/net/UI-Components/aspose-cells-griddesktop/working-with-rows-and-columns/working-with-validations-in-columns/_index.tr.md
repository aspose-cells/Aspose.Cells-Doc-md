---
title: Sütunlarda Doğrulamalarla Çalışma
type: docs
weight: 80
url: /tr/net/aspose-cells-griddesktop/work-with-validations-in-columns/
keywords: GridDesktop, doğrulama, doğrulamalar
description: Bu makale, GridDesktop ta sütunlardaki doğrulamaların nasıl kullanılacağını tanıtıyor.
---

{{% alert color="primary" %}} 

Önceki konularımızdan birinde, doğrulamaları tartışmıştık ancak bu, [Çalışsayfalardaki Doğrulamalar](/cells/tr/net/working-with-validations-in-worksheets/) bağlamında yapılmıştı (doğrulama ve doğrulama modları hakkında genel bilgi için geliştiriciler bu konuya başvurabilir). Bu konuda, sütunlarla ilgili olarak doğrulamaları açıklayacağız. Bu özellik kullanılarak, geliştiricilerin çalışsayfanın herhangi bir sütununa bir doğrulama kuralı uygulamaları mümkündür. Detayı inceleyelim.

{{% /alert %}} 
## **Sütun Doğrulaması Ekleme**
Bir sütuna herhangi bir doğrulama eklemek için lütfen aşağıdaki adımları izleyin:

- **Form**'unuza Aspose.Cells.GridDesktop kontrolünü ekleyin
- Herhangi bir istenen **Çalışma Sayfası**'na erişin
- Herhangi bir sütuna istenen doğrulamayı **Ekleyin**

**ÖNEMLİ:** Daha fazla bilgi için (veya **Zorunlu Doğrulama**, **Düzenli İfade Doğrulama** ve **Özel Doğrulama** gibi doğrulama modları) ve **Özel Doğrulama** uygulamak için lütfen [Çalışma Sayfalarındaki Doğrulamalarla Çalışma](/cells/tr/net/working-with-validations-in-worksheets/) sayfasına bakın.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithRowsandColumns-WorkingWithColumnValidations-AddValidation.cs" >}}
## **Sütun Doğrulamasına Erişme**
Belirli bir sütun doğrulamasına erişmek için lütfen aşağıdaki adımları takip edin:

- İstenen **Çalışma Sayfasına** erişin
- **Çalışma Sayfası** içinde belirli bir sütun **Doğrulamasına** erişin
- İstenirse **Doğrulama** özelliklerini düzenleyin



{{< highlight csharp >}}

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
Çalışma sayfasından belirli bir sütun doğrulamasını kaldırmak için lütfen aşağıdaki adımları takip edin:

- İstenen **Çalışma Sayfasına** erişin
- **Çalışma Sayfası** içinde belirli bir sütun **Doğrulamasını** kaldırın



{{< highlight csharp >}}

 //Accessing first worksheet of the Grid

Worksheet sheet = gridDesktop1.Worksheets[0];

//Removing the Validation applied on a specific column

sheet.Columns[2].RemoveValidation();

{{< /highlight >}}
