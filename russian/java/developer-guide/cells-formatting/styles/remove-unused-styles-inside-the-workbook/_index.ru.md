---
title: Удалить неиспользуемые стили внутри книги
type: docs
weight: 470
url: /ru/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Неиспользуемые стили в файле Excel занимают не только пространство, но и вызывают проблемы с производительностью при конвертации в разные форматы, такие как PDF, HTML и другие. Aspose.Cells предоставляет [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) для удаления всех неиспользуемых стилей внутри рабочей книги.

{{% /alert %}} 
## **Удалить неиспользуемые стили внутри книги**
Следующий код объясняет использование [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). Код загружает [шаблон Excel](5473451.xlsx), который вы можете скачать по предоставленной ссылке. В нём есть неиспользуемый стиль под названием **AsposeStyle**, который после выполнения кода будет удалён вместе со всеми другими неиспользуемыми стилями. Посмотрите следующий скриншот для дополнительной иллюстрации.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
