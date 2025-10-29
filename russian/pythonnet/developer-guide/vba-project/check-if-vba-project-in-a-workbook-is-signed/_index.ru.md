---
title: Проверка подписан ли проект VBA в книге Excel
type: docs
weight: 70
url: /ru/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Вы можете проверить, подписан ли ваш проект VBA в Microsoft Excel через меню **Tools > Digital Signatures...**. Аналогично, его можно проверить программно, используя свойство [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) Aspose.Cells for Python via .NET.

{{% /alert %}}

## **Проверьте, подписан ли VBA-проект в рабочей книге в Python**

Следующий код загружает книгу и проверяет, подписан ли ее проект VBA, используя свойство [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). Свойство вернет **true**, если проект подписан, в противном случае оно вернет **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
