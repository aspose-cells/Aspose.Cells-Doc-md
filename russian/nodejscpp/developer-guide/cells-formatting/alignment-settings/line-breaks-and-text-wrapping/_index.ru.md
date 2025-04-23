---  
title: Перенос строк и перенос текста
linktitle: Перенос строк и перенос текста  
description: Как реализовать перенос текста и перенос слов с помощью библиотеки Aspose.Cells в Node.js через C++. Используя библиотеку Aspose.Cells, вы можете легко вставлять текст в ячейки и устанавливать метод переноса текста, такой как ручной перенос слов, автоматический перенос и т. д. В этом документе подробно описано, как реализовать эти функции и приведен пример.  
keywords: Aspose.Cells, перенос строк, перенос текста, расположение текста Node.js через C++  
type: docs  
weight: 60  
url: /ru/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
Чтобы гарантировать, что текст в ячейке может быть прочитан, можно применить явные разрывы строк и перенос текста. Перенос текста превращает одну строку в несколько в ячейке, а явные разрывы строк устанавливаются точно там, где вы их хотите.  
{{% /alert %}}  

## **Перенос текста в ячейке**  
Чтобы переносить текст внутри ячейки, используйте метод [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **Использование явных переносов строк**  
Вы можете использовать '\n' в JavaScript для вставки явных переносов строк в ячейке.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



