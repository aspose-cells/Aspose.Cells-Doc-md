---
title: VBA kodlarını Yönetme — Excel Makro Etkin çalışma kitabı
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/nodejs-cpp/manage-vba-project/
description: VBA Modülü ekleyin ve VBA veya Makroyu Aspose.Cells for Node.js via C++ ile düzenleyin.
---

## **Node.js kullanarak VBA Modülü ekleyin**
{{% alert color="primary" %}}

Aspose.Cells, Aspose.Cells for Node.js via C++ kullanarak yeni bir VBA Modülü ve Makro Kodu eklemenize olanak tanır. Lütfen yeni VBA Modülü eklemek için [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) yöntemini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM formatında kaydeder. Çıktı XLSM dosyasını Microsoft Excel’de açıp **Geliştirici > Görsel Basic** menü komutlarına tıklarsanız, "TestModule" adlı bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

İşte VBA Modülü ve Makro Kodu ile çıktı XLSM dosyasını oluşturmak için örnek kod.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **VBA veya Makro düzenle Node.js kullanarak**

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ kullanarak VBA veya Makro Kodunu değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projesini okumak ve değiştirmek için aşağıdaki modülleri ve sınıfları eklemiştir.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyasındaki VBA veya Makro Kodunu değiştirmeyi gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, içeriğinde VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler.

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilmiş olacaktır

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Verilen bağlantılardan [kaynak Excel dosyasını](5112508.xlsm) ve [çıktı Excel dosyasını](5112511.xlsm) indirebilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Gelişmiş Konular**
- [Çalışma Kitabındaki VBA projeye bir kütüphane referansı ekle](/cells/tr/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Makroyu Form Kontrole Ata](/cells/tr/nodejs-cpp/assign-macro-to-form-control/)
- [VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et](/cells/tr/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalı Olup Olmadığını Kontrol Et](/cells/tr/nodejs-cpp/check-if-vba-code-is-signed/)
- [Çalışma Kitabındaki VBA projesinin imzalı olup olmadığını kontrol edin](/cells/tr/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korunup Görüntülemeye Kilitli Olup Olmadığını Kontrol Edin](/cells/tr/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama](/cells/tr/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Sertifika ile Bir VBA Kod Projesini Dijital Olarak İmzalama](/cells/tr/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarma](/cells/tr/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Bir çalışma kitabı yüklenirken VBA Projesini Filtreleme](/cells/tr/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korunup Korunmadığını Bulma](/cells/tr/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruma](/cells/tr/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
