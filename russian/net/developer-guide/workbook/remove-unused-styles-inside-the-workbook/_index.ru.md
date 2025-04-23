---
title: Удалить неиспользуемые стили внутри книги
type: docs
weight: 340
url: /ru/net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Неиспользуемые стили в файле Excel не только занимают место, но также вызывают проблемы производительности при преобразовании в различные форматы, такие как PDF, HTML и т. д. Aspose.Cells предоставляет [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) для удаления всех неиспользуемых стилей внутри книги.

{{% /alert %}}

В следующем коде объясняется использование [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles). Код загружает [файл-шаблон Excel](5115520.xlsx), который вы можете скачать по предоставленной ссылке. Он содержит неиспользуемый стиль с именем **AsposeStyle**, этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
