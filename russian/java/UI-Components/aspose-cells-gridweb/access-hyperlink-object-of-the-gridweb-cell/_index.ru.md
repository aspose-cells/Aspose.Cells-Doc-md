---
title: Доступ к объекту гиперссылки GridWeb Cell
type: docs
weight: 60
url: /ru/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Возможные сценарии использования**
Вы можете проверить, содержит ли ячейка гиперссылку или нет, используя следующие два метода. Эти методы вернут значение null, если ячейка не содержит гиперссылки, а если она содержит гиперссылку, она вернет объект GridHyperlink.

- GridHyperlinkCollection.getHyperlink (ячейка GridCell)
- GridHyperlinkCollection.getHyperlink (строка int, столбец int)
##  **Открыть гиперссылку в новом или существующем окне**
 Если ваш файл Excel содержит гиперссылку, которая ведет на какой-либо URL-адрес, например<http://wwww.aspose.com/> и вы загружаете его в GridWeb, тогда гиперссылки будут отображаться с целевым атрибутом, установленным на _blank. Это означает, что когда вы щелкнете гиперссылку в ячейке GridWeb, она откроется в новом окне вместо существующего. Кроме того, если вы хотите открыть гиперссылку в существующем окне, установите для GridHyperlink.Target значение _self.
##  **Доступ к объекту гиперссылки GridWeb Cell**
Следующий пример кода осуществляет доступ к гиперссылке ячейки A1. Если ячейка A1 содержит гиперссылку, она вернет объект GridHyperlink, в противном случае она вернет ноль.
##  **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
