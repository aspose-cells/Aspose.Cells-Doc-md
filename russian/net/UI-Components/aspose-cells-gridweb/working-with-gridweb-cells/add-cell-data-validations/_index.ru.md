---
title: Добавить проверку данных ячеек
type: docs
weight: 90
url: /ru/net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb, валидация, проверка данных, GridValidation
description: В этой статье рассматривается добавление проверки данных (GridValidation) в GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb позволяет добавлять **проверки данных** с помощью метода GridWorksheet.Validations.Add(). Используя этот метод, вы должны указать **диапазон ячеек**. Но если вы хотите создать проверку данных в одной ячейке, то вы можете сделать это напрямую, используя метод GridCell.CreateValidation(). Аналогично, вы можете удалить **проверку данных** из ячейки с помощью метода GridCell.RemoveValidation().

{{% /alert %}} 
## **Создание проверки данных в ячейке сетки GridWeb**
В следующем образце кода создается **Проверка данных** в ячейке B3. Если вы введете значение, которое не находится между 20 и 40, ячейка B3 покажет **Ошибка проверки** в виде **Красного XXXX**, как показано на этом снимке экрана.

![todo:image_alt_text](add-cell-data-validations_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
