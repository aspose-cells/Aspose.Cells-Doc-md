---
title: C++ ile Koruma ve Koruma Kaldırma
linktitle: Şifreleme ve Koruma
description: Bu bölümde Excel dosyalarının şifrelenmesi ve şifrelerinin çözülmesi ile Excel verilerinin korunması anlatılmaktadır; dosya şifreleme, salt okunur koruma, çalışma kitabı yapısı koruması, çalışma sayfası koruması ve C++ kodu kullanılarak dijital imzalar konuları ele alınmaktadır.
keywords: Aspose.Cells, Aspose.Cells for C++, şifrele, şifre çöz, parola, koru, korumayı kaldır, çalışma kitabı koruması, çalışma sayfası koruması, salt okunur, dijital imza, C++
type: docs
weight: 68
url: /tr/cpp/protect-and-unprotect/
alias: [/cpp/security-features/]
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel çalışma kitapları genellikle yetkisiz erişimden korunması gereken hassas finansal, ticari veya kişisel bilgileri depolar. Aspose.Cells for C++, Microsoft Excel'in yeteneklerini yansıtan kapsamlı bir koruma özellikleri seti sunar ve verilerinizi dosya düzeyinde, çalışma kitabı düzeyinde ve çalışma sayfası düzeyinde güvenceye almanıza olanak tanır.

{{% alert color="primary" %}}
Aspose.Cells for C++, MS Excel'e benzer şekilde dosya düzeyinden veri düzeyine kadar geniş bir koruma özellikleri yelpazesi sunar. Bu yetenekler arasında dosyaları parola ile şifreleme, değiştirme parolası yoluyla salt okunur erişimi zorunlu kılma, çalışma kitabı yapısını koruma, çalışma sayfalarını koruma ve çalışma kitaplarını dijital olarak imzalama yer alır.
{{% /alert %}}

## Excel dosyalarını şifreleme ve şifre çözme
Bir Excel dosyasında ayarlanan bir parola, yetkisiz kullanıcıların çalışma kitabı içeriğini açmasını veya görüntülemesini engeller. Bir çalışma kitabını şifrelemek için `workbook.GetSettings().SetPassword()` alanına bir parola dizesi atayın ve ardından çalışma kitabını kaydedin. Aspose.Cells, dosyayı şifrelenmiş biçimde yazar. Şifrelenmiş bir çalışma kitabını şifre çözme amacıyla açmak için bir `LoadOptions` nesnesi oluşturun, `LoadOptions.SetPassword()` alanını şifreleme sırasında kullanılan parolayla ayarlayın ve bunu `Workbook` yapıcısına geçirin. Aspose.Cells, sağlanan parolayı saydam bir şekilde uygular; böylece kodunuzun geri kalanı, dosya normal bir çalışma kitabıymış gibi şifresi çözülmüş içerikle etkileşime girebilir.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(u"Confidential Data");
    workbook.GetSettings().SetPassword(U16String("OpenPassword123"));
    workbook.Save(u"encrypted.xlsx");
    LoadOptions loadOptions;
    loadOptions.SetPassword(U16String("OpenPassword123"));
    Workbook decryptedWorkbook(u"encrypted.xlsx", loadOptions);
    U16String cellValue = decryptedWorkbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue();
    std::cout << "Decrypted cell A1 value: " << cellValue.ToUtf8() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Salt okunur koruma (değiştirme parolası)
Excel iki farklı parola katmanını destekler. İlki, dosyanın kendisini şifreleyen ve önceki bölümde ele alınan açma parolasıdır. İkincisi, kullanıcıların çalışma kitabını açmasını engellemeyen değiştirme parolasıdır; bunun yerine Excel, değiştirme parolası sağlanmadığı sürece dosyanın salt okunur modda açılmasını önerir. Bu davranışı Aspose.Cells'te `workbook.GetSettings().GetWriteProtection()` aracılığıyla yapılandırın. `Password` özelliğini değiştirme parolasına ve `Author` özelliğini korumayı kimin uyguladığını belirlemek için ayarlayın. Sağlanan değiştirme parolasının doğru olup olmadığını kontrol etmek için `WriteProtection.ValidatePassword()` yöntemini kullanın; eşleşme durumunda `true`, aksi durumda `false` döndürür.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    Cell a1 = cells.Get(u"A1");
    a1.PutValue(u"Sample Data");
    workbook.GetSettings().GetWriteProtection().SetPassword(u"ModifyPwd");
    workbook.GetSettings().GetWriteProtection().SetAuthor(u"AuthorName");
    workbook.Save(u"WriteProtectedWorkbook.xlsx");
    bool isCorrectValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"ModifyPwd");
    std::cout << "ValidatePassword(\"ModifyPwd\") returned: " << (isCorrectValid ? "True" : "False") << std::endl;
    bool isWrongValid = workbook.GetSettings().GetWriteProtection().ValidatePassword(u"WrongPwd");
    std::cout << "ValidatePassword(\"WrongPwd\") returned: " << (isWrongValid ? "True" : "False") << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Çalışma kitabı yapısını koruma ve korumayı kaldırma
Çalışma kitabı yapısının korunması, diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, yeni çalışma sayfaları eklemesini, çalışma sayfalarını taşımasını, silmesini, gizlemesini veya yeniden adlandırmasını engeller. Korunan durum, herhangi bir sayfadaki hücre içeriklerinden ziyade sayfa yapısı için geçerlidir. Yapı koruması uygulamak için `workbook.Protect(ProtectionType::Structure, "password")` çağırın. Korumayı kaldırmak için `workbook.Unprotect("password")` çağırın ve doğru parolayı sağlayın. Burada kullanılan `ProtectionType::Structure` enum değeri, `ProtectionType::Windows` gibi diğer koruma türlerinden farklıdır.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Yeni bir çalışma kitabı oluştur
    Workbook workbook;
    // İkinci bir çalışma sayfası ekle
    workbook.GetWorksheets().Add();
    // İlk çalışma sayfasının A1 hücresine örnek bir değer yaz
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(u"Sample Data");
    // Çalışma kitabının yapısını koru
    workbook.Protect(ProtectionType::Structure, u"StructPwd");
    // Çalışma kitabını structure_protected.xlsx olarak kaydet
    U16String filePath = u"structure_protected.xlsx";
    workbook.Save(filePath);
    // Dosyayı yeni bir Workbook örneğine yeniden yükle
    Workbook loadedWorkbook(filePath);
    // Yapı korumasını kaldır
    loadedWorkbook.Unprotect(u"StructPwd");
    // Onay mesajını yazdır
    std::cout << "Structure protection has been successfully removed from the workbook." << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Çalışma sayfalarını koruma ve korumayı kaldırma
Çalışma sayfası koruması, bir çalışma sayfasının hücrelerini yanlışlıkla veya kasıtlı değişikliklere karşı kilitler. Kullanıcılar, parolayı sağlamadan kilitli hücreleri düzenleyemez. Bu, paylaşılan elektronik tablolarda formülleri, başlıkları veya belirlenmiş veri girişi alanlarını korumak için kullanılan tipik korumadır. Bir çalışma sayfasını korumak için `worksheet.Protect(ProtectionType::All, "password")` çağırın. `ProtectionType::All` kullanmak, kilitli hücreleri seçme, hücreleri biçimlendirme, satır ve sütun ekleme ve satır ve sütun silme gibi mevcut tüm koruma seçeneklerini etkinleştirir. Korumayı kaldırmak için `worksheet.Unprotect("password")` çağırın ve doğru parolayı sağlayın. `Contents`, `Objects` ve `Scenarios` gibi diğer koruma türlerini bit düzeyinde VEYA kullanarak birleştirerek daha ayrıntılı kontrol sağlanabilir.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Data");
    sheet.Protect(ProtectionType::All, u"SheetPwd");
    workbook.Save(u"sheet_protected.xlsx");
    Workbook workbookReloaded(u"sheet_protected.xlsx");
    Worksheet sheetReloaded = workbookReloaded.GetWorksheets().Get(0);
    sheetReloaded.Unprotect(u"SheetPwd");
    std::cout << "Worksheet protection removed successfully.\n";
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Dijital imzaları ekleme ve doğrulama
Dijital imza, alıcılara çalışma kitabı içeriğinin orijinal olduğunu ve imzalandığından bu yana değiştirilmediğini garanti eder. Aspose.Cells, `Aspose::Cells::DigitalSignatures` ad alanı aracılığıyla dijital imza desteği sağlar. Tipik iş akışı bir `.pfx` sertifika dosyasını yükler, onu bir `Aspose::Cells::DigitalSignatures::DigitalSignature` içine sarar, imzayı bir `DigitalSignatureCollection` öğesine ekler ve koleksiyonu `workbook.AddDigitalSignature(DigitalSignatureCollection)` aracılığıyla çalışma kitabına uygular. `DigitalSignature.GetComments()` özelliği, imzalama zamanı ve amacı gibi imzalama bağlamını kaydedebilir. İmzalandıktan sonra çalışma kitabında yapılan herhangi bir değişiklik imzayı geçersiz kılar; bu nedenle alıcı tarafta bir doğrulama adımı tahrifatı tespit edebilir.

```cpp
#include "Aspose.Cells.h"
#include <chrono>
#include <ctime>
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;
int main() {
    Aspose::Cells::Startup();
    std::time_t t = std::time(nullptr);
    std::tm tm{};
    localtime_s(&tm, &t);
    Date currentDate{0};
    currentDate.year = tm.tm_year + 1900;
    currentDate.month = tm.tm_mon + 1;
    currentDate.day = tm.tm_mday;
    currentDate.hour = tm.tm_hour;
    currentDate.minute = tm.tm_min;
    currentDate.second = tm.tm_sec;
    DigitalSignature signature(u"signature.pfx", u"pfx-password", u"Signed by Aspose.Cells", currentDate);
    DigitalSignatureCollection signatures;
    signatures.Add(signature);
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Sample Value");
    workbook.AddDigitalSignature(signatures);
    workbook.Save(u"signed_workbook.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## İlgili Makaleler
- [Excel Dosyalarını Şifreleme ve Şifre Çözme](/cells/tr/cpp/encrypt-and-decrypt-excel-files/)
- [Çalışma Kitabı Yapısını Koruma ve Korumayı Kaldırma](/cells/tr/cpp/protect-and-unprotect-workbook-structure/)
- [Çalışma Sayfasını Koruma ve Korumayı Kaldırma](/cells/tr/cpp/protect-and-unprotect-worksheets/)
- [Paylaşılan Çalışma Kitabını Parola ile Koruma veya Korumayı Kaldırma](/cells/tr/cpp/password-protect-or-unprotect-the-shared-workbook/)
- [Aspose.Cells Kullanarak Değiştirme Parolasını Kontrol Etme](/cells/tr/cpp/check-password-to-modify-using-aspose-cells/)
- [Şifrelenmiş Office Open XML - OOXML Dosyalarının Dosya Biçimini Algılama](/cells/tr/cpp/detect-file-format-of-encrypted-office-open-xml-ooxml-files/)
- [Excel Dosyalarını Şifreleme](/cells/tr/cpp/encrypting-excel-files/)
- [Bir Dosya Biçimini Algılama ve Dosyanın Şifrelenmiş Olup Olmadığını Kontrol Etme](/cells/tr/cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/)

{{< app/cells/assistant language="cpp" >}}