---
title: Bir Çalışmada VBA Projesinin İmzalı Olup Olmadığını Kontrol Edin
type: docs
weight: 70
url: /tr/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

VBA projenizin imzalı olup olmadığını Microsoft Excel'de **Araçlar > Dijital İmzalar...** menüsüyle kontrol edebilirsiniz. Aynı zamanda, Aspose.Cells for Python via .NET [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) özelliği kullanılarak programatik olarak kontrol edebilirsiniz.

{{% /alert %}}

## **Bir Çalışma Kitabındaki VBA projesinin Python'da İmzalanıp İmzalanmadığını Kontrol Et**

Aşağıdaki kod, çalışbook yükler ve [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) özelliğini kullanarak VBA projesinin imzalı olup olmadığını kontrol eder. Proje imzalıysa **true** döndürecek, aksi takdirde **false** döndürecektir.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

