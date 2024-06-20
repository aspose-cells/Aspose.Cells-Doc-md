---
title: Удалить неиспользуемые стили внутри книги
type: docs
weight: 470
url: /ru/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Неиспользуемые стили в файле Excel не только занимают место, но также вызывают проблемы с производительностью при конвертировании в разные форматы, такие как PDF, HTML и т. д. Aspose.Cells предоставляет метод [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)), чтобы удалить все неиспользуемые стили внутри книги.

{{% /alert %}} 
## **Удалить неиспользуемые стили внутри книги**
Следующий код объясняет использование [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)). Код загружает [шаблонный файл Excel](5473451.xlsx), который можно загрузить по предоставленной ссылке. В файле содержится неиспользуемый стиль с именем **AsposeStyle**, этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода. См. следующий снимок экрана для большей иллюстрации.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
