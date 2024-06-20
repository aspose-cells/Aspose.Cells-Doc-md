---
title: VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et
type: docs
weight: 120
url: /tr/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells, VBA kodunun dijital imzasının [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) özelliğini kullanarak geçerli olup olmadığını kontrol etmenizi sağlar. İmza geçerliyse **true** döndürecek, aksi takdirde **false** döndürecektir. VBA kodunun dijital imzası değiştirildiğinde geçersiz hale gelir.

{{% /alert %}}

## **C#'da VBA Kodunun Dijital İmzasının Geçerli Olup Olmadığını Kontrol Et**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [örnek excel dosyası](5115030.xlsm) kullanarak bu özelliğin kullanımını göstermektedir. Aynı excel dosyasının geçerli bir imzası vardır ancak VBA kodunu değiştirip çalıştırdıktan sonra imzanın geçersiz olduğunu buluruz.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
