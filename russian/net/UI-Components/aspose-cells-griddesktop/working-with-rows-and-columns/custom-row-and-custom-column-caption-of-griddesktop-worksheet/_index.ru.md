---
title: Настраиваемая строка и настраиваемый заголовок столбца рабочего листа GridDesktop
type: docs
weight: 120
url: /ru/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **Возможные сценарии использования**
Вы можете настроить заголовок строки и столбца рабочего листа GridDesktop. Обычно строка начинается с 1, а столбец начинается с A. Вы можете изменить это поведение и использовать собственные подписи для строк и столбцов рабочего листа GridDesktop. Чтобы изменить заголовки строк и столбцов, реализуйте интерфейсы ICustomRowCaption и ICustomColumnCaption.
## **Настраиваемая строка и настраиваемый заголовок столбца рабочего листа GridDesktop**
Следующий пример кода реализует интерфейсы ICustomRowCaption и ICustomColumnCaption и изменяет заголовки строк и столбцов. На снимке экрана показан результат выполнения этого примера кода для справки.



![дело:изображение_альтернативный_текст](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Образец кода**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
