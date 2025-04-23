---  
title: Редактирование гиперссылок на листе
type: docs  
weight: 330  
url: /ru/nodejs-cpp/editing-hyperlinks-of-worksheet/  
description: Узнайте, как редактировать гиперссылки листа через API Aspose.Cells for Node.js via C++.  
keywords: Редактировать гиперссылки, Редактировать гиперссылки листа, Редактировать гиперссылку клетки, Получить все гиперссылки листа  
---  

{{% alert color="primary" %}}  
Aspose.Cells позволяет получить доступ ко всем гиперссылкам листа с помощью коллекции [**Worksheet.getHyperlinks()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getHyperlinks--). Вы можете получить доступ к каждой гиперссылке из этой коллекции по одной и отредактировать ее свойства.  
{{% /alert %}}  

Следующий пример получает все гиперссылки листа и использует их метод [**Hyperlink.setAddress(string)**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#setAddress-string-) для установки сайта Aspose.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-EditHyperlinks.js" >}}



