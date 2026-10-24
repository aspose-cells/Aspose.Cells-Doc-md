---
title: Korumayı Tanımla ve Kaldır
linktitle: Şifreleme ve Koruma
type: docs
weight: 68
url: /tr/net/protect-and-unprotect/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
alias: [/net/security-features/]
description: Bu bölüm, Excel dosyalarını şifreleme ve şifresini çözme ile Excel verilerini koruma yöntemlerini, dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruma, çalışma sayfası koruma ve C# kodu kullanarak dijital imzalar konularını ele almaktadır
keywords: Aspose.Cells, .NET, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, C#
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, ticari veya kişisel bilgiler içerir. Aspose.Cells for .NET, Microsoft Excel'in yeteneklerini yansıtan kapsamlı bir koruma özellikleri seti sunar ve verilerinizi dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde güvence altına almanıza olanak tanır.

{{% alert color="primary" %}}
Aspose.Cells for .NET, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaları parolayla şifreleme, değiştirme parolası aracılığıyla salt okunur erişimi zorunlu kılma, çalışma kitabı yapısını koruma, çalışma sayfalarını koruma ve çalışma kitaplarını dijital olarak imzalama yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifresini çözme
Bir Excel dosyasına ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `Workbook.Settings.Password` özelliğine bir parola dizesi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifresini çözmek üzere açmak için bir `LoadOptions` nesnesi oluşturun, `LoadOptions.Password` özelliğini şifreleme sırasında kullanılan parolayla aynı olacak şekilde ayarlayın ve bunu `Workbook` yapıcısına iletin. Aspose.Cells, sağlanan parolayı saydam bir şekilde uygular; böylece kodunuzun geri kalanı, dosya normal bir çalışma kitabıymış gibi şifresi çözülmüş içerikle etkileşim kurabilir.

```csharp
using System;
using Aspose.Cells;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cell cell = sheet.Cells["A1"];
cell.PutValue("Confidential Data");
workbook.Settings.Password = "OpenPassword123";
workbook.Save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.Password = "OpenPassword123";
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
Console.WriteLine("Decrypted cell A1 value: " + decryptedWorkbook.Worksheets[0].Cells["A1"].StringValue);
```

## Salt okunur koruma (değiştirme parolası)
Excel iki ayrı parola katmanını destekler. Birincisi, dosyanın kendisini şifreleyen açma parolasıdır ve bu önceki bölümde ele alınmıştır. İkincisi, kullanıcıların çalışma kitabını açmasını engellemeyen değiştirme parolasıdır; bunun yerine Excel, değiştirme parolası sağlanmadığı sürece dosyayı salt okunur modda açmayı önerir. Bu davranışı Aspose.Cells'de `Workbook.Settings.WriteProtection` üzerinden yapılandırın. `Password` özelliğini değiştirme parolası olarak ve `Author` özelliğini korumayı kimin uyguladığını tanımlamak için ayarlayın. Sağlanan değiştirme parolasının doğru olup olmadığını kontrol etmek için `WriteProtection.ValidatePassword(string)` yöntemini kullanın; eşleşme durumunda `true`, aksi durumda `false` döndürür.

```csharp
using System;
using Aspose.Cells;
// Sıfırdan yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Data");
// Yazma korumasını yapılandır: değiştirme parolasını ve yazarı ayarla
workbook.Settings.WriteProtection.Password = "ModifyPwd";
workbook.Settings.WriteProtection.Author = "AuthorName";
// Yazma korumasının kalıcı olması için çalışma kitabını kaydet
workbook.Save("WriteProtectedWorkbook.xlsx");
// Doğru parolayı kullanarak değiştirme parolasını doğrula
bool isCorrectValid = workbook.Settings.WriteProtection.ValidatePassword("ModifyPwd");
Console.WriteLine("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
// Diğer dalı göstermek için yanlış bir parola kullanarak değiştirme parolasını doğrula
bool isWrongValid = workbook.Settings.WriteProtection.ValidatePassword("WrongPwd");
Console.WriteLine("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısını korumak, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korunan durum, herhangi bir sayfadaki hücre içerikleri yerine sayfa yapısı için geçerlidir. Yapı koruması uygulamak için `workbook.Protect(ProtectionType.Structure, "password")` yöntemini çağırın. Korumayı kaldırmak için `workbook.Unprotect("password")` yöntemini çağırın ve doğru parolayı sağlayın. Burada kullanılan `ProtectionType.Structure` enum değeri, `ProtectionType.Windows` gibi diğer koruma türlerinden farklıdır.

```csharp
using System;
using Aspose.Cells;
// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
// İkinci bir çalışma sayfası ekle
workbook.Worksheets.Add();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.Worksheets[0].Cells[0, 0].PutValue("Sample Data");
// Çalışma kitabının yapısını koru
workbook.Protect(ProtectionType.Structure, "StructPwd");
// Çalışma kitabını structure_protected.xlsx olarak kaydet
string filePath = "structure_protected.xlsx";
workbook.Save(filePath);
// Dosyayı yeni bir Workbook örneğine yeniden yükle
Workbook loadedWorkbook = new Workbook(filePath);
// Yapı korumasını kaldır
loadedWorkbook.Unprotect("StructPwd");
// Onay mesajını yazdır
Console.WriteLine("Structure protection has been successfully removed from the workbook.");
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı değişikliklere karşı kilitler. Kullanıcılar, parola sağlamadan kilitli hücreleri düzenleyemez. Bu koruma, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için tipik olarak kullanılır. Bir çalışma sayfasını korumak için `worksheet.Protect(ProtectionType.All, "password")` yöntemini çağırın. `ProtectionType.All` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.Unprotect("password")` yöntemini doğru parolayla çağırın. Daha ayrıntılı kontrol, `Contents`, `Objects` ve `Scenarios` gibi diğer koruma türlerinin bitsel VEYA kullanılarak birleştirilmesiyle sağlanır.

```csharp
using System;
using Aspose.Cells;
var workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
sheet.Cells["A1"].PutValue("Sample Data");
sheet.Protect(ProtectionType.All, "SheetPwd");
workbook.Save("sheet_protected.xlsx");
var workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.Worksheets[0];
sheetReloaded.Unprotect("SheetPwd");
Console.WriteLine("Worksheet protection removed successfully.");
```

## Dijital imzaları ekleme ve doğrulama
Dijital imza, alıcılara çalışma kitabı içeriğinin gerçek olduğunu ve imzalandıktan sonra değiştirilmediğini garanti eder. Aspose.Cells, `Aspose.Cells.DigitalSignatures` ad alanı aracılığıyla dijital imza desteği sağlar. Tipik iş akışı, `System.Security.Cryptography.X509Certificates.X509Certificate2` aracılığıyla bir `.pfx` sertifika dosyasını yükler, bunu bir `Aspose.Cells.DigitalSignatures.DigitalSignature` içine sarar, imzayı bir `DigitalSignatureCollection` öğesine ekler ve koleksiyonu `Workbook.AddDigitalSignature(DigitalSignatureCollection)` aracılığıyla çalışma kitabına uygular. `DigitalSignature.Comments` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar; bu nedenle alıcı taraftaki bir doğrulama adımıyla kurcalama tespit edilebilir.

```csharp
using System;
using System.IO;
using System.Security.Cryptography.X509Certificates;
using Aspose.Cells;
using Aspose.Cells.DigitalSignatures;
X509Certificate2 certificate = new X509Certificate2("signature.pfx", "pfx-password");
DigitalSignature signature = new DigitalSignature(certificate, "Signed by Aspose.Cells", DateTime.Now);
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.Add(signature);
Workbook workbook = new Workbook();
workbook.Worksheets[0].Cells["A1"].PutValue("Sample Value");
workbook.AddDigitalSignature(signatures);
workbook.Save("signed_workbook.xlsx");
Console.WriteLine("The workbook has been digitally signed.");
```

## İlgili Makaleler
- [Excel dosyalarını şifreleme ve şifrelerini çözme](/cells/tr/net/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/net/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/net/protect-and-unprotect-worksheets/)
- [Paylaşılan Çalışma Kitabını Parola ile Koruma veya Korumayı Kaldırma](/cells/tr/net/password-protect-or-unprotect-the-shared-workbook/)
- [Dijital İmzaları Atama ve Doğrulama](/cells/tr/net/assign-and-validate-digital-signatures/)
- [Aspose.Cells kullanarak Değiştirme Parolasını Kontrol Etme](/cells/tr/net/check-password-to-modify-using-aspose-cells/)
- [Şifrelenmiş Office Open XML - OOXML Dosyalarının Dosya Biçimini Algılama](/cells/tr/net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel Dosyalarını Şifreleme](/cells/tr/net/encrypting-excel-files/)
- [Bir Dosya Biçimi Nasıl Algılanır ve Dosyanın Şifrelenmiş Olup Olmadığı Nasıl Kontrol Edilir](/cells/tr/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="csharp" >}}