---
title: Node.js ile C++ kullanarak Koruma ve Korumayı Kaldırma
linktitle: Şifreleme ve Koruma
description: Bu bölüm, Excel dosyalarını şifreleme ve şifre çözme ile Excel verilerini koruma yöntemlerini tanıtır; dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruması, çalışma sayfası koruması ve JavaScript kodu kullanılarak dijital imzaları kapsar
keywords: Aspose.Cells, Node.js, C++, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, JavaScript
type: docs
weight: 68
url: /tr/nodejs-cpp/protect-and-unprotect/
alias: [/nodejs-cpp/security-features/]
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, iş veya kişisel bilgiler içerir. Aspose.Cells for Node.js via C++, Microsoft Excel'in yeteneklerini yansıtan kapsamlı bir koruma özellikleri seti sunar ve verilerinizi dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde güvence altına almanıza olanak tanır.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaları parola ile şifreleme, değiştirme parolası aracılığıyla salt okunur erişimi zorunlu kılma, çalışma kitabı yapısını koruma, çalışma sayfalarını koruma ve çalışma kitaplarını dijital olarak imzalama yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasında ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `workbook.getSettings().setPassword()` yöntemine bir parola dizesi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifre çözme amacıyla açmak için bir `LoadOptions` nesnesi oluşturun, `loadOptions.setPassword()` yöntemini şifreleme sırasında kullanılan parolayla ayarlayın ve bunu `Workbook` yapıcısına geçirin. Aspose.Cells, sağlanan parolayı saydam bir şekilde uygular; böylece kodunuzun geri kalanı, dosya normal bir çalışma kitabıymış gibi şifresi çözülmüş içerikle etkileşime girebilir.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
let cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
let loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("OpenPassword123");
let decryptedWorkbook = new AsposeCells.Workbook("encrypted.xlsx", loadOptions);
console.log("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Salt okunur koruma (değiştirme parolası)
Excel iki farklı parola katmanını destekler. İlki açma parolasıdır; dosyanın kendisini şifreler ve önceki bölümde ele alınmıştır. İkincisi ise değiştirme parolasıdır; kullanıcıların çalışma kitabını açmasını engellemez, bunun yerine Excel, değiştirme parolası sağlanmadığı sürece dosyayı salt okunur modda açmayı önerir. Bu davranışı Aspose.Cells'te `workbook.getSettings().getWriteProtection()` aracılığıyla yapılandırın. `password` özelliğini değiştirme parolasına ve `author` özelliğini korumayı uygulayan kişiyi tanımlayacak şekilde ayarlayın. Sağlanan bir değiştirme parolasının doğru olup olmadığını kontrol etmek için `writeProtection.validatePassword(string)` yöntemini kullanın; eşleşme durumunda `true`, aksi takdirde `false` döndürür.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Yazma korumasını yapılandır: değiştirme parolasını ve yazarı ayarla
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Yazma korumasının kalıcı olması için çalışma kitabını kaydet
workbook.save("WriteProtectedWorkbook.xlsx");
// Doğru parolayı kullanarak değiştirme parolasını doğrula
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Diğer dalı göstermek için yanlış bir parola kullanarak değiştirme parolasını doğrula
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısını korumak, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korumalı durum, sayfa yapısı için geçerlidir; herhangi bir sayfadaki hücre içerikleri için değil. Yapı koruması uygulamak için `workbook.protect(ProtectionType.Structure, "password")` yöntemini çağırın. Korumayı kaldırmak için `workbook.unprotect("password")` yöntemini çağırın ve doğru parolayı sağlayın. Burada `ProtectionType.Structure` enum değeri kullanılmıştır ve `ProtectionType.Windows` gibi diğer koruma türlerinden farklıdır.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
// İkinci bir çalışma sayfası ekle
workbook.getWorksheets().add();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Çalışma kitabı yapısını koru
workbook.protect(AsposeCells.ProtectionType.Structure, "StructPwd");
// Çalışma kitabını structure_protected.xlsx olarak kaydet
let filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Dosyayı yeni bir Workbook örneğine yeniden yükle
let loadedWorkbook = new AsposeCells.Workbook(filePath);
// Yapı korumasını kaldır
loadedWorkbook.unprotect("StructPwd");
// Onay mesajını yazdır
console.log("Structure protection has been successfully removed from the workbook.");
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı olarak yapılan değişikliklere karşı kilitler. Kullanıcılar, parola sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için kullanılan tipik koruma yöntemidir. Bir çalışma sayfasını korumak için `worksheet.protect(ProtectionType.All, "password")` yöntemini çağırın. `ProtectionType.All` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.unprotect("password")` yöntemini doğru parolayla çağırın. Bit düzeyinde VEYA kullanılarak `Contents`, `Objects` ve `Scenarios` gibi diğer koruma türleri birleştirilerek daha ayrıntılı denetim sağlanabilir.

```javascript
const AsposeCells = require("aspose.cells.node");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.All, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Dijital imzaları ekleme ve doğrulama
Dijital imza, alıcılara çalışma kitabı içeriğinin gerçek olduğunu ve imzalandığından beri değiştirilmediğini garanti eder. Aspose.Cells, `Aspose.Cells.DigitalSignatures` ad alanı aracılığıyla dijital imza desteği sağlar. Tipik iş akışı, Node.js crypto yardımcı programlarını kullanarak bir `.pfx` sertifika dosyasını yükler, bunu bir `Aspose.Cells.DigitalSignatures.DigitalSignature` içinde sarar, imzayı bir `DigitalSignatureCollection` öğesine ekler ve koleksiyonu `workbook.addDigitalSignature(digitalSignatureCollection)` aracılığıyla çalışma kitabına uygular. `digitalSignature.comments` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar; bu nedenle alıcı tarafta yapılan bir doğrulama adımıyla tahrifat tespit edilebilir.

```javascript
const AsposeCells = require("aspose.cells.node");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

## İlgili Makaleler
- [Excel dosyalarını şifreleme ve şifre çözme](/cells/tr/nodejs-cpp/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/nodejs-cpp/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/nodejs-cpp/protect-and-unprotect-worksheets/)
- [Paylaşılan Çalışma Kitabını Parola ile Koruma veya Korumayı Kaldırma](/cells/tr/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Dijital İmzaları Atama ve Doğrulama](/cells/tr/nodejs-cpp/assign-and-validate-digital-signatures/)
- [Aspose.Cells kullanarak Değiştirme Parolasını Kontrol Etme](/cells/tr/nodejs-cpp/check-password-to-modify-using-aspose-cells/)
- [Şifrelenmiş Office Open XML - OOXML Dosyalarının Dosya Biçimini Algılama](/cells/tr/nodejs-cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel Dosyalarını Şifreleme](/cells/tr/nodejs-cpp/encrypting-excel-files/)
- [Bir Dosya Biçimini Algılama ve Dosyanın Şifrelenmiş olup olmadığını Kontrol Etme](/cells/tr/nodejs-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="nodejs-cpp" >}}