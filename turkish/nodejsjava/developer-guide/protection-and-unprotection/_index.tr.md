---
title: Korumayı Tanımla ve Kaldır
linktitle: Şifreleme ve Koruma
description: Bu bölüm, Excel dosyalarını şifreleme ve şifre çözme ile Excel verilerini koruma işlemlerini, dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruma, çalışma sayfası koruma ve dijital imzaları JavaScript kodu kullanarak ele alır
keywords: Aspose.Cells, Node.js via Java, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, JavaScript
type: docs
weight: 68
url: /tr/nodejs-java/protect-and-unprotect/
alias: [/nodejs-java/security-features/]
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, iş veya kişisel bilgiler içerir. Aspose.Cells for Node.js via Java, Microsoft Excel'in yeteneklerini yansıtan kapsamlı bir koruma özellikleri seti sunarak verilerinizi dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde güvence altına almanıza olanak tanır.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaların parola ile şifrelenmesi, değiştirme parolası aracılığıyla salt okunur erişimin zorunlu kılınması, çalışma kitabı yapısının korunması, çalışma sayfalarının korunması ve çalışma kitaplarının dijital olarak imzalanması yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasına ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `workbook.getSettings().setPassword(...)` çağrısına bir parola dizesi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifre çözme amacıyla açmak için bir `LoadOptions` nesnesi oluşturun, `loadOptions.setPassword(...)` çağrısını şifreleme sırasında kullanılan aynı parolaya ayarlayın ve bunu `Workbook` yapıcısına iletin. Aspose.Cells, sağlanan parolayı şeffaf bir şekilde uygular; böylece kodunuzun geri kalanı, dosya normal bir çalışma kitabıymış gibi şifresi çözülmüş içerikle etkileşime girebilir.

```javascript
const AsposeCells = require("aspose.cells");
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
Excel iki ayrı parola katmanını destekler. Birincisi, dosyanın kendisini şifreleyen açma parolasıdır ve önceki bölümde ele alınmıştır. İkincisi, kullanıcıların çalışma kitabını açmasını engellemeyen değiştirme parolasıdır; bunun yerine Excel, değiştirme parolası sağlanmadığı sürece dosyayı salt okunur modda açmayı önerir. Bu davranışı Aspose.Cells'de `workbook.getSettings().getWriteProtection()` aracılığıyla yapılandırın. `Password` özelliğini değiştirme parolasına ve `Author` özelliğini korumayı kimin uyguladığını belirtecek şekilde ayarlayın. Sağlanan değiştirme parolasının doğru olup olmadığını kontrol etmek için `writeProtection.validatePassword(string)` yöntemini kullanın; eşleşme durumunda `true`, aksi takdirde `false` döndürür.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
// Yazma korumasını yapılandır: değiştirme parolasını ve yazarı ayarla
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
// Çalışma kitabını, yazma korumasının kalıcı olması için kaydet
workbook.save("WriteProtectedWorkbook.xlsx");
// Doğru parolayı kullanarak değiştirme parolasını doğrula
let isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
console.log("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Diğer dalı göstermek için yanlış bir parola kullanarak değiştirme parolasını doğrula
let isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
console.log("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısının korunması, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korumalı durum, herhangi bir sayfadaki hücre içeriklerinden ziyade sayfa yapısı için geçerlidir. Yapı koruması uygulamak için `workbook.protect(ProtectionType.Structure, "password")` çağırın. Korumayı kaldırmak için `workbook.unprotect("password")` çağırın ve doğru parolayı sağlayın. Burada `ProtectionType.Structure` enum değeri kullanılmıştır ve `ProtectionType.Windows` gibi diğer koruma türlerinden farklıdır.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
// İkinci bir çalışma sayfası ekle
workbook.getWorksheets().add();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Çalışma kitabı yapısını koru
workbook.protect(AsposeCells.ProtectionType.STRUCTURE, "StructPwd");
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
Çalışma sayfası koruma, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı değişikliklere karşı kilitler. Kullanıcılar, parolayı sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için kullanılan tipik koruma biçimidir. Bir çalışma sayfasını korumak için `worksheet.protect(ProtectionType.All, "password")` çağırın. `ProtectionType.All` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.unprotect("password")` çağırın ve doğru parolayı sağlayın. `Contents`, `Objects` ve `Scenarios` gibi diğer koruma türlerini bitsel VEYA kullanarak birleştirerek daha ayrıntılı denetim sağlanabilir.

```javascript
const AsposeCells = require("aspose.cells");
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(AsposeCells.ProtectionType.ALL, "SheetPwd");
workbook.save("sheet_protected.xlsx");
let workbookReloaded = new AsposeCells.Workbook("sheet_protected.xlsx");
let sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
console.log("Worksheet protection removed successfully.");
```

## Dijital imzaları ekleme ve doğrulama
Bir dijital imza, alıcılara çalışma kitabı içeriğinin orijinal olduğunu ve imzalanmasından bu yana değiştirilmediğini garanti eder. Aspose.Cells, `AsposeCells.DigitalSignature` ve `AsposeCells.DigitalSignatureCollection` gibi sınıflar aracılığıyla dijital imza desteği sağlar. Tipik iş akışı, bir `.pfx` sertifika dosyasından doğrudan parolası ve imza yorumlarıyla birlikte bir `AsposeCells.DigitalSignature` oluşturur, imzayı bir `DigitalSignatureCollection`'a ekler ve koleksiyonu `workbook.addDigitalSignature(DigitalSignatureCollection)` yoluyla çalışma kitabına uygular. `DigitalSignature.Comments` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar; bu nedenle alıcı tarafta bir doğrulama adımı tahrifatı tespit edebilir.

```javascript
const AsposeCells = require("aspose.cells");
let signature = new AsposeCells.DigitalSignature("signature.pfx", "pfx-password", "Signed by Aspose.Cells", new Date());
let signatures = new AsposeCells.DigitalSignatureCollection();
signatures.add(signature);
let workbook = new AsposeCells.Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
console.log("The workbook has been digitally signed.");
```

{{< app/cells/assistant language="nodejs-java" >}}