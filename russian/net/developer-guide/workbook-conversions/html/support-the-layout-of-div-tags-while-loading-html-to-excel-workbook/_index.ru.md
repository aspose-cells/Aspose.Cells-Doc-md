---
title: Поддержка макета тегов DIV при загрузке HTML в книгу Excel
type: docs
weight: 50
url: /ru/net/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/
---
{{% alert color="primary" %}} 

Обычно макет тегов div игнорируется при загрузке HTML в объект книги Excel. Однако, если вы хотите, чтобы макет тегов div не игнорировался, установите[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) собственность на**истинный** . Значение по умолчанию для этого свойства**ЛОЖЬ**.

{{% /alert %}} 

 Следующий пример кода иллюстрирует использование[HTMLLoadOptions.SupportDivTag](https://reference.aspose.com/cells/net/aspose.cells/htmlloadoptions/properties/supportdivtag) имущество. Пожалуйста, загрузите[Aspose Логотип](5115218.png) используется внутри ввода HTML и[выходной файл excel](5115220.xlsx) генерируется кодом.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DivTagsLayout-1.cs" >}}
