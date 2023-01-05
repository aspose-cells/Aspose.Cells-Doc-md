---
title: Добавить Cell Проверка данных
type: docs
weight: 90
url: /ru/net/add-cell-data-validations/
---
{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb позволяет добавлять**Валидация данных** с помощью метода GridWorksheet.Validations.Add(). Используя этот метод, вы должны указать**Cell Ассортимент** Но если вы хотите создать проверку данных в одной ячейке GridCell, вы можете сделать это напрямую, используя метод GridCell.CreateValidation(). Аналогично можно удалить**Валидация данных** из GridCell с помощью метода GridCell.RemoveValidation().

{{% /alert %}} 
## **Создание проверки данных в GridCell GridWeb**
 Следующий пример кода создает**Валидация данных** в ячейке B3. Если вы введете любое значение, отличное от 20 и 40, в ячейке B3 отобразится**Ошибка проверки** в виде**Красный ХХХ** как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
