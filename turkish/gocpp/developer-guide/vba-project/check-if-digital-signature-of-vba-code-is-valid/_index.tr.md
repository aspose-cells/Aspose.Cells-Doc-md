---
title: Golang ile C++ kullanarak VBA Kodunun Dijital İmzasının Geçerli olup olmadığını kontrol edin
linktitle: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aspose.Cells ile Golang kullanarak VBA kodunda dijital imzanın geçerliliğini nasıl kontrol edeceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, VBA kodunun dijital imzasının geçerliliğini [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/) özelliği kullanarak kontrol etmenizi sağlar. İmza geçerliyse **true**, değilse **false** döner. VBA kodu değiştirildiğinde dijital imza geçersiz hale gelir.

{{% /alert %}}

## **C++ ile VBA Kodunun Dijital İmzasının Geçerli olup olmadığını Kontrol Edin**

 Aşağıdaki kod, sağlanan bağlantıdan indirilebilir [örnek excel dosyasıyla](5115030.xlsm) kullanımını gösterir. Aynı Excel dosyasının geçerli bir imzası vardır, fakat VBA kodunu değiştirdiğimizde ve çalışma kitabını kaydettiğimizde, imzası geçersiz hale gelir.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
