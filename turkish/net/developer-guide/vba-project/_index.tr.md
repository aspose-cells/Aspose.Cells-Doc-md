---
title: Etkinleştirilmiş Çalışma Kitabının VBA Kodlarını Yönet
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/net/manage-vba-project/
description: Aspose.Cells kütüphanesi ile VBA Modülü ekle ve VBA yı değiştir
---

## **C# İçinde VBA Modülü Ekle**
{{% alert color="primary" %}}

Aspose.Cells, yeni bir VBA Modülü ve Makro Kodu eklemenize ve değiştirmenize olanak tanır. Yeni bir VBA Modülü eklemek için [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) yöntemini kullanınız

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM biçiminde kaydeder. Bir kez çıktı XLSM dosyasını Microsoft Excel’de açarsanız ve **Geliştirici > Görsel Temel** menü komutlarına tıklayarak “TestModülü” adlı bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aşağıdaki örnek kod, VBA Modülü ve Makro Kodu içeren kaynak Excel dosyasını yükler

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **C# İçinde VBA veya Makro Değiştir**

{{% alert color="primary" %}} 

VBA veya Makro Kodunu, Aspose.Cells kullanarak değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projeyi okumak ve değiştirmek için aşağıdaki ad alanını ve sınıfları eklemiştir.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyasındaki VBA veya Makro Kodunu değiştirmeyi gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, içinde belirtilen VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilmiş olacaktır

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Verilen bağlantılardan [kaynak Excel dosyasını](5112508.xlsm) ve [çıktı Excel dosyasını](5112511.xlsm) indirebilirsiniz.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Gelişmiş Konular**
- [Çalışma Kitabındaki VBA projeye bir kütüphane referansı ekle](/cells/tr/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Makroyu Form Kontrole Ata](/cells/tr/net/assign-macro-to-form-control/)
- [VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et](/cells/tr/net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalı Olup Olmadığını Kontrol Et](/cells/tr/net/check-if-vba-code-is-signed/)
- [Çalışma Kitabındaki VBA projesinin imzalı olup olmadığını kontrol edin](/cells/tr/net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korunup Görüntülemeye Kilitli Olup Olmadığını Kontrol Edin](/cells/tr/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama](/cells/tr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Sertifika ile Bir VBA Kod Projesini Dijital Olarak İmzalama](/cells/tr/net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarma](/cells/tr/net/export-vba-certificate-to-file-or-stream/)
- [Bir çalışma kitabı yüklenirken VBA Projesini Filtreleme](/cells/tr/net/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korunup Korunmadığını Bulma](/cells/tr/net/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruma](/cells/tr/net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="csharp" >}}
