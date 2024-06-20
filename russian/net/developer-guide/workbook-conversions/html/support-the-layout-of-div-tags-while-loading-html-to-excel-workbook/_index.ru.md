---
title: Поддерживайте макет тегов DIV при загрузке HTML в книгу Excel
type: docs
weight: 50
url: /ru/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---

{{% alert color="primary" %}} 

Обычно макет div-тегов игнорируется при загрузке HTML в объект электронной книги Excel. Однако, если вы хотите, чтобы макет div-тегов не игнорировался, установите свойство [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) в **true**. Значение этого свойства по умолчанию **false**.

{{% /alert %}} 

Следующий образец кода иллюстрирует использование свойства [HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag). Пожалуйста, загрузите использованный входной HTML [логотип Aspose](5115218.png) и [выходной файл Excel](5115220.xlsx), сгенерированные кодом.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
