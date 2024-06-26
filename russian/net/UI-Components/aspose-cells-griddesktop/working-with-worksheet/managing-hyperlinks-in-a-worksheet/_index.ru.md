---
title: Управление гиперссылками в листе рабочей книги
type: docs
weight: 90
url: /ru/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop, гиперссылка, гиперссылка, гиперссылки
description: Эта статья представляет, как работать с гиперссылкой в GridDesktop.
---

{{% alert color="primary" %}} 

Используя Aspose.Cells.GridDesktop, также возможно добавлять гиперссылки к простым значениям, хранящимся в ячейках листа рабочей книги. Допустим, в некоторых ячейках у вас может быть некоторые значения, с которыми вы хотели бы связать более подробную информацию на веб-странице. В этом случае желательно добавить гиперссылку к этой ячейке, чтобы если пользователь нажмет на нее, он будет направлен на эту веб-страницу. В этой теме мы объясним, как разработчики могут добавлять и изменять гиперссылки в своих листах рабочей книги.

{{% /alert %}} 
## **Добавление гиперссылок**
Чтобы добавить гиперссылку в ячейку с помощью Aspose.Cells.GridDesktop, выполните следующие действия:

- Добавьте элемент управления Aspose.Cells.GridDesktop на ваш **Форм**
- Получить доступ к любому желаемому **Рабочему листу**
- Получите доступ к желаемой **ячейке** листа, которая будет содержать гиперссылку
- Добавьте какое-либо значение в ячейку для создания гиперссылки
- Добавьте **гиперссылку** к листу, указав имя ячейки, на которой будет применена гиперссылка

Коллекция **Hyperlinks** в объекте **Worksheet** предоставляет перегруженный метод **Add**. Разработчики могут использовать любую перегруженную версию метода **Add** в соответствии с их конкретными потребностями.

Нижеприведенный код добавит гиперссылку на ячейки **B2** и **C3** таблицы.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Доступ к гиперссылкам**
После того как гиперссылка будет добавлена в ячейку, может потребоваться получить доступ и изменить гиперссылку во время выполнения. Для этого разработчики могут просто получить доступ к гиперссылке из **Hyperlinks** коллекции **Worksheet**, указав ячейку (используя имя ячейки или ее расположение в терминах номера строки и столбца), в которую добавлена гиперссылка. После того как гиперссылка будет получена, разработчики могут изменить ее URL во время выполнения.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Удаление гиперссылок**
Чтобы удалить существующую гиперссылку, разработчики могут просто получить доступ к желаемой таблице, а затем **удалить** гиперссылку из **Hyperlinks** коллекции **Worksheet**, указав ячейку с гиперссылкой (используя ее имя или номер строки и столбца).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Если вы хотите добавить гиперссылку в ячейку и хотите отобразить URL гиперссылки в ячейке вместо какого-либо значения, то не добавляйте никакого значения в ячейку, просто добавьте гиперссылку в эту ячейку. При этом ячейка будет содержать гиперссылку, а URL гиперссылки также будет отображаться в ячейке как ее значение.

{{% /alert %}}
