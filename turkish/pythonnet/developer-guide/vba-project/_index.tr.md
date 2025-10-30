---
title: Etkinleştirilmiş Çalışma Kitabının VBA Kodlarını Yönet
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/python-net/manage-vba-project/
description: Aspose.Cells for Python via .NET ile VBA Modülü ekleyin ve VBA veya Makro üzerinde değişiklik yapın.
---

## **Python'da VBA Modülü Ekle**
{{% alert color="primary" %}}

Aspose.Cells, Aspose.Cells for Python via .NET kullanarak yeni bir VBA Modülü ve Makro Kodunu eklemenize izin verir. Lütfen yeni VBA Modülü eklemek için [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/) metodunu kullanın

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM biçiminde kaydeder. Bir kez çıktı XLSM dosyasını Microsoft Excel’de açarsanız ve **Geliştirici > Görsel Temel** menü komutlarına tıklayarak “TestModülü” adlı bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Aşağıdaki örnek kod, VBA Modülü ve Makro Kodu içeren kaynak Excel dosyasını yükler

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **Python'da VBA veya Makro Değiştir**

{{% alert color="primary" %}} 

VBA veya Makro kodunu Aspose.Cells for Python via .NET kullanarak değiştirebilirsiniz. Aspose.Cells for Python via .NET, VBA projesini okumak ve değiştirmek için aşağıdaki ad alanı ve sınıfları eklemiştir.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Bu makale, Aspose.Cells for Python via .NET kullanarak kaynak Excel dosyasındaki VBA veya Makro kodunu nasıl değiştireceğinizi gösterecek.

{{% /alert %}} 

Aşağıdaki örnek kod, içinde belirtilen VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells for Python via .NET örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu şu şekilde değiştirilecektir

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Verilen bağlantılardan [kaynak Excel dosyasını](5112508.xlsm) ve [çıktı Excel dosyasını](5112511.xlsm) indirebilirsiniz.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Gelişmiş Konular**
- [Çalışma Kitabındaki VBA projeye bir kütüphane referansı ekle](/cells/tr/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et](/cells/tr/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalı Olup Olmadığını Kontrol Et](/cells/tr/python-net/check-if-vba-code-is-signed/)
- [Çalışma Kitabındaki VBA projesinin imzalı olup olmadığını kontrol edin](/cells/tr/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korunup Görüntülemeye Kilitli Olup Olmadığını Kontrol Edin](/cells/tr/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Sertifika ile Bir VBA Kod Projesini Dijital Olarak İmzalama](/cells/tr/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarma](/cells/tr/python-net/export-vba-certificate-to-file-or-stream/)
- [Bir çalışma kitabı yüklenirken VBA Projesini Filtreleme](/cells/tr/python-net/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korunup Korunmadığını Bulma](/cells/tr/python-net/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruma](/cells/tr/python-net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="python-net" >}}
