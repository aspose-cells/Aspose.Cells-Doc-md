---
title: Excel dosyalarını şifrele, şifreyi çöz, koru ve korumasız bırak
linktitle: Şifreleme ve Koruma
description: Bu bölüm, Excel dosyalarını şifrelemeyi ve şifresini çözmeyi, Excel verilerini korumayı tanıtır; dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruması, çalışma sayfası koruması ve Java koduyla dijital imzaları kapsar
keywords: Aspose.Cells, Java, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza
type: docs
weight: 68
url: /tr/java/protect-and-unprotect/
alias: [/java/security-features/]
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, ticari veya kişisel bilgiler depolar. Aspose.Cells for Java, Microsoft Excel'in yeteneklerini yansıtan kapsamlı bir koruma özellikleri seti sunarak verilerinizi dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde güvence altına almanızı sağlar.

{{% alert color="primary" %}}
Aspose.Cells for Java, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaları parola ile şifreleme, değiştirme parolası aracılığıyla salt okunur erişimi zorunlu kılma, çalışma kitabı yapısını koruma, çalışma sayfalarını koruma ve çalışma kitaplarını dijital olarak imzalama yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasında ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `Workbook.Settings.Password` alanına (`workbook.getSettings().setPassword(...)` aracılığıyla erişilen) bir parola dizgisi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifreli bir çalışma kitabını şifre çözme amacıyla açmak için bir `LoadOptions` nesnesi oluşturun, `LoadOptions.Password` alanını (`loadOptions.setPassword(...)` aracılığıyla) şifreleme sırasında kullanılan aynı parolaya ayarlayın ve `Workbook` yapıcısına iletin. Aspose.Cells, sağlanan parolayı saydam olarak uygular, böylece kodunuzun geri kalanı şifresi çözülmüş içerikle dosya normal bir çalışma kitabıymış gibi etkileşim kurabilir.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cell cell = sheet.getCells().get("A1");
cell.putValue("Confidential Data");
workbook.getSettings().setPassword("OpenPassword123");
workbook.save("encrypted.xlsx");
LoadOptions loadOptions = new LoadOptions();
loadOptions.setPassword("OpenPassword123");
Workbook decryptedWorkbook = new Workbook("encrypted.xlsx", loadOptions);
System.out.println("Decrypted cell A1 value: " + decryptedWorkbook.getWorksheets().get(0).getCells().get("A1").getStringValue());
```

## Salt okunur koruma (değiştirme parolası)
Excel iki ayrı parola katmanını destekler. Birincisi, dosyanın kendisini şifreleyen açma parolasıdır ve bir önceki bölümde ele alınmıştır. İkincisi, kullanıcıların çalışma kitabını açmasını engellemeyen değiştirme parolasıdır; bunun yerine Excel, değiştirme parolası sağlanmadığı sürece dosyanın salt okunur modda açılmasını önerir. Bu davranışı Aspose.Cells'de `Workbook.Settings.WriteProtection` (`workbook.getSettings().getWriteProtection()` aracılığıyla erişilen) üzerinden yapılandırın. `Password` özelliğini (`writeProtection.setPassword(...)` aracılığıyla) değiştirme parolasına ve `Author` özelliğini (`writeProtection.setAuthor(...)` aracılığıyla) korumayı kimin uyguladığını belirlemek için ayarlayın. Sağlanan bir değiştirme parolasının doğru olup olmadığını kontrol etmek için `WriteProtection.validatePassword(String)` yöntemini kullanın; eşleşme durumunda `true`, aksi takdirde `false` döndürür.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data");
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd");
workbook.getSettings().getWriteProtection().setAuthor("AuthorName");
workbook.save("WriteProtectedWorkbook.xlsx");
boolean isCorrectValid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd");
System.out.println("ValidatePassword(\"ModifyPwd\") returned: " + isCorrectValid);
boolean isWrongValid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd");
System.out.println("ValidatePassword(\"WrongPwd\") returned: " + isWrongValid);
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısını korumak, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, çalışma sayfalarını silmesini, çalışma sayfalarını gizlemesini veya yeniden adlandırmasını engeller. Korumalı durum, herhangi bir sayfadaki hücre içeriklerinden çok sayfa yapısı için geçerlidir. Yapı koruması uygulamak için `workbook.protect(ProtectionType.STRUCTURE, "password")` çağırın. Korumayı kaldırmak için `workbook.unprotect("password")` çağırın ve doğru parolayı sağlayın. Burada `ProtectionType.STRUCTURE` enum değeri kullanılmıştır ve `ProtectionType.WINDOWS` gibi diğer koruma türlerinden farklıdır.

```java
import com.aspose.cells.*;
// Yeni bir çalışma kitabı oluştur
Workbook workbook = new Workbook();
// İkinci bir çalışma sayfası ekle
workbook.getWorksheets().add();
// İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data");
// Çalışma kitabı yapısını koru
workbook.protect(ProtectionType.STRUCTURE, "StructPwd");
// Çalışma kitabını structure_protected.xlsx olarak kaydet
String filePath = "structure_protected.xlsx";
workbook.save(filePath);
// Dosyayı yeni bir Çalışma Kitabı örneğine yeniden yükle
Workbook loadedWorkbook = new Workbook(filePath);
// Yapı korumasını kaldır
loadedWorkbook.unprotect("StructPwd");
// Onay mesajını yazdır
System.out.println("Structure protection has been successfully removed from the workbook.");
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı değişikliklere karşı kilitler. Kullanıcılar parolayı sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan e-tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için kullanılan tipik korumadır. Bir çalışma sayfasını korumak için `worksheet.protect(ProtectionType.ALL, "password")` çağırın. `ProtectionType.ALL` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.unprotect("password")` çağırın ve doğru parolayı sağlayın. `CONTENTS`, `OBJECTS` ve `SCENARIOS` gibi diğer koruma türlerini bitsel VEYA kullanarak birleştirerek daha ayrıntılı kontrol sağlanabilir.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
sheet.getCells().get("A1").putValue("Sample Data");
sheet.protect(ProtectionType.ALL, "SheetPwd", "SheetPwd");
workbook.save("sheet_protected.xlsx");
Workbook workbookReloaded = new Workbook("sheet_protected.xlsx");
Worksheet sheetReloaded = workbookReloaded.getWorksheets().get(0);
sheetReloaded.unprotect("SheetPwd");
System.out.println("Worksheet protection removed successfully.");
```

## Dijital imzaları ekleme ve doğrulama
Dijital imza, alıcılara çalışma kitabı içeriğinin orijinal olduğunu ve imzalandıktan sonra değiştirilmediğini garanti eder. Aspose.Cells, `com.aspose.cells.DigitalSignatures` paketi aracılığıyla dijital imza desteği sağlar. Tipik iş akışı, bir `.pfx` sertifika dosyasını Java güvenlik API'leri (örneğin `java.security.KeyStore` ve `java.security.cert.X509Certificate`) aracılığıyla yükler, bunu bir `com.aspose.cells.DigitalSignatures.DigitalSignature` içinde sarar, imzayı bir `DigitalSignatureCollection`'a ekler ve koleksiyonu `workbook.addDigitalSignature(DigitalSignatureCollection)` aracılığıyla çalışma kitabına uygular. `DigitalSignature.getComments()` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar, böylece alıcı taraftaki bir doğrulama adımı tahrifatı tespit edebilir.

```java
import com.aspose.cells.*;
import java.io.FileInputStream;
import java.security.KeyStore;
KeyStore pfxKeyStore = KeyStore.getInstance("PKCS12");
pfxKeyStore.load(new FileInputStream("signature.pfx"), "pfx-password".toCharArray());
DigitalSignature signature = new DigitalSignature(pfxKeyStore, "pfx-password", "Signed by Aspose.Cells", new DateTime());
DigitalSignatureCollection signatures = new DigitalSignatureCollection();
signatures.add(signature);
Workbook workbook = new Workbook();
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value");
workbook.addDigitalSignature(signatures);
workbook.save("signed_workbook.xlsx");
System.out.println("The workbook has been digitally signed.");
```

## İlgili Makaleler
- [Excel dosyalarını şifreleme ve şifre çözme](/cells/tr/java/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/java/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/java/protect-and-unprotect-worksheet/)
- [Paylaşılan Çalışma Kitabını Parola ile Koruma veya Korumayı Kaldırma](/cells/tr/java/password-protect-or-unprotect-the-shared-workbook/)
- [Dijital İmzaları Atama ve Doğrulama](/cells/tr/java/assign-and-validate-digital-signatures/)
- [Şifrelenmiş Office Open XML - OOXML Dosyalarının Dosya Biçimini Algılama](/cells/tr/java/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Bir Dosya Biçiminin Nasıl Algılanacağı ve Dosyanın Şifrelenmiş Olup Olmadığının Kontrol Edilmesi](/cells/tr/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="java" >}}