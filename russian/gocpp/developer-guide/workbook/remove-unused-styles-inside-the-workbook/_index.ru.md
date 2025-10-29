---  
title: Удаление неиспользуемых стилей внутри рабочей книги с помощью Golang через C++  
linktitle: Удалить неиспользуемые стили внутри книги  
type: docs  
weight: 340  
url: /ru/go-cpp/remove-unused-styles-inside-the-workbook/  
description: Удалите неиспользуемые стили в файле Excel с помощью Aspose.Cells и Golang через C++.  
---  

{{% alert color="primary" %}}  

Неиспользуемые стили в Excel файлах занимают не только место, но и вызывают проблемы с производительностью при преобразовании в разные форматы, такие как PDF, HTML и др. Aspose.Cells предоставляет [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) для удаления всех неиспользуемых стилей внутри рабочей книги.  

{{% /alert %}}  

Следующий код показывает использование [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/). Код загружает [шаблон Excel файла](5115520.xlsx), который можно скачать по предоставленной ссылке. Он содержит неиспользуемый стиль под названием **AsposeStyle**; этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}
