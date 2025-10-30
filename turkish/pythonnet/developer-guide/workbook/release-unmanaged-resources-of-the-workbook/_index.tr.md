---
title: Çalışma Kitabının Yönetilmeyen Kaynaklarını Serbest Bırak Python via .NET ile
linktitle: Yönetilmeyen Kaynakları Serbest Bırak
type: docs
weight: 310
url: /tr/python-net/release-unmanaged-resources-of-the-workbook/
description: Aspose.Cells for Python via .NET kullanarak Excel çalışma kitaplarıyla çalışırken yönetilmeyen kaynakları doğru şekilde nasıl serbest bırakacağınızı öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) metodunu sağlar; bu metod, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) nesnesinin yönetilmeyen kaynaklarını serbest bırakmak için kullanılır. Bu desen, dosya tutucuları, akışlar veya Python'un çöp toplayıcısı tarafından otomatik olarak yönetilmeyen bellek tahsisleri gibi unmanaged kaynaklarla çalışmak için hayati öneme sahiptir.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfı, kaynak yönetimi için Python'un bağlam yöneticisi protokolünü uygular. Ya açıkça [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) metodunu çağırabilirsiniz ya da uygun temizlik için Python'un `with` ifadesini kullanabilirsiniz.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
{{< app/cells/assistant language="python-net" >}}
