---
title: Korumayı Tanımla ve Kaldır
linktitle: Koruma
description: Bu bölüm, Python kodu kullanarak Excel dosyalarının nasıl şifreleneceğini ve şifre çözüleceğini, Excel verilerinin nasıl korunacağını anlatır. Kapsanan konular arasında dosya şifreleme, salt okunur koruma, çalışma kitabı yapısının korunması, çalışma sayfası koruması ve dijital imzalar yer alır.
keywords: Aspose.Cells, Python via Java, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, Python
type: docs
weight: 68
url: /tr/python-java/protect-and-unprotect/
alias: [/python-java/security-features/]
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları sıklıkla yetkisiz erişimden korunması gereken hassas finansal, iş veya kişisel bilgiler içerir. Aspose.Cells for Python via Java, Microsoft Excel'in yeteneklerini yansıtan kapsamlı koruma özellikleri sunar. Bu özellikler, verilerinizi dosya, çalışma kitabı ve çalışma sayfası düzeyinde güvence altına almanıza olanak tanır.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özelliği yelpazesi sunar. Bu özellikler; dosyaların parolayla şifrelenmesini, değiştirme parolasıyla salt okunur erişimin zorunlu kılınmasını, çalışma kitabı yapısının ve çalışma sayfalarının korunmasını ve çalışma kitaplarının dijital olarak imzalanmasını kapsar.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasına ayarlanan parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `workbook.getSettings().setPassword(...)` ifadesine bir parola dizesi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifre çözme amacıyla açmak için bir `LoadOptions` nesnesi oluşturun, `load_options.setPassword(...)` aracılığıyla şifreleme sırasında kullanılan parolanın aynısını ayarlayın ve bunu `Workbook` yapıcısına iletin. Aspose.Cells, sağlanan parolayı saydam biçimde kullanır. Böylece kodunuzun geri kalan kısmı, şifre çözülmüş içerik üzerinde dosya normal bir çalışma kitabıymış gibi çalışabilir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cell, LoadOptions
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cell = sheet.getCells().get("A1")
cell.putValue("Confidential Data")
workbook.getSettings().setPassword("OpenPassword123")
workbook.save("encrypted.xlsx")
load_options = LoadOptions()
load_options.setPassword("OpenPassword123")
decrypted_workbook = Workbook("encrypted.xlsx", load_options)
print("Decrypted cell A1 value: " + decrypted_workbook.getWorksheets().get(0).getCells().get("A1").getStringValue())
jpype.shutdownJVM()
```

## Salt okunur koruma (değiştirme parolası)
Excel iki farklı parola katmanını destekler. İlk katman, dosyanın kendisini şifreleyen ve önceki bölümde ele alınan açma parolasıdır. İkinci katman, çalışma kitabının açılmasını engellemeyen bir değiştirme parolasıdır. Değiştirme parolası sağlanmadığında Excel, dosyanın salt okunur modda açılmasını önerir. Bu davranışı Aspose.Cells içinde `workbook.getSettings().getWriteProtection()` aracılığıyla yapılandırın. `setPassword(...)` ile parolayı değiştirme parolası olarak, `setAuthor(...)` ile ise yazarı, korumayı kimin uyguladığını belirlemek üzere ayarlayın. Sağlanan bir değiştirme parolasının doğru olup olmadığını kontrol etmek için `writeProtection.validatePassword(String)` yöntemini kullanın. Yöntem, eşleşme durumunda `true`, diğer durumlarda `false` döndürür.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Sıfırdan yeni bir çalışma kitabı oluştur
workbook = Workbook()
# İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Data")
# Yazma korumasını yapılandır: değiştirme parolasını ve yazarı ayarla
workbook.getSettings().getWriteProtection().setPassword("ModifyPwd")
workbook.getSettings().getWriteProtection().setAuthor("AuthorName")
# Yazma korumasının kalıcı olması için çalışma kitabını kaydet
workbook.save("WriteProtectedWorkbook.xlsx")
# Doğru parolayı kullanarak değiştirme parolasını doğrula
is_correct_valid = workbook.getSettings().getWriteProtection().validatePassword("ModifyPwd")
print("ValidatePassword(\"ModifyPwd\") returned: " + str(is_correct_valid))
# Diğer dalı göstermek için yanlış bir parola kullanarak değiştirme parolasını doğrula
is_wrong_valid = workbook.getSettings().getWriteProtection().validatePassword("WrongPwd")
print("ValidatePassword(\"WrongPwd\") returned: " + str(is_wrong_valid))
jpype.shutdownJVM()
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısının korunması, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korumalı durum, çalışma sayfalarının yapısı için geçerlidir; herhangi bir çalışma sayfasındaki hücre içerikleri için geçerli değildir. Çalışma kitabı yapısını korumak için `workbook.protect(ProtectionType.STRUCTURE, "password")` çağırın. Korumayı kaldırmak için doğru parolayı belirterek `workbook.unprotect("password")` çağırın. Burada kullanılan `ProtectionType.STRUCTURE` enum değeri, `ProtectionType.WINDOWS` gibi diğer koruma türlerinden farklıdır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, ProtectionType
# Yeni bir çalışma kitabı oluştur
workbook = Workbook()
# İkinci bir çalışma sayfası ekle
workbook.getWorksheets().add()
# İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Sample Data")
# Çalışma kitabı yapısını koru
workbook.protect(ProtectionType.STRUCTURE, "StructPwd")
# Çalışma kitabını structure_protected.xlsx olarak kaydet
file_path = "structure_protected.xlsx"
workbook.save(file_path)
# Dosyayı yeni bir Çalışma Kitabı örneğine yeniden yükle
loaded_workbook = Workbook(file_path)
# Yapı korumasını kaldır
loaded_workbook.unprotect("StructPwd")
# Onay mesajını yazdır
print("Structure protection has been successfully removed from the workbook.")
jpype.shutdownJVM()
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini kazara veya kasıtlı olarak yapılan değişikliklere karşı kilitler. Kullanıcılar parolayı sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenen veri girişi alanlarını korumak için kullanılan tipik korumadır. Bir çalışma sayfasını korumak için `worksheet.protect(ProtectionType.ALL, "password")` çağırın. `ProtectionType.ALL` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için doğru parolayı belirterek `worksheet.unprotect("password")` çağırın. Daha ayrıntılı denetim için `ProtectionType.CONTENTS`, `ProtectionType.OBJECTS` ve `ProtectionType.SCENARIOS` gibi diğer koruma türlerini bit düzeyinde OR işlemiyle birleştirin.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, ProtectionType
workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
worksheet.getCells().get("A1").putValue("Sample Data")
worksheet.protect(ProtectionType.ALL, "SheetPwd", None)
workbook.save("sheet_protected.xlsx")
workbook_reloaded = Workbook("sheet_protected.xlsx")
sheet_reloaded = workbook_reloaded.getWorksheets().get(0)
sheet_reloaded.unprotect("SheetPwd")
print("Worksheet protection removed successfully.")
jpype.shutdownJVM()
```

## Dijital imzaları ekleme ve doğrulama
Bir dijital imza, alıcılara çalışma kitabı içeriğinin özgün olduğunu ve imzalandığından beri değiştirilmediğini güvence altına alır. Aspose.Cells, `Aspose.Cells.DigitalSignatures` ad alanı aracılığıyla dijital imza desteği sağlar. Tipik iş akışında `java.security.KeyStore` aracılığıyla bir `.pfx` sertifika dosyası yüklenir. Bu sertifika bir `Aspose.Cells.DigitalSignatures.DigitalSignature` nesnesine sarılır. İmza, bir `DigitalSignatureCollection` koleksiyonuna eklenir ve koleksiyon `workbook.addDigitalSignature(digitalSignatureCollection)` aracılığıyla çalışma kitabına uygulanır. `digitalSignature.getComments()` özelliği, imzalama zamanı ve amacı gibi bağlam bilgilerini kaydedebilir. Çalışma kitabı imzalandıktan sonra yapılan herhangi bir değişiklik, imzayı geçersiz kılar. Bu nedenle alıcı tarafında bir doğrulama adımı gerçekleştirilerek kurcalama tespit edilebilir.

```python
import jpype
import jpype.imports
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, DigitalSignature, DigitalSignatureCollection
from java.security import KeyStore
from java.io import FileInputStream
from java.util import Date
# Java KeyStore kullanarak PFX dosyasından sertifika yükle
key_store = KeyStore.getInstance("PKCS12")
fis = FileInputStream("signature.pfx")
key_store.load(fis, "pfx-password")
fis.close()
# Sertifikayı al
alias = key_store.aliases().nextElement()
certificate = key_store.getCertificate(alias)
# Dijital imza oluştur
signature = DigitalSignature(certificate, "Signed by Aspose.Cells", Date())
signatures = DigitalSignatureCollection()
signatures.add(signature)
# Çalışma kitabı oluştur ve imza ekle
workbook = Workbook()
workbook.getWorksheets().get(0).getCells().get("A1").putValue("Sample Value")
workbook.addDigitalSignature(signatures)
workbook.save("signed_workbook.xlsx")
print("The workbook has been digitally signed.")
jpype.shutdownJVM()
```

## İlgili Makaleler
- [Excel dosyalarını şifreleme ve şifre çözme](/cells/tr/python-java/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/python-java/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/python-java/protect-and-unprotect-worksheet/)
- [Aspose.Cells kullanarak Değiştirme Parolasını Kontrol Etme](/cells/tr/python-java/check-password-to-modify-using-aspose-cells/)

{{< app/cells/assistant language="python" >}}