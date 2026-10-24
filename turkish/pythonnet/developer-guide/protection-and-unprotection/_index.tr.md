---
title: Korumayı Tanımla ve Kaldır
linktitle: Şifreleme ve Koruma
description: Bu bölüm Excel dosyalarını şifreleme ve şifre çözme ile Excel verilerini koruma işlemlerini tanıtır; dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruma, çalışma sayfası koruma ve Python kodu kullanarak dijital imzaları kapsar
keywords: Aspose.Cells, Python via .NET, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, Python
type: docs
weight: 68
url: /tr/python-net/protect-and-unprotect/
alias: [/python-net/security-features/]
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, ticari veya kişisel bilgiler içerir. Aspose.Cells for Python via .NET, Microsoft Excel'in yeteneklerini yansıtan, dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde verilerinizi güvence altına almanıza olanak tanıyan kapsamlı bir koruma özellikleri seti sunar.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET, dosya düzeyinden veri düzeyine kadar MS Excel'e benzer geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaların parolayla şifrelenmesi, değiştirme parolası aracılığıyla salt okunur erişimin zorunlu kılınması, çalışma kitabı yapısının korunması, çalışma sayfalarının korunması ve çalışma kitaplarının dijital olarak imzalanması yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasında ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `workbook.settings.password` alanına bir parola dizgisi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifresini çözmek için açmak amacıyla bir `LoadOptions` nesnesi oluşturun, `load_options.password` alanını şifreleme sırasında kullanılan parolayla aynı olacak şekilde ayarlayın ve bunu `Workbook` yapıcısına iletin. Aspose.Cells sağlanan parolayı şeffaf bir şekilde uygular, böylece kodunuzun geri kalanı dosya normal bir çalışma kitabıymış gibi şifresi çözülmüş içerikle etkileşime girebilir.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
cell = sheet.cells.get("A1")
cell.put_value("Confidential Data")
workbook.settings.password = "OpenPassword123"
workbook.save("encrypted.xlsx")
load_options = ac.LoadOptions()
load_options.password = "OpenPassword123"
decrypted_workbook = ac.Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.worksheets[0].cells.get("A1").string_value)
```

## Salt okunur koruma (değiştirme parolası)
Excel iki ayrı parola katmanını destekler. Birincisi açma parolasıdır; dosyanın kendisini şifreler ve önceki bölümde ele alınmıştır. İkincisi değiştirme parolasıdır; kullanıcıların çalışma kitabını açmasını engellemez, bunun yerine Excel, değiştirme parolası sağlanmadıkça dosyayı salt okunur modda açmayı önerir. Bu davranışı Aspose.Cells'te `workbook.settings.write_protection` üzerinden yapılandırın. `password` özelliğini değiştirme parolası olarak, `author` özelliğini ise korumayı kimin uyguladığını belirlemek için ayarlayın. Sağlanan bir değiştirme parolasının doğru olup olmadığını kontrol etmek amacıyla `write_protection.validate_password(string)` yöntemini kullanın; eşleşme durumunda `true`, aksi durumda `false` döndürür.

```python
import aspose.cells as ac
# Sıfırdan yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
# İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.worksheets[0].cells.get("A1").put_value("Sample Data")
# Yazma korumasını yapılandır: değiştirme parolasını ve yazarı ayarla
workbook.settings.write_protection.password = "ModifyPwd"
workbook.settings.write_protection.author = "AuthorName"
# Yazma korumasının kalıcı olması için çalışma kitabını kaydet
workbook.save("WriteProtectedWorkbook.xlsx")
# Değiştirme parolasını doğru parolayı kullanarak doğrula
is_correct_valid = workbook.settings.write_protection.validate_password("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Diğer dalı göstermek için yanlış bir parola kullanarak değiştirme parolasını doğrula
is_wrong_valid = workbook.settings.write_protection.validate_password("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısının korunması, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korunan durum, sayfa yapısı için geçerlidir ve herhangi bir sayfadaki hücre içerikleri için geçerli değildir. Yapı koruması uygulamak için `workbook.protect(ProtectionType.STRUCTURE, "password")` çağrısı yapın. Korumayı kaldırmak için `workbook.unprotect("password")` çağrısı yapın ve doğru parolayı sağlayın. Burada kullanılan `ProtectionType.STRUCTURE` enum değeri, `ProtectionType.WINDOWS` gibi diğer koruma türlerinden farklıdır.

```python
import aspose.cells as ac
# Yeni bir çalışma kitabı oluştur
workbook = ac.Workbook()
# İkinci bir çalışma sayfası ekle
workbook.worksheets.add()
# İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.worksheets[0].cells.get(0, 0).put_value("Sample Data")
# Çalışma kitabı yapısını koru
workbook.protect(ac.ProtectionType.STRUCTURE, "StructPwd")
# Çalışma kitabını structure_protected.xlsx olarak kaydet
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Dosyayı yeni bir Çalışma Kitabı örneğine yeniden yükle
loaded_workbook = ac.Workbook(file_path)
# Yapı korumasını kaldır
loaded_workbook.unprotect("StructPwd")
# Onay mesajını yazdır
print("Structure protection has been successfully removed from the workbook.")
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı yapılan değişikliklere karşı kilitler. Kullanıcılar parolayı sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için kullanılan tipik koruma yöntemidir. Bir çalışma sayfasını korumak için `worksheet.protect(ProtectionType.ALL, "password")` çağrısı yapın. `ProtectionType.ALL` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi tüm kullanılabilir koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.unprotect("password")` çağrısını doğru parolayla birlikte yapın. `Contents`, `Objects` ve `Scenarios` gibi diğer koruma türlerini bitsel VEYA kullanarak birleştirerek daha ayrıntılı denetim elde edebilirsiniz.

```python
import aspose.cells as ac
workbook = ac.Workbook()
sheet = workbook.worksheets[0]
sheet.cells.get("A1").put_value("Sample Data")
sheet.protect(ac.ProtectionType.ALL, "SheetPwd")
workbook.save("sheet_protected.xlsx")
workbook_reloaded = ac.Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.worksheets[0]
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
```

## Dijital imzaları ekleme ve doğrulama
Bir dijital imza, alıcılara çalışma kitabı içeriğinin otantik olduğunu ve imzalandığından bu yana değiştirilmediğini garanti eder. Aspose.Cells, `aspose.cells.digital_signatures` ad alanı aracılığıyla dijital imza desteği sağlar. Tipik iş akışı, `System.Security.Cryptography.X509Certificates.X509Certificate2` aracılığıyla bir `.pfx` sertifika dosyası yükler, bunu bir `aspose.cells.digital_signatures.DigitalSignature` içinde sarmalar, imzayı bir `DigitalSignatureCollection`'a ekler ve koleksiyonu `workbook.add_digital_signature(DigitalSignatureCollection)` aracılığıyla çalışma kitabına uygular. `digital_signature.comments` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar; bu nedenle alıcı tarafta yapılan bir doğrulama adımıyla kurcalama tespit edilebilir.

```python
from datetime import datetime
import aspose.cells as ac
from aspose.cells.digitalsignatures import DigitalSignature, DigitalSignatureCollection
with open("signature.pfx", "rb") as certificate_file:
    certificate = certificate_file.read()
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", datetime.now())
signatures = DigitalSignatureCollection()
signatures.add(signature)
workbook = ac.Workbook()
workbook.worksheets[0].cells.get("A1").put_value("Sample Value")
workbook.add_digital_signature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
```

## İlgili Makaleler
- [Excel dosyalarını şifreleme ve şifre çözme](/cells/tr/python-net/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/python-net/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/python-net/protect-and-unprotect-worksheets/)
- [Paylaşılan Çalışma Kitabını Parolayla Koruma veya Korumayı Kaldırma](/cells/tr/python-net/password-protect-or-unprotect-the-shared-workbook/)
- [Dijital İmzaları Atama ve Doğrulama](/cells/tr/python-net/assign-and-validate-digital-signatures/)
- [Aspose.Cells Kullanarak Değiştirme Parolasını Kontrol Etme](/cells/tr/python-net/check-password-to-modify-using-aspose-cells/)
- [Şifrelenmiş Office Open XML - OOXML Dosyalarının Dosya Biçimini Algılama](/cells/tr/python-net/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel Dosyalarını Şifreleme](/cells/tr/python-net/encrypting-excel-files/)
- [Bir Dosya Biçimi Nasıl Algılanır ve Dosyanın Şifrelenmiş Olup Olmadığı Nasıl Kontrol Edilir](/cells/tr/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="python-net" >}}