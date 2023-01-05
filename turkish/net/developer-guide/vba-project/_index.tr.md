---
title: Excel Makro Etkin çalışma kitabının VBA kodlarını yönetin.
linktitle: Makro Projesi
type: docs
weight: 200
url: /tr/net/manage-vba-project/
description: Aspose.Cells kitaplığı ile VBA Modülü ekleyin ve VBA veya Makroyu Değiştirin.
---
## **C#'de bir VBA Modülü ekleyin**
{{% alert color="primary" %}}

 Aspose.Cells, Aspose.Cells'i kullanarak yeni bir VBA Modülü ve Makro Kodu eklemenizi sağlar. Lütfen[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) çalışma kitabına yeni VBA Modülü ekleme yöntemi

{{% /alert %}}

Aşağıdaki örnek kod, yeni bir çalışma kitabı oluşturur ve yeni bir VBA Modülü ve Makro Kodu ekler ve çıktıyı XLSM biçiminde kaydeder. Bir kez, XLSM çıktı dosyasını Microsoft Excel'de açacaksınız ve**Geliştirici > Visual Basic** menü komutları, "TestModule" adında bir modül göreceksiniz ve içinde aşağıdaki makro kodunu göreceksiniz.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

İşte XLSM çıktı dosyasını VBA Modülü ve Makro Kodu ile oluşturmak için örnek kod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **C#'de VBA'yı veya Makroyu değiştirin**

{{% alert color="primary" %}} 

Aspose.Cells'i kullanarak VBA veya Makro Kodunu değiştirebilirsiniz. Aspose.Cells, Excel dosyasındaki VBA projesini okumak ve değiştirmek için aşağıdaki ad alanını ve sınıfları ekledi.

- Aspose.Cells.Vba
- Vba Projesi
- VbaModül Koleksiyonu
- Vba Modülü

Bu makale, Aspose.Cells kullanarak kaynak Excel dosyası içindeki VBA veya Makro Kodunu nasıl değiştireceğinizi gösterecektir.

{{% /alert %}} 

Aşağıdaki örnek kod, içinde aşağıdaki VBA veya Makro kodu bulunan kaynak Excel dosyasını yükler.

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Aspose.Cells örnek kodunun yürütülmesinden sonra, VBA veya Makro kodu bu şekilde değiştirilecektir.

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 indirebilirsiniz[kaynak Excel dosyası](5112508.xlsm) ve[çıktı excel dosyası](5112511.xlsm) verilen linklerden



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **ileri konular**
- [Çalışma kitabında VBA projesine bir kitaplık başvurusu ekleyin](/cells/tr/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Form Denetimine Makro Ata](/cells/tr/net/assign-macro-to-form-control/)
- [VBA Kodunun Dijital İmzasının Geçerli olup olmadığını kontrol edin](/cells/tr/net/check-if-digital-signature-of-vba-code-is-valid/)
- [VBA Kodunun İmzalanıp İmzalanmadığını Kontrol Edin](/cells/tr/net/check-if-vba-code-is-signed/)
- [Çalışma Kitabındaki VBA projesinin İmzalı olup olmadığını kontrol edin](/cells/tr/net/check-if-vba-project-in-a-workbook-is-signed/)
- [VBA Projesinin Korumalı ve Görüntüleme için Kilitli olup olmadığını kontrol edin](/cells/tr/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [VBA Macro UserForm DesignerStorage'ı Şablondan Hedef Çalışma Kitabına Kopyalayın](/cells/tr/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Sertifikalı Bir VBA Kodu Projesini Dijital Olarak İmzalayın](/cells/tr/net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA Sertifikasını Dosyaya veya Akışa Aktarın](/cells/tr/net/export-vba-certificate-to-file-or-stream/)
- [Çalışma kitabı yüklerken VBA Projesini filtreleme](/cells/tr/net/filter-vba-project-while-loading-a-workbook/)
- [VBA Projesinin Korumalı olup olmadığını öğrenin](/cells/tr/net/find-out-if-vba-project-is-protected/)
- [Excel Çalışma Kitabının VBA Projesini Parolayla Koruyun](/cells/tr/net/password-protect-the-vba-project-of-excel-workbook/)

